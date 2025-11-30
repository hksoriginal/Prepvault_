svd_markdown_code = r"""
# Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a fundamental technique in linear algebra and statistics that is widely used in various fields, including machine learning, signal processing, and image compression. SVD provides a way to decompose a matrix into three other matrices, revealing important properties of the original matrix.

## Definition

Given an $$( m \times n )$$ matrix $$( A )$$, SVD allows us to express $$( A )$$ as:

$$
[
A = U \Sigma V^T
]
$$

where:
- $$( U )$$ is an $$( m \times m )$$ orthogonal matrix.
- $$( \Sigma )$$ is an $$( m \times n )$$ diagonal matrix with non-negative real numbers on the diagonal.
- $$( V^T )$$ is the transpose of an $$( n \times n )$$ orthogonal matrix $$( V )$$.

### Components

1. **U Matrix**: The columns of $$( U )$$ are called the left singular vectors of $$( A )$$. They represent the directions of the data in the original space.

2. **Σ (Sigma) Matrix**: The diagonal entries of $$( \Sigma )$$ are called the singular values. They are non-negative and typically arranged in descending order. The singular values indicate the importance of the corresponding singular vectors.

3. **V Matrix**: The columns of $$( V )$$ are called the right singular vectors of $$( A )$$. They represent the directions in the feature space.

## Properties of SVD

- **Dimensionality Reduction**: SVD can be used to reduce the dimensionality of data by retaining only the largest singular values and their corresponding singular vectors. This is often used in Principal Component Analysis (PCA).

- **Rank of the Matrix**: The rank of the matrix $$( A )$$ is equal to the number of non-zero singular values in $$( \Sigma )$$.

- **Reconstruction**: The original matrix $$( A )$$ can be reconstructed by combining the singular values and vectors:
$$
[
A \approx U_k \Sigma_k V_k^T
]
$$

where $$( U_k )$$, $$( \Sigma_k )$$, and $$( V_k )$$ represent the truncated matrices containing the top $$( k )$$ singular values and vectors.

## Applications of SVD

1. **Image Compression**: SVD is widely used in image processing to reduce the size of image files while maintaining quality.

2. **Recommender Systems**: SVD is employed in collaborative filtering methods to predict user preferences based on past behaviors.

3. **Noise Reduction**: SVD can be used to filter out noise from data by retaining only significant singular values.

4. **Latent Semantic Analysis**: In natural language processing, SVD is utilized to discover relationships between words and documents.

## Example

To illustrate SVD, consider the following example using Python's NumPy library:

```python
import numpy as np

# Create a sample matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Perform SVD
U, Sigma, Vt = np.linalg.svd(A)

print("U Matrix:")
print(U)
print("\nSigma Values:")
print(Sigma)
print("\nV^T Matrix:")
print(Vt)
```
"""
