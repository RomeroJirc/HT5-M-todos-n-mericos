def runge_kutta_4th_order(f, x0, y0, x_final, h):
    # Inicializamos las variables
    x = x0
    y = y0

    # Iteramos hasta llegar al valor deseado de x
    while x < x_final:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        # Actualizamos y utilizando el método de Runge-Kutta de 4to orden
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        # Actualizamos x
        x = round(x + h, 5)  # Redondeamos x a 5 cifras decimales

    return round(y, 5)

# Definimos la función diferencial y' = x - y
def differential(x, y):
    return x - y

# Valores iniciales
x0 = 1.0
y0 = 2.0
x_final = 1.2
h = 0.1

# Aplicamos el método
result = runge_kutta_4th_order(differential, x0, y0, x_final, h)
print(f"La aproximación de y(1.2) es: {result}")