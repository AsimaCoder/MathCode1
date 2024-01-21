def calc_x(y, z):
    return (12 - y - z) * 0.1

def calc_y(x, z):
    return (13 - 2 * x - z) * 0.1

def calc_z(x, y):
    return (14 - 2 * x - 2 * y) * 0.1

def gauss_seidel(x0, y0, z0, tolerance=0.0001, max_iterations=10):
    for iteration in range(max_iterations):
        print(f"Iteration {iteration + 1}:")
        
        new_x = calc_x(y0, z0)
        print(f"x = {new_x}")
        new_y = calc_y(new_x, z0)
        print(f"y = {new_y}")
        new_z = calc_z(new_x, new_y)
        print(f"z = {new_z}")

        if (abs(new_x - x0) < tolerance and
            abs(new_y - y0) < tolerance and
            abs(new_z - z0) < tolerance):
            break

        x0, y0, z0 = new_x, new_y, new_z

    return new_x, new_y, new_z, iteration + 1

x0, y0, z0 = 0, 0, 0

x, y, z, num_iterations = gauss_seidel(x0, y0, z0)

print(f"\nSolution: x = {x}, y = {y}, z = {z}")
print(f"Converged in {num_iterations} iterations")