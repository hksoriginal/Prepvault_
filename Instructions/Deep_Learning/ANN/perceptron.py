perceptron_explanation = r"""
# Perceptron in Deep Learning

## Introduction

The **Perceptron** is one of the simplest types of artificial neural networks and serves as a foundational building block for deep learning. It was first introduced by Frank Rosenblatt in 1958 and is used primarily for binary classification tasks.

## Structure of a Perceptron

A perceptron consists of the following components:

1. **Input Layer**: The perceptron receives input data in the form of features. Each input feature is represented as a node.

2. **Weights**: Each input feature is associated with a weight that signifies its importance. The perceptron adjusts these weights during the learning process.

3. **Bias**: A bias term is added to the weighted sum of the inputs. It allows the model to fit the data better by providing an additional degree of freedom.

4. **Activation Function**: The output of the perceptron is determined by an activation function. For a simple perceptron, the step function is often used, which outputs a value of 1 if the weighted sum is above a certain threshold and 0 otherwise.

## Mathematical Representation

The output $$ y $$ of a perceptron can be mathematically represented as:

$$ 
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right) 
$$

Where:
- $$ x_i $$ = input features
- $$ w_i $$ = weights
- $$ b $$ = bias
- $$ f $$ = activation function (e.g., step function)

## Learning Process

The perceptron uses a learning algorithm to update the weights and bias based on the errors in the predictions. The key steps in the learning process are:

1. **Initialization**: Start with random weights and bias.
  
2. **Forward Pass**: Calculate the output using the current weights, bias, and input features.

3. **Error Calculation**: Determine the error by comparing the predicted output to the actual output.

4. **Weight Update**: Update the weights and bias using the Perceptron Learning Rule:
   $$
   w_i = w_i + \eta (y_{\text{true}} - y_{\text{pred}}) x_i
   $$
   $$
   b = b + \eta (y_{\text{true}} - y_{\text{pred}})
   $$
   Where $$ \eta $$ is the learning rate, $$ y_{\text{true}} $$ is the true output, and $$ y_{\text{pred}} $$ is the predicted output.

5. **Iteration**: Repeat the process for a number of epochs or until convergence.

## Limitations

While perceptrons are fundamental to understanding neural networks, they have limitations:

- **Linearity**: A single perceptron can only classify linearly separable data. It struggles with more complex, non-linear relationships.

- **Multi-Class Classification**: Perceptrons are inherently binary classifiers, and extending them to multi-class problems requires additional techniques, such as one-vs-all strategies.

## Python Implementation
```python
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Training the Perceptron
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self._activation_function(linear_output)
                
                # Update weights and bias
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self._activation_function(linear_output)
        return y_predicted

    def _activation_function(self, x):
        # Step activation function
        return np.where(x >= 0, 1, 0)


# Example Usage
if __name__ == "__main__":
    # Sample dataset (AND logic gate)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 0, 0, 1])  # AND output

    # Create Perceptron model
    perceptron = Perceptron(learning_rate=0.1, n_iters=10)
    perceptron.fit(X, y)

    # Predictions
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)

```
## Tensorflow Implementation
```python
import tensorflow as tf

# Create a simple Perceptron model
class Perceptron(tf.keras.Model):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.dense = tf.keras.layers.Dense(1, activation='sigmoid')

    def call(self, x):
        return self.dense(x)

# Generate synthetic data (XOR problem)
def generate_data(num_samples=100):
    X = tf.random.uniform((num_samples, 2), minval=-1, maxval=1)
    Y = tf.cast(X[:, 0] * X[:, 1] > 0, tf.float32)
    return X, tf.expand_dims(Y, axis=1)

# Training function
def train(model, X, Y, num_epochs=100, learning_rate=0.01):
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                  loss='binary_crossentropy')

    model.fit(X, Y, epochs=num_epochs, verbose=1)

# Main
if __name__ == '__main__':
    X, Y = generate_data(num_samples=100)

    model = Perceptron()
    train(model, X, Y)

```



## `scikit-learn` Implementation
```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Create a synthetic dataset
X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Perceptron model
perceptron = Perceptron(max_iter=1000, tol=1e-3, random_state=42)

# Fit the model to the training data
perceptron.fit(X_train, y_train)

# Make predictions on the test set
y_pred = perceptron.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

```
## Pytorch Implementation
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Create a synthetic dataset
np.random.seed(0)
n_samples = 100
X = np.random.rand(n_samples, 2)  # 2 features
y = (X[:, 0] + X[:, 1] > 1).astype(np.float32)  # Class label: 1 if sum of features > 1 else 0

# Convert to PyTorch tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).view(-1, 1)  # Reshape for compatibility

# Define the Perceptron model
class Perceptron(nn.Module):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.fc = nn.Linear(2, 1)  # 2 input features, 1 output

    def forward(self, x):
        return torch.sigmoid(self.fc(x))  # Apply sigmoid activation

# Instantiate the model, define the loss function and the optimizer
model = Perceptron()
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.1)  # Stochastic Gradient Descent

# Training loop
n_epochs = 1000
for epoch in range(n_epochs):
    # Forward pass
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{n_epochs}], Loss: {loss.item():.4f}')

# Plotting the decision boundary
with torch.no_grad():
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    Z = model(torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype=torch.float32))
    Z = Z.reshape(xx.shape).numpy()

    plt.contourf(xx, yy, Z, levels=[0, 0.5, 1], alpha=0.5)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Perceptron Decision Boundary')
    plt.show()

```

## Conclusion

The perceptron laid the groundwork for more complex neural networks and deep learning architectures. Understanding its workings is essential for anyone looking to delve into the world of artificial intelligence and machine learning.
"""
