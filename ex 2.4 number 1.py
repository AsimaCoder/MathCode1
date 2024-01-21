def i(x):
    return x**3 - x - 1

def bisect(func, lower_bound, upper_bound, tolerance=0.0001):
    iterations = 0
    lower_y = func(lower_bound)
    upper_y = func(upper_bound)

    print(f"Initial bounds: lower_bound = {lower_bound}, upper_bound = {upper_bound}")
    print(f"Initial function values: lower_y = {lower_y}, upper_y = {upper_y}")

    while abs(upper_bound - lower_bound) > tolerance:
        midpoint = (lower_bound + upper_bound) / 2
        midpoint_y = func(midpoint)

        print(f"\nIteration {iterations + 1}:")
        print(f"Bisected to: x = {midpoint}, y = f(x) = {midpoint_y}")

        if midpoint_y * lower_y < 0:
            upper_bound = midpoint
            upper_y = midpoint_y
        else:
            lower_bound = midpoint
            lower_y = midpoint_y

        print(f"Updated bounds: upper_bound = {upper_bound}, lower_bound = {lower_bound}")

        iterations += 1

    return midpoint

# change these initial bounds as needed
lower_bound = 1  # for example, for (iii), set lower_bound = 0
upper_bound = 2

root = bisect(i, lower_bound, upper_bound)
print(f"\nRoot found at x = {root}")