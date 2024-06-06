import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema masa-resorte
m = 1      # masa
k = 1      # coeficiente de elasticidad
b = 1      # friccion
f = 1      # fuerza externa
x0 = 0.0   # posición inicial 
v0 = 0.0   # velocidad inicial
t_max = 10 # tiempo de simulacion 
h = 0.01   # paso de integracion

# Variables para almacenar los resultados
t_values = np.arange(0, t_max, h)
x_values = []
v_values = []

# v'(t)
def acceleration(x, v):
  return -k/m * x - b/m * v + 1/m * f

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
  
# Graficar los resultados
def plot():
  plt.plot(t_values, x_values, label='Posición (m)')
  plt.plot(t_values, v_values, label='Velocidad (m/s)')
  plt.xlabel('Tiempo (s)')
  plt.legend()
  plt.title('Simulación del Modelo Masa-Resorte')
  plt.savefig('img/mygraph.png')

def main():
  # Inicializar las condiciones iniciales
  x = x0
  v = x0
  
  euler(x,v)
  
  plot()
  
if __name__ == '__main__':
  main()