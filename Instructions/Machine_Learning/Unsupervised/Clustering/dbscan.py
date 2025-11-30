dbscan_markdown = r"""
# DBSCAN: Density-Based Spatial Clustering of Applications with Noise

## Introduction
DBSCAN is a clustering algorithm that groups together points that are closely packed together, marking as outliers points that lie alone in low-density regions. It is particularly useful for spatial data and can find clusters of arbitrary shapes.

## Key Concepts

### 1. Core Points
A point is considered a core point if it has at least a minimum number of points (`MinPts`) within a specified radius (`ε` or epsilon). 

### 2. Border Points
A border point is a point that is not a core point but falls within the neighborhood of a core point. 

### 3. Noise Points
Noise points are those that are neither core points nor border points. These points do not belong to any cluster.

### 4. Epsilon (`ε`)
The radius within which the algorithm searches for neighboring points. It defines the size of the neighborhood around a core point.

### 5. Minimum Points (`MinPts`)
The minimum number of points required to form a dense region. Typically, `MinPts` is chosen based on the dimensionality of the data (e.g., `MinPts = 2 * number_of_dimensions`).

## Algorithm Steps
1. For each point in the dataset, determine its neighborhood using the `ε` distance.
2. If the point is a core point, create a new cluster and add all points within its neighborhood.
3. Expand the cluster by checking all neighboring points:
   - If a neighboring point is a core point, include its neighborhood in the cluster.
   - Continue this process until all points in the cluster are identified.
4. Mark any remaining points as noise or add them to existing clusters if they are within the `ε` distance of a core point.

## Advantages
- **Ability to find arbitrary-shaped clusters:** Unlike k-means, which requires spherical clusters, DBSCAN can find clusters of varying shapes and sizes.
- **No need to specify the number of clusters:** It automatically determines the number of clusters based on the density of the data.
- **Robust to outliers:** DBSCAN effectively identifies noise points.

## Disadvantages
- **Parameter sensitivity:** The results are highly dependent on the selection of `ε` and `MinPts`.
- **Not suitable for clusters of varying densities:** DBSCAN may struggle with datasets containing clusters of differing densities.
- **High-dimensional data challenges:** Performance may degrade in high-dimensional spaces due to the curse of dimensionality.

## Use Cases
- Geospatial data analysis
- Image segmentation
- Anomaly detection in network data

## Example
```python
from sklearn.cluster import DBSCAN
import numpy as np

# Sample data
data = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])

# DBSCAN clustering
dbscan = DBSCAN(eps=3, min_samples=2)
clusters = dbscan.fit_predict(data)

print(clusters)
```

"""
