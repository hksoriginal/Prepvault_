strides_markdown = r"""
# Understanding Strides in Deep Learning

In deep learning, particularly in convolutional neural networks (CNNs), the term **stride** refers to the number of pixels by which the filter (or kernel) moves across the input image. Understanding strides is crucial for designing CNN architectures effectively.

## Key Concepts

1. **Filter/Kernels**: A filter is a small matrix that slides over the input image to extract features. Common sizes are 3x3, 5x5, etc.

2. **Stride**: 
   - The stride defines how much the filter moves after each operation.
   - For example, a stride of 1 means the filter moves one pixel to the right (or down) for the next operation, while a stride of 2 means it moves two pixels.

3. **Padding**: Padding refers to adding extra pixels around the input image. It can be important for controlling the spatial dimensions of the output.

## How Strides Work

Let's break down how strides affect the output size of a convolutional layer:

### Formula for Output Size

The output size $$ O $$ of a convolution operation can be calculated using the following formula:

$$
O = \left\lfloor \frac{(W - K + 2P)}{S} \right\rfloor + 1
$$

Where:
- $$ O $$ = Output size
- $$ W $$ = Input size (width or height)
- $$ K $$ = Kernel size (width or height)
- $$ P $$ = Padding
- $$ S $$ = Stride

### Example Calculation

Let's say we have:
- Input size $$ W = 32 $$ (32x32 image)
- Kernel size $$ K = 3 $$ (3x3 filter)
- Padding $$ P = 0 $$
- Stride $$ S = 1 $$

Using the formula:

$$
O = \left\lfloor \frac{(32 - 3 + 2*0)}{1} \right\rfloor + 1 = \left\lfloor \frac{29}{1} \right\rfloor + 1 = 30
$$

Thus, the output size would be $$ 30 \times 30 $$.

### Effects of Different Strides

- **Stride = 1**: This results in a detailed output with a larger spatial size. The filter moves one pixel at a time, ensuring that more features are captured.
  
- **Stride > 1**: This results in a reduced output size. For example, a stride of 2 means that the filter skips every other pixel. This can lead to a loss of fine details but increases computational efficiency.

## Visual Representation

Here's a visual representation of how strides work with a 3x3 filter:

Input Image (5x5): [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

Filter (3x3): [[1, 0, -1], [1, 0, -1], [1, 0, -1]]

Stride = 1 Output Image: [[ 8, 10], [ 18, 20]]

Stride = 2 Output Image: [[ 8], [18]]


## Summary

Strides play a crucial role in determining the output size of convolutional layers in CNNs. By adjusting the stride, practitioners can control the level of detail captured and the computational efficiency of the model. 

Understanding and choosing the right stride, in conjunction with filter size and padding, is essential for building effective deep learning architectures.
"""
