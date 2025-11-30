classification_evaluation_metrics = r"""
# Evaluation Metrics for Classification Algorithms

When working with classification models, it's important to assess the model's performance using various evaluation metrics. Below are the key evaluation metrics:

### 1. **Accuracy**
Accuracy measures how often the model makes correct predictions. It's calculated as:

$$
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Where:
- **TP (True Positive)**: Correctly predicted positive instances
- **TN (True Negative)**: Correctly predicted negative instances
- **FP (False Positive)**: Incorrectly predicted positive instances
- **FN (False Negative)**: Incorrectly predicted negative instances

### 2. **Precision**
Precision focuses on how accurate the positive predictions are. It's the ratio of correctly predicted positive observations to the total predicted positives:

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

Precision answers: *Of all the observations predicted positive, how many are actually positive?*

### 3. **Recall (Sensitivity or True Positive Rate)**
Recall measures the model’s ability to detect positive instances. It's the ratio of correctly predicted positive observations to all actual positives:

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

Recall answers: *Of all the actual positive observations, how many were predicted correctly?*

### 4. **F1-Score**
The F1-score is the harmonic mean of precision and recall. It provides a balance between precision and recall and is especially useful when you need to consider both metrics:

$$
\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

F1-Score is useful when the class distribution is imbalanced.

### 5. **Specificity (True Negative Rate)**
Specificity measures the proportion of actual negatives that were correctly identified as such:

$$
\text{Specificity} = \frac{TN}{TN + FP}
$$

Specificity answers: *Of all the actual negative observations, how many were predicted correctly?*

### 6. **ROC Curve and AUC (Area Under the Curve)**
The **Receiver Operating Characteristic (ROC) curve** plots the True Positive Rate (Recall) against the False Positive Rate (FPR). The AUC represents the area under the ROC curve, which quantifies the model's ability to distinguish between classes.

- **False Positive Rate (FPR)**: The proportion of negative instances that were incorrectly classified as positive.
  
$$
\text{FPR} = \frac{FP}{FP + TN}
$$

- **AUC**: AUC represents the likelihood that the classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one. An AUC of 1 means perfect classification, while 0.5 means random guessing.

### 7. **Log Loss (Logarithmic Loss or Cross-Entropy Loss)**
Log loss measures the performance of a classification model where the prediction is a probability value between 0 and 1. It penalizes false classifications with a high degree of confidence.

$$
\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]
$$

Where:
- $y_i$ is the actual label (0 or 1)
- $\hat{y}_i$ is the predicted probability for the positive class
- $N$ is the number of samples

### 8. **Confusion Matrix**
The confusion matrix provides a complete picture of the model's performance. It breaks down the predicted outcomes into True Positives, True Negatives, False Positives, and False Negatives:

|               | Predicted Positive | Predicted Negative |
|---------------|-------------------|-------------------|
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

From the confusion matrix, you can compute metrics like accuracy, precision, recall, specificity, and more.

### 9. **Balanced Accuracy**
Balanced Accuracy is an improvement of Accuracy in cases of imbalanced datasets. It averages the recall obtained on each class.

$$
\text{Balanced Accuracy} = \frac{1}{2} \left( \frac{TP}{TP + FN} + \frac{TN}{TN + FP} \right)
$$

Balanced accuracy helps in evaluating the model when the classes are imbalanced.

## Summary of Key Metrics
- **Accuracy**: Overall correctness
- **Precision**: Correctness of positive predictions
- **Recall**: Ability to capture positive instances
- **F1-Score**: Balance between precision and recall
- **Specificity**: Correctness of negative predictions
- **ROC-AUC**: Ability to distinguish between classes
- **Log Loss**: Measure of confidence in probabilistic predictions
- **Confusion Matrix**: Detailed breakdown of model performance
"""
