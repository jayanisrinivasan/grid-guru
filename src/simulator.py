# src/simulator.py

def simulate_grid(load_profile, solar_profile, num_days):
    """
    Simulates net energy for a microgrid over a number of days.
    Repeats load and solar profiles if they are shorter than num_days.

    Args:
        load_profile (list of float): Daily energy consumption (kWh)
        solar_profile (list of float): Daily solar generation (kWh)
        num_days (int): Number of days to simulate

    Returns:
        list of float: Net energy (solar - load) per day
    """
    if not load_profile or not solar_profile:
        raise ValueError("Profiles must not be empty.")

    net_energy = []
    for day in range(num_days):
        load = load_profile[day % len(load_profile)]
        solar = solar_profile[day % len(solar_profile)]
        net_energy.append(solar - load)

    return net_energy
