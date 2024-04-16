
---

# Numerical Methods for Root Finding

This repository contains Python implementations of various numerical methods for root finding, including the bisection method, false position method, fixed-point iteration, Newton-Raphson method, and secant method. These methods are commonly used in numerical analysis to approximate roots of continuous functions.

## Methods Implemented

- **Bisection Method**: A simple and robust method for finding a root of a function within a given interval.
- **False Position Method**: A method that combines aspects of the bisection method and linear interpolation to converge faster than bisection alone.
- **Fixed-Point Iteration**: A method that transforms a function into an equivalent form to find its fixed points, which may correspond to roots of the original function.
- **Newton-Raphson Method**: An iterative method that uses the derivative of a function to approximate its roots efficiently.
- **Secant Method**: An iterative method that approximates the root of a function by interpolating linearly between two points.

## Usage

To use these methods, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the code.
4. Import the desired methods from `func.py` into your Python script.
5. Use the imported methods with appropriate parameters to find roots of functions.

Example usage:

```python
from func import bissection, false_position_method, point_fix, newton_raphson, secant_method, fi, derivative_f, f

# Example usage of the bisection method
root = bissection(f, 0, 1)

# Example usage of the false position method
root = false_position_method(f, 0, 1)

# Example usage of the fixed-point iteration method
root = point_fix(fi, 0)

# Example usage of the Newton-Raphson method
root = newton_raphson(f, derivative_f, 0)

# Example usage of the secant method
root = secant_method(f, 0, 1)
```

## Contributors

- [Paulo César Moraes de Menezes](https://www.linkedin.com/in/paulo-c%C3%A9sar-moraes-04181b247/) - Maintainer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
