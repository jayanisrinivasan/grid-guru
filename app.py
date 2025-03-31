# app.py

from src.simulator import simulate_grid
from src.optimizer import optimize_dispatch
from src.visualizer import plot_power_flow

def main():
    # Example parameters
    simulation_days = 7
    load_profile = [3, 4, 5, 6, 7, 6, 5]  # kWh per day
    solar_profile = [2, 3, 5, 6, 8, 7, 4]  # kWh per day

    simulation_results = simulate_grid(load_profile, solar_profile, simulation_days)
    dispatch_plan = optimize_dispatch(simulation_results)
    plot_power_flow(simulation_results, dispatch_plan)

if __name__ == "__main__":
    main()
