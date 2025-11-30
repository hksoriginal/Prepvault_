kmeans_explanation = r"""
# K-Means Clustering

K-Means clustering is a popular unsupervised machine learning algorithm used for partitioning a dataset into distinct groups (clusters). The main objective is to group the data points such that the points in the same cluster are more similar to each other than to those in other clusters.

## How K-Means Works

The K-Means algorithm operates through the following steps:

1. **Initialization**:
   - Choose the number of clusters, $$( K )$$.
   - Randomly initialize $$( K )$$ centroids in the feature space.

2. **Assignment Step**:
   - For each data point, calculate the distance to each centroid (often using Euclidean distance).
   - Assign each data point to the cluster with the nearest centroid.

3. **Update Step**:
   - Recalculate the centroids by taking the mean of all data points assigned to each cluster.
   - The new centroid for each cluster is computed as:
     $$
     [
     C_k = \frac{1}{N_k} \sum_{x_i \in C_k} x_i
     ]
     $$
     where $$( C_k )$$ is the centroid of cluster $$( k )$$, $$( N_k )$$ is the number of points in cluster $$( k )$$, and $$( x_i )$$ are the points in cluster $$( k )$$.

4. **Convergence Check**:
   - Repeat the Assignment and Update steps until convergence, which occurs when:
     - The centroids no longer change significantly.
     - The assignments of points to clusters do not change.

## Key Considerations

- **Choosing $$( K )$$**:
  - Selecting the optimal number of clusters, $$( K )$$, can be challenging. Methods like the **Elbow Method** and **Silhouette Score** can be employed to determine the best $$( K )$$.
  
### Elbow Method

The Elbow Method involves the following steps:

1. Run K-Means clustering for a range of $$( K )$$ values (e.g., 1 to 10).
2. For each $$( K )$$, calculate the **Within-Cluster Sum of Squares (WCSS)**, which measures the total variance within the clusters:
   $$
   
   WCSS = \sum_{i=1}^{K} \sum_{x_j \in C_i} ||x_j - C_i||^2
   
   $$
   where $$( C_i )$$ is the centroid of cluster $$( i )$$.

3. Plot $$( K )$$ against WCSS.
4. Look for a "knee" or "elbow" point in the plot, where the rate of decrease sharply changes. This point suggests a suitable number of clusters.
  
### Silhouette Score

The Silhouette Score is another method for determining the quality of clustering:

1. For each data point, calculate its silhouette score:
   $$
   
   s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
   
   $$
   where:
   - $$( a(i) )$$ is the average distance between the point and all other points in the same cluster.
   - $$( b(i) )$$ is the average distance between the point and all points in the nearest neighboring cluster.

2. The silhouette score ranges from -1 to 1:
   - A score close to 1 indicates that the point is well clustered.
   - A score near 0 indicates that the point is on or very close to the decision boundary between two neighboring clusters.
   - A negative score indicates that the point may have been assigned to the wrong cluster.

3. The overall silhouette score for a clustering solution can be calculated as the average of the silhouette scores for all data points.

- **Distance Metric**:
  - K-means typically uses Euclidean distance, but other distance metrics can be applied depending on the data characteristics.

- **Sensitivity to Initialization**:
  - The choice of initial centroids can affect the final clusters. Multiple runs with different initializations (e.g., using the K-means++ algorithm) can help mitigate this issue.

- **Scalability**:
  - K-means is computationally efficient for large datasets but may struggle with high-dimensional data.

## Applications of K-Means Clustering

K-means clustering is widely used in various fields, including:

- **Customer Segmentation**: Identifying distinct groups of customers based on purchasing behavior.
- **Image Compression**: Reducing the number of colors in an image by clustering similar colors.
- **Document Clustering**: Grouping similar documents for topic modeling or information retrieval.

## Conclusion

K-means clustering is a versatile and straightforward method for unsupervised learning. While it has some limitations, its ease of implementation and interpretability make it a popular choice for clustering tasks.

## Example Code

Here’s a simple implementation of K-means clustering using Python's `scikit-learn` library:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
X = np.random.rand(100, 2)

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Getting the cluster centers and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

# Kmeans from Scratch

```python
import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4):
        \"""
Initialize the KMeans model.

Args:
    n_clusters - - The number of clusters to form
    max_iter - - Maximum number of iterations
    tol - - Tolerance to declare convergence
    \"""
        self.n_clusters = n_clusters  # Number of clusters
        self.max_iter = max_iter  # Maximum number of iterations
        self.tol = tol  # Tolerance for convergence
        self.centroids = None  # Centroids of the clusters
        self.labels_ = None  # Cluster labels for each data point

    def fit(self, X):
        \"""
    Fit the KMeans model to the data.

    Args:
        X - - Input data, shape(n_samples, n_features)
        \"""
        # Randomly initialize centroids
        random_indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        for i in range(self.max_iter):
            # Assignment step
            distances = self._compute_distances(X)  # Calculate distances from points to centroids
            self.labels_ = np.argmin(distances, axis=1)  # Assign labels based on closest centroid
            
            # Update step
            new_centroids = np.array([X[self.labels_ == j].mean(axis=0) for j in range(self.n_clusters)])
            
            # Check for convergence
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break
            
            self.centroids = new_centroids  # Update centroids

    def _compute_distances(self, X):
        \"""
        Compute distances between each data point and the centroids.

        Args:
        X - - Input data, shape(n_samples, n_features)

        Returns:
        distances - - Distance from each data point to each centroid, shape(n_samples, n_clusters)
        \"""
        return np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)  # Broadcasting to calculate distances

    def predict(self, X):
        \"""
        Predict the closest cluster for each data point.

        Args:
        X - - Input data, shape(n_samples, n_features)

        Returns:
        labels - - Predicted cluster labels for each data point
        \"""
        distances = self._compute_distances(X)
        return np.argmin(distances, axis=1)  # Return labels of the closest centroids


# Example usage:
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic dataset
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Initialize KMeans model
kmeans = KMeans(n_clusters=4)

# Fit the model to the data
kmeans.fit(X)

# Make predictions
predicted_labels = kmeans.predict(X)

# Plotting the results
plt.scatter(X[:, 0], X[:, 1], c=predicted_labels, s=30, cmap='viridis')
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', s=200, alpha=0.75, marker='X')  # Centroids
plt.title("K-means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

```

"""
