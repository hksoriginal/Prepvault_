pooling_markdown = r"""
# Pooling in Deep Learning

Pooling is a critical operation in Convolutional Neural Networks (CNNs) that reduces the spatial dimensions of the input feature maps. This operation helps in decreasing the number of parameters and computations in the network, thereby controlling overfitting and allowing the model to learn hierarchical features.

## Types of Pooling

### 1. Max Pooling

Max pooling takes the maximum value from each patch of the feature map. This operation retains the most prominent features while reducing the spatial size. The operation can be defined mathematically as:

$$
Y_{i,j} = \max_{m,n} X_{s(i), s(j)}
$$

where:
- \( Y \) is the pooled feature map,
- \( X \) is the input feature map,
- \( s(i) \) and \( s(j) \) represent the indices of the pooling window,
- \( m, n \) iterate over the pooling window dimensions.

### 2. Average Pooling

Average pooling calculates the average of the values in each patch of the feature map. This operation smooths the feature map and helps in generalizing the learned features. It can be defined as:

$$
Y_{i,j} = \frac{1}{k} \sum_{m,n} X_{s(i), s(j)}
$$

where:
- \( k \) is the total number of elements in the pooling window.

### 3. Global Pooling

Global pooling reduces each feature map to a single value. For example, in global average pooling, the average of all values in a feature map is computed:

$$
Y = \frac{1}{H \times W} \sum_{i=1}^{H} \sum_{j=1}^{W} X_{i,j}
$$

where:
- \( H \) and \( W \) are the height and width of the feature map.

## Purpose of Pooling

1. **Dimensionality Reduction**: Pooling reduces the spatial size of the representation, leading to fewer parameters and computations in the network.
  
2. **Translation Invariance**: Pooling helps the model become invariant to small translations in the input, allowing it to focus on the most critical features.

3. **Preventing Overfitting**: By reducing the dimensionality, pooling helps to prevent overfitting in deep networks.

## Pooling Layers

Pooling is typically implemented using pooling layers in deep learning frameworks like TensorFlow and PyTorch. Here is an example of how to implement max pooling in PyTorch:

```python
import torch
import torch.nn as nn

# Define a Max Pooling layer
max_pool = nn.MaxPool2d(kernel_size=2, stride=2)

# Sample input (1, 1, 4, 4) - (batch size, channels, height, width)
input_tensor = torch.tensor([[[[1, 2, 3, 4], 
                                [5, 6, 7, 8], 
                                [9, 10, 11, 12], 
                                [13, 14, 15, 16]]]]], dtype=torch.float32)

# Apply max pooling
output_tensor = max_pool(input_tensor)
print(output_tensor)

## Conclusion
Pooling is an essential operation in deep learning, particularly in CNNs, as it aids in reducing computational complexity, improving model performance, and controlling overfitting. Understanding and effectively applying different types of pooling techniques is crucial for building efficient and robust neural network architectures. 
"""
