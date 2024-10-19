import numpy as np
import matplotlib.pyplot as plt

# Definimos la función derivada
def f(x, y):
    return -5 * y + 5 * x**2 + 27

# Parámetros iniciales
x0 = 0          # Valor inicial de x
y0 = 1/3        # Valor inicial de y
h = 0.1         # Tamaño del paso
x_final = 1     # Valor final de x

# Número de pasos
n_steps = int((x_final - x0) / h) + 1

# Inicializamos los arrays para x e y
x_values = np.linspace(x0, x_final, n_steps)
y_values = np.zeros(n_steps)
y_values[0] = y0  # Condición inicial

# Implementamos el método de Euler
for i in range(1, n_steps):
    y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])

# Mostramos los resultados
for i in range(n_steps):
    print(f"x = {x_values[i]:.1f}, y = {y_values[i]:.6f}")

# Gráfica de los resultados
plt.plot(x_values, y_values, label='Aproximación de Euler', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución aproximada usando el método de Euler')
plt.legend()
plt.grid(True)
plt.show()