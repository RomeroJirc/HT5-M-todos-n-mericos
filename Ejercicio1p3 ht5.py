import numpy as np
import matplotlib.pyplot as plt

# Función que define la ecuación diferencial
def f(t, y):
    return y**2 / (t + 1)

# Método de Euler
def euler(f, t0, y0, h, n):
    t_values = np.linspace(t0, t0 + n*h, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0
    
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return t_values, y_values

# Valores iniciales y parámetros
t0 = 1
y0 = -1 / np.log(2)  # Condición inicial
h = 0.1
n = int((2 - t0) / h)

# Solución aproximada usando Euler
t_values, y_approx = euler(f, t0, y0, h, n)

# Aquí podemos definir la solución exacta si la encontramos simbólicamente
def exact_solution(t):
    # Suponiendo que la solución exacta es conocida
    return -1 / np.log(t + 1)

# Solución exacta
y_exact = exact_solution(t_values)

# Cálculo del error porcentual
error_percent = np.abs((y_exact - y_approx) / y_exact) * 100

# Mostrar resultados
for i in range(len(t_values)):
    print(f"t = {t_values[i]:.2f}, y_aprox = {y_approx[i]:.5f}, y_exact = {y_exact[i]:.5f}, error = {error_percent[i]:.2f}%")

# Graficar
plt.plot(t_values, y_approx, label="Euler Approximation", marker='o')
plt.plot(t_values, y_exact, label="Exact Solution", linestyle='--')
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()