---
author: Mostafa Samir Ali
tags:
  - AI
---
# hypothesis testing
 - A **statistical hypothesis test** is a method of statistical inference used to decide whether the data sufficiently supports a particular hypothesis.
- A statistical hypothesis test typically involves a calculation of a [test statistic](https://en.wikipedia.org/wiki/Test_statistic "Test statistic"). Then a decision is made, either by comparing the test statistic to a [critical value](https://en.wikipedia.org/wiki/Critical_value_(statistics) "Critical value (statistics)") or equivalently by evaluating a [_p_-value](https://en.wikipedia.org/wiki/P-value "P-value") computed from the test statistic. 

# p-value 
- p-value is used to quantify how confident we are that A is different than B 
- the closer p-value to 0 , the more confident we have that A is different than B 
* **the less the p-value the more we reject the null hypothesis , if the p-value less than the threshold we applied , then we will reject the null hypothesis**  
- the smaller --> the more different 
- the bigger --> the more similar
- getting a *small p-value* where there is *no difference* is called a **false positive** 
- false positive is a wrong assumption or claim about the hypothesis 
* determining whether a is different than b is called hypothesis testing

- in linear regression our hypothesis is the feature have a strong correlation with the target
- while the null hypothesis is the feature don't have a strong correlation with the target

# p-value coding

This Python code is used to perform Ordinary Least Squares (OLS) regression on the Diabetes dataset from `sklearn`. It uses both `statsmodels` and `scikit-learn` libraries to run the regression and display the results. Here's a step-by-step breakdown of the code:

### 1. **Import Required Libraries**
```python
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
```
- `pandas` and `numpy`: These are general-purpose libraries for data manipulation and numerical operations.
- `datasets`: A module in `sklearn` that provides a collection of toy datasets, including the `diabetes` dataset.
- `linear_model`: A submodule from `sklearn` for linear models, but in this code, it's not used directly for training the model (the code uses `statsmodels` for regression).
- `statsmodels.api`: This is a statistical modeling library that includes tools for fitting statistical models, like Ordinary Least Squares (OLS) regression.
- `scipy.stats`: Provides statistical functions (though it's not used in this code).

### 2. **Load Diabetes Dataset**
```python
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target
```
- `diabetes = datasets.load_diabetes()`: Loads the diabetes dataset, which contains medical records (e.g., age, BMI, blood pressure) and a target variable, which is a disease progression measure.
- `X = diabetes.data`: This contains the independent variables (features) of the dataset, such as age, sex, BMI, etc.
- `y = diabetes.target`: This is the dependent variable, representing the disease progression measure.

### 3. **Add Constant to the Features Matrix**
```python
X2 = sm.add_constant(X)
```
- `sm.add_constant(X)`: Adds a constant (intercept term) to the features matrix `X`. This step is necessary for the OLS regression in `statsmodels` to include the intercept in the model. In regression, the constant term represents the baseline value when all predictors are zero.

### 4. **Fit an OLS Model using `statsmodels`**
```python
est = sm.OLS(y, X2)
est2 = est.fit()
```
- `sm.OLS(y, X2)`: This creates an OLS regression model where:
  - `y` is the dependent variable (target),
  - `X2` is the independent variables (features) including the constant term.
  
- `est.fit()`: Fits the OLS model to the data. The result is stored in `est2`, which contains all the estimated coefficients, statistics, and other results from the regression.

### 5. **Display the Summary of the Model**
```python
print(est2.summary())
```
- `est2.summary()`: Displays a detailed summary of the fitted regression model, which includes:
  - Coefficients for each feature and the intercept.
  - Statistical significance of each coefficient (p-values).
  - R-squared value, which indicates the proportion of variance explained by the model.
  - Other metrics like standard errors, t-values, confidence intervals, F-statistic, and more.

### Summary of Output from `est2.summary()`
The output summary provides detailed statistics about the OLS regression:
- **coef**: Coefficients for each feature and the intercept.
- **std err**: Standard error of each coefficient.
- **t**: t-statistic, used to test whether the coefficient is significantly different from zero.
- **P>|t|**: p-value corresponding to the t-test. Small p-values (usually < 0.05) suggest that the corresponding feature is statistically significant.
- **[0.025, 0.975]**: The 95% confidence interval for each coefficient.
- **R-squared**: The proportion of the variance in the dependent variable that is predictable from the independent variables.
- **Adj. R-squared**: Adjusted R-squared, which accounts for the number of predictors in the model.

### Conclusion
This code performs OLS regression on the diabetes dataset using `statsmodels`. It adds a constant term to the feature matrix (for the intercept), fits an OLS model, and then outputs a summary of the results, which includes the estimated coefficients and their statistical significance.


```python
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())
```

```python
                         OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.518
Model:                            OLS   Adj. R-squared:                  0.507
Method:                 Least Squares   F-statistic:                     46.27
Date:                Wed, 08 Mar 2017   Prob (F-statistic):           3.83e-62
Time:                        10:08:24   Log-Likelihood:                -2386.0
No. Observations:                 442   AIC:                             4794.
Df Residuals:                     431   BIC:                             4839.
Df Model:                          10                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        152.1335      2.576     59.061      0.000     147.071     157.196
x1           -10.0122     59.749     -0.168      0.867    -127.448     107.424
x2          -239.8191     61.222     -3.917      0.000    -360.151    -119.488
x3           519.8398     66.534      7.813      0.000     389.069     650.610
x4           324.3904     65.422      4.958      0.000     195.805     452.976
x5          -792.1842    416.684     -1.901      0.058   -1611.169      26.801
x6           476.7458    339.035      1.406      0.160    -189.621    1143.113
x7           101.0446    212.533      0.475      0.635    -316.685     518.774
x8           177.0642    161.476      1.097      0.273    -140.313     494.442
x9           751.2793    171.902      4.370      0.000     413.409    1089.150
x10           67.6254     65.984      1.025      0.306     -62.065     197.316
==============================================================================
Omnibus:                        1.506   Durbin-Watson:                   2.029
Prob(Omnibus):                  0.471   Jarque-Bera (JB):                1.404
Skew:                           0.017   Prob(JB):                        0.496
Kurtosis:                       2.726   Cond. No.                         227.
==============================================================================
```