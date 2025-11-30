svm_explanation = r"""
# Support Vector Machine (SVM)

A **Support Vector Machine (SVM)** is a supervised machine learning algorithm used for classification, regression, and outlier detection. SVMs are most commonly used for classification tasks.

## Key Concepts:

### 1. **Hyperplane**
In the context of SVM, a hyperplane is a decision boundary that separates different classes. The hyperplane can be thought of as a line in two-dimensional space or a plane in three dimensions. In higher dimensions, it's referred to as a hyperplane.

- For a binary classification problem, the goal of SVM is to find the optimal hyperplane that best separates the two classes.

### 2. **Support Vectors**
Support vectors are the data points that are closest to the hyperplane. These points are critical for determining the position of the hyperplane. The hyperplane is defined in such a way that it maximizes the margin between the two classes, and support vectors are the ones that lie on the boundary of this margin.

### 3. **Margin**
The margin is the distance between the hyperplane and the nearest data points (support vectors) from both classes. SVM aims to maximize this margin to ensure that the model has a better generalization capability.

### 4. **Hard Margin vs Soft Margin**
- **Hard Margin**: The model assumes that all data points are perfectly separable. However, in real-world problems, this is not often the case.
- **Soft Margin**: To handle noise or overlap between classes, SVM introduces the concept of a soft margin, which allows some data points to violate the margin or even be misclassified.

### 5. **Kernel Trick**
For cases where the data is not linearly separable, SVM uses a technique called the **kernel trick**. The kernel trick maps the input data into a higher-dimensional feature space, where a linear hyperplane can separate the classes. Popular kernels include:
- **Linear Kernel**: Works when the data is linearly separable.
- **Polynomial Kernel**: Maps the input data into a higher polynomial space.
- **Radial Basis Function (RBF) Kernel**: A popular choice for non-linearly separable data.

### 6. **Mathematical Formulation**
The decision boundary can be defined as:
$$
w \cdot x + b = 0
$$
Where:
- \( w \) is the weight vector (normal to the hyperplane),
- \( x \) is the input vector (data point),
- \( b \) is the bias term (offset of the hyperplane).

The goal of SVM is to solve the following optimization problem:
$$
\min \frac{1}{2} ||w||^2
$$
Subject to the constraint:
$$
y_i (w \cdot x_i + b) \geq 1 \quad \text{for all } i
$$
Where \( y_i \) is the class label of the data point \( x_i \).

### 7. **Advantages of SVM:**
- **Effective in high-dimensional spaces**: SVM works well with a large number of features, especially when the number of dimensions exceeds the number of samples.
- **Robust to outliers**: Thanks to the margin, SVM focuses on the support vectors and is less sensitive to outliers.
- **Versatile**: By using different kernel functions, SVM can handle both linearly separable and non-linearly separable data.

### 8. **Disadvantages of SVM:**
- **Choice of kernel**: The performance of SVM heavily depends on the choice of kernel and its parameters.
- **Memory-intensive**: SVM can be memory-intensive for large datasets, especially when the number of support vectors is large.
- **Slow for large datasets**: Training time increases significantly with the size of the dataset.

## Example Use Case
SVM can be used for a wide range of applications, including:
- **Image classification**
- **Text categorization**
- **Bioinformatics** (e.g., cancer detection)
- **Spam detection**

## Python Example using SVM (with Scikit-learn)
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the SVM model (RBF kernel)
svm_model = SVC(kernel='rbf', gamma='auto')

# Train the model
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(report)
"""