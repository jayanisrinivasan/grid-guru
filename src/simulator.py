# src/simulator.py

def simulate_grid(load, solar, days):
    result = []
    for day in range(days):
        net = solar[day % len(solar)] - load[day % len(load)]
        result.append(net)
    return result
