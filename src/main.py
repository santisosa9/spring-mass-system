from integrators import getTimeIntervals, euler, heun, analytical_solution
from plots import plot, plot_equal, plot_analytic
from config.config import read_config

def main():
  
    params = read_config()

    x0 = params["x0"]
    v0 = params["v0"]
    
    t_values = getTimeIntervals()

    euler_x_values, euler_v_values = euler(x0, v0)
    heun_x_values, heun_v_values = heun(x0, v0)
    analytic_x_values, analytic_v_values = analytical_solution()
    
    plot(t_values, euler_x_values, euler_v_values, 0)
    plot(t_values, heun_x_values, heun_v_values, 1)
    plot_equal(
        t_values, euler_x_values, euler_v_values, heun_x_values, heun_v_values
    )
    plot_analytic(t_values, heun_x_values,heun_v_values,analytic_x_values,analytic_v_values)

if __name__ == "__main__":
    main()
