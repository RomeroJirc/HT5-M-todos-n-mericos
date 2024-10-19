import numpy as np
import matplotlib.pyplot as plt

# Definimos la derivada y' = -(y + 1)(y + 3)
def f(t, y):
    return -(y + 1) * (y + 3)

# Método de Euler
def euler_method(f, t0, y0, h, t_final):
    t_values = np.arange(t0, t_final + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values

# Parámetros iniciales
t0 = 0      # Tiempo inicial
y0 = -2     # Valor inicial de y
h = 0.2     # Tamaño de paso
t_final = 2 # Tiempo final

# Resolver usando el método de Euler
t_values, y_values = euler_method(f, t0, y0, h, t_final)

# Mostrar los resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t:.1f}, y ≈ {y:.5f}")

# Gráfica de la solución
plt.plot(t_values, y_values, 'o-', label="Aproximación Euler")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solución aproximada usando el Método de Euler')
plt.legend()
plt.grid(True)
plt.show()