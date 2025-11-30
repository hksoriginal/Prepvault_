transformer_architecture_markdown = r"""
# Transformer Architecture in Deep Learning

## Introduction
The Transformer architecture, introduced by Vaswani et al. in the paper "Attention is All You Need" (2017), revolutionized the field of Natural Language Processing (NLP) and beyond. Unlike recurrent neural networks (RNNs) that process data sequentially, Transformers leverage self-attention mechanisms, allowing them to process data in parallel and capture long-range dependencies effectively.

## Key Components

### 1. Encoder-Decoder Structure
The Transformer model consists of an **encoder** and a **decoder**. Each of these components is made up of multiple layers.

- **Encoder:** Takes input sequences and generates a set of continuous representations.
- **Decoder:** Takes the encoder's output and produces the output sequence, which is typically shifted for training (teacher forcing).

### 2. Multi-Head Self-Attention
Self-attention allows the model to weigh the importance of different words in a sentence when encoding or decoding them. Multi-head attention expands this idea by running multiple self-attention mechanisms in parallel.

- **Self-Attention Mechanism:**
  - Computes attention scores using query, key, and value vectors.
  - The attention score for a word relative to other words is calculated, enabling the model to focus on relevant parts of the input.

- **Multi-Head Attention:**
  - Applies multiple self-attention operations (heads) to capture various relationships.
  - The outputs of all heads are concatenated and linearly transformed.

### 3. Position-wise Feedforward Networks
After the multi-head attention step, the output is passed through a feedforward neural network applied independently to each position. This consists of two linear transformations with a ReLU activation in between.

### 4. Positional Encoding
Transformers lack a sense of order in the input data. To address this, positional encodings are added to the input embeddings to provide information about the relative positions of words in the sequence.

- Positional encodings can be sinusoidal functions or learned embeddings.

### 5. Layer Normalization and Residual Connections
To stabilize training, Layer Normalization is applied after each sub-layer (self-attention and feedforward). Additionally, residual connections are used, which add the input of a layer to its output, aiding gradient flow.

## Transformers in TensorFlow
```python
import tensorflow as tf
from tensorflow.keras.layers import Layer, Input, Embedding, MultiHeadAttention, Dense, LayerNormalization, Dropout
from tensorflow.keras.models import Model

class PositionalEncoding(Layer):
    def __init__(self, max_position, d_model):
        super(PositionalEncoding, self).__init__()
        self.pos_encoding = self.get_positional_encoding(max_position, d_model)

    def get_positional_encoding(self, max_position, d_model):
        angle_rates = 1 / tf.pow(10000, (2 * (tf.range(d_model // 2, dtype=tf.float32) // 2)) / tf.cast(d_model, tf.float32))
        angles = tf.range(max_position, dtype=tf.float32)[:, tf.newaxis] * angle_rates[tf.newaxis, :]
        pos_encoding = tf.concat([tf.sin(angles), tf.cos(angles)], axis=-1)
        pos_encoding = pos_encoding[tf.newaxis, ...]
        return pos_encoding

    def call(self, x):
        return x + self.pos_encoding[:, :tf.shape(x)[1], :]

class TransformerBlock(Layer):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.attention = MultiHeadAttention(num_heads=num_heads, key_dim=d_model)
        self.ffn = tf.keras.Sequential([
            Dense(dff, activation='relu'),  # Feed forward layer
            Dense(d_model)  # Output layer
        ])
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(rate)
        self.dropout2 = Dropout(rate)

    def call(self, x, training):
        attn_output = self.attention(x, x)
        out1 = self.layernorm1(x + self.dropout1(attn_output, training=training))
        ffn_output = self.ffn(out1)
        return self.layernorm2(out1 + self.dropout2(ffn_output, training=training))

class Transformer(Model):
    def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size, maximum_position_encoding, rate=0.1):
        super(Transformer, self).__init__()
        self.encoder_embedding = Embedding(input_vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(maximum_position_encoding, d_model)
        self.enc_layers = [TransformerBlock(d_model, num_heads, dff, rate) for _ in range(num_layers)]
        self.dropout = Dropout(rate)
        self.final_layer = Dense(input_vocab_size)

    def call(self, x, training):
        x = self.encoder_embedding(x)
        x = self.pos_encoding(x)
        for enc_layer in self.enc_layers:
            x = enc_layer(x, training)
        return self.final_layer(x)

# Hyperparameters
num_layers = 4
d_model = 128
num_heads = 8
dff = 512
input_vocab_size = 10000  # Adjust as needed
maximum_position_encoding = 1000
dropout_rate = 0.1

# Create the Transformer model
transformer_model = Transformer(num_layers, d_model, num_heads, dff, input_vocab_size, maximum_position_encoding)

# Sample input
sample_input = tf.constant([[1, 2, 3], [4, 5, 6]])  # Example input (batch size of 2)
output = transformer_model(sample_input, training=False)
print(output)

```
## Transformers in Pytorch
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.encoding = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(torch.log(torch.tensor(10000.0)) / d_model))
        self.encoding[:, 0::2] = torch.sin(position * div_term)
        self.encoding[:, 1::2] = torch.cos(position * div_term)
        self.encoding = self.encoding.unsqueeze(0)  # Add batch dimension

    def forward(self, x):
        return x + self.encoding[:, :x.size(1), :]

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // num_heads
        self.wq = nn.Linear(d_model, d_model)
        self.wk = nn.Linear(d_model, d_model)
        self.wv = nn.Linear(d_model, d_model)
        self.dense = nn.Linear(d_model, d_model)

    def split_heads(self, x, batch_size):
        x = x.view(batch_size, -1, self.num_heads, self.depth)
        return x.permute(0, 2, 1, 3)  # (batch_size, num_heads, seq_len, depth)

    def forward(self, q, k, v):
        batch_size = q.size(0)
        q = self.split_heads(self.wq(q), batch_size)
        k = self.split_heads(self.wk(k), batch_size)
        v = self.split_heads(self.wv(v), batch_size)

        attn_weights = F.softmax(torch.matmul(q, k.transpose(-2, -1)) / (self.depth ** 0.5), dim=-1)
        output = torch.matmul(attn_weights, v)
        output = output.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, self.d_model)
        return self.dense(output)

class FeedForward(nn.Module):
    def __init__(self, d_model, dff):
        super(FeedForward, self).__init__()
        self.linear1 = nn.Linear(d_model, dff)
        self.linear2 = nn.Linear(dff, d_model)

    def forward(self, x):
        return self.linear2(F.relu(self.linear1(x)))

class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.attention = MultiHeadAttention(d_model, num_heads)
        self.ffn = FeedForward(d_model, dff)
        self.layernorm1 = nn.LayerNorm(d_model)
        self.layernorm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(rate)
        self.dropout2 = nn.Dropout(rate)

    def forward(self, x):
        attn_output = self.attention(x, x, x)
        out1 = self.layernorm1(x + self.dropout1(attn_output))
        ffn_output = self.ffn(out1)
        return self.layernorm2(out1 + self.dropout2(ffn_output))

class Transformer(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size, max_pos_encoding, rate=0.1):
        super(Transformer, self).__init__()
        self.embedding = nn.Embedding(input_vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model)
        self.enc_layers = nn.ModuleList([TransformerBlock(d_model, num_heads, dff, rate) for _ in range(num_layers)])
        self.final_layer = nn.Linear(d_model, input_vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = self.pos_encoding(x)
        for enc_layer in self.enc_layers:
            x = enc_layer(x)
        return self.final_layer(x)

# Hyperparameters
num_layers = 4
d_model = 128
num_heads = 8
dff = 512
input_vocab_size = 10000  # Adjust as needed
max_pos_encoding = 1000
dropout_rate = 0.1

# Create the Transformer model
transformer_model = Transformer(num_layers, d_model, num_heads, dff, input_vocab_size, max_pos_encoding)

# Sample input
sample_input = torch.tensor([[1, 2, 3], [4, 5, 6]])  # Example input (batch size of 2)
output = transformer_model(sample_input)
print(output)

```



## Applications

Transformers have been applied successfully in various domains beyond NLP, including:

-   **Machine Translation:** State-of-the-art results in translating text between languages.
-   **Image Processing:** Vision Transformers (ViTs) apply the Transformer architecture to images for tasks like classification.
-   **Speech Recognition:** Models like wav2vec leverage transformers for processing audio data.


"""
