clustering_evaluation_metrices = r"""
# Evaluation Metrics for Clustering Algorithms

Clustering algorithms group similar data points together, but evaluating the quality of clusters requires different metrics compared to supervised learning tasks. Here are the most common evaluation metrics for clustering algorithms:

## 1. **Inertia (Within-cluster Sum of Squares)**

Inertia measures the internal cohesion of clusters. It calculates the sum of squared distances between data points and the centroid of the cluster they belong to. Lower inertia indicates more compact clusters.

**Formula**:
$$
\text{Inertia} = \sum_{i=1}^{k} \sum_{x \in C_i} ||x - \mu_i||^2
$$
Where:
- $$C_i$$ is the i-th cluster.
- $$\mu_i$$ is the centroid of the i-th cluster.
- $$x$$ represents a data point in cluster $$C_i$$.

Lower values of inertia indicate better clustering but should not be the only criterion used.

## 2. **Silhouette Score**

The silhouette score combines the measure of cohesion and separation. It takes into account how similar a point is to its own cluster compared to other clusters. The score ranges from -1 to 1:
- +1: The data point is well-clustered and far from other clusters.
- 0: The data point is on the boundary between two clusters.
- -1: The data point is likely in the wrong cluster.

**Formula**:
$$
S(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$
Where:
- $$a(i)$$ is the average distance between a point and all other points in the same cluster.
- $$b(i)$$ is the average distance between a point and points in the nearest cluster.

## 3. **Davies-Bouldin Index (DBI)**

The Davies-Bouldin Index measures the average similarity ratio of each cluster to its most similar cluster. The lower the DBI, the better the clustering.

**Formula**:
$$
DBI = \frac{1}{k} \sum_{i=1}^{k} \max_{j \neq i} \left( \frac{\sigma_i + \sigma_j}{d(C_i, C_j)} \right)
$$
Where:
- $$\sigma_i$$ is the average distance between the points in cluster $$i$$ and the centroid of cluster $$i$$.
- $$d(C_i, C_j)$$ is the distance between the centroids of clusters $$i$$ and $$j$$.

## 4. **Adjusted Rand Index (ARI)**

The ARI is a measure of similarity between two data clusterings (i.e., a predicted clustering and a true clustering) by calculating the similarity of the assignments. It adjusts for chance and is especially useful when you have ground truth labels for the data.

**Formula**:
$$
ARI = \frac{\sum_{ij} \binom{n_{ij}}{2} - \left[\sum_i \binom{a_i}{2} \sum_j \binom{b_j}{2}\right] / \binom{n}{2}}{0.5 \left[\sum_i \binom{a_i}{2} + \sum_j \binom{b_j}{2}\right] - \left[\sum_i \binom{a_i}{2} \sum_j \binom{b_j}{2}\right] / \binom{n}{2}}
$$
Where:
- $$n_{ij}$$ is the number of points in both cluster $$i$$ of the ground truth and cluster $$j$$ of the predicted labels.
- $$a_i$$ and $$b_j$$ are the marginal sums for the ground truth and predicted cluster contingency table.

ARI values range between -1 and 1, where 1 represents perfect agreement, and 0 represents random labeling.

## 5. **Normalized Mutual Information (NMI)**

NMI measures the mutual dependence between the true labels and the predicted clusters. It ranges from 0 to 1, where 1 indicates perfect correlation between the true and predicted clusters, and 0 indicates no correlation.

**Formula**:
$$
NMI(U, V) = \frac{2 \cdot I(U, V)}{H(U) + H(V)}
$$
Where:
- $$I(U, V)$$ is the mutual information between the true and predicted clusters.
- $$H(U)$$ and $$H(V)$$ are the entropy of the true clusters and predicted clusters, respectively.

## 6. **Fowlkes-Mallows Index (FMI)**

The Fowlkes-Mallows Index evaluates the similarity between true labels and predicted clusters by considering the number of true positive, false positive, and false negative pairs.

**Formula**:
$$
FMI = \sqrt{ \frac{TP}{TP + FP} \times \frac{TP}{TP + FN} }
$$
Where:
- $$TP$$ is the number of true positive pairs.
- $$FP$$ is the number of false positive pairs.
- $$FN$$ is the number of false negative pairs.

Values of FMI range from 0 to 1, with 1 indicating perfect clustering.

## 7. **Calinski-Harabasz Index (Variance Ratio Criterion)**

The Calinski-Harabasz Index (or Variance Ratio Criterion) evaluates clusters based on the ratio of between-cluster dispersion to within-cluster dispersion. Higher values indicate better-defined clusters.

**Formula**:
$$
CH = \frac{\text{Tr}(B_k)}{\text{Tr}(W_k)} \times \frac{n - k}{k - 1}
$$
Where:
- $$\text{Tr}(B_k)$$ is the trace of the between-cluster dispersion matrix.
- $$\text{Tr}(W_k)$$ is the trace of the within-cluster dispersion matrix.
- $$n$$ is the number of points.
- $$k$$ is the number of clusters.

Higher values imply better clustering performance.

## Summary of Metrics

| Metric | Description | Range |
|--------|-------------|-------|
| Inertia | Measures cohesion within clusters | $$ [0, \infty) $$ |
| Silhouette Score | Combines cohesion and separation | $$ [-1, 1] $$ |
| Davies-Bouldin Index | Measures cluster similarity | $$ [0, \infty) $$ (lower is better) |
| Adjusted Rand Index | Measures similarity to ground truth | $$ [-1, 1] $$ |
| Normalized Mutual Information | Measures information overlap with ground truth | $$ [0, 1] $$ |
| Fowlkes-Mallows Index | Measures similarity to ground truth based on pair counts | $$ [0, 1] $$ |
| Calinski-Harabasz Index | Ratio of between-cluster and within-cluster dispersion | Higher is better |
"""
