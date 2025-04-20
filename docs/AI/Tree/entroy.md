---
author: Mostafa Samir Ali
tags:
  - AI
  - "#Trees"
---
- in order to understand entropy we need to understand expected values

# Expected Values

## Definition
The **expected value** is a fundamental concept in probability and statistics. It represents the long-run average value of a random variable over many trials or experiments. In simpler terms, it's what you would expect to happen on average if an experiment is repeated many times.

## Formula
For a discrete random variable \( X \) with possible outcomes $( x_1, x_2, \dots, x_n )$ and corresponding probabilities $( P(x_1), P(x_2), \dots, P(x_n) )$, the expected value $( E(X) )$ is calculated as:

$$
E(X) = \sum_{i=1}^{n} x_i \cdot P(x_i)
$$

For a continuous random variable, the expected value is calculated using an integral:

$$
E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
$$

where $( f(x) )$ is the probability density function (PDF) of $( X )$.

## Interpretation
- The expected value is the "center" or "mean" of a probability distribution.
- It does not necessarily correspond to any actual outcome of the random variable.
- It provides a measure of the central tendency of the distribution.

## Example
### Discrete Case
Consider rolling a fair six-sided die. The possible outcomes are \( 1, 2, 3, 4, 5, 6 \), each with a probability of \( \frac{1}{6} \). The expected value is:

$$
E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6} = 3.5
$$

### Continuous Case
For a continuous random variable \( X \) with a uniform distribution between \( 0 \) and \( 1 \), the expected value is:

$$
E(X) = \int_{0}^{1} x \cdot 1 \, dx = \frac{1}{2}
$$

## Properties of Expected Values
1. **Linearity**: $( E(aX + bY) = aE(X) + bE(Y) )$, where $( a )$ and $( b )$ are constants.
2. **Independence**: If \( X \) and \( Y \) are independent, $( E(XY) = E(X) \cdot E(Y) )$.
3. **Constants**: The expected value of a constant $( c ) is ( c ), i.e., ( E(c) = c ).$

## Applications
- Used in decision-making under uncertainty (e.g., finance, insurance, and gambling).
- Helps in calculating risk and return in investments.
- Forms the basis for more advanced statistical concepts like variance and covariance.

## Limitations
- The expected value may not always be meaningful for skewed distributions or distributions with heavy tails.
- It does not provide information about the variability or spread of the outcomes.

---

# resources 

- https://www.youtube.com/watch?v=KLs_7b7SKi4 expected value
- https://www.youtube.com/watch?v=YtebGVx-Fxw entropy





