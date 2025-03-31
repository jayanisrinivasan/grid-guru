# src/visualizer.py

import matplotlib.pyplot as plt

def plot_power_flow(net_energy, dispatch):
    plt.plot(net_energy, label="Net Energy")
    plt.plot(dispatch, label="Battery Dispatch")
    plt.xlabel("Day")
    plt.ylabel("Energy (kWh)")
    plt.title("Microgrid Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()
