import numpy as np
import matplotlib.pyplot as plt

# --- Ejercicio 1.4 ---
# Función que define la ecuación diferencial (Ejercicio 1.4)
def f(t, y):
    return t * np.exp(2*t) - 2*y

# Método de Euler
def euler(f, t0, y0, h, n):
    t_values = np.linspace(t0, t0 + n*h, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0
    
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return t_values, y_values

# Valores iniciales y parámetros para el ejercicio 1.4
t0 = 0
y0 = 0  # Condición inicial
h = 0.5
n = int((1 - t0) / h)

# Solución aproximada usando Euler (Ejercicio 1.4)
t_values, y_approx = euler(f, t0, y0, h, n)

# Aquí definimos la solución exacta (Ejercicio 1.4)
def exact_solution(t):
    return (1/5)*(np.exp(2*t)*(5*t - 1) + 1)

# Solución exacta (Ejercicio 1.4)
y_exact = exact_solution(t_values)

# Cálculo del error porcentual (Ejercicio 1.4)
error_percent = np.abs((y_exact - y_approx) / y_exact) * 100

# Mostrar resultados
print("Resultados para el Ejercicio 1.4:")
for i in range(len(t_values)):
    print(f"t = {t_values[i]:.2f}, y_aprox = {y_approx[i]:.5f}, y_exact = {y_exact[i]:.5f}, error = {error_percent[i]:.2f}%")

# Graficar los resultados
plt.figure(figsize=(6, 4))
plt.plot(t_values, y_approx, label="Euler Approximation", marker='o')
plt.plot(t_values, y_exact, label="Exact Solution", linestyle='--')
plt.xlabel("t")
plt.ylabel("y")
plt.title("Ejercicio 1.4")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()