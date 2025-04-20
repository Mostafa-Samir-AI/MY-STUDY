# cost function
- cost function evaluates how accurately the model maps the input and output data relationship
- a cost function is used to measure how wrong our model is in finding the relation between input and output
- Cost Function helps us to get the best values for $a_0$ and $a_1$ , in order to get the best fit line for data points.
- The difference between the <u>predicted values</u> ($y'_i$) and the <u>actual values</u> ($y_i$) gives the error.
$$ error = y'_i - y_i $$

| loss                            | cost                                  |
| ------------------------------- | ------------------------------------- |
| measure the error in one sample | measures the error in the entire data |
- the main idea is to evaluate the performance of the machine learning model

# cost function for different models
- cost function differ according to the type of algorithm used in the machine learning application 

## types of cost function
1. regression cost function
2. Binary class cost function
3. Multi-class cost function

### regression cost function
 - *regression* It is a predictive modeling technique to examine the relationship between independent features and dependent outcomes.
 - When the cost function deals with the problem statement of the Regression Model, it is known as Regression Cost Function. <u>It computes the error as the distance between the actual output and the predicted output.</u>


#### 1.M.E: mean error
-  ME is the most straightforward approach and acts as a foundation for other Regression Cost Functions. It computes the error for every training dataset and calculates the mean of all derived errors.
- ME is usually not suggested because the error values are either positive or negative. During mean calculation, they cancel each other and give a zero-mean error outcome.
#### 2.M.S.E : mean square error
-  MSE, also known as L2 Loss, is used most frequently and successfully improves the drawbacks of both ME and MAE. It computes the “square” of the distance between the actual output and predicted output, preventing negative error possibilities.
- MSE penalizes high errors caused by the anomalies and is beneficial to Loss Function Optimization Algorithms for evaluating optimal coefficients.
$$Cost\ Function\ (J) = \frac{1}{n}\sum_{i = 0}^{n} \left(pred_i - actual\right)^2$$
#### 3. M.A.E : mean absolute error
- It computes the absolute distance between the actual output and predicted output and is insensitive to anomalies. In addition, <u>MAE does not penalize high errors caused by these anomalies.</u>
- MAE comes with the drawback of being non-differentiable at zero. Thus, fail to perform well in Loss Function Optimization Algorithms that involve differentiation to evaluate optimal coefficients.



> [!hint] ## chatGPT

> [!NOTE]
> ## When to Use Different Types of Regression Cost Functions
> 
> Choosing the appropriate cost function for regression depends on several factors, including the nature of your data and the assumptions about the error distribution. Here are some common types of regression cost functions and when they are typically used:
> 
> 1. **Mean Squared Error (MSE)**:
>    - **When to use**: MSE is the most common cost function for regression tasks. It squares the difference between the predicted and actual values, penalizing larger errors more heavily. It's suitable when errors are normally distributed and you want to optimize for the average error.
>    - **Example**: Linear regression, polynomial regression.
> 
> 2. **Mean Absolute Error (MAE)**:
>    - **When to use**: MAE measures the average absolute difference between predicted and actual values. It's less sensitive to outliers compared to MSE and is useful when you have outliers in your data or when you want a more interpretable error metric.
>    - **Example**: Robust regression, decision trees.
> 
> 3. **Huber Loss**:
>    - **When to use**: Huber loss is a combination of MSE and MAE. It behaves like MSE for smaller errors and like MAE for larger errors, making it robust to outliers while still being differentiable everywhere.
>    - **Example**: Robust regression, gradient boosting machines.
> 
> 4. **Quantile Loss**:
>    - **When to use**: Quantile loss is used when you want to predict quantiles of the target distribution rather than the expected value. It's particularly useful in scenarios where you want to model the uncertainty of predictions.
>    - **Example**: Quantile regression.
> 
> 5. **Logarithmic Loss (Log Loss)**:
>    - **When to use**: Log loss is often used in logistic regression and binary classification problems. It measures the performance of a classification model where the prediction output is a probability value between 0 and 1.
>    - **Example**: Logistic regression, binary classification.
> 
> 6. **Poisson Loss**:
>    - **When to use**: Poisson loss is used when dealing with count data, where the target variable represents the number of occurrences of some event. It's designed to model count data with a Poisson distribution.
>    - **Example**: Poisson regression.
> 
> 7. **Hinge Loss**:
>    - **When to use**: Hinge loss is primarily used in support vector machines (SVMs) for classification tasks. It's suitable for binary classification problems and encourages correct classification with a margin.
>    - **Example**: Support vector machines (SVMs).

### Binary Classification Cost function (logistic regression)
- Binary Classification Cost Functions deal with the problem statement of the Classification Models & predict categorical values like 0 or 1.
- Binary Classification Cost Functions downsize Class 1’s error possibilities by minimizing the discrepancies between the actual and predicted probability distributions. 
- It estimates these errors in the classification models by calculating the mean of cross-entropy for all given datasets.
$$ y'_i = \sigma(w^Tx+b)$$
$$ Cost (J) = -\frac{1}{n}\sum_{i=1}^{m} \left[y_i.log(y'_i)\ +\ (1-y_i).log(1-y'_i)\right]$$
- Cross-entropy(D) = - $y*log(p)$ when y = 1  
- Cross-entropy(D) = - $(1-y)*log(1-p)$ when y = 0 
### multi-class Cost function
- Multi-class Classification Cost Functions work for more than two classes in the classification model. 
- The functionality is the same as that of the Binary Classification Cost Functions, but with slight extensions.
- These score values outline the average difference between the actual and predicted probability distributions.
- cost functions utilize the Softmax Function to calculate the probability of an observation belonging to a predicted class .
- In a multi-class classification problem, cross-entropy will generate a score that summarizes the mean difference between actual and anticipated probability distribution.

