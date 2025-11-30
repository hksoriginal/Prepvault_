lasso_markdown_code = r"""
# Lasso Regression

## Introduction
Lasso Regression (Least Absolute Shrinkage and Selection Operator) is a type of linear regression that uses regularization to enhance the prediction accuracy and interpretability of the statistical model it produces. Regularization helps prevent overfitting by adding a penalty to the loss function based on the size of the coefficients.

## Mathematical Formulation
The objective of Lasso regression is to minimize the following cost function:

$$
\text{Cost Function} = ||y - X\beta||^2_2 + \lambda ||\beta||_1
$$

Where:
- $$y$$ is the vector of observed values.
- $$X$$ is the matrix of input features.
- $$\beta$$ is the vector of coefficients.
- $$\lambda$$ is the regularization parameter (also known as the penalty term).

The first term, $$||y - X\beta||^2_2$$, is the residual sum of squares (RSS), and the second term, $$\lambda ||\beta||_1$$, is the L1 penalty, which encourages sparsity in the coefficients.

## Properties of Lasso Regression
1. **Feature Selection**: Lasso can reduce the coefficients of some features to zero, effectively performing variable selection.
2. **Bias-Variance Tradeoff**: By introducing a penalty, Lasso can reduce model variance, although it may introduce some bias.
3. **Interpretable Models**: Due to feature selection, the resulting model is often easier to interpret.

## Choosing the Regularization Parameter ($$\lambda$$)
The choice of $$\lambda$$ is crucial:
- A small $$\lambda$$ value results in a model similar to standard linear regression (risk of overfitting).
- A large $$\lambda$$ value leads to higher bias but lower variance (risk of underfitting).

Cross-validation is commonly used to select the optimal value of $$\lambda$$.

## Implementation in Python
Lasso regression can be easily implemented using libraries like `scikit-learn`. Here’s a simple example:

```python
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Sample data
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.rand(100)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the model
lasso = Lasso(alpha=0.1)  # Set regularization parameter
lasso.fit(X_train, y_train)

# Predict
y_pred = lasso.predict(X_test)

# Coefficients
print("Coefficients:", lasso.coef_)
```

# Lasso Regresson from scratch

```python
import numpy as np

class LassoRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000, lambda_param=1.0):
        \"""
Initialize the Lasso Regression model.

Args:
    learning_rate - - The learning rate for gradient descent
    n_iterations - - Number of iterations for gradient descent
    lambda_param - - The regularization parameter (lambda )
    \"""
        self.learning_rate = learning_rate  # Learning rate
        self.n_iterations = n_iterations  # Number of iterations
        self.lambda_param = lambda_param  # Regularization parameter
        self.theta = None  # Coefficients (weights)
    
    def fit(self, X, y):
        \"""
    Fit the lasso regression model to the training data.

    Args:
        X - - Training feature data, shape(n_samples, n_features)
        y - - Target labels, shape(n_samples,)
        \"""
        # Add a bias (intercept) term by adding a column of ones to X
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add bias term
        m = X_b.shape[0]  # Number of samples
        
        # Initialize weights to zero
        self.theta = np.zeros(X_b.shape[1])  # Coefficients initialization
        
        # Gradient Descent
        for iteration in range(self.n_iterations):
            # Compute the predictions
            y_pred = X_b.dot(self.theta)  # Predicted values
            
            # Calculate the gradients
            gradients = (2/m) * X_b.T.dot(y_pred - y)  # Gradient of the MSE
            
            # Add L1 penalty to the gradients (subgradient)
            for j in range(len(self.theta)):
                if self.theta[j] > 0:
                    gradients[j] += self.lambda_param
                elif self.theta[j] < 0:
                    gradients[j] -= self.lambda_param
            
            # Update the weights
            self.theta -= self.learning_rate * gradients  # Update weights
    
    def predict(self, X):
        \"""
        Predict the target values for the input data.

        Args:
        X - - Input feature data, shape(n_samples, n_features)

        Returns:
        predictions - - Predicted target values
        \"""
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add bias term
        return X_b.dot(self.theta)  # Return predicted values


# Example usage:
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Generate a random linear regression dataset
X, y = make_regression(n_samples=1000, n_features=5, noise=10, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Lasso Regression model
lasso_model = LassoRegression(learning_rate=0.01, n_iterations=1000, lambda_param=0.1)

# Fit the model to the training data
lasso_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lasso_model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

```

### Explanation:

1.  **Initialization**: The `LassoRegression` class is initialized with parameters for the learning rate, number of iterations, and the regularization parameter $$ \lambda $$.

2.  **Fitting the Model**:

    -   The `fit` method adds a bias term to the feature matrix and initializes the coefficients.
    -   In the gradient descent loop, the predicted values are computed, and the gradients are calculated. The L1 penalty is added to the gradients using a subgradient approach (considering the sign of each coefficient).
    -   The coefficients are updated based on the calculated gradients.
3.  **Making Predictions**:

    -   The `predict` method adds the bias term and computes the predicted values based on the learned coefficients.
4.  **Example Usage**:

    -   A synthetic linear regression dataset is generated using `make_regression`.
    -   The dataset is split into training and testing sets.
    -   The model is fitted to the training data, predictions are made on the test data, and the Mean Squared Error (MSE) is calculated for evaluation.

"""
