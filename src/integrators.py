import numpy as np
from math import exp, sqrt, sin, cos
from config.config import read_config

params = read_config()

m = params["m"]
k = params["k"]
b = params["b"]
f = params["f"]
t_max = params["t_max"]
h = params["h"]

def getTimeIntervals():
  return np.arange(0, t_max, h)

t_values = getTimeIntervals()

# v'(t)
def acceleration(x, v):
    return -k / m * x - b / m * v + 1 / m * f

# Metodo de integración numérica (Euler)
def euler(x, v):
    euler_x_values = []
    euler_v_values = []
    for t in t_values:
        euler_x_values.append(x)
        euler_v_values.append(v)
        a = acceleration(x, v)
        v_aux = v
        v += h * a
        x += h * v_aux
    return euler_x_values, euler_v_values

# Metodo de integración numérica (Heun)
def heun(x, v):
    heun_x_values = []
    heun_v_values = []
    for t in t_values:
        heun_x_values.append(x)
        heun_v_values.append(v)
        a = acceleration(x, v)
        x_aux = x + h * v
        v_aux = v + h * a
        a_aux = acceleration(x_aux, v_aux)
        x += h * (v + v_aux) / 2
        v += h * (a + a_aux) / 2
    return heun_x_values, heun_v_values

# Solución analítica para k = b = m = 1, F(t) = 1 para t >= 0, x(0) = 0, v(0) = 0
def analytical_solution():
    x = 0
    v = 0
    analytic_v_values = []
    analytic_x_values = []
    for t in t_values:
        x = 1 - (sqrt(3) / 3) * exp(-t / 2) * sin(sqrt(3) / 2 * t) - exp(-t / 2) * cos(sqrt(3) / 2 * t)
        v = (sqrt(12) / 3) * exp(-t / 2) * sin(sqrt(3) / 2 * t)
        analytic_x_values.append(x)
        analytic_v_values.append(v)
    return analytic_x_values, analytic_v_values