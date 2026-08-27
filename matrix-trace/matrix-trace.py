import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    n = len(A) #A es una matriz cuadrada

    trace = 0.0
    for i in range(n):
        trace = trace + A[i][i]

    return float(trace)
    pass