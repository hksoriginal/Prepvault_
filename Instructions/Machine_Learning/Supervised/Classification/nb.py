naive_bayes_explanation = r"""
# Naive Bayes Algorithm

## Overview
Naive Bayes is a family of probabilistic algorithms based on Bayes' Theorem, used for classification tasks. It assumes that the presence of a particular feature in a class is independent of the presence of any other feature. Despite its simplicity and the strong independence assumption, Naive Bayes performs surprisingly well in many real-world applications.

## Bayes' Theorem
Bayes' Theorem is given by the formula:

$$
P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}
$$

Where:
- \( P(A|B) \): The probability of class \( A \) given the feature \( B \) (posterior).
- \( P(B|A) \): The probability of feature \( B \) given the class \( A \) (likelihood).
- \( P(A) \): The probability of class \( A \) (prior).
- \( P(B) \): The probability of feature \( B \) (evidence).

## Types of Naive Bayes Classifiers
1. **Gaussian Naive Bayes**: Assumes that the features follow a Gaussian (normal) distribution.
2. **Multinomial Naive Bayes**: Used for discrete data, commonly used in text classification.
3. **Bernoulli Naive Bayes**: Similar to Multinomial Naive Bayes but assumes binary features (0 or 1).

## Steps in Naive Bayes Classification
1. **Training Phase**:
   - Calculate prior probabilities \( P(A) \) for each class.
   - Calculate the likelihood \( P(B|A) \) for each feature given the class.

2. **Prediction Phase**:
   - For a new instance, calculate the posterior probability for each class using Bayes' Theorem.
   - Select the class with the highest posterior probability.

## Advantages
- **Simplicity**: Easy to understand and implement.
- **Efficiency**: Fast training and prediction.
- **Performance**: Works well with large datasets.

## Disadvantages
- **Independence Assumption**: Assumes that features are independent, which is rarely the case in real-world data.
- **Zero Probability Problem**: If a class does not have a particular feature, it can lead to a zero probability in the calculation. This can be mitigated using Laplace Smoothing.

## Example Code (Python)
Here’s a simple implementation using the `scikit-learn` library:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Naive Bayes classifier
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
```
"""
