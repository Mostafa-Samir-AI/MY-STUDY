---
author: Mostafa Samir Ali
tags:
  - AI
---

# Gradient descent 
- is an algorithm that is used to optimize the cost function
- its used to minimize the error as possible
- gradient descent equation
$$\theta'_j = \theta_j - \alpha\frac{\partial\ J}{\partial\ \theta}$$
 **where** 
- $\theta'_j$ = new parameter value
- $\theta_j$ = old value
- $\alpha$ = learning rate

- the gradient descent is the derivative of the cost function 
# how to do gradient descent
- important note: gradient descent is a <u>simultaneous update</u>
## steps for correct simultaneous update
1. calculate tmp_w $$tmp.w = w - \alpha \frac{\partial}{\partial w}\ J(w,b)$$
2. calculate tmp_b $$tmp.b = b - \alpha \frac{\partial}{\partial b}\ J(w,b)$$
3. update both $w$ and $b$ $$w = tmp.w \ \ \ b = tmp.b $$ 
4. repeating until the values are too low (cost is too low)

![[Pasted image 20240428123147.png]]

![[Pasted image 20240428123930.png]]
# learning rate
- learning rate is a hyper parameter defined by the user to adjust the speed and precision of the learning algorithm 
- a large learning rate may cause missing the minimum value for the cost function
- while a small learning rate will make the learning process too slow