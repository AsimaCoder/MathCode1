def i(x):
    """ function definition for i(x) """
    return x ** 10 - 1

def bisect(func, lower_bound, upper_bound, tolerance=0.0001):
    """ bisection method implementation """
    iterations = 0
    while True:
        mid_point = (lower_bound + upper_bound) / 2
        f_mid = func(mid_point)

        if f_mid > 0:
            upper_bound = mid_point
        else:
            lower_bound = mid_point

        iterations += 1
        if abs(f_mid) < tolerance or abs(upper_bound - lower_bound) < tolerance:
            break

    return lower_bound, iterations

def false_position(func, lower_bound, upper_bound, tolerance=0.0001):
    """ false Position method implementation """
    iterations = 0
    while True:
        f_lower = func(lower_bound)
        f_upper = func(upper_bound)
        root = lower_bound - (f_lower * (upper_bound - lower_bound)) / (f_upper - f_lower)

        if func(root) > 0:
            upper_bound = root
        else:
            lower_bound = root

        iterations += 1
        if abs(func(root)) < tolerance:
            break

    return root, iterations

# running Bisection Method
lower_bound_bisection, upper_bound_bisection = 0, 1.3
root_bisection, iterations_bisection = bisect(i, lower_bound_bisection, upper_bound_bisection)
print(f"Bisection Method: Root = {root_bisection} (after {iterations_bisection} iterations)")

lower_bound_false_position, upper_bound_false_position = 0, 1.3
root_false_position, iterations_false_position = false_position(i, lower_bound_false_position, upper_bound_false_position)
print(f"False Position Method: Root = {root_false_position} (after {iterations_false_position} iterations)")

better_method = "Bisection" if iterations_bisection < iterations_false_position else "False Position"
print(f"{better_method} method is better here with fewer iterations.")