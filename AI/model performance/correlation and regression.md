---
author: Mostafa Samir Ali
tags:
  - AI
---
# Correlation and Regression
- Correlation is used to give the relationship between the variables whereas linear regression uses an equation to express this relationship.
## Correlation
- Correlation is the measure of dependency of the dependent variable on the independent variable in regression problems
- Correlation can be defined as a measurement that is used to quantify the relationship between variables. 
	- If an increase (or decrease) in one variable causes a corresponding increase (or decrease) in another then the two variables are said to be **directly correlated**. 
	- Similarly, if an increase in one causes a decrease in another or vice versa, then the variables are said to be **indirectly correlated**. 
	- If a change in an independent variable <u>does not cause a change in the dependent variable</u> then they are **uncorrelated**. 
- Thus, correlation can be positive (direct correlation), negative (indirect correlation), or zero.


## measuring Correlation in python
```python
# measuring correlation

plt.figure(figsize=(20,8))
sns.heatmap(df_numeric.corr(),annot=True) # including a heatmap
plt.show()
```

- we can select features with the highest correlation to pass to the model
```python
filt = df_numeric.corr().loc[:, "price"].apply(lambda x: x >= 0.5 or x <= -0.4)
price_corr[filt]
```

![[Screenshot 2024-10-23 144745.png | center]]
# $R^2$
- $R^2$ is too similar too R (Correlation) , then why we use it ?
	- interpretation is much easier
	- where R = 0.7 is twice good as R = 0.5
	- while $R^2$ = 0.7 is 1.4 as good as $R^2$ = 0.5
- $R^2$ is the square of R , it defines the correlation more accurate than the R

## Calculations and formula
1. calculate the variation around the mean in the data
	- we calculate the sum of square around the mean 
	- then divide it on number of samples
	- $$Var(mean) = \frac{(data - mean)^2}{n}$$

![[Screenshot 2024-10-23 145939.png | center]]

2. find the least squares fit and calculate the variance around it
	- calculate the sum of squares around the it
	- divide it by number of samples
	- $$Var(fit) = \frac{(data - fit)^2}{n}$$

![[Screenshot 2024-10-23 150308.png | center]]

3. calculate $R^2$ 
	- we calculate $R^2$ by the formula $$R^2 = \frac{Var(mean) - Var(fit)}{Var(mean)}$$
![[Pasted image 20241023150958.png | center]]

## what $R^2$ tell us ?
- if the result of $R^2$ is equal to `0.81` it means that there are less variation in the fit line about `81 %` than in the mean
- <u>it also mean that the feature can explain</u> `81 %` <u>of the target </u>   

![[Screenshot 2024-10-23 151720.png | center]]


## $R^2$ coding
```python
# import R2
from sklearn.metrics import r2_score

# calculate R2
r2 = r2_score(x, y) 
print('r2 score for perfect model is', r2)
```

# RESOURCES  
- https://www.youtube.com/watch?v=xTpHD5WLuoA
- https://www.youtube.com/watch?v=11c9cs6WpJU
