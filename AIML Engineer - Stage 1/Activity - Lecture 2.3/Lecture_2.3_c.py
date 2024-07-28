import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x):
    """
    A simple quadratic function: f(x) = x^2 - 4x + 4
    """
    return x**2 - 4*x + 4

x = np.linspace(-2, 6, 100)

y = quadratic_function(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x) = x^2 - 4x + 4')
plt.title('Quadratic Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')

plt.show()