def secant_method(f, x0, x1, tolerance=0.0001):
    """ Implement the Secant method for finding roots of a function. """
    iterations = 0

    while abs(x0 - x1) > tolerance:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        print(f"Iteration {iterations}: x = {x2}")

        x0, x1 = x1, x2
        iterations += 1

    return x1, iterations

def function_example(x):
    return x**3 + x**2 + x + 7  

x0 = -3  # Initial guess, change as per your requirement
x1 = -2  # Second initial guess, also can change
root, num_iterations = secant_method(function_example, x0, x1)

print(f"Root found: {root}")
print(f"Total number of iterations: {num_iterations}")
