import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import time

# Function to integrate
def f(x):
    return x ** 2

# Integration limits
a = 0  # Lower limit
b = 2  # Upper limit

def monte_carlo_integration(f, a, b, num_points):
    """
    Compute the definite integral using the Monte Carlo method
    
    Args:
        f: Function to integrate
        a, b: Lower and upper integration limits
        num_points: Number of random points
        
    Returns:
        Estimate of the integral
    """
    # Find the maximum value of the function on the interval [a, b]
    x_values = np.linspace(a, b, 1000)
    max_y = max(f(x) for x in x_values)
    
    # Generate random points
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, max_y, num_points)
    
    # Count points under the curve
    under_curve = sum(y_random <= f(x_random))
    
    # Compute the area
    area = (b - a) * max_y
    integral_estimate = (under_curve / num_points) * area
    
    return integral_estimate

def visualize_monte_carlo(f, a, b, num_points):
    """Visualization of the Monte Carlo method for integration"""
    # Find the maximum value of the function on the interval [a, b]
    x_values = np.linspace(a, b, 1000)
    max_y = max(f(x) for x in x_values)
    
    # Generate random points
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, max_y, num_points)
    
    # Determine which points are under the curve
    under_curve = y_random <= f(x_random)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot points (red under the curve, blue above)
    plt.scatter(x_random[under_curve], y_random[under_curve], color='red', s=1, alpha=0.5, label='Under the curve')
    plt.scatter(x_random[~under_curve], y_random[~under_curve], color='blue', s=1, alpha=0.5, label='Above the curve')
    
    # Plot the function
    x = np.linspace(a, b, 1000)
    plt.plot(x, f(x), 'g-', linewidth=2, label='f(x) = x^2')
    
    # Configure the plot
    plt.xlim(a, b)
    plt.ylim(0, max_y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Monte Carlo Method for Integrating f(x) = x^2 from {a} to {b}')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Analytical calculation for f(x) = x^2 from 0 to 2
    analytical_result = (b**3 - a**3) / 3  # [x^3/3] from a to b
    
    # Compute the integral using scipy.integrate.quad
    quad_result, quad_error = spi.quad(f, a, b)
    
    print(f"Analytical value of the integral: {analytical_result}")
    print(f"Value of the integral using scipy.integrate.quad: {quad_result} (error: {quad_error})")
    
    # Compute the integral using the Monte Carlo method with different numbers of points
    point_counts = [1000, 10000, 100000, 1000000]
    
    for num_points in point_counts:
        start_time = time.time()
        result = monte_carlo_integration(f, a, b, num_points)
        end_time = time.time()
        
        error = abs(result - analytical_result)
        relative_error = error / analytical_result * 100
        
        print(f"\nMonte Carlo method with {num_points} points:")
        print(f"Result: {result}")
        print(f"Absolute error: {error}")
        print(f"Relative error: {relative_error:.4f}%")
        print(f"Execution time: {(end_time - start_time):.4f} seconds")
    
    # Visualize the Monte Carlo method with 5000 points for better representation
    visualize_monte_carlo(f, a, b, 5000)

if __name__ == "__main__":
    main()
