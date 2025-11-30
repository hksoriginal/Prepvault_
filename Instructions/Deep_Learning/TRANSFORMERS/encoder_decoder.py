encoder_decoder_markdown_code = r"""
# Encoder-Decoder Architecture in Transformers

## Overview

The Encoder-Decoder architecture is a fundamental design in the Transformer model, primarily used in tasks like machine translation, summarization, and text generation. It consists of two main components: the **encoder**, which processes the input data, and the **decoder**, which generates the output data.

## Architecture Components

### 1. Encoder

- **Purpose**: The encoder takes the input sequence and transforms it into a continuous representation (contextualized embeddings).
- **Structure**: The encoder is composed of a stack of identical layers (commonly 6 in the original Transformer model). Each layer consists of:
  - **Multi-Head Self-Attention Mechanism**: Allows the model to focus on different parts of the input sequence simultaneously. It computes attention scores and helps capture long-range dependencies.
  - **Feed-Forward Neural Network**: A fully connected feed-forward network applied to each position independently. It consists of two linear transformations with a ReLU activation in between.
  - **Layer Normalization**: Applied after each sub-layer (self-attention and feed-forward) to stabilize and accelerate training.
  - **Residual Connections**: Added to help with the flow of gradients during backpropagation.
  
  
## Encoder in Pytorch
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // num_heads

        assert d_model % num_heads == 0

        self.wq = nn.Linear(d_model, d_model)  # Query
        self.wk = nn.Linear(d_model, d_model)  # Key
        self.wv = nn.Linear(d_model, d_model)  # Value

        self.dense = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        batch_size = x.size(0)
        x = x.view(batch_size, -1, self.num_heads, self.depth)
        return x.permute(0, 2, 1, 3)  # (batch_size, num_heads, seq_len, depth)

    def forward(self, v, k, q, mask):
        batch_size = q.size(0)

        q = self.wq(q)  # (batch_size, seq_len, d_model)
        k = self.wk(k)  # (batch_size, seq_len, d_model)
        v = self.wv(v)  # (batch_size, seq_len, d_model)

        q = self.split_heads(q)  # (batch_size, num_heads, seq_len_q, depth)
        k = self.split_heads(k)  # (batch_size, num_heads, seq_len_k, depth)
        v = self.split_heads(v)  # (batch_size, num_heads, seq_len_v, depth)

        # Scaled dot-product attention
        scaled_attention_logits = torch.matmul(q, k.transpose(-2, -1))  # (batch_size, num_heads, seq_len_q, seq_len_k)
        scaled_attention_logits /= (self.depth ** 0.5)

        if mask is not None:
            scaled_attention_logits += (mask * -1e9)

        attention_weights = F.softmax(scaled_attention_logits, dim=-1)  # (batch_size, num_heads, seq_len_q, seq_len_k)

        output = torch.matmul(attention_weights, v)  # (batch_size, num_heads, seq_len_q, depth)
        output = output.permute(0, 2, 1, 3)  # (batch_size, seq_len_q, num_heads, depth)

        output = output.contiguous().view(batch_size, -1, self.d_model)  # (batch_size, seq_len_q, d_model)

        return self.dense(output)  # (batch_size, seq_len_q, d_model)


class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(EncoderLayer, self).__init__()
        self.mha = MultiHeadAttention(d_model, num_heads)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, dff),  # (batch_size, seq_len, dff)
            nn.ReLU(),
            nn.Linear(dff, d_model)  # (batch_size, seq_len, d_model)
        )

        self.layernorm1 = nn.LayerNorm(d_model, eps=1e-6)
        self.layernorm2 = nn.LayerNorm(d_model, eps=1e-6)
        self.dropout1 = nn.Dropout(rate)
        self.dropout2 = nn.Dropout(rate)

    def forward(self, x, training, mask):
        attn_output = self.mha(x, x, x, mask)  # Self-attention
        out1 = self.layernorm1(x + self.dropout1(attn_output))  # Residual connection

        ffn_output = self.ffn(out1)  # Feed-forward network
        return self.layernorm2(out1 + self.dropout2(ffn_output))  # Residual connection


class Encoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size, maximum_position_encoding, rate=0.1):
        super(Encoder, self).__init__()

        self.d_model = d_model
        self.num_layers = num_layers
        self.embedding = nn.Embedding(input_vocab_size, d_model)  # Input embedding
        self.pos_encoding = self.positional_encoding(maximum_position_encoding, self.d_model)

        self.enc_layers = nn.ModuleList(
            [EncoderLayer(d_model, num_heads, dff, rate) for _ in range(num_layers)]
        )
        self.dropout = nn.Dropout(rate)

    def positional_encoding(self, position, d_model):
        angle_rads = self.get_angles(torch.arange(position)[:, None], torch.arange(d_model)[None, :], d_model)

        # Applying sin to even index in the array; 2i
        angle_rads[:, 0::2] = torch.sin(angle_rads[:, 0::2])
        # Applying cos to odd index in the array; 2i+1
        angle_rads[:, 1::2] = torch.cos(angle_rads[:, 1::2])

        pos_encoding = angle_rads[None, ...]
        return pos_encoding

    def get_angles(self, position, i, d_model):
        angle_rates = 1 / (10000 ** (2 * (i // 2) / d_model))
        return position * angle_rates

    def forward(self, x, training, mask):
        seq_len = x.size(1)
        x = self.embedding(x)  # (batch_size, input_seq_len, d_model)
        x *= (self.d_model ** 0.5)  # Scale the embeddings
        x += self.pos_encoding[:, :seq_len, :]  # Add positional encoding
        x = self.dropout(x)

        for i in range(self.num_layers):
            x = self.enc_layers[i](x, training, mask)

        return x  # (batch_size, input_seq_len, d_model)

```

- **Input Representation**: The input tokens are first embedded into a high-dimensional space, and positional encodings are added to provide information about the position of each token in the sequence.

### 2. Decoder

- **Purpose**: The decoder generates the output sequence based on the encoder's output and previously generated tokens.
- **Structure**: Similar to the encoder, the decoder consists of a stack of identical layers. Each layer includes:
  - **Masked Multi-Head Self-Attention Mechanism**: Prevents the decoder from attending to future tokens in the output sequence during training, ensuring that predictions for a position depend only on known outputs.
  - **Multi-Head Attention over Encoder Outputs**: Allows the decoder to focus on relevant parts of the encoder's output while generating each token.
  - **Feed-Forward Neural Network**: Same structure as in the encoder.
  - **Layer Normalization and Residual Connections**: Used similarly as in the encoder.

- **Output Generation**: The decoder produces one token at a time, and the process is typically autoregressive, meaning each token is generated based on previously generated tokens.

## Attention Mechanism

The attention mechanism is central to the transformer's ability to model relationships within sequences. The key operations are:

1. **Scaled Dot-Product Attention**: Computes attention scores by taking the dot product of queries (Q) and keys (K), scaling them by the square root of their dimension, applying a softmax function to get attention weights, and then combining these weights with values (V).

   $$ 
   
   \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
   
   $$

2. **Multi-Head Attention**: Instead of performing a single attention function, the transformer computes multiple sets of attention in parallel (heads), allowing the model to learn different representations at different positions.

## Positional Encoding

Since the transformer architecture does not have recurrence or convolution, it requires positional encodings to incorporate information about the position of tokens in the sequence. These encodings are added to the input embeddings and can be computed using sine and cosine functions of different frequencies.

### Positional Encoding Formula:

$$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)
$$
$$
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)
$$

where \(pos\) is the position and \(i\) is the dimension index.

## Summary

The Encoder-Decoder architecture in Transformers is powerful for sequence-to-sequence tasks. It leverages attention mechanisms to efficiently model dependencies, handles variable-length input and output sequences, and allows for parallelization during training. This architecture has led to significant advancements in natural language processing and beyond.
"""
