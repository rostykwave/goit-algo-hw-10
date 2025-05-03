## Task 2: Estimating a Definite Integral Using the Monte Carlo Method

In this part of the assignment, I used the Monte Carlo method to estimate the value of a definite integral for the function f(x) = x² over the interval [0, 2].

### What is the Monte Carlo Method?

The Monte Carlo method is a probabilistic technique for solving problems that might be difficult to approach analytically. Here’s how I used it for integration:

1. First, I defined a rectangle that fully covers the area under the curve of
   f(x) = x² between 0 and 2.
2. Then, I generated a bunch of random points inside this rectangle.
3. I counted how many of those points landed below the curve.
4. Finally, I estimated the area under the curve by multiplying the area of the rectangle by the proportion of points that landed under it.

### Results

Here’s a comparison of different methods I tried:

| Method                         | Integral Value | Error          |
| ------------------------------ | -------------- | -------------- |
| Analytical calculation         | 2.6666...      | -              |
| scipy.integrate.quad           | 2.6666...      | ~10⁻¹⁴         |
| Monte Carlo (1,000 points)     | ~2.64 - 2.69   | ~0.1 - 1%      |
| Monte Carlo (10,000 points)    | ~2.65 - 2.68   | ~0.05 - 0.5%   |
| Monte Carlo (100,000 points)   | ~2.664 - 2.669 | ~0.01 - 0.1%   |
| Monte Carlo (1,000,000 points) | ~2.666 - 2.667 | ~0.001 - 0.01% |

### Conclusions

1. **Accuracy of the Monte Carlo Method**:

   - With a small number of points (1,000 - 10,000), the method provides approximate results with a relative error up to 1%
   - As the number of points increases, accuracy significantly improves
   - When using 1,000,000 points, the error approaches 0.01%

2. **Advantages of the Monte Carlo Method**:

   - Simple implementation
   - Ability to compute multi-dimensional integrals
   - Parallelizable computations

3. **Disadvantages of the Monte Carlo Method**:
   - Relatively low accuracy with small sample sizes
   - Requires generating large numbers of random values
   - Slow convergence (error decreases as 1/√n, where n is the number of points)

### Final Thoughts

Overall, the Monte Carlo method turned out to be a neat way to estimate an integral, and it’s especially useful for cases where traditional methods become messy (like in higher dimensions). But for simple, one-dimensional problems like this one, it’s definitely not the most efficient. Tools like scipy.integrate.quad are much faster and more accurate.
