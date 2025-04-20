---
author: Mostafa Samir Ali
tags:
  - AI
  - data_pre_processing
---
![[Screenshot 2024-12-23 001635.png | center]]
# Cross Validation
- we have a problem with high bias and overfitting 
- we cannot depend on only test data to give us insights about model performance 
- also if we depend on the test data only, we will have to do make radical changes from the beginneing if the evaluation score is not ok
- so we use validation 
- validation is an indication of a problem not the solution of a problem
- validation will indicate high bias but will not fix it , we fix it using some techniques , *look at* [[bias and variance]] 
- **Cross-Validation** also referred to **as out of sampling technique** . It is a resampling procedure used to evaluate machine learning models and access how the model will perform for an independent **test dataset**. In simple words it allows us to utilize our data even better.

## Some of the different cross-validation techniques are:

1. Holdout cross-validation
<br><br>
2. k-fold cross-validation
<br><br>
3. Stratified k-fold cross-validation
<br><br>
4. Leave one out cross-validation
<br><br>
5. Repeated random subsampling validation
<br><br>
6. Time Series cross-validation
<br><br>
7. Leave p out cross-validation
<br><br>
---

# 1. HoldOut Validation Approach- Train And Test Split
- this is a classical approach where we depend on test data only to evaluate the model
- In this method, Dataset is **randomly split into train and test data**. 
- split of training data is generally more than test data. 
- The training data is used to induce the model and validation data is evaluates the performance of the model. 

![[qdkjkkv0.bmp | center]]

>[!multi-column]
>> [!TODO] ## pros
>> - easy to implement
>
>> [!warning] ## cons
>> - Not suitable for an imbalanced dataset.
>> - A lot of data is isolated from training set.

---
# 2. K-fold Cross validation
- In k-fold cross-validation, the original dataset is equally partitioned into k subparts or folds. Out of the k-folds or groups, for each iteration, one group is selected as validation data, and the remaining (k-1) groups are selected as training data.
- The process is repeated for k times until each group is treated as validation and remaining as training data.
- The final accuracy of the model is computed by taking the mean accuracy of the k-models validation data.
![[tkq9ys5c.bmp | center]]

>[!multi-column]
>> [!TODO] ## pros
>> - The model has low bias.
>> - Low time complexity
>> - The entire dataset is utilized for both training and validation.
>
>> [!warning] ## cons
>> - Not suitable for an **imbalanced dataset**.

---
# 3. Stratified k-fold cross-validation
- Stratified k-fold cross-validation works well for an **imbalanced dataset**.
- In Stratified k-fold cross-validation, the dataset is partitioned into k groups or folds such that the validation data/Test set has an equal number of instances of target class label.
- This ensures that one particular class is not over present in the validation or train data especially when the dataset is imbalanced.
- The final score is computed by taking the mean of scores of each fold.

![[Untitled 3.png| center]]

>[!multi-column]
>> [!TODO] ## pros
>> - Works well for an imbalanced dataset.
>
>> [!warning] ## cons
>> - Now suitable for time series dataset.

---

# 4. Leave-one-out cross-validation
- Leave-one-out cross-validation (LOOCV) is an exhaustive cross-validation technique. It is a category of LpOCV with the case of p=1.
- For a dataset having n rows, 1st row is selected for validation, and the rest (n-1) rows are used to train the model. For the next iteration, the 2nd row is selected for validation and rest to train the model. Similarly, the process is repeated until n steps or the desired number of operations.
- Exhaustive cross-validation methods are cross-validation methods that learn and test in all possible ways.
- *use it when the dataset is small*

![[Screenshot 2024-12-23 010750.png | center]]

![[i.webp | center]]

>[!multi-column]
>> [!TODO] ## pros
>> - Simple, easy to understand, and implement.
>
>> [!warning] ## cons
>> - The model may lead to a low bias.
>> - he computation time required is high.

---
# 5. Repeated Random Test-Train Splits
- Repeated random subsampling validation also referred to **as Monte Carlo cross-validation** splits the dataset randomly into training and validation. Unlikely k-fold cross-validation split of the dataset into not in groups or folds but splits in this case in random.
- The number of iterations is not fixed and decided by analysis. The results are then averaged over the splits.
- This technique is a hybrid of **traditional train-test splitting** and **the k-fold cross-validation** method. In this technique, we create random splits of the data in the training-test set manner and then repeat the process of splitting and evaluating the algorithm multiple times, just like the cross-validation method.

![[b4gcuezf.bmp | center]]

>[!multi-column]
>> [!TODO] ## pros
>> - The proportion of train and validation splits is not dependent on the number of iterations or partitions.
>
>> [!warning] ## cons
>> - Some samples may not be selected for either training or validation.
>> - Not suitable for an imbalanced dataset.

---

# 6. Time Series cross-validation
- The order of the data is very important for time-series related problem. 
- For time-related dataset <u>random split or k-fold split of data into train and validation may not yield good results.</u>
- For the time-series dataset, the split of data into train and validation is according to the time also referred to as **forward chaining method** or **rolling cross-validation**. 
- For a particular iteration, the next instance of train data can be treated as validation data.
- As mentioned in the above diagram, for the 1st iteration, 1st 3 rows are considered as train data and the next instance T4 is validation data. 
- The chance of choice of train and validation data is forwarded for further iterations.

![[i 1.webp | center]]

---

# 7. Leave p-out cross-validation
- leave no. of rows out to make it eh validation set
- Leave p-out cross-validation (LpOCV) is an exhaustive cross-validation technique, that involves using p-observation as validation data, and remaining data is used to train the model.
- This is repeated in all ways to cut the original sample on a validation set of p observations and a training set.
- A variant of LpOCV with p=2 known as leave-pair-out cross-validation has been recommended as a nearly unbiased method for estimating the area under ROC curve of a binary classifier.
- A particular case of this method is when p = 1. This is known as Leave one out cross validation

---
# Resources
- https://www.youtube.com/watch?v=PF2wLKv2lsI
- https://medium.com/@sunils0506/types-of-cross-validations-f1ad3a871f67
- https://colab.research.google.com/drive/1ipHCKUBYDR_A-zQb1TRJgfWyZ4VvKFi8?usp=sharing

