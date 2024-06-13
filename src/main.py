import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema masa-resorte
m = 1  # masa
k = 0.5  # coeficiente de elasticidad
b = 0.5  # friccion
f = 1  # fuerza externa
x0 = 0.0  # posición inicial
v0 = 0.0  # velocidad inicial
t_max = 25  # tiempo de simulacion
h = 0.1  # paso de integracion

# Variables para almacenar los resultados de euler
t_values = np.arange(0, t_max, h)
v_values = []
x_values = []

# Variables para almacenar los resultados de heun
heun_t_values = np.arange(0, t_max, h)
heun_v_values = []
heun_x_values = []

# Variables para almacenar los resultados analíticos
analytic_t_values = np.arange(0, t_max, h)

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
    for t in heun_t_values:
        heun_x_values.append(x)
        heun_v_values.append(v)

        a = acceleration(x, v)
        x_aux = x + h * v
        v_aux = v + h * a

        a_aux = acceleration(x_aux, v_aux)
        x += h * (v + v_aux) / 2
        v += h * (a + a_aux) / 2

# Solución analítica
def system_of_equations(y, t):
    x, v = y
    x_prime = v
    v_prime = acceleration(x, v)
    return [x_prime, v_prime]

def analytical_solution(t_values):
    analytic_y0 = [x0, v0]
    analytic_solution = odeint(system_of_equations, analytic_y0, t_values)
    return analytic_solution.T

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


def plot_equal(t, x, v, t1, x1, v1, t2, x2, v2):
    plt.clf()
    plt.plot(t, x, label="Posición Euler(m)")
    plt.plot(t, v, label="Velocidad Euler(m/s)")
    plt.plot(t1, x1, label="Posición Heun(m)")
    plt.plot(t1, v1, label="Velocidad Heun(m/s)")
    plt.plot(t2, x2, label="Posición Analitic(m)")
    plt.plot(t2, v2, label="Velocidad Analitic(m)")
    plt.xlabel("Tiempo (s)")
    plt.legend(fontsize='x-small', loc='lower right', framealpha=0.3)
    plt.title("Simulación del Modelo Masa-Resorte")
    plt.savefig("img/mygraph3.png")


def main():
    # Inicializar las condiciones iniciales
    x = x0
    v = x0

    analytic_x_values, analytic_v_values = analytical_solution(analytic_t_values)

    euler(x, v)
    plot(t_values, x_values, v_values, 0)

    heun(x, v)
    plot(heun_t_values, heun_x_values, heun_v_values, 1)


    plot_equal(
        t_values, x_values, v_values, heun_t_values, heun_x_values, heun_v_values,
        analytic_t_values, analytic_x_values, analytic_v_values
    )


if __name__ == "__main__":
    main()
