---
author: Mostafa Samir Ali
tags:
  - AI
---

# Confusion matrix


- positive **--model-->** positive (True P) ✅
- positive **--model-->** negative (False N)
- Negative **--model-->** Negative (True Negative) ✅
- Negative **--model-->** Positive (False Positive)

The **confusion matrix** and the associated evaluation metrics are key concepts in measuring the performance of classification models in machine learning. Here's a breakdown:

---

# Confusion Matrix
- 2x2 confusion matrix
![[confusion-matrix.jpeg | center]]

- 3x3 confusion matrix
![[confusion-Matrix.png | center]]

A confusion matrix is a 2x2 table for binary classification (and larger matrices for multi-class problems) that shows the comparison between actual labels and predicted labels:

|                     | **Predicted Positive** | **Predicted Negative** |
| ------------------- | ---------------------- | ---------------------- |
| **Actual Positive** | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative** | False Positive (FP)    | True Negative (TN)     |

- **True Positive (TP):** Correctly predicted positive instances.
- **False Positive (FP):** Incorrectly predicted as positive when it was negative (Type I error).
- **True Negative (TN):** Correctly predicted negative instances.
- **False Negative (FN):** Incorrectly predicted as negative when it was positive (Type II error).

---

![[Screenshot 2024-12-17 010517.png | center]]
# **Evaluation Metrics**

#### 1. Accuracy

**Definition:** The proportion of correct predictions among all predictions.

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

- **Pros:** Useful when the dataset is balanced.
- **Cons:** Misleading for imbalanced datasets.

---

#### 2. Precision (Positive Predictive Value)

**Definition:** The proportion of correctly predicted positive instances out of all predicted positive instances.

$$Precision = \frac{TP}{TP + FP}$$

>[!TIP]
> - Precision : among the predictions the model made , how many of those actually correct

- **Use case:** When minimizing false positives is important (e.g., email spam detection).

---

#### 3. Recall (Sensitivity or True Positive Rate)

**Definition:** The proportion of correctly predicted positive instances out of all actual positive instances.

$$Recall = \frac{TP}{TP + FN}$$

>[!TIP]
> - Recall : the data have +ve points class , how many of those the model got in it's prediction 

- **Use case:** When minimizing false negatives is crucial (e.g., disease detection).

---

#### 4. F1 Score

**Definition:** The harmonic mean of Precision and Recall, balancing their trade-off.

$$F1\ Score=2⋅\frac{Precision⋅Recall}{Precision+Recall}$$

- **Use case:** When Precision and Recall are equally important.

---

#### 5. Specificity (True Negative Rate)

**Definition:** The proportion of correctly predicted negative instances out of all actual negative instances.
- same as recall but for the -ve class  
$${Specificity} = \frac{TN}{TN + FP}$$

- **Use case:** When identifying true negatives is important (e.g., avoiding unnecessary treatments).

---

You're right—let's address **sensitivity** properly and clarify its role in the context of the other metrics:

---

#### 6. Sensitivity (True Positive Rate, TPR)

**Definition:** Sensitivity, also known as the **True Positive Rate (TPR)** or **Recall**, measures the ability of a model to correctly identify all positive instances.

$${Sensitivity} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$

- **Meaning:** Out of all the actual positive cases, what proportion did the model correctly identify?
- **Focus:** Reducing **false negatives**.
- **Use Case:** Sensitivity is critical in scenarios where missing positive cases is costly, such as:
    - Detecting diseases in healthcare.
    - Identifying fraud in financial systems.

### **Relation to Other Metrics**

- Sensitivity and **Recall** are the same metric. The names vary depending on the domain (e.g., "sensitivity" in medicine vs. "recall" in machine learning).
- Often paired with **specificity** to assess the trade-off between catching true positives and avoiding false positives.

# ROC & AUC
---
#### 7. ROC Curve (Receiver Operating Characteristic Curve)

**Definition:** A plot of the True Positive Rate (Sensitivity) against the False Positive Rate (1 - Specificity) at different threshold levels.

- **True Positive Rate (TPR):** Same as Recall.
- **False Positive Rate (FPR):**


$${FPR} = \frac{FP}{FP + TN}$$

- **Insights:** The curve shows the trade-off between Sensitivity and Specificity.

>[!NOTE] # ROC
> - among the predictions 
> 	- how many the model got <u>+ve points correct</u> out of all +ve points in the data 
> 	- how many the model got <u>-ve points wrong</u> out of all -ve points in the data


---

#### 8. AUC (Area Under the Curve)

**Definition:** The area under the ROC curve, representing the model's ability to distinguish between classes.

- used to compare between different ROC models 
- the more the area the more TPR and the more good the model
- the model with greater AUC is better 
- **Range:** From 0 to 1.
    - **1:** Perfect classification.
    - **0.5:** Random guessing (no discrimination).
    - **<0.5:** Worse than random.


![[Roc_curve.svg.png | center]]

---

### Summary of Relationships

- **Accuracy** gives an overall view but is less useful in imbalanced datasets.
- **Precision** is useful when false positives are costly.
- **Recall** is crucial when false negatives are costly.
- **F1 Score** balances Precision and Recall.
- **Specificity** is the complement of Recall for the negative class.
- **ROC and AUC** provide a visual and quantitative way to evaluate classification thresholds.

Let me know if you’d like a practical example or further clarification!


---
# Practical
## Confusion matrix
- how to apply confusion matrix 
- we can use heatmap in seaborn or confusion_matrix_display from sklearn
<br><br>
### code
```python
# confusion matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test , y_pred_2)
```


## visualize 
- using heatmap
```python
# Visualization using Seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()
```

![[Untitled 4.png| center]]

- using `ConfusionMatrixDisplay`
```python
from sklearn.metrics import ConfusionMatrixDisplay

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

```

![[Untitled 1 2.png| center]]

## Evaluation matrix

```python
# import dependencies 
from sklearn.metrics import f1_score , accuracy_score , precision_score , recall_score 

# calculating errors
error_dict = {
"acc" : accuracy_score(y_test , y_pred) ,
"recall" : recall_score(y_test , y_pred ,average = "macro") ,
"pre" : precision_score(y_test , y_pred ,average = "macro") ,
"f1" : f1_score(y_test , y_pred ,average = "macro")
}
```
- out
![[Screenshot 2024-12-17 235745.png | center]]




# resources
- https://www.youtube.com/watch?v=Kdsp6soqA7o
- https://www.youtube.com/watch?v=4jRBRDbJemM
- https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc