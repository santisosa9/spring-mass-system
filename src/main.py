import numpy as np
import matplotlib.pyplot as plt
from math import exp, sqrt, sin, cos
from config.config import read_config

# Leer configuración desde config.properties
params = read_config()

# Parámetros del sistema masa-resorte
m = params["m"]
k = params["k"]
b = params["b"]
f = params["f"]
x0 = params["x0"]
v0 = params["v0"]
t_max = params["t_max"]
h = params["h"]

# Variables para almacenar los resultados de euler
t_values = np.arange(0, t_max, h)
v_values = []
x_values = []

# Variables para almacenar los resultados de heun
heun_v_values = []
heun_x_values = []

# Variables para almacenar los resultados analíticos
analytic_v_values = []
analytic_x_values = []

# v'(t)
def acceleration(x, v):
    return -k / m * x - b / m * v + 1 / m * f

# Metodo de integración numérica (Euler)
def euler(x, v):
    x_values.clear
    v_values.clear
    for t in t_values:
        x_values.append(x)
        v_values.append(v)
        a = acceleration(x, v)
        v_aux = v
        v += h * a
        x += h * v_aux


def heun(x, v):
    heun_x_values.clear()
    heun_v_values.clear()
    for t in t_values:
        heun_x_values.append(x)
        heun_v_values.append(v)

        a = acceleration(x, v)
        x_aux = x + h * v
        v_aux = v + h * a

        a_aux = acceleration(x_aux, v_aux)
        x += h * (v + v_aux) / 2
        v += h * (a + a_aux) / 2

# Solución analítica para k = b = m = 1, F(t) = 1 para t>= 0, x(0)=0, v(0)=0
def analytical_solution(t_values):
    x= 0
    v= 0
    analytic_x_values.clear()
    analytic_v_values.clear()
    for t in t_values:
        x = 1 - (sqrt(3) / 3) * exp(-t / 2) * sin(sqrt(3) / 2 * t) - exp(-t / 2) * cos(sqrt(3) / 2 * t)
        v = (sqrt(12) / 3) * exp(-t / 2) * sin(sqrt(3) / 2 * t)
        analytic_x_values.append(x)
        analytic_v_values.append(v)

# Graficar los resultados
def plot(t, x, v, flag):
    plt.clf()
    if flag == 0:
        plt.plot(t, x, label="Posición Euler(m)")
        plt.plot(t, v, label="Velocidad Euler(m/s)")
    else:
        plt.plot(t, x, label="Posición Heun(m)")
        plt.plot(t, v, label="Velocidad Heun(m/s)")
    plt.xlabel("Tiempo (s)")
    plt.legend()
    plt.title("Simulación del Modelo Masa-Resorte")
    if flag == 0:
        plt.savefig("img/mygraph.png")
    else:
        plt.savefig("img/mygraph2.png")

#plotea la Euler y Heun con los mismos parametros
def plot_equal(t, x, v, x1, v1):
    plt.clf()
    plt.plot(t, x, label="Posición Euler(m)")
    plt.plot(t, v, label="Velocidad Euler(m/s)")
    plt.plot(t, x1, label="Posición Heun(m)")
    plt.plot(t, v1, label="Velocidad Heun(m/s)")
    plt.xlabel("Tiempo (s)")
    plt.legend(fontsize='x-small', loc='lower right', framealpha=0.3)
    plt.title("Simulación del Modelo Masa-Resorte")
    plt.savefig("img/mygraph3.png")

#plotea la analitica y la Heun
def plot_analitic(t, x, v, x1, v1):
    plt.clf()
    plt.plot(t, x, label="Posición Heun(m)")
    plt.plot(t, v, label="Velocidad Heun(m/s)")
    plt.plot(t, x1, label="Posición Analitic(m)")
    plt.plot(t, v1, label="Velocidad Analitic(m)")
    plt.xlabel("Tiempo (s)")
    plt.legend(fontsize='x-small', loc='lower right', framealpha=0.3)
    plt.title("Simulación del Modelo Masa-Resorte")
    plt.savefig("img/mygraph2.png")


def main():
    # Inicializar las condiciones iniciales
    x = x0
    v = x0

    analytical_solution(t_values)

    euler(x, v)
    plot(t_values, x_values, v_values, 0)

    heun(x, v)
    plot(t_values, heun_x_values, heun_v_values, 1)

    plot_equal(
        t_values, x_values, v_values, heun_x_values, heun_v_values
    )

    plot_analitic(t_values, heun_x_values,heun_v_values,analytic_x_values,analytic_v_values)


if __name__ == "__main__":
    main()
