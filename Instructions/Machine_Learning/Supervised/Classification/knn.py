knn_explanation = """
# K-Nearest Neighbors (KNN)

K-Nearest Neighbors (KNN) is a simple, instance-based machine learning algorithm used for both classification and regression tasks. It operates on the principle of identifying the closest training examples in the feature space and making predictions based on the majority class (in classification) or the average value (in regression) of those neighbors.

## Key Concepts

### 1. Instance-Based Learning
KNN is a type of instance-based learning, meaning it does not explicitly learn a model but instead makes decisions based on the instances in the training data. When a new sample is to be classified or predicted, the algorithm calculates the distance between the new sample and all training samples.

### 2. Distance Metrics
To determine the "nearness" of points, KNN employs distance metrics. The most common distance metrics include:
- **Euclidean Distance**: The straight-line distance between two points in Euclidean space.
- **Manhattan Distance**: The sum of the absolute differences of their Cartesian coordinates.
- **Minkowski Distance**: A generalization of Euclidean and Manhattan distances.

The Euclidean distance is defined as:

$$
d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}
$$

Where \( p \) and \( q \) are points in n-dimensional space.

### 3. Choosing K
The parameter **K** in KNN determines how many neighbors will be considered when making predictions:
- If K=1, the class of the nearest neighbor is assigned to the new sample.
- Larger values of K can smooth out the predictions, reducing the sensitivity to noise.

Choosing the optimal K is crucial. Typically, K is chosen using techniques like cross-validation.

## Algorithm Steps

1. **Load the Dataset**: Read in the dataset and preprocess it (if necessary).
2. **Choose K**: Decide on the number of neighbors to consider.
3. **Calculate Distances**: For a new sample, calculate its distance to all training samples.
4. **Identify Neighbors**: Sort the distances and identify the K closest neighbors.
5. **Make Predictions**:
   - **Classification**: The class with the majority among the K neighbors is assigned to the new sample.
   - **Regression**: The average of the K neighbors' values is assigned.

## Pros and Cons

### Advantages:
- Simple to understand and implement.
- Naturally handles multi-class problems.
- Non-parametric: makes no assumptions about the underlying data distribution.

### Disadvantages:
- Computationally expensive, especially with large datasets, as it requires distance calculations for all training samples.
- Sensitive to irrelevant features and the scale of the data.
- Performance can degrade with high-dimensional data (curse of dimensionality).

## Example Implementation

Here's a simple implementation of KNN using Python's scikit-learn library:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create KNN classifier
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

# KNN from Scratch

```python
import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        \"""
Initialize the KNN classifier.

Args:
    k - - Number of neighbors to consider for classification
    \"""
        self.k = k  # Number of neighbors
        self.X_train = None  # Training feature data
        self.y_train = None  # Training labels
    
    def fit(self, X, y):
        \"""
    Fit the KNN classifier to the training data.

    Args:
        X - - Training feature data, shape(n_samples, n_features)
        y - - Training labels, shape(n_samples,)
        \"""
        self.X_train = X  # Store training data
        self.y_train = y  # Store training labels
    
    def predict(self, X):
        \"""
        Predict the class labels for the input data.

        Args:
        X - - Input feature data, shape(n_samples, n_features)

        Returns:
        predictions - - Predicted labels for each input sample
        \"""
        predictions = [self._predict(x) for x in X]  # Predict for each sample
        return np.array(predictions)  # Return predictions as an array
    
    def _predict(self, x):
        \"""
        Predict the class label for a single sample.

        Args:
        x - - Input feature vector(1D)

        Returns:
        The predicted class label
        \"""
        # Compute distances from the input sample to all training samples
        distances = self._compute_distances(x)  # Calculate distances
        # Get the indices of the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]  # Sort distances and select the first k
        # Get the labels of the k nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]  # Find labels for these neighbors
        # Return the most common label among the neighbors
        most_common = Counter(k_nearest_labels).most_common(1)  # Count the occurrences
        return most_common[0][0]  # Return the most common label
    
    def _compute_distances(self, x):
        \"""
        Compute the Euclidean distance between a single sample and all training samples.

        Args:
        x - - Input feature vector(1D)

        Returns:
        distances - - Array of distances from x to each training sample
        \"""
        # Calculate Euclidean distance
        distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))  # Apply distance formula
        return distances  # Return the distances


# Example usage:
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Generate a random binary classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the KNN classifier
knn = KNN(k=5)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

```



### Explanation:

1.  **Class Initialization**:

    -   The `KNN` class is initialized with a parameter `k`, which specifies the number of nearest neighbors to consider for making predictions.
2.  **Fitting the Model**:

    -   The `fit` method stores the training data and corresponding labels for later use in predictions.
3.  **Prediction**:

    -   The `predict` method takes in new data points and predicts their class labels using the `_predict` method.
    -   The `_predict` method computes distances to all training samples, identifies the k nearest neighbors, and finds the most common class label among those neighbors using the `Counter` class from the `collections` module.
4.  **Distance Calculation**:

    -   The `_compute_distances` method calculates the Euclidean distance between a given data point and all training points using vectorized operations for efficiency.
5.  **Example Usage**:

    -   In the example usage, we generate a synthetic binary classification dataset using `make_classification`, split it into training and testing sets, fit the KNN classifier, and evaluate its accuracy.




"""
