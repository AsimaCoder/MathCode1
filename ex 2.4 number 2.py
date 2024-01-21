
import math

def f(x):
    return x - math.cos(x)

def bisection_method(func, lower_bound, upper_bound, tolerance=0.0001):
    if func(lower_bound) * func(upper_bound) >= 0:
        print("Bisection method fails.")
        return None

    print(f"Initial bounds: lower_bound = {lower_bound}, upper_bound = {upper_bound}")

    while (upper_bound - lower_bound) / 2.0 > tolerance:
        midpoint = (lower_bound + upper_bound) / 2.0
        midpoint_value = func(midpoint)

        print(f"Bisected to: x = {midpoint}, f(x) = {midpoint_value}")

        if midpoint_value * func(lower_bound) < 0:
            upper_bound = midpoint
        else:
            lower_bound = midpoint

    return (lower_bound + upper_bound) / 2.0

lower_bound = 0
upper_bound = 1

root = bisection_method(f, lower_bound, upper_bound)
if root is not None:
    print(f"Root found at x = {root}")
else:
    print("No root found in the given interval.")


