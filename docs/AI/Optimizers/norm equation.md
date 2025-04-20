---
author: Mostafa Samir Ali
tags:
  - AI
---

# norm equation

- norm equation is a method that is used to reach the most optimized parameters that fit the model perfectly

$$\theta = (X^T . X)^{-1} .X^Ty$$
## pros 
- reach the global minimum at one step
- garentees the value of global minimum
## cons
- use alot of computetional power since it contains alot of multiplications and inverses

```python
import numpy as np

# Example data
X = np.array([[1, 1], [1, 2], [1, 3]])  # Add a column of ones for the bias term
y = np.array([1, 2, 3])

# Normal equation formula
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print("Theta (coefficients):", theta)

```
- out `Theta (coefficients): [-1.77635684e-15  1.00000000e+00]`