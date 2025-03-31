# src/optimizer.py

def optimize_dispatch(net_energy):
    dispatch = []
    battery = 0
    for net in net_energy:
        battery += net
        dispatch.append(battery)
    return dispatch
