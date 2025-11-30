hierarchial_markdown_code = r"""
# Hierarchical Clustering

Hierarchical Clustering is a method of cluster analysis that seeks to build a hierarchy of clusters. It is used in various fields, including biology, marketing, and data analysis. The primary goal is to group a set of objects in such a way that objects in the same group (or cluster) are more similar to each other than to those in other groups.

## Types of Hierarchical Clustering

Hierarchical clustering can be broadly classified into two types:

1. **Agglomerative Clustering (Bottom-Up Approach)**:
   - This is the most common type of hierarchical clustering.
   - It starts with each object as a separate cluster and iteratively merges the closest pairs of clusters until only one cluster remains.
   - The steps involved are:
     1. Compute the distance matrix for all pairs of points.
     2. Identify the closest two clusters.
     3. Merge the two clusters.
     4. Update the distance matrix.
     5. Repeat steps 2-4 until all points are clustered.

2. **Divisive Clustering (Top-Down Approach)**:
   - This approach starts with a single cluster containing all objects and recursively splits it into smaller clusters.
   - This method is less common and more computationally intensive.

## Distance Measures

To determine the closeness of clusters, different distance metrics can be used, such as:

- **Euclidean Distance**: The most common distance measure, calculated as the square root of the sum of the squared differences between corresponding elements.
  
- **Manhattan Distance**: The sum of the absolute differences between the coordinates.

- **Cosine Similarity**: A measure of similarity between two non-zero vectors.

## Linkage Criteria

Linkage criteria determine how the distance between clusters is calculated during the clustering process. Common methods include:

1. **Single Linkage**: The distance between the closest points in two clusters.
2. **Complete Linkage**: The distance between the farthest points in two clusters.
3. **Average Linkage**: The average distance between all pairs of points in two clusters.
4. **Ward's Linkage**: Minimizes the total within-cluster variance. This is often preferred for its computational efficiency.

## Dendrogram

A dendrogram is a tree-like diagram that illustrates the arrangement of the clusters formed by hierarchical clustering. It displays the hierarchy of clusters and can be used to decide the number of clusters by cutting the tree at a certain level.

### How to Interpret a Dendrogram:

- **Vertical Axis**: Represents the distance or dissimilarity between clusters.
- **Horizontal Axis**: Represents the individual data points.
- The height at which two clusters are joined indicates their distance.

## Example in Python

Hierarchical clustering can be easily implemented in Python using libraries such as `scipy` and `scikit-learn`. Here is a simple example:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Sample data
data = np.array([[1, 2], [2, 1], [3, 4], [5, 6], [8, 8]])

# Perform hierarchical clustering
linked = linkage(data, 'single')

# Create a dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=[str(i) for i in range(len(data))], distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram')
plt.xlabel('Data points')
plt.ylabel('Distance')
plt.show()
```

"""
