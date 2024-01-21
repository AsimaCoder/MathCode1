def cubic_function(x):
    return x**3 - 5*x + 1

def regula_falsi(func, lower_bound, upper_bound, tolerance=0.0001):
    lower_y = func(lower_bound)
    upper_y = func(upper_bound)

    def update_bounds(x0, y0, lower_x, upper_x, lower_y, upper_y):
        if y0 > 0:
            upper_x, upper_y = x0, y0
        else:
            lower_x, lower_y = x0, y0
        return lower_x, upper_x, lower_y, upper_y

    iteration = 0
    while True:
        x0 = lower_bound - (upper_bound - lower_bound) / (upper_y - lower_y) * lower_y
        y0 = func(x0)

        lower_bound, upper_bound, lower_y, upper_y = update_bounds(x0, y0, lower_bound, upper_bound, lower_y, upper_y)

        iteration += 1
        if abs(x0 - (lower_bound - (upper_bound - lower_bound) / (upper_y - lower_y) * lower_y)) < tolerance:
            break

    return x0, iteration

# Initial bounds for the root finding
lower_bound = 0
upper_bound = 1

root, iterations = regula_falsi(cubic_function, lower_bound, upper_bound)
root, iterations

