loss_functions_markdown = r"""
# Loss Functions in Deep Learning

In deep learning, the loss function (or objective function) is used to measure how well the model's predictions match the true target values. Loss functions vary depending on the problem type (regression, classification, etc.).

### 1. **Mean Squared Error (MSE)**
- **Used For**: Regression problems.
- **Definition**: MSE calculates the average of the squared differences between predicted and true values.
- **Formula**: 
    $$
    MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    $$
    where $$y_i$$ is the true value and $$\hat{y}_i$$ is the predicted value.
    
- **Characteristics**: 
  - Penalizes larger errors more than smaller ones due to squaring.
  - It is a smooth and differentiable function, making it ideal for gradient-based optimization.

---

### 2. **Mean Absolute Error (MAE)**
- **Used For**: Regression problems.
- **Definition**: MAE calculates the average of the absolute differences between predicted and true values.
- **Formula**:
    $$
    MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
    $$
    
- **Characteristics**:
  - Treats all errors equally.
  - Less sensitive to outliers compared to MSE.
  - Not differentiable at zero, which can make optimization slightly harder.

---

### 3. **Huber Loss**
- **Used For**: Regression problems.
- **Definition**: Huber loss is a combination of MSE and MAE. It behaves like MAE for large errors and like MSE for smaller errors.
- **Formula**:
    $$
    L_{\delta}(y, \hat{y}) = 
    \begin{cases} 
    \frac{1}{2} (y_i - \hat{y}_i)^2 & \text{for } |y_i - \hat{y}_i| \leq \delta \\
    \delta \cdot (|y_i - \hat{y}_i| - 0.5 \cdot \delta) & \text{otherwise}
    \end{cases}
    $$
    
- **Characteristics**:
  - Less sensitive to outliers than MSE.
  - Smooth and differentiable for both small and large errors.

---

### 4. **Cross-Entropy Loss**
- **Used For**: Classification problems.
- **Definition**: Cross-entropy loss (or log loss) is used for binary or multi-class classification problems. It measures the difference between two probability distributions: the true label distribution and the predicted probability distribution.
- **Formula (Binary Classification)**:
    $$
    L(y, \hat{y}) = - \left( y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \right)
    $$
    where $$y$$ is the true label (0 or 1), and $$\hat{y}$$ is the predicted probability.
  
- **Formula (Multi-Class Classification)**:
    $$
    L(y, \hat{y}) = - \sum_{i=1}^{C} y_i \log(\hat{y}_i)
    $$
    where $$C$$ is the number of classes, $$y_i$$ is the true label (one-hot encoded), and $$\hat{y}_i$$ is the predicted probability for class $$i$$.
    
- **Characteristics**:
  - Encourages correct class probabilities to be maximized.
  - Penalizes incorrect predictions more severely when the predicted probability is far from the true label.

---

### 5. **Kullback-Leibler Divergence (KL Divergence)**
- **Used For**: Measuring the difference between two probability distributions.
- **Definition**: KL Divergence measures how one probability distribution $$P$$ diverges from a second, approximate distribution $$Q$$.
- **Formula**:
    $$
    D_{KL}(P || Q) = \sum_{i} P(x_i) \log \left( \frac{P(x_i)}{Q(x_i)} \right)
    $$
    
- **Characteristics**:
  - Asymmetric (i.e., $$D_{KL}(P || Q) \neq D_{KL}(Q || P)$$).
  - Useful for applications like variational autoencoders (VAEs).

---

### 6. **Hinge Loss**
- **Used For**: Binary classification with Support Vector Machines (SVMs).
- **Definition**: Hinge loss is used for "maximum-margin" classification problems, such as SVMs.
- **Formula**:
    $$
    L(y, \hat{y}) = \max(0, 1 - y \cdot \hat{y})
    $$
    where $$y$$ is the true label ($$-1$$ or $$1$$) and $$\hat{y}$$ is the predicted label.
    
- **Characteristics**:
  - Encourages predictions to be far from the decision boundary.
  - Only penalizes predictions that are on the wrong side of the margin.

---

### 7. **Cosine Similarity Loss**
- **Used For**: Tasks involving similarity measurement (e.g., face recognition).
- **Definition**: Cosine similarity measures the cosine of the angle between two vectors, used to compute the loss based on how similar two vectors are.
- **Formula**:
    $$
    L(y, \hat{y}) = 1 - \cos(\theta) = 1 - \frac{y \cdot \hat{y}}{\|y\| \| \hat{y} \|}
    $$
    
- **Characteristics**:
  - Often used in problems like document similarity, facial recognition, etc.
  - The closer the vectors, the smaller the loss.

---
### 8. **Negative Log Likelihood (NLL)**
- **Used For**: Multi-class classification.
- **Definition**: NLL is similar to cross-entropy, but it works directly with log-probabilities instead of probabilities.
- **Formula**:
    $$
    L(y, \hat{y}) = -\sum_{i=1}^{C} y_i \log(\hat{y}_i)
    $$
    
- **Characteristics**:
  - Suitable for models that output log-probabilities (e.g., softmax).
  - Can be used with class weights to handle imbalanced datasets.

---

### 9. **Poisson Loss**
- **Used For**: Count data.
- **Definition**: Poisson loss is suitable for modeling count data and is often used in Poisson regression models.
- **Formula**:
    $$
    L(y, \hat{y}) = \hat{y} - y \cdot \log(\hat{y})
    $$
    
- **Characteristics**:
  - Useful when predicting the occurrence of an event over a fixed period.
  - Assumes that the predicted value is a positive rate.

"""
