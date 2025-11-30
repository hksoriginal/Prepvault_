padding_markdown = r"""
# Padding in Deep Learning

Padding is a technique used in Convolutional Neural Networks (CNNs) to control the spatial dimensions of the output feature maps. It adds extra pixels around the border of an image or feature map before applying a convolution operation. 

## Purpose of Padding

1. **Control Output Size**: Padding allows you to control the spatial dimensions of the output feature maps. Without padding, the dimensions of the output feature map decrease after each convolution layer, which can lead to very small feature maps, especially in deeper networks.

2. **Preserve Information**: By adding padding, we can ensure that the borders of the input are not neglected during the convolution operation. This is especially important for images, where information near the edges can be crucial.

3. **Prevent Overfitting**: Padding can also help prevent overfitting by introducing additional variation in the input data.

## Types of Padding

1. **Valid Padding**: No padding is added to the input. The output size is reduced based on the filter size.
   - Output size is calculated as:
   $$
   \text{Output Size} = \frac{\text{Input Size} - \text{Filter Size}}{\text{Stride}} + 1
   $$

2. **Same Padding**: Padding is added so that the output size is the same as the input size. The amount of padding is usually calculated as:
   - For a kernel of size $$( k )$$ and stride $$( s )$$:
   $$
   \text{Padding} = \left\lfloor \frac{(s - 1) + (k - 1)}{2} \right\rfloor
   $$

3. **Full Padding**: This type of padding adds enough pixels to ensure that every input pixel is covered by the kernel at least once.
   - The formula for the output size is:
   $$
   \text{Output Size} = \frac{\text{Input Size} + 2 \times \text{Padding} - \text{Filter Size}}{\text{Stride}} + 1
   $$

## Example Calculation

Consider an input feature map of size $$( 5 \times 5 )$$ and a convolutional filter of size $$( 3 \times 3 )$$ with a stride of 1.

- **Valid Padding**:
  - Output size:
  $$
  \text{Output Size} = \frac{5 - 3}{1} + 1 = 3
  $$

- **Same Padding**:
  - Padding required:
  $$
  \text{Padding} = \left\lfloor \frac{(1 - 1) + (3 - 1)}{2} \right\rfloor = 1
  $$
  - Output size:
  $$
  \text{Output Size} = \frac{5 + 2 \times 1 - 3}{1} + 1 = 5
  $$

## Conclusion

Padding is an essential concept in deep learning, particularly in convolutional networks. It helps in preserving spatial dimensions and ensuring that important features, especially at the edges of the input data, are captured effectively. By choosing the appropriate type of padding, one can enhance the performance of a neural network significantly.
"""
