import numpy as np
from scipy.integrate import solve_ivp

# Definimos la ecuación diferencial
def dydx(x, y):
    return 1 + x**2 * y**2

# Condición inicial
x0 = 0
y0 = 1

# Intervalo de integración y punto de evaluación
x_eval = 0.5

# Resolvemos la ecuación diferencial usando RK45
sol = solve_ivp(dydx, [x0, x_eval], [y0], method='RK45', rtol=1e-10, atol=1e-10)

# Obtenemos el valor de y en x = 0.5
y_rk45 = sol.y[0, -1]

print(f"Solución aproximada en x = {x_eval} usando RK45: y(x) = {y_rk45:.5f}")