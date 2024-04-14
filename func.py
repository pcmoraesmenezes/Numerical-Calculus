import time


def f(x):
    """
    Define your function here. Example:
    x**2 - 3*x + 2
    """
    return x**2 - 3*x + 2


def derivative_f(x):
    """
    Define the derivative of your function here.
    Example: 2*x - 3
    """
    return 2*x - 3


def fi(x):
    """
    Define the iteration function for the fixed point method here.
    Example: (x**2 + 2) / 3
    """
    return (x**2 + 2) / 3


def bolzano(func, a, b):
    """
    :param func: Function to be analyzed
    :param a: Start of the interval
    :param b: End of the interval
    :return: True if the function changes sign in the interval, False otherwise
    """
    if func(a) * func(b) < 0:
        return True
    return False


def time_execution(func):
    """
    Decorator to measure the execution time of a function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@time_execution
def bissection(func, a, b, aprox=1e-10, max_iter=None):
    """
    :param func: Function to be analyzed
    :param a: Start of the interval
    :param b: End of the interval
    :param aprox: Desired precision
    :param max_iter: Maximum number of iterations
    :return: Approximate root of the function
    """
    if not bolzano(func, a, b):
        print("Wrong interval. Function does not change sign.")
        return None

    iteration = 0
    previous_x = None

    while max_iter is None or max_iter > 0:
        x = (a + b) / 2
        iteration += 1
        print(f"Iteration {iteration}: a={a}, b={b}, x={x}, f(x)={func(x)}")
        if func(x) == 0:
            print(f"Exact root found. Root: {x}")
            return x
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
        if previous_x is not None and abs(x - previous_x) < aprox:
            print("No more progress. Stopping.")
            break
        if max_iter is not None:
            max_iter -= 1
        previous_x = x

    print(f"Conevergence reached. Root: {x}")
    return x


@time_execution
def false_position_method(f, a, b, epsilon=1e-10, max_iterations=None):
    if not bolzano(f, a, b):
        print("Wrong interval. Function does not change sign.")
        return None

    iteration = 0
    while max_iterations is None or iteration < max_iterations:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iteration += 1
        print(f"Iteration {iteration}: a={a}, b={b}, c={c}, f(c)={f(c)}")
        if abs(f(c)) < epsilon:
            print(f"Convergence reached. Root: {c}")
            return c, iteration
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("False position method reached the maximum number of iterations")
    return None


@time_execution
def point_fix(func, x0, aprox=1e-10, max_iter=None):
    """
    :param func: Function to be analyzed
    :param x0: Initial guess
    :param aprox: Desired precision
    :param max_iter: Maximum number of iterations
    :return: Approximate root of the function
    """
    iteration = 0
    while max_iter is None or max_iter > 0:
        x = func(x0)
        iteration += 1
        print(f"Iteration {iteration}: x0={x0}, x={x}, f(x)={func(x)}")
        if abs(x - x0) < aprox:
            print(f"Convergence reached. Root: {x}")
            return x
        x0 = x
        if max_iter is not None:
            max_iter -= 1
    print("Convergence not reached.")
    return x


@time_execution
def newton_raphson(func, derivative_func, x0, aprox=1e-10, max_iter=None):
    """
    :param func: Function to be analyzed
    :param derivative_func: Derivative of the function
    :param x0: Initial guess
    :param aprox: Desired precision
    :param max_iter: Maximum number of iterations
    """
    iteration = 0
    while max_iter is None or max_iter > 0:
        x = x0 - func(x0) / derivative_func(x0)
        iteration += 1
        print(f"Iteration {iteration}: x0={x0}, x={x}, f(x)={func(x)}")
        if abs(x - x0) < aprox:
            print(f"Convergence reached. Root: {x}")
            return x
        x0 = x
        if max_iter is not None:
            max_iter -= 1
    print("Convergence not reached.")
    return x


@time_execution
def secant_method(func, x0, x1, aprox=1e-10, max_iter=None):
    """
    :param func: Function to be analyzed
    :param x0: First initial guess
    :param x1: Second initial guess
    :param aprox: Desired precision
    :param max_iter: Maximum number of iterations
    """
    iteration = 0
    while max_iter is None or max_iter > 0:
        x = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        iteration += 1
        print(f"Iteration {iteration}: x0={x0}, x1={x1}, x={x}, f(x)={func(x)}") # noqa
        if abs(x - x1) < aprox:
            print(f"Convergence reached. Root: {x}")
            return x
        x0, x1 = x1, x
        if max_iter is not None:
            max_iter -= 1
    print("Maximum number of iterations reached.")
    return x
