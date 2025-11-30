zscore_markdown = r"""
# Z-Score Method of Anomaly Detection

## Introduction
The Z-Score method is a statistical technique used to identify anomalies in a dataset. It measures how many standard deviations an element is from the mean of the dataset. If the Z-Score of a data point exceeds a certain threshold, it is considered an anomaly.

## Formula
The Z-Score for a data point $$( x )$$ is calculated using the formula:

$$
Z = \frac{x - \mu}{\sigma}
$$

Where:
- $$( Z )$$ is the Z-Score
- $$( x )$$ is the data point
- $$( mu )$$ is the mean of the dataset
- $$( \sigma )$$ is the standard deviation of the dataset

## Steps to Implement Z-Score Anomaly Detection

1. **Collect Data**: Gather the data that you want to analyze for anomalies.
  
2. **Calculate the Mean**: Compute the mean ($$ \mu $$) of the dataset.
  
3. **Calculate the Standard Deviation**: Compute the standard deviation ($$ \sigma $$) of the dataset.
  
4. **Calculate Z-Scores**: For each data point, calculate its Z-Score using the formula mentioned above.

5. **Set a Threshold**: Determine a threshold value for the Z-Score. Common choices are 2 or 3, meaning that any data point with a Z-Score beyond this threshold is considered an anomaly.

6. **Identify Anomalies**: Compare each Z-Score to the threshold. Data points with Z-Scores greater than the threshold are flagged as anomalies.

## Example
```python
import numpy as np

# Sample data
data = [10, 12, 12, 13, 12, 14, 15, 19, 22, 25, 30]

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Calculate Z-Scores
z_scores = [(x - mean) / std_dev for x in data]

# Set threshold
threshold = 2

# Identify anomalies
anomalies = [data[i] for i, z in enumerate(z_scores) if abs(z) > threshold]

print("Anomalies:", anomalies)
```

"""
