optimizers_markdown_code = r"""
# Deep Learning Optimizers

Optimizers are algorithms or methods used to update the weights of a neural network during training in order to minimize the loss function. Here’s a detailed overview of some commonly used optimizers in deep learning:

## 1. Stochastic Gradient Descent (SGD)

- **Description**: The most basic optimizer, SGD updates the weights by calculating the gradient of the loss function with respect to the weights and moving in the opposite direction.
- **Update Rule**:
$$
w = w - \eta \cdot \nabla L(w)
$$
where:
- $$ w $$ = weights
- $$ \eta $$ = learning rate
- $$ \nabla L(w) $$ = gradient of the loss function
- **Pros**: Simple, easy to implement.
- **Cons**: Can be slow to converge and may get stuck in local minima.

## 2. Momentum

- **Description**: Momentum improves upon SGD by adding a fraction of the previous update to the current update, helping to accelerate SGD in the relevant direction and dampen oscillations.
- **Update Rule**:
$$
v = \beta v + (1 - \beta) \nabla L(w) \\
w = w - \eta v
$$
where $$ \beta $$ is the momentum factor (typically between 0.5 and 0.9).
- **Pros**: Faster convergence, less oscillation.
- **Cons**: Requires tuning of the momentum factor.

## 3. Nesterov Accelerated Gradient (NAG)

- **Description**: NAG is a variant of momentum that calculates the gradient based on the future position of the weights, which can lead to better convergence.
- **Update Rule**:
$$
v = \beta v + (1 - \beta) \nabla L(w - \eta \beta v) \\
w = w - \eta v
$$
- **Pros**: More responsive and can lead to faster convergence.
- **Cons**: More complex implementation.

## 4. AdaGrad

- **Description**: AdaGrad adapts the learning rate for each parameter based on the historical gradients, making it more suitable for dealing with sparse data.
- **Update Rule**:
$$
G = G + \nabla L(w)^2 \\
w = w - \frac{\eta}{\sqrt{G + \epsilon}} \nabla L(w)
$$
where $$ G $$ is the sum of the squares of the gradients and $$ \epsilon $$ is a small constant to prevent division by zero.
- **Pros**: Automatically adjusts learning rates.
- **Cons**: Learning rate becomes too small over time.

## 5. RMSprop

- **Description**: RMSprop is designed to overcome the diminishing learning rates problem of AdaGrad by using a moving average of the squared gradients.
- **Update Rule**:
$$
G = \beta G + (1 - \beta) \nabla L(w)^2 \\
w = w - \frac{\eta}{\sqrt{G + \epsilon}} \nabla L(w)
$$
- **Pros**: Well-suited for non-stationary objectives.
- **Cons**: Requires tuning of the decay rate.

## 6. Adam (Adaptive Moment Estimation)

- **Description**: Adam combines the benefits of both AdaGrad and RMSprop. It maintains an exponentially decaying average of past gradients and squared gradients.
- **Update Rule**:
$$
m = \beta_1 m + (1 - \beta_1) \nabla L(w) \\
v = \beta_2 v + (1 - \beta_2) \nabla L(w)^2 \\
\hat{m} = \frac{m}{1 - \beta_1^t} \\
\hat{v} = \frac{v}{1 - \beta_2^t} \\
w = w - \frac{\eta}{\sqrt{\hat{v}} + \epsilon} \hat{m}
$$
- **Pros**: Generally works well in practice, adaptive learning rates.
- **Cons**: May require tuning of hyperparameters.

## 7. Nadam

- **Description**: Nadam is an extension of Adam that incorporates Nesterov momentum into the Adam framework.
- **Update Rule**:
Similar to Adam but with an additional momentum term:
$$
m = \beta_1 m + (1 - \beta_1) \nabla L(w) \\
v = \beta_2 v + (1 - \beta_2) \nabla L(w)^2 \\
\hat{m} = \frac{m}{1 - \beta_1^t} \\
\hat{v} = \frac{v}{1 - \beta_2^t} \\
w = w - \eta \cdot \frac{\hat{m}}{\sqrt{\hat{v}} + \epsilon}
$$
- **Pros**: Can converge faster and yield better generalization.
- **Cons**: More computationally intensive.

## 8. FTRL (Follow The Regularized Leader)

- **Description**: Primarily used in online learning and convex optimization. It maintains a weight vector that reflects the average of previous updates.
- **Update Rule**:
The update mechanism varies but often includes a regularization term.
- **Pros**: Effective for large-scale online learning.
- **Cons**: Complexity in implementation.

## Conclusion

Choosing the right optimizer can significantly impact the performance and convergence speed of a neural network. It often requires experimentation to determine the best one for a specific task.
"""
