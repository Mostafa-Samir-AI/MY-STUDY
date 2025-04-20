---
author: Mostafa Samir Ali
tags:
  - AI
  - Machine_learning
---

# Bias vs Variance
- First let us try to understand what these are, then we will examine Bias and Variance with the help of a sample dataset to understand the real time calculation.

- Let me try to illustrate with a simple example, an analogy before diving into the concept.

- Consider an example of a student going to attend a math exam.
- Now the task is **studying the book** or the **relevant chapter**s**/modules** for the exam.

- If the student studies by just _skimming_ over the topics and chapters instead of actually studying the same then the same student will not be able to perform well in the exam as he/she had only skimmed the topic. (underfitting)
![[Pasted image 20240908104704.png]]
<br>
<br>
- Consider another scenario wherein the student _memorizes_ all the contents in the chapters and problems instead of actually studying/understanding the concept,theories and its implication — In this case if any question which comes out of the book but based on the concepts, that student will not be able to tackle or counter the problem. (overfitting)
![[Pasted image 20240908104745.png]]
### What must be the ideal scenario for the model then?

- The ideal one is that we must be **_able to_** **_generalize the model_**. (i.e) In the above case, we must be able to resolve any problem by studying the concepts,theories and approach for the problem rather than skimming or memorizing the problems.
---
## regression models
- bias : error of the training data
- variance : error of the test data

- high bias and high variance --> under fitting
- low bias and high variance --> over fitting

## classification problem
- error is measured by percentage
<br>
<br>
**also**
<br>
<br>
- high bias and high variance --> under fitting
- low bias and high variance --> over fitting
- high bias and low variance --> error prone

- There are various ways to evaluate a machine-learning model. We can use MSE (Mean Squared Error) for Regression; Precision, Recall, and <u>ROC (Receiver of Characteristics)</u> for a Classification Problem along with Absolute Error. In a similar way, Bias and Variance help us in parameter tuning and deciding better-fitted models among several built.

- **Bias** <u>is one type of error that occurs due to wrong assumptions about data such as assuming data is linear when in reality, data follows a complex function.</u>
- **Variance** <u>gets introduced with high sensitivity to variations in training data.</u> This also is one type of error since we want to make our model robust against noise. 
- There are two types of error in machine learning. 
	- *Reducible* error and *Irreducible* error.
	- Bias and Variance come under ***reducible error***.
---
# model Bias Vs model Variance
| S.No. | Model Bias | Model Variance |
|-------|------------|----------------|
| 1 | Bias are the simplifying assumptions made by a model to make the target function easier to learn. | Variance is the amount that the estimate of the target (Y) function will change if different training data was used. |
| 2 | It captures the rigidity of the model: the strength of the assumption the model has about the functional form of the mapping between inputs and outputs. | The variance of the model is the amount the performance of the model changes when it is fit on different training data. It also captures the impacts of the specifics the data has on the model. |
| 3 | Generally, parametric algorithms have a high bias making them fast to learn and easier to understand but generally less flexible. In turn, they have lower predictive performance on complex problems that fail to meet the simplifying assumptions of the algorithm's bias. | The target function is estimated from the training data by a machine learning algorithm, so we should expect the algorithm to have some variance. Ideally, it should not change too much from one training dataset to the next, meaning that the algorithm is good at picking out the hidden underlying mapping between the inputs and the output variables. |
| 4 | A model with high bias is helpful when the bias matches the true but unknown underlying mapping function for the predictive modeling problem. Yet, a model with a large bias will be completely useless when the functional form for the problem is mismatched with the assumptions of the model, e.g., assuming a linear relationship for data with a high non-linear relationship. | A model with high variance will change a lot with small changes to the training dataset. Conversely, a model with low variance will change little with small or even large changes to the training dataset. |
| 5 | Low Bias: Suggests less assumptions about the form of the target function. | Low Variance: Suggests small changes to the estimate of the target function with changes to the training dataset. |


---
# What is Bias ?
- Bias is simply defined as the <u>inability of the model</u> because of that there is some difference or error occurring between the model’s predicted value and the actual value.
- Bias is a systematic error that occurs due to wrong assumptions in the [machine learning](https://www.geeksforgeeks.org/machine-learning/) process.
<br />
<br />

1. **True Value and Estimator**: 
   - Let \( Y \) represent the true value of a parameter or quantity we are interested in estimating.
   - Let $( \hat{Y} )$ represent an estimator of \( Y \), which is our best guess or prediction of \( Y \) based on the sample of data we have.

2. **Bias of the Estimator $( \hat{Y} )$**:
   - The bias of an estimator $( \hat{Y} )$ tells us, on average, how much the estimator $( \hat{Y} )$ differs from the true value \( Y \).
   - Mathematically, it is defined as:
     
     $$[ \text{Bias}(\hat{Y}) = E(\hat{Y}) - Y ]$$
     where $E( \hat{Y} )$ is the expected value (average value) of the estimator $( \hat{Y} )$.

3. **Interpretation**:
   - If $Bias(\hat Y) = 0$, it means that on average, our estimator $( \hat{Y} )$ is exactly equal to the true value \( Y \), indicating no bias.
   - If $Bias (\hat Y) \not = 0$, it means there is a systematic difference between the estimator $( \hat{Y} )$ and the true value \( Y \).

4. **Measurement of Fit**:
   - The bias gives us insight into how well our estimator fits the true value. A smaller bias indicates that the estimator is closer, on average, to the true value, suggesting a better fit.

- **Low Bias:** Low bias value means fewer assumptions are taken to build the target function. In this case, the model will closely match the training dataset.
- **High Bias:** High bias value means more assumptions are taken to build the target function. In this case, the model will not match the training dataset closely. ***(Under fitting)***

### Ways to reduce high bias in Machine Learning:

- **Use a more complex model:** One of the main reasons for high bias is the very simplified model. it will not be able to capture the complexity of the data. In such cases, we can make our mode more complex by increasing the number of hidden layers in the case of a [deep neural network.](https://www.geeksforgeeks.org/introduction-deep-learning/) Or we can use a more complex model like [Polynomial regression](https://www.geeksforgeeks.org/python-implementation-of-polynomial-regression/) for [non-linear datasets](https://www.geeksforgeeks.org/non-linear-regression-examples-ml/), [CNN](https://www.geeksforgeeks.org/introduction-convolution-neural-network/) for [image processing](https://www.geeksforgeeks.org/image-processing/), and [RNN](https://www.geeksforgeeks.org/introduction-to-recurrent-neural-network/) for sequence learning.
 <br />
 <br />
- **Increase the number of features:** By adding more features to train the dataset will increase the complexity of the model. And improve its ability to capture the underlying patterns in the data.
<br />
<br />

- **Reduce** [**Regularization**](https://www.geeksforgeeks.org/regularization-in-machine-learning/) **of the model:** Regularization techniques such as [L1 or L2 regularization](https://www.geeksforgeeks.org/ml-implementing-l1-and-l2-regularization-using-sklearn/) can help to prevent [overfitting](https://www.geeksforgeeks.org/underfitting-and-overfitting-in-machine-learning/) and improve the generalization ability of the model. if the model has a high bias, reducing the strength of regularization or removing it altogether can help to improve its performance.
<br />
<br />

- **Increase the size of the training data:** Increasing the size of the training data can help to reduce bias by providing the model with more examples to learn from the dataset.

# What is Variance ?
- Variance : difference in fits between datasets is called variance 
- Variance is the measure of spread in data from its mean 
- <u> the difference in fits between different datasets is called</u> **variance**
- In machine learning variance is the amount by which the performance of a predictive model changes when it is trained on different subsets of the training data.
- Variance is the variability of the model that <u>how much it is sensitive to another subset of the training dataset</u>. 
- how much it can adjust on the new subset of the training dataset.
- measured as the **MSE** 
<br />
<br />
- **Low variance:** Low variance means that the model is less sensitive to changes in the training data and can produce consistent estimates of the target function with different subsets of data from the same [distribution](https://www.geeksforgeeks.org/introduction-of-statistical-data-distributions/). This is the case of underfitting when the model fails to generalize on both training and test data.
- **High variance:** High variance means that the model is very sensitive to changes in the training data and can result in significant changes in the estimate of the target function when trained on different subsets of data from the same distribution. This is the case of overfitting when the model performs well on the training data but poorly on new, unseen test data. It fits the training data too closely that it fails on the new training dataset.

### Ways to Reduce the reduce Variance in Machine Learning:

- [**Cross-validation**](https://www.geeksforgeeks.org/cross-validation-machine-learning/)**:** By splitting the data into training and testing sets multiple times, cross-validation can help identify if a model is overfitting or underfitting and can be used to tune hyperparameters to reduce variance.
<br />
<br />
- [**Feature selection:**](https://www.geeksforgeeks.org/feature-selection-techniques-in-machine-learning/) By choosing the only relevant feature will decrease the model’s complexity. and it can reduce the variance error.
<br />
<br />
- [**Regularization**](https://www.geeksforgeeks.org/regularization-in-machine-learning/)**:** We can use L1 or L2 regularization to reduce variance in machine learning models
<br />
<br />
- [**Ensemble methods**](https://www.geeksforgeeks.org/ensemble-classifier-data-mining/)**:** It will combine multiple models to improve generalization performance. [Bagging, boosting](https://www.geeksforgeeks.org/bagging-vs-boosting-in-machine-learning/), and stacking are common ensemble methods that can help reduce variance and improve generalization performance.
<br />
<br />
- **Simplifying the model:** Reducing the complexity of the model, such as decreasing the number of parameters or layers in a neural network, can also help reduce variance and improve generalization performance.
<br />
<br />
- [**Early stopping**](https://www.geeksforgeeks.org/choose-optimal-number-of-epochs-to-train-a-neural-network-in-keras/)**:** Early stopping is a technique used to prevent overfitting by stopping the training of the deep learning model when the performance on the validation set stops improving.

![[Pasted image 20240731193738.png]]

# Bias Variance Tradeoff

- If the algorithm is too simple (hypothesis with linear equation) then it may be on high bias and low variance condition and thus is error-prone. If algorithms fit too complex (hypothesis with high degree equation) then it may be on high variance and low bias. 
- In the latter condition, the new entries will not perform well. 
- Well, there is something between both of these conditions, known as a Trade-off or Bias Variance Trade-off. 
- This tradeoff in complexity is why there is a tradeoff between bias and variance. 
- An algorithm can’t be more complex and less complex at the same time. For the graph, the perfect tradeoff will be like this.
<br />
<br />

![[Pasted image 20240731194650.png]]

# ideal model
- ideal model have low Bias --> fit the training data good but not overfitting
- also have low variability --> low variance , it can fit a testing data with low error

* we need to find the sweet spot between bias and variance where both are low values 
* this point is called sweet spot
* we use
	* Regularization
	* Boosting 
	* Bagging

- a good machine learning algorithm have low bias and low variance
- three common methods are used to find a sweet spot between simple and complex models and they are (regularization , boosting and bagging)

# practical 
- we can measure bias and variance by 2 approaches 
	1. measuring bias and variance by sklearn 
	2. measuring bias and variance by mlxtend
## Approach [1] measure with sklearn 
- steps
1. import dependencies
2. generate a dataset and split it 
3. select a model and train it
4. make predictions
5. measure both bias and variance using sklearn

### Linear Regression

#### Import dependencies
```python
# importing dependencies

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
```
- in this case of study we will use M.S.E to measure the loss 
- you can see it in [[cost function]]
#### Generate a dataset and split the data
```python
# Generate sample data
np.random.seed(0)
X = np.sort(np.random.rand(100, 1) * 2 - 1)
y = np.sin(2 * np.pi * X).ravel() + np.random.randn(100) * 0.1

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

#### Select a model and train it
- we will select a simple model to train and that is *Linear Regression*
```python
# selecting a model
from sklearn.linear_model import LinearRegression

# make instance
linear_reg = LinearRegression()

# Train a linear regression model (high bias)
linear_reg.fit(X_train, y_train)
```

#### Make predictions
```python
# Predict and calculate error for the linear model
y_train_pred_linear = linear_reg.predict(X_train) # to measure Bias
y_test_pred_linear = linear_reg.predict(X_test) # to measure Variance
```

> [!Hint] ## Pro tip
> - notice that we made prediction for 2 values `X_train` and `X_test`
> - `X_train` --> give result to `y_train_predict` ==> which is used in calculate Bias
> - `X_test` --> give result to `y_pred` ==> which is used to calculate Variance

#### Measure loss
- we use M.S.E in this approach to measure loss
```python
# calculate both Bias and variance
mse_train_linear = mean_squared_error(y_train, y_train_pred_linear) # Bias
mse_test_linear = mean_squared_error(y_test, y_test_pred_linear) # Variance

print(f'Linear Model - MSE Train: {mse_train_linear}, MSE Test: {mse_test_linear}')
```
- out `Linear Model - MSE Train: 0.42961675678188493, MSE Test: 0.5085346009643199`

### Polynomial Regression
- trying another algorithm like polynomial regression
```python
# Train a polynomial regression model (potentially high variance)
poly = PolynomialFeatures(degree=10)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_train, y_train)

# Predict and calculate error for the polynomial model
y_train_pred_poly = poly_reg.predict(X_poly_train) # to measure Bias
y_test_pred_poly = poly_reg.predict(X_poly_test) #  to measure Variance

# measure both Bias and variance 
mse_train_poly = mean_squared_error(y_train, y_train_pred_poly) # Bias 
mse_test_poly = mean_squared_error(y_test, y_test_pred_poly) # Variance

print(f'Polynomial Model - MSE Train: {mse_train_poly}, MSE Test: {mse_test_poly}')
```
- out `Polynomial Model - MSE Train: 0.009980460331205926, MSE Test: 0.008758257996484393`

### Some important notes
- we noticed that the polynomial regression preformed better than the Linear regression
- but is this really good numbers ? lets discuss it
#### Are These Values Bad?

- To assess whether the MSE values are "bad," you need to compare them to a baseline:

    1. Relative to the Scale of the Target Variable:
       - If your target values (e.g., y) are generally small (e.g., between 0 and 1), an MSE of 0.4296 or 0.5085 might be considered large.
       - If the target values are large (e.g., between 1000 and 10000), these MSE values might be small and thus acceptable.

    2. Relative to Other Models:
       - You should compare these values to other models' MSE on the same dataset. A model with a significantly lower MSE would be considered better.

    3. Rule of Thumb:
        A lower MSE indicates better model performance. However, what constitutes "low" depends on the domain, dataset, and problem context.

#### How to Interpret These Specific MSE Values:

- Are They Bad?
  - Without knowing the actual scale of your target variable, it’s hard to say definitively. However, since the MSE is a numerical value derived from your target variable’s units, the MSE should ideally be as close to zero as possible.
  - If the MSE is close to or larger than the variance of the target values, it suggests the model isn’t performing well.

Would you like to analyze it further with respect to your dataset's actual values?

#### to make it clear
- our data values are in range of [-1,1] 
- so bias and the variance in Linear Regression is too high 
- while in Polynomial Regression <u>the values of bias and variance is too low compared to the scale of the data</u> 

## Approach [2] measure Bias Variance sweet point with mlxtend

### Installation
- at first we need to install mlxtend library
```bash
pip install mlxtend 
```

### Working with mlxtend 
- we will use `bais_variance_decop` method that present in `mlxtend.evaluate` module
```python
# Estimation of bias and variance using bias_variance_decomp 
mse, bias, var = bias_variance_decomp(model_lr, X_train, y_train, X_test, y_test, loss='mse', num_rounds=200, random_seed=123)
```

- __Estimator__ : A classifier or regressor object or class implementing a fit predict method similar to the scikit-learn API.

- __X_train__ : expects an array, shape=(num_examples, num_features)

A training dataset for drawing the bootstrap samples to carry out the bias-variance decomposition.

- __y_train__ : expects an array, shape=(num_examples)

Targets (class labels, continuous values in case of regression) associated with the X_train examples.

- __X_test__ : expects an array, shape=(num_examples, num_features)

The test dataset for computing the average loss, bias, and variance.

- __y_test__ : expects an array, shape=(num_examples)

Targets (class labels, continuous values in case of regression) associated with the X_test examples.

- __loss__ : str (default='0-1_loss')

Loss function for performing the bias-variance decomposition. Currently allowed values are ‘mse’ [in case of regression] and ‘0–1_loss’ [in case of classifer].

- __num_rounds__ : int (default=200)

Number of bootstrap rounds for performing the bias-variance decomposition.

- __random_seed__ : int (default=None)

Random seed for the bootstrap sampling used for the bias-variance decomposition.

- __fit_params__ : additional parameters

Additional parameters to be passed to the .fit() function of the estimator when it is fit to the bootstrap samples (This is included as a part of latest mlxtend version)

#### Returns

- avg_expected_loss, avg_bias, avg_var : returns the average expected

average bias, and average bias (all floats), where the average is computed over the data points in the test set.

---
#### Approach 2.1 : calculating for Regression
##### (A) Linear regression
###### initializing data and preparing the model
```python
#This library is used to decompose bias and variance in our models
from mlxtend.evaluate import bias_variance_decomp
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso
import warnings
warnings.filterwarnings('ignore')

#We will load the Boston house dataset for our example
from sklearn.datasets import fetch_california_housing
from sklearn import metrics

# From the library load the necessary rows & columns
X1, y1 = fetch_california_housing(return_X_y=True)

# Split the dataset into train and test 
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.33, random_state=1)

# Model definition
model_lr = LinearRegression()
```

###### Running `bias_variance_decomp`
```python
# Estimation of bias and variance using bias_variance_decomp 
mse, bias, var = bias_variance_decomp(model_lr, X_train, y_train, X_test, y_test, loss='mse', num_rounds=200, random_seed=123)
y_pred=model_lr.predict(X_test)
```

###### Summarize the result
```python
# summarize results
print('MSE from bias_variance lib [avg expected loss]: %.3f' % mse)
print('Avg Bias: %.3f' % bias)
print('Avg Variance: %.3f' % var)
print('Mean Square error by Sckit-learn lib: %.3f' % metrics.mean_squared_error(y_test,y_pred))
```
- out 
```txt
MSE from bias_variance lib [avg expected loss]: 0.527
Avg Bias: 0.525
Avg Variance: 0.002
Mean Square error by Sckit-learn lib: 0.527
```

##### After scaling
```python
# using standardization
from sklearn.preprocessing import StandardScaler
scaling = StandardScaler()

# scaling both X and Y
X1 = scaling.fit_transform(X1)
y1 = scaling.fit_transform(y1.reshape(20640 , 1))
```

###### Running 
```python
# should squeeze to original shape
y1 = np.squeeze(y1)

# data splitting
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.33, random_state=1)

# Model definition
model_lr = LinearRegression()

# Estimation of bias and variance using bias_variance_decomp 
#Note here we are using loss as 'mse' and setting default bootstrap num_rounds to 200
mse, bias, var = bias_variance_decomp(model_lr, X_train, y_train, X_test, y_test, loss='mse', num_rounds=200, random_seed=123)
y_pred=model_lr.predict(X_test)


# summarize results
print('MSE from bias_variance lib [avg expected loss]: %.3f' % mse)
print('Avg Bias: %.3f' % bias)
print('Avg Variance: %.3f' % var)
print('Mean Square error by Sckit-learn lib: %.3f' % metrics.mean_squared_error(y_test,y_pred))
```
- out
```txt
MSE from bias_variance lib [avg expected loss]: 0.396
Avg Bias: 0.394
Avg Variance: 0.002
Mean Square error by Sckit-learn lib: 0.396
```

##### (B) Lasso Regression 
```python
# importing lasso regression
from sklearn.linear_model import Lasso

# initializing lasso regression
lasso_model = Lasso(alpha=0.05)

# calculating the error
error_reg_las, bias_reg_las, var_reg_las = bias_variance_decomp(lasso_model, X_train, y_train, X_test, y_test, loss='mse', random_seed=123)

# dispaly result
print('MSE from bias_variance lib [avg expected loss]: %.3f' % error_reg_las)
print('Avg Bias: %.5f' % bias_reg_las)
print('Avg Variance: %.5f' % var_reg_las)
print('Mean Square error by Sckit-learn lib: %.3f' % metrics.mean_squared_error(y_test,y_pred))
```
- out
```txt
MSE from bias_variance lib [avg expected loss]: 0.557
Avg Bias: 0.55636
Avg Variance: 0.00057
Mean Square error by Sckit-learn lib: 6.277
```

---
#### Approach 2.2 : Calculate for Classifiers
- For classifier, we are going to use the same library — the only difference is the loss function.
- Here we are going to use- 0–1 loss function.
- Let us say you have a classification problem (0 or 1) and say hypothetically your dataset has 20 rows.
- After classification with any of the algorithms, eg: naive baye’s — if we find out that it has predicted 15 correctly and 5 were misclassified this is identified and is called as 0–1 loss.
- __All the rightly predicted items 15 will be marked as “0” and all the misclassified items will be marked as “1”__.
- Bias is 1 if the main prediction does not agree with the true label y and 0 otherwise
- The Variance of the 0–1 loss is defined as the probability that the predicted label does not match the main prediction:
<br>
<br>

- Variance = $P(ŷ ≠ E[ŷ])$

$$\boxed{Loss= Bias+variance}$$

---
- load the data
```python
# importing 0-1 loss
from sklearn.metrics import zero_one_loss

# loading iris dataset
from sklearn.datasets import load_iris

iris = load_iris()

X , y = iris.data , iris.target


#splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=123,
                                                    shuffle=True,
                                                    stratify=y)
```

##### Decision Tree
```python
# importing decision tree
from sklearn.tree import DecisionTreeClassifier

# instance of the model
clf_dt = DecisionTreeClassifier(random_state=123)

# training the model
clf_dt.fit(X_train,y_train)

# testing the prediction
y_pred=clf_dt.predict(X_test)

# calculating the error
avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
        clf_dt, X_train, y_train, X_test, y_test, 
        loss='0-1_loss',
        random_seed=123)

print("before pruning\n")
print('Average expected loss: %.3f' % avg_expected_loss)
print('Average bias: %.3f' % avg_bias)
print('Average variance: %.3f' % avg_var)
print('Sklearn 0-1 loss: %.3f\n\nafter pruning\n' % zero_one_loss(y_test,y_pred))


### After Pruning ###
clf_dt_prnd = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=123)

# training
clf_dt_prnd.fit(X_train,y_train)

# testing
y_pred=clf_dt_prnd.predict(X_test)

#calculating the error
avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
        clf_dt_prnd, X_train, y_train, X_test, y_test, 
        loss='0-1_loss',
        random_seed=123)

print('Average expected loss--After pruning: %.3f' % avg_expected_loss)
print('Average bias--After pruning: %.3f' % avg_bias)
print('Average variance--After pruning: %.3f' % avg_var)
print('Sklearn 0-1 loss--After pruning: %.3f' % zero_one_loss(y_test,y_pred))
```
- out 
```txt
before pruning

Average expected loss: 0.062
Average bias: 0.022
Average variance: 0.040
Sklearn 0-1 loss: 0.133

after pruning

Average expected loss--After pruning: 0.060
Average bias--After pruning: 0.022
Average variance--After pruning: 0.038
Sklearn 0-1 loss--After pruning: 0.089
```

##### Random Forest 
```python
# import random forest
from sklearn.ensemble import RandomForestClassifier

# instance of the model
clf_RF = RandomForestClassifier(max_depth=2, random_state=0)

# training the model
clf_RF.fit(X_train,y_train)

# testing
y_pred=clf_RF.predict(X_test)

# calculating the error
avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
        clf_RF, X_train, y_train, X_test, y_test, 
        loss='0-1_loss',
        random_seed=123)

print('Average expected loss: %.3f' % avg_expected_loss)
print('Average bias: %.3f' % avg_bias)
print('Average variance: %.3f' % avg_var)
print('Sklearn 0-1 loss: %.3f' % zero_one_loss(y_test,y_pred)) 
```

- out 
```txt
Average expected loss: 0.045
Average bias: 0.022
Average variance: 0.023
Sklearn 0-1 loss: 0.022
```

<br>
<br>

---
<br>
<br>

# resources
- https://medium.com/analytics-vidhya/calculation-of-bias-variance-in-python-8f96463c8942 (median)
- https://www.geeksforgeeks.org/bias-vs-variance-in-machine-learning/ (geeks for geeks)
- https://youtu.be/EuBBz3bI-aA?si=FBoeosYobuJlyrAz (StatQuest)
- https://github.com/rasbt/mlxtend (mlxtend library)
