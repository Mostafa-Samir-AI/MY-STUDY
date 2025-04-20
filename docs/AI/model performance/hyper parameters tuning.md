---
author: Mostafa Samir Ali
tags:
  - AI
  - data_pre_processing
---


# hyper parameter tuning
- **Hyperparameter tuning** is the process of optimizing the hyperparameters of a machine learning model to achieve the best performance on a given dataset. Unlike model parameters (e.g., weights in a neural network), hyperparameters are set before the learning process begins and are not learned from the data.

# what are hyper parameters ? 
Hyperparameters are the configurations that guide the training process of a model. Examples include:

- **Learning rate**: Controls the step size in gradient descent.
- **Number of estimators**: Number of trees in a Random Forest.
- **Depth of a tree**: Maximum depth for decision trees.
- **Regularization parameters**: Controls overfitting (e.g., `alpha` in Lasso regression).
- **Batch size**: Number of samples in each training iteration.

# Why hyper parameter tuning ? 
The choice of hyperparameters can significantly impact:

- **Model accuracy**: Tuning hyperparameters can improve predictive performance.
- **Generalization**: Proper tuning helps avoid underfitting or overfitting.
- **Training time**: Efficient hyperparameters can reduce training duration.

# Methods
1. Grid search
2. Random search
3. Bayesian Optimization
4. Automated machine learning (AutoML)
5. Manual search --> done by user

![[1bf0f3af-22ce-46b1-a0a5-d34ee4544514_772x441.png | center]]

## 1. Grid search
- **Grid search** is a hyperparameter tuning technique that performs an **exhaustive search over a specified hyperparameter space** to find the combination of hyperparameters that yields the best model performance.

### How it works
- We define the hyperparameter search space as a parameter grid.
- The **parameter grid** is a dictionary where you specify each hyperparameter you want to tune with a list of values to explore. 
<br><br>
- Grid search then systematically explores every possible combination of hyperparameters from the parameter grid. <u>It fits and evaluates the model for each combination using cross-validation and selects the combination that yields the best performance.</u>

### code
- first we need to specify the parameters `grid_search` will test
- then we pass all information to the grid search algorithm

```python
# model
from sklearn.tree import RandomForestClassifier
model = RandomForestClassifier()


# specify parameters 
param = {"n_estimator" : [100 , 200] , 
		 "max_depth" : [10 , 20]
		}

# specify the Cross validation / by default k-fold
from sklearn.model_selection import StratifiedKFold
ssplit = StratifiedKFold(n_split = 5)

# import grid search
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(estimator = model , 
						 param_grid = param , 
						 cv = ssplit , 
						 scoring = "accuracy")

# fitting the data
grid_search.fit(x , y)

# seeing results
print("Best Parameters:", grid_search.best_params_) 
print("Best Score:", grid_search.best_score_)
```

### Pros and cons
Using grid search for hyperparameter tuning has the following advantages:

- Grid search explores all specified combinations, ensuring you don't miss the best hyperparameters within the defined search space.
- It is a good choice for exploring smaller hyperparameter spaces.

On the flip side, however:

- Grid search can be computationally expensive, especially when dealing with a large number of hyperparameters and their values. It may not be feasible for very complex models or extensive hyperparameter searches.

## 2. Random search
- **Randomized search** is another hyperparameter tuning technique that **explores random combinations of hyperparameters within specified distributions or ranges**. It's particularly useful when dealing with a large hyperparameter search space.
- <u>Randomly samples hyperparameter combinations instead of trying all combinations, making it faster than Grid Search</u>


### code 
```python
# model
from sklearn.tree import RandomForestClassifier
model = RandomForestClassifier()


# specify parameters 
param = {"n_estimator" : [100 , 200] , 
		 "max_depth" : [10 , 20]
		}

# specify the Cross validation / by default k-fold
from sklearn.model_selection import StratifiedKFold
ssplit = StratifiedKFold(n_split = 5)

# import grid search
from sklearn.model_selection import RandomSearchCV
rand_search = RandomSearchCV(estimator = model , 
						 param_grid = param , 
						 cv = ssplit , 
						 scoring = accuracy)

# fitting the data
rand_search.fit(x , y)

# seeing results
print("Best Parameters:", rand_search.best_params_) 
print("Best Score:", rand_search.best_score_)
```

### pros and cons

Let’s sum up the advantages of randomized search:

- Randomized search is efficient when dealing with a large number of hyperparameters or a wide range of values because it doesn't require an exhaustive search.
- It can handle various parameter types, including continuous and discrete values.

Here are some limitations of randomized search:

- Due to its random nature, it may not always find the best hyperparameters. But it often finds good ones quickly.
- Unlike grid search, it doesn't guarantee that all possible combinations will be explored.

---
## **3. Bayesian Optimization**

- **Description**: Uses probabilistic models to predict the performance of hyperparameters and select the next set of parameters to evaluate.
- **Tools**: Libraries like `Hyperopt`, `Optuna`, or `Scikit-Optimize`.

## **4. Automated Machine Learning (AutoML)**

- **Description**: Automates hyperparameter tuning as part of the machine learning pipeline.
- **Tools**: Libraries like `Auto-sklearn` and `H2O AutoML`.

## **5. Manual Search**

- **Description**: A trial-and-error approach where you adjust hyperparameters based on intuition and domain knowledge.
- **When Useful**: When computational resources are limited or for simple models.


# resources
- https://www.kdnuggets.com/hyperparameter-tuning-gridsearchcv-and-randomizedsearchcv-explained
