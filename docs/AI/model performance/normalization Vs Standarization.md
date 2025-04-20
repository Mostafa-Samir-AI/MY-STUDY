---
author: Mostafa Samir Ali
tags:
  - AI
---

- standardization --> normal dist
- normalization
- robust scaling ❓
- log scaling ❓
# normalization and standardization

- normalization helps to scale the data between 0 and 1 [0:1]
- standardization helps to scale the value according to <u>standard normal distribution</u>  --> the mean is 0 and the standard deviation is 1 [-1:1] 

<br>

- the formula for normalization is $$X_n = \frac{X - X\ min}{X\ max - X\ min} $$
- the formula for standardization (also called Z-normalization)$$z = \frac{x-\mu}{\sigma}$$

## some algorithms do not require scaling the values you have like 
- decision tree 
- random forest  
- XG Boost
- all Boosting algorithms

---

- Normalization and standardization are two techniques used to transform data into a common scale. 
- Normalization is a technique used to scale numerical data in the range of 0 to 1. This technique is useful when the distribution of the data is not known or when the data is not normally distributed. 
- On the other hand, standardization is a technique used to transform data into a standard normal distribution. This technique is useful when the distribution of the data is known and when the data is normally distributed. 
- Both techniques have different applications, and choosing the right technique based on the data and the problem you're trying to solve is important.

*  Normalization and standardization are two essential techniques used in data preprocessing in machine learning and data science. Both techniques are used to transform data into a common scale to make it easier to process and analyze. 
* Although these techniques are often used interchangeably, they have different applications and can be used in different contexts. In this article, we will explore the differences between normalization and standardization, their applications, and how to use them effectively in your data analysis.

### Table of Contents

- Difference Between Normalization and Standardization: Normalization vs Standardization
- What is Normalization?
    - Advantages and Disadvantages
- What is Standardization?
    - Advantages and Disadvantages
- When to use Normalization?
- When to use Standardization?
- Key Difference Between Normalization and Standardization

### What is the Difference Between Standardization and Normalization?

|Parameter|Standardization|Normalization|
|---|---|---|
|Definition|Transforms data to have a mean of 0 and a standard deviation of 1.|Scales data to a fixed range, typically 0 to 1.|
|Formula|Z = (x-mean)/standard deviation|Xnorm = (X - Xmax) / (Xmax - Xmin)|
|Objective|To change the distribution of the variables to a standard normal distribution.|To change the scale of the variables so that they fit within a specific range.|
|Dependency on Distribution|Assumes the distribution of data is normal.|Does not assume any distribution of the data.|
|Use Cases|Useful in algorithms that assume data is normally distributed, e.g., linear regression and logistic regression.|Useful in algorithms that are sensitive to the magnitude of values, e.g., neural networks, k-nearest neighbours.|
|Sensitivity to Outliers|Less sensitive to outliers.|Highly sensitive to outliers since min and max are affected by extreme values.|
|Scale of Transformation|Variable scales are transformed to center around 0, with deviations measured in units of the standard deviation.|Variable scales are compressed or stretched to fit within the target range.|
|Suitability for Data|More suitable for data with a Gaussian distribution or when maintaining zero-centered data is important.|Suitable for data that does not follow a Gaussian distribution and when a bounded range is necessary.|
|Impact on Shape of Data|Maintains the shape of the original data distribution but aligns it to a standard scale.|It may alter the shape of the data distribution, especially if there are significant outliers.|

# What is Normalization?

Normalization in machine learning is a data preprocessing technique used to change the value of the numerical column in the dataset to a common scale without distorting the differences in the range of values or losing information.

In simple terms, normalization refers to the process of transforming features in a dataset to a specific range. This range can be different depending on the chosen normalization technique.

The two most common normalization techniques are Min-Max Scaling and Z-Score Normalization, which is also called standardization.

**Min-Max Scaling**

This method rescales the features to a fixed range, usually 0 to 1. The formula for calculating the scaled value of a feature is:

**Normalized Value = (Value - Min) / (Max - Min)**

Where:

- **Value**: Original value of the feature.
- **Min**: Minimum value of the feature across all the data points.
- **Max**: Maximum value of the feature across all the data points.

**Advantages and Disadvantages of Normalization**

|Advantages|Disadvantages|
|---|---|
|Improves Algorithm Performance: Normalization can lead to faster convergence and improve the performance of machine learning algorithms, especially those that are sensitive to the scale of input features.|Data Dependency: The normalization process makes the training data dependent on the specific scale, which might not be appropriate for all kinds of data distributions.|
|Consistent Scale: It brings all the variables to the same scale, making it easier to compare the importance of features directly.|Loss of Information: In some cases, normalization can lead to a loss of information, especially if the data is sparse and the normalization compresses different values into a small range.|
|Reduces the Impact of Outliers: Methods like Min-Max scaling can reduce the impact of outliers, although this can also be a disadvantage in cases where outliers are important.|Sensitivity to New Data: The parameters used for normalization (min, max, mean, standard deviation) can change with the introduction of new data, requiring re-normalization with updated parameters.|
|Necessary for Certain Algorithms: Some algorithms, like k-nearest Neighbors (k-NN) and neural networks, require data to be normalized for effective performance.|May Not Always Improve Performance: For some algorithms, particularly tree-based algorithms like decision trees and random forests, normalization may not improve and can sometimes even degrade the model’s performance.|
|Easier to Learn: When features are on a similar scale, gradient descent (used in training many machine learning models) can converge more quickly.|Time and Resources: The normalization process adds extra steps to data preprocessing, which requires additional computation time and resources.|

# What is Standardization?

Standardization is a data preprocessing technique used in statistics and machine learning to transform the features of your dataset so that they have a mean of 0 and a standard deviation of 1. This process involves rescaling the distribution of values so that the mean of observed values is aligned to 0 and the standard deviation to 1.

- Standardization aims to adjust the scale of data without distorting differences in the ranges of values or losing information.
- Unlike other scaling techniques, standardization maintains all original data points' information (except for cases of constant columns).
- It ensures that no single feature dominates the model's output due to its scale, leading to more balanced and interpretable models.

#### Formula of Standardization

**Z = (x-mean)/standard deviation**

#### Advantages and Disadvantages of Standardization

**Advantages:**

- Improves Convergence Speed: Standardization can speed up the convergence of many machine learning algorithms by ensuring features have the same scale.
- Handles Outliers Better: It is less sensitive to outliers compared to Min-Max scaling because it scales data based on the distribution's standard deviation.
- Useful for Algorithms Assuming Normal Distribution: Many machine learning algorithms assume that the input features are normally distributed. Standardization makes this assumption more valid.
- Easier Feature Comparison: Standardized features have a mean of 0 and a standard deviation of 1, making it easier to compare the importance of different features directly.
- Necessary for Certain Algorithms: Algorithms like Support Vector Machines (SVM), k-nearest Neighbors (k-NN), and Principal Component Analysis (PCA) often perform better with standardized data.
- Facilitates Gradient Descent: For models that use gradient descent as an optimization technique, standardization helps prevent the optimization from being skewed by the feature scale.

**Disadvantages:**

- Not Bound to a Specific Range: Unlike Min-Max scaling, standardization does not bound features to a specific range, which might be a requirement for certain algorithms.
- May Hide Useful Information: In some cases, the process of standardizing can hide useful information about outliers that could be beneficial for the model.
- Requirement for Recalculation: Whenever new data is added to the dataset, the standardization process may need to be recalculated and applied again to maintain consistency.
- May Not Be Necessary for Some Models: For models like decision trees and random forests, standardization may not affect their performance, as these models are not sensitive to the scale of the input features.
- Computational Resources: The process requires additional computations, which can be a concern for very large datasets or limited computational resources.
- Misinterpretation of Results: The transformation of features into a standard scale can sometimes make the interpretation of results more challenging, especially for those not familiar with the transformed scale.

# When to use Normalization?

- **When using algorithms that assume the input features are on a similar scale or bounded range**, such as neural networks. These algorithms often assume input values are in the range [0,1].
- When you want to speed up the convergence of gradient descent by ensuring all features contribute equally to the cost function.
- If the data doesn't follow a Gaussian distribution.
- For models where the magnitude of variables is important, such as k-nearest neighbours.

# When to use Standardization?

- **Algorithms that assume the input features are normally distributed with zero mean and unit variance**, such as Support Vector Machines, Logistic Regression, etc.
- Standardization can be a better choice if your data contains many outliers as it scales the data based on the standard deviation.
- It is often used before applying Principal Component Analysis (PCA) to ensure that each feature contributes equally to the analysis.
- If the data features exhibit a Gaussian distribution, meaning that the data is normally distributed.

# Key Difference Between Normalization and Standardization

- Standardization transforms data to have a mean of 0 and a standard deviation of 1, whereas normalization scales the data to a specific user-defined range between 0-1 or -1-1.
- Normalization makes no assumption about the underlying data distribution, while standardization


# practical

- applying normalization and standardization in code

## normalization
- in order to use normalization we need to import the (MinMaxScaler) function from sklearn library , preprocessing module
- steps:-
	1. import MinMaxScaler
	2. fit transform the features
	3. replace the old features with the scaled one

```python
# import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

# make an object from the function
scalling  = MinMaxScaler()

# scalling the data features 
scalling.fit_transform(df[["col_1" , "col_2"]])

# replacing the old data with the scalled data
df[["col_1" , "col_2"]] = scalling.fit_transform(df[["col_1" , "col_2"]])
```


## standardization
- in order to use normalization we need to import the (StandardScaler) function from sklearn library , preprocessing module
- steps:-
	1. import StandardScaler
	2. fit transform the features
	3. replace the old features with the scaled one

```python
# import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# make an object from the function
scalling  = StandardScaler()

# scalling the data features 
scalling.fit_transform(df[["col_1" , "col_2"]])

# replacing the old data with the scalled data
df[["col_1" , "col_2"]] = scalling.fit_transform(df[["col_1" , "col_2"]])
```

