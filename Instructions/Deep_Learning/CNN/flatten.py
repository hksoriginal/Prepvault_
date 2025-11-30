flatten_markdown = r"""
# Flattening in Deep Learning

Flattening is a critical step in deep learning models, particularly in convolutional neural networks (CNNs). It involves transforming a multi-dimensional array (tensor) into a one-dimensional array (vector) to prepare it for the next layer, typically a fully connected layer.

## Purpose of Flattening

1. **Transition to Fully Connected Layers**: After several layers of convolution and pooling, the output is usually a 3D tensor (e.g., height × width × channels). Fully connected layers require a 1D input. Flattening allows us to convert this multi-dimensional output into a vector that can be fed into fully connected layers.

2. **Maintaining Information**: Flattening retains the information present in the multi-dimensional array, ensuring that the spatial relationships learned by the convolutional layers are preserved in the final output.

## How Flattening Works

Consider an input feature map from a convolutional layer. For example, let’s say the output feature map has a shape of $$(3 \times 3 \times 2)$$ (height × width × channels). The flattening process will transform this tensor into a one-dimensional vector with a length equal to the product of its dimensions.

### Mathematical Representation

If we denote the dimensions of the input tensor as $$(H)$$, $$(W)$$, and $$(C)$$ (height, width, and channels, respectively), the flattening operation can be mathematically represented as:

$$
[
\text{Flattened\_vector} = \text{reshape}(T) \quad \text{where} \quad T \in \mathbb{R}^{H \times W \times C}
]
$$

The resulting flattened vector will have a dimension of:

$$
[
\text{Dimension} = H \times W \times C
]
$$

### Example

Given a tensor $$(T)$$ with dimensions $$(3 \times 3 \times 2)$$:

$$

T = \begin{bmatrix}
\begin{bmatrix} t_{1,1,1} & t_{1,2,1} \\ t_{1,3,1} \end{bmatrix} & 
\begin{bmatrix} t_{1,1,2} & t_{1,2,2} \\ t_{1,3,2} \end{bmatrix} \\
\begin{bmatrix} t_{2,1,1} & t_{2,2,1} \\ t_{2,3,1} \end{bmatrix} & 
\begin{bmatrix} t_{2,1,2} & t_{2,2,2} \\ t_{2,3,2} \end{bmatrix} \\
\begin{bmatrix} t_{3,1,1} & t_{3,2,1} \\ t_{3,3,1} \end{bmatrix} & 
\begin{bmatrix} t_{3,1,2} & t_{3,2,2} \\ t_{3,3,2} \end{bmatrix}
\end{bmatrix}

$$

After flattening, the output will be:

$$

\text{Flattened\_vector} = \begin{bmatrix} t_{1,1,1} & t_{1,2,1} & t_{1,3,1} & t_{1,1,2} & t_{1,2,2} & t_{1,3,2} \\ t_{2,1,1} & t_{2,2,1} & t_{2,3,1} & t_{2,1,2} & t_{2,2,2} & t_{2,3,2} \\ t_{3,1,1} & t_{3,2,1} & t_{3,3,1} & t_{3,1,2} & t_{3,2,2} & t_{3,3,2} \end{bmatrix}

$$

## Implementation

In popular deep learning frameworks like TensorFlow and PyTorch, flattening can be easily implemented using built-in functions. For example, in PyTorch:

```python
import torch
import torch.nn as nn

# Example input tensor
input_tensor = torch.rand((1, 3, 3, 2))  # Batch size of 1, height 3, width 3, channels 2

# Flattening layer
flatten = nn.Flatten()

# Apply flattening
flattened_output = flatten(input_tensor)

print(flattened_output.shape)  # Output: torch.Size([1, 18])
```
## Implementation in Tensorflow
```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Create a Sequential model
model = models.Sequential()

# Add a convolutional layer
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))  # Input shape: 28x28x1 (e.g., grayscale images)

# Add a pooling layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Add another convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Add another pooling layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the previous layer
model.add(layers.Flatten())

# Add a fully connected layer
model.add(layers.Dense(128, activation='relu'))

# Add an output layer (for 10 classes, e.g., digits 0-9)
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Display the model summary
model.summary()

```

"""
