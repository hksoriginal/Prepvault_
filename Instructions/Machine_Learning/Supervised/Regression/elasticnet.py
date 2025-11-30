elastic_net_markdown = r"""
# Elastic Net

Elastic Net is a linear regression model that incorporates both **L1 (Lasso)** and **L2 (Ridge)** regularization techniques. This model is particularly useful when there are multiple features that are correlated with each other. By combining both types of regularization, Elastic Net can handle high-dimensional data and perform variable selection effectively.

## Key Concepts

### 1. Regularization

Regularization is a technique used to prevent overfitting by adding a penalty term to the loss function. The two types of regularization in Elastic Net are:

- **L1 Regularization (Lasso)**: Adds the absolute value of the coefficients as a penalty term. This can shrink some coefficients to zero, effectively performing variable selection.
  
- **L2 Regularization (Ridge)**: Adds the squared value of the coefficients as a penalty term. This tends to shrink all coefficients, but none are set to zero.

### 2. Loss Function

The loss function for Elastic Net can be defined as follows:

$$
L(\beta) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \alpha \left( \frac{1 - r}{2} \sum_{j=1}^{p} \beta_j^2 + r \sum_{j=1}^{p} |\beta_j| \right)
$$

Where:
- $$(n)$$ is the number of samples.
- $$(y_i)$$ is the true response value.
- $$(\hat{y}_i)$$ is the predicted response value.
- $$(\beta_j)$$ represents the coefficients.
- $$(r)$$ is the mixing parameter between Lasso and Ridge $$((0 \leq r \leq 1)$$).
- $$(\alpha)$$ is the overall regularization strength.

### 3. Mixing Parameter $$((r))$$

- When $$(r = 0)$$, Elastic Net is equivalent to Lasso.
- When $$(r = 1)$$, Elastic Net is equivalent to Ridge.
- Values between 0 and 1 represent a mix of both types of regularization.

## Advantages of Elastic Net

1. **Handles Multicollinearity**: Elastic Net is effective in situations where there are highly correlated predictors. It selects groups of correlated variables rather than just one.

2. **Feature Selection**: It performs variable selection while maintaining the stability of the model.

3. **Flexibility**: The mixing parameter $$(r)$$ allows for tuning the model according to the problem at hand.

## Implementation in Python

Here's how to implement Elastic Net regression using the `scikit-learn` library:

```python
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample data
X = [[0, 0], [1, 1], [2, 2], [3, 3]]
y = [0, 1, 2, 3]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an Elastic Net model
model = ElasticNet(alpha=1.0, l1_ratio=0.5)

# Fit the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, predictions)

print(f"Mean Squared Error: {mse}")
```
"""
