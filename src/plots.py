import matplotlib.pyplot as plt

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

def plot_equal(t, x, v, x1, v1):
    plt.clf()
    plt.plot(t, x, label="Posición Euler(m)")
    plt.plot(t, v, label="Velocidad Euler(m/s)")
    plt.plot(t, x1, label="Posición Heun(m)")
    plt.plot(t, v1, label="Velocidad Heun(m/s)")
    plt.xlabel("Tiempo (s)")
    plt.legend(fontsize="x-small", loc="lower right", framealpha=0.3)
    plt.title("Simulación del Modelo Masa-Resorte")
    plt.savefig("img/mygraph3.png")

def plot_analytic(t, x, v, x1, v1):
    plt.clf()
    plt.plot(t, x, label="Posición Heun(m)")
    plt.plot(t, v, label="Velocidad Heun(m/s)")
    plt.plot(t, x1, label="Posición Analítica(m)")
    plt.plot(t, v1, label="Velocidad Analítica(m)")
    plt.xlabel("Tiempo (s)")
    plt.legend(fontsize="x-small", loc="lower right", framealpha=0.3)
    plt.title("Simulación del Modelo Masa-Resorte")
    plt.savefig("img/mygraph4.png")
