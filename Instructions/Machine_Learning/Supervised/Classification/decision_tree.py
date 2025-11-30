decision_tree_explanation = r"""

## Overview
A Decision Tree is a flowchart-like structure used for both classification and regression tasks in machine learning. It splits the dataset into subsets based on the value of input features, leading to a decision at each leaf node.

## Structure
- **Root Node**: Represents the entire dataset, which is split into two or more homogeneous sets.
- **Decision Nodes**: Nodes that represent the feature on which the data is split.
- **Leaf Nodes**: Terminal nodes that represent the output or class label.

## How Decision Trees Work
1. **Select Feature**: Choose a feature to split the data based on a specific criterion (e.g., Gini impurity, information gain).
2. **Split Dataset**: Divide the dataset into subsets based on the selected feature.
3. **Repeat**: Recursively repeat the process for each subset until:
   - All data points in a subset belong to the same class.
   - There are no features left to split.
   - A predefined depth of the tree is reached.

## Criteria for Splitting
- **Gini Impurity**: Measures the impurity of a node, with lower values indicating better purity.
- **Entropy**: Measures the disorder or unpredictability in the data.
- **Information Gain**: The reduction in entropy after the dataset is split.

### Gini Impurity Formula
$$ [ Gini(D) = 1 - \sum_{i=1}^{C} (p_i)^2 ] $$
Where $$( p_i )$$ is the probability of class $$( i )$$ in dataset $$( D )$$ and $$( C )$$ is the number of classes.

### Entropy Formula
$$[ Entropy(D) = -\sum_{i=1}^{C} p_i \log_2(p_i) ] $$

## Advantages of Decision Trees
- **Easy to Interpret**: Visual and intuitive representation.
- **No Need for Feature Scaling**: Works well with both numerical and categorical data.
- **Handles Non-linear Relationships**: Can model complex relationships.

## Disadvantages of Decision Trees
- **Overfitting**: Tends to create overly complex trees that do not generalize well.
- **Instability**: Small changes in the data can lead to different splits and structures.
- **Biased towards Dominant Classes**: Can be biased if one class dominates the dataset.

## Pruning Techniques
To combat overfitting, decision trees can be pruned:
- **Pre-pruning**: Stops the tree from growing when certain conditions are met (e.g., maximum depth).
- **Post-pruning**: Removes nodes after the tree has been created to reduce complexity.

## Implementation Example (using Python's scikit-learn)
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict on test set
predictions = model.predict(X_test)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')
```

# Decision Tree Algorithm Implementation from Scratch

```python
import numpy as np

# Helper function to calculate Gini Impurity
def gini(y):
    \"""
Calculate Gini Impurity for a set of labels.

Args:
    y - - Array of labels(1D)

    Returns:
    gini - - Gini impurity value
    \"""
    classes = np.unique(y)
    gini_impurity = 1.0
    for cls in classes:
        p = np.sum(y == cls) / len(y)  # Probability of class 'cls'
        gini_impurity -= p ** 2
    return gini_impurity

# Helper function to split the data based on a feature and a threshold
def split(X, y, feature, threshold):
    \"""
    Split the dataset into two subsets based on a feature and threshold.

    Args:
    X - - Input feature matrix
    y - - Target label vector
    feature - - Index of the feature to split on
    threshold - - Threshold value to split the feature

    Returns:
    left_X, right_X, left_y, right_y - - Split data and labels
    \"""
    left_idx = X[:, feature] <= threshold
    right_idx = X[:, feature] > threshold
    return X[left_idx], X[right_idx], y[left_idx], y[right_idx]

# Node class to represent each node in the decision tree
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        \"""
    Initialize a node in the decision tree.

    Args:
        feature - - The index of the feature used for splitting
        threshold - - The value to split the feature on
        left - - Left child node
        right - - Right child node
        value - - Value for leaf node(class label for classification)
        \"""
        self.feature = feature  # Index of the feature to split on
        self.threshold = threshold  # Threshold value for splitting
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Leaf node value (if it’s a leaf)

# Decision Tree class
class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100):
        \"""
        Initialize the decision tree classifier.

        Args:
        min_samples_split - - The minimum number of samples required to split a node
        max_depth - - The maximum depth of the tree
        \"""
        self.min_samples_split = min_samples_split  # Minimum samples to split
        self.max_depth = max_depth  # Maximum depth of the tree
        self.root = None  # The root node of the tree
    
    # Function to find the best split
    def best_split(self, X, y):
        \"""
        Find the best feature and threshold to split the data.

        Args:
        X - - Input feature matrix
        y - - Target label vector

        Returns:
        best_feature, best_threshold - - Feature index and threshold that provide the best split
        \"""
        n_samples, n_features = X.shape
        best_feature, best_threshold = None, None
        best_gini = float('inf')  # Set the best Gini score to infinity initially
        
        for feature in range(n_features):  # Iterate over each feature
            thresholds = np.unique(X[:, feature])  # Get unique values of the feature
            for threshold in thresholds:
                # Split the dataset based on the current feature and threshold
                X_left, X_right, y_left, y_right = split(X, y, feature, threshold)
                
                # Skip split if any side is empty
                if len(y_left) == 0 or len(y_right) == 0:
                    continue
                
                # Calculate Gini impurity for the split
                gini_left = gini(y_left)
                gini_right = gini(y_right)
                
                # Weighted Gini impurity
                gini_split = (len(y_left) / n_samples) * gini_left + (len(y_right) / n_samples) * gini_right
                
                # Update if we found a better split
                if gini_split < best_gini:
                    best_gini = gini_split
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold
    
    # Function to build the decision tree recursively
    def build_tree(self, X, y, depth=0):
        \"""
        Recursively build the decision tree.

        Args:
        X - - Input feature matrix
        y - - Target label vector
        depth - - Current depth of the tree

        Returns:
        A Node object representing the root of the tree
        \"""
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))
        
        # Stopping conditions (when to stop splitting):
        if (depth >= self.max_depth or n_samples < self.min_samples_split or n_labels == 1):
            leaf_value = self.most_common_label(y)
            return Node(value=leaf_value)
        
        # Find the best split
        feature, threshold = self.best_split(X, y)
        
        # If no good split found, make this a leaf node
        if feature is None:
            leaf_value = self.most_common_label(y)
            return Node(value=leaf_value)
        
        # Split the data
        X_left, X_right, y_left, y_right = split(X, y, feature, threshold)
        
        # Recursively build the left and right subtree
        left_child = self.build_tree(X_left, y_left, depth + 1)
        right_child = self.build_tree(X_right, y_right, depth + 1)
        
        # Return the current node with left and right children
        return Node(feature=feature, threshold=threshold, left=left_child, right=right_child)
    
    def most_common_label(self, y):
        \"""
        Find the most common label in a list of labels.

        Args:
        y - - Array of labels

        Returns:
        The most frequent label
        \"""
        return np.bincount(y).argmax()
    
    # Function to fit the tree
    def fit(self, X, y):
        \"""
        Fit the decision tree model to the data.

        Args:
        X - - Input feature matrix
        y - - Target label vector
        \"""
        self.root = self.build_tree(X, y)
    
    # Function to make predictions for a single sample
    def _predict(self, x, tree):
        \"""
        Predict the class label for a single sample by traversing the tree.

        Args:
        x - - Input feature vector(1D)
        tree - - The current node in the decision tree

        Returns:
        The predicted class label
        \"""
        # If we are at a leaf node, return the value (predicted label)
        if tree.value is not None:
            return tree.value
        
        # Otherwise, traverse the tree recursively
        feature_value = x[tree.feature]
        if feature_value <= tree.threshold:
            return self._predict(x, tree.left)
        else:
            return self._predict(x, tree.right)
    
    # Function to predict for a batch of samples
    def predict(self, X):
        \"""
        Predict the class labels for a batch of samples.

        Args:
        X - - Input feature matrix(2D)

        Returns:
        predictions - - Predicted labels for each sample
        \"""
        return [self._predict(x, self.root) for x in X]


# Example usage:
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Generate a random binary classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree
tree = DecisionTree(max_depth=10)
tree.fit(X_train, y_train)

# Make predictions on the test set
y_pred = tree.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


```

"""
