regression_evaluation_metrices = r"""
# Evaluation Metrics for Regression Machine Learning Algorithms

Evaluating the performance of regression models requires specific metrics to measure how well the model's predicted values match the actual values. Below are the commonly used evaluation metrics:

## 1. Mean Absolute Error (MAE)
MAE measures the average of the absolute differences between predicted and actual values. It gives an idea of how much error to expect from the predictions, without considering the direction of the error.

**Formula:**

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$


Where:
- $$( y_i )$$ = Actual value
- $$( \hat{y}_i )$$ = Predicted value
- $$( n )$$ = Total number of data points


## 2. Mean Squared Error (MSE)
MSE calculates the average of the squared differences between predicted and actual values. By squaring the errors, this metric gives higher weight to larger errors, making it more sensitive to outliers.

**Formula:**

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

## 3. Root Mean Squared Error (RMSE)
RMSE is the square root of MSE. It provides an error metric in the same units as the target variable, making it more interpretable. Like MSE, RMSE penalizes larger errors more than smaller ones.

**Formula:**

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

## 4. R-squared (R²)
R² measures the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, where 1 indicates that the model perfectly predicts the target variable, and 0 means the model explains none of the variability.

**Formula:**

$$
R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
$$

Where:
- $$( \bar{y} )$$ = Mean of the actual values

## 5. Adjusted R-squared
Adjusted R² accounts for the number of predictors in the model. It adjusts the R² value by penalizing the addition of non-informative predictors.

**Formula:**

$$
\text{Adjusted } R^2 = 1 - \left( \frac{(1 - R^2)(n - 1)}{n - p - 1} \right)
$$

Where:
- $$( p )$$ = Number of predictors
- $$( n )$$ = Number of observations

## 6. Mean Absolute Percentage Error (MAPE)
MAPE expresses the error as a percentage of the actual values, making it useful when the scale of the target variable is important.

**Formula:**

$$
\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100
$$

## 7. Explained Variance Score
This metric measures how much of the variance in the target variable is explained by the model, similar to R² but without normalization to the total variance.

**Formula:**

$$
\text{Explained Variance} = 1 - \frac{\text{Var}(y_i - \hat{y}_i)}{\text{Var}(y_i)}
$$

## Conclusion
Each of these metrics provides a different perspective on the model's performance, and the choice of metric depends on the specific problem. For example, MSE and RMSE emphasize larger errors more, while MAE provides a balanced view of error magnitude. R² and Adjusted R² help in understanding the explanatory power of the model.
"""
