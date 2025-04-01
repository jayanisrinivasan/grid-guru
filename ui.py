# ui.py (Upgraded Grid Guru with input validation)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# Add src/ to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from simulator import simulate_grid
from optimizer import optimize_dispatch
from visualizer import plot_power_flow

st.set_page_config(page_title="Grid Guru Simulator", page_icon="⚡", layout="centered")

st.markdown("""
# ⚡ Grid Guru Web Simulator
Model your microgrid with solar + load data, dispatch optimization, and cost tracking.
""")

st.sidebar.header("⚙️ Simulation Settings")
days = st.sidebar.slider("Simulation Days", 1, 30, 7)

uploaded = st.sidebar.file_uploader("Upload CSV (with 'load' and 'solar' columns)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    load = df['load'].tolist()
    solar = df['solar'].tolist()
else:
    load_input = st.text_input("Daily Load Profile (comma-separated)", "3,4,5,6,7,6,5")
    solar_input = st.text_input("Daily Solar Profile (comma-separated)", "2,3,5,6,8,7,4")
    try:
        load = [float(x.strip()) for x in load_input.split(",") if x.strip() != ""]
        solar = [float(x.strip()) for x in solar_input.split(",") if x.strip() != ""]
    except ValueError:
        st.error("Invalid input: Please enter only numbers separated by commas.")
        st.stop()

if st.button("Simulate"):
    try:
        if len(load) == 0 or len(solar) == 0:
            st.error("Load and solar inputs must not be empty.")
            st.stop()

        # Simulate with repeating profiles to match days
        net = simulate_grid(load, solar, days)
        dispatch, grid_draw, grid_cost = optimize_dispatch(net)

        # Plot
        fig, ax = plt.subplots()
        ax.plot(net, label="Net Energy", linewidth=2)
        ax.plot(dispatch, label="Battery Dispatch", linewidth=2)
        ax.set_xlabel("Day")
        ax.set_ylabel("Energy (kWh)")
        ax.set_title("Energy Flow Simulation")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Metrics
        st.subheader("📊 Simulation Summary")
        st.metric("Total Grid Energy Used (kWh)", round(sum(grid_draw), 2))
        st.metric("Estimated Grid Cost ($)", f"{sum(grid_cost):.2f}")

        # Download Results
        grid_draw += [0] * (days - len(grid_draw))
        grid_cost += [0] * (days - len(grid_cost))
        df_out = pd.DataFrame({
            "Day": list(range(days)),
            "Net Energy": net,
            "Battery Dispatch": dispatch,
            "Grid Draw": grid_draw,
            "Cost ($)": grid_cost
        })
        st.download_button("📥 Download CSV", df_out.to_csv(index=False), "results.csv", "text/csv")

    except Exception as e:
        st.error(f"Simulation error: {e}")
