# src/optimizer.py (Upgraded)

def optimize_dispatch(net_energy, max_battery=5, min_battery=0, efficiency=0.9, peak_price=0.30):
    dispatch = []
    grid_draw = []
    cost = []
    battery = 0

    for i, net in enumerate(net_energy):
        if net >= 0:
            battery = min(battery + net * efficiency, max_battery)
        else:
            need = abs(net)
            if battery >= need:
                battery -= need / efficiency
                grid = 0
            else:
                grid = need - battery
                battery = 0
            cost.append(grid * peak_price)
            grid_draw.append(grid)
        dispatch.append(battery)

    return dispatch, grid_draw, cost
