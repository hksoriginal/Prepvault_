attention_mechanism = r"""
# Attention Mechanism in Transformer Architecture

The Transformer model, introduced by Vaswani et al. in 2017, utilizes a mechanism known as **Attention** to effectively capture relationships between different parts of a sequence, regardless of their distance from one another. Unlike previous architectures (such as RNNs), Transformers rely entirely on attention mechanisms, making them faster and more parallelizable. 

## Key Concepts of Attention in Transformers

### 1. **Self-Attention**
Self-attention, also known as **Scaled Dot-Product Attention**, allows each word in a sequence to attend to all other words. This helps capture dependencies between words in a sentence, which is particularly useful for natural language processing tasks.

Each word in the sequence is represented as three vectors:
- **Query (Q)**
- **Key (K)**
- **Value (V)**

These vectors are learned during training and enable the model to focus on different parts of the sequence.

### 2. **Scaled Dot-Product Attention**
Given queries $$Q$$, keys $$K$$, and values $$V$$, the attention mechanism computes a weighted sum of the values, where the weights are determined by the similarity between queries and keys.

The process is as follows:

1. **Compute the dot products** between each query and all keys.
2. **Scale the dot product** by dividing by $$\sqrt{d_k}$$, where $$d_k$$ is the dimension of the keys. This scaling helps prevent excessively large values in the softmax function, which could lead to vanishing gradients.
3. **Apply the Softmax function** to obtain the attention weights.
4. **Multiply the weights by the values** $$V$$ to get the final weighted sum for each word in the sequence.

The mathematical representation of Scaled Dot-Product Attention is:

$$
\text{Attention}(Q, K, V) = \text{softmax} \left( \frac{Q K^T}{\sqrt{d_k}} \right) V
$$

### 3. **Multi-Head Attention**
In practice, the Transformer uses **Multi-Head Attention**. Rather than using a single attention function, multiple attention heads are used to capture different aspects of relationships within the sequence.

Each head learns different representations by using independent sets of $$Q$$, $$K$$, and $$V$$ matrices, allowing the model to focus on various parts of the sequence simultaneously. The outputs of each head are then concatenated and projected through a linear transformation.

The formula for Multi-Head Attention is as follows:

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O
$$

where $$\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$ and $$W_i^Q, W_i^K, W_i^V, W^O$$ are learned projection matrices.

### 4. **Position-Wise Feed-Forward Networks**
After applying Multi-Head Attention, the output is passed through a Position-Wise Feed-Forward Network. This network consists of two fully connected layers with a ReLU activation in between. It is applied independently to each position in the sequence.

### 5. **Positional Encoding**
Since Transformers do not have a sense of the order of words, **Positional Encoding** is added to the input embeddings to provide information about the positions within the sequence. Positional encodings are vectors added to the embeddings, which encode positional information using sine and cosine functions.

## Summary of the Attention Process
1. Compute $$Q$$, $$K$$, and $$V$$ matrices.
2. Calculate attention scores using the scaled dot-product of $$Q$$ and $$K$$.
3. Apply softmax to obtain the attention weights.
4. Multiply the attention weights by $$V$$ to get the output for each word.
5. Use Multi-Head Attention to capture diverse patterns.
6. Add positional encoding to maintain sequential order information.

The attention mechanism allows the Transformer model to selectively focus on relevant parts of the input sequence, enabling efficient parallel processing and making it particularly effective for natural language processing tasks.
"""
