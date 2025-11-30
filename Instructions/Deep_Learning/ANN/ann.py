ann_markdown_text = r"""
# Artificial Neural Networks (ANN) in Deep Learning

## Introduction
Artificial Neural Networks (ANN) are a fundamental component of deep learning. They are inspired by the biological neural networks that constitute animal brains. ANNs consist of interconnected groups of artificial neurons that process information using a connectionist approach.

## Structure of an ANN
An ANN is typically organized into three types of layers:

1. **Input Layer**: This layer receives the input data. Each neuron in this layer represents one feature of the input data.

2. **Hidden Layer(s)**: These layers perform computations and transformations on the inputs received from the previous layer. An ANN can have one or more hidden layers. The complexity of the model increases with the number of hidden layers.

3. **Output Layer**: This layer produces the final output of the model. Each neuron in this layer represents a possible output class or value.

### Neuron Model
Each neuron in an ANN performs the following operations:

1. **Weighted Sum**: Each input \( x_i \) is multiplied by a weight \( w_i \), and the results are summed up along with a bias \( b \):

   $$
   z = \sum_{i=1}^{n} w_i x_i + b
   $$

2. **Activation Function**: The weighted sum \( z \) is passed through an activation function \( f \) to introduce non-linearity into the model:

   $$
   a = f(z)
   $$

   Common activation functions include:
   - **Sigmoid**: 
   $$
   f(z) = \frac{1}{1 + e^{-z}}
   $$
   - **ReLU (Rectified Linear Unit)**: 
   $$
   f(z) = \max(0, z)
   $$
   - **Tanh**: 
   $$
   f(z) = \tanh(z)
   $$

## Training an ANN
The training process of an ANN involves two main phases:

1. **Forward Propagation**: The input data is passed through the network, layer by layer, until the output is produced.

2. **Backpropagation**: The output is compared to the actual target values using a loss function (e.g., Mean Squared Error for regression tasks, Cross-Entropy for classification). The error is then propagated backward through the network to update the weights and biases using an optimization algorithm (e.g., Stochastic Gradient Descent, Adam).

### Loss Function
The choice of loss function depends on the type of task:
- For binary classification, binary cross-entropy is often used.
- For multi-class classification, categorical cross-entropy is preferred.
- For regression tasks, mean squared error is a common choice.

### Optimization Algorithm
Optimization algorithms adjust the weights to minimize the loss function. Some popular algorithms include:
- **Gradient Descent**: Updates weights in the opposite direction of the gradient of the loss function.
- **Adam**: Combines the benefits of two other extensions of stochastic gradient descent.

## Applications of ANNs
ANNs have a wide range of applications, including but not limited to:
- **Image Recognition**: Convolutional Neural Networks (CNNs) are a specialized type of ANN for image data.
- **Natural Language Processing (NLP)**: Recurrent Neural Networks (RNNs) and Transformers are used for language tasks.
- **Speech Recognition**: ANNs are used to convert spoken language into text.
- **Game Playing**: ANNs can learn to play games, such as Chess and Go, by predicting moves.

## Conclusion
Artificial Neural Networks are powerful tools for solving complex problems in various fields. Their ability to learn from data and model non-linear relationships makes them essential for advancements in deep learning and artificial intelligence.

## Implementation from scratch
```python
import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Simple ANN class
class SimpleANN:
    def __init__(self, input_size, hidden_size, output_size):
        # Weights initialization
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Weights between input and hidden layer
        self.weights_input_hidden = np.random.uniform(size=(self.input_size, self.hidden_size))
        # Weights between hidden and output layer
        self.weights_hidden_output = np.random.uniform(size=(self.hidden_size, self.output_size))
        
    def feedforward(self, X):
        # Input to hidden layer
        self.hidden_layer_activation = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_activation)
        
        # Hidden to output layer
        self.output_layer_activation = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        output = sigmoid(self.output_layer_activation)
        
        return output

    def backpropagation(self, X, y, output, learning_rate):
        # Calculate the error
        output_error = y - output
        
        # Calculate the gradient
        output_gradient = sigmoid_derivative(output)
        output_delta = output_error * output_gradient
        
        # Update weights between hidden and output layer
        self.weights_hidden_output += np.dot(self.hidden_layer_output.T, output_delta) * learning_rate
        
        # Calculate the hidden layer error
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        
        # Calculate the gradient for the hidden layer
        hidden_gradient = sigmoid_derivative(self.hidden_layer_output)
        hidden_delta = hidden_error * hidden_gradient
        
        # Update weights between input and hidden layer
        self.weights_input_hidden += np.dot(X.T, hidden_delta) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for _ in range(epochs):
            output = self.feedforward(X)
            self.backpropagation(X, y, output, learning_rate)

# Example usage
if __name__ == "__main__":
    # Input data (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    # Output data
    y = np.array([[0], [1], [1], [0]])

    # Create ANN
    ann = SimpleANN(input_size=2, hidden_size=2, output_size=1)

    # Train the ANN
    ann.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the ANN
    print("Output after training:")
    print(ann.feedforward(X))

```
## Implementation in Pytorch
```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define the ANN model
class SimpleANN(nn.Module):
    def __init__(self):
        super(SimpleANN, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # Input layer to hidden layer
        self.fc2 = nn.Linear(2, 1)  # Hidden layer to output layer

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Example usage
if __name__ == "__main__":
    # Input data (XOR problem)
    X = torch.tensor([[0.0, 0.0],
                      [0.0, 1.0],
                      [1.0, 0.0],
                      [1.0, 1.0]], dtype=torch.float32)

    # Output data
    y = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float32)

    # Create ANN
    model = SimpleANN()

    # Loss and optimizer
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    # Train the model
    for epoch in range(10000):
        # Forward pass
        outputs = model(X)
        loss = criterion(outputs, y)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Test the ANN
    with torch.no_grad():
        print("Output after training:")
        print(model(X).numpy())

```
## Implementation in Tensorflow
```python
import tensorflow as tf
from tensorflow import keras

# Define the ANN model
model = keras.Sequential([
    keras.layers.Dense(2, activation='sigmoid', input_shape=(2,)),  # Hidden layer
    keras.layers.Dense(1, activation='sigmoid')                     # Output layer
])

# Compile the model
model.compile(optimizer='sgd', loss='binary_crossentropy')

# Input data (XOR problem)
X = tf.constant([[0.0, 0.0],
                 [0.0, 1.0],
                 [1.0, 0.0],
                 [1.0, 1.0]])

# Output data
y = tf.constant([[0.0], [1.0], [1.0], [0.0]])

# Train the model
model.fit(X, y, epochs=10000, verbose=0)

# Test the ANN
print("Output after training:")
print(model.predict(X))

```
## Implementation from Scikit-learn
```python
from sklearn.neural_network import MLPClassifier
import numpy as np

# Input data (XOR problem)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output data
y = np.array([0, 1, 1, 0])

# Create ANN
model = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', solver='sgd', max_iter=10000)

# Train the model
model.fit(X, y)

# Test the ANN
print("Output after training:")
print(model.predict(X))

```


## References
- Ian Goodfellow, Yoshua Bengio, and Aaron Courville. *Deep Learning*. MIT Press.
- Michael Nielsen. *Neural Networks and Deep Learning*. [Online Book](http://neuralnetworksanddeeplearning.com/)
"""
