import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    d_manhattan = 0.0
    N = len(x)

    for i in range(N):
        d_manhattan = d_manhattan + np.abs(x[i]-y[i])
    return d_manhattan
    pass