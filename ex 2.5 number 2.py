def derivative(f, x, h=1e-5):
    """ Approximate the derivative of a function at a given point. """
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, initial_guess, tolerance=0.0001):
    """ Implement the Newton-Raphson method for finding roots of a function. """
    x0 = initial_guess
    iterations = 0

    while True:
        f_x0 = f(x0)
        f_prime_x0 = derivative(f, x0)

        if f_prime_x0 == 0:
            return None, iterations

        x1 = x0 - f_x0 / f_prime_x0
        print(f"Iteration {iterations}: x = {x0}")

        if abs(x1 - x0) < tolerance:
            return x1, iterations

        x0 = x1
        iterations += 1

def function_example(x):
    return x**4 + x**3 - 7*x**2 - x + 5  

initial_guess = (2 + 3) / 2  
root, num_iterations = newton_raphson(function_example, initial_guess)

print(f"Root found: {root}")
print(f"Total number of iterations: {num_iterations}")