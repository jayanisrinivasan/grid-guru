# ui.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
from simulator import simulate_grid
from optimizer import optimize_dispatch
from visualizer import plot_power_flow
import matplotlib.pyplot as plt

st.title("⚡ Grid Guru Web Simulator")
st.markdown("Model your microgrid with solar + load data.")

days = st.slider("Simulation Days", 1, 30, 7)
load = st.text_input("Daily Load Profile (comma-separated)", "3,4,5,6,7,6,5")
solar = st.text_input("Daily Solar Profile (comma-separated)", "2,3,5,6,8,7,4")

if st.button("Simulate"):
    try:
        load_vals = [float(x) for x in load.split(",")]
        solar_vals = [float(x) for x in solar.split(",")]
        net = simulate_grid(load_vals, solar_vals, days)
        dispatch = optimize_dispatch(net)

        fig, ax = plt.subplots()
        ax.plot(net, label="Net Energy")
        ax.plot(dispatch, label="Battery Dispatch")
        ax.set_xlabel("Day")
        ax.set_ylabel("kWh")
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")
