import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    X_matriz = np.array(X)
    Y_vector = np.array(y)
    X_matriz_T = np.transpose(X_matriz)

    w = X_matriz_T @ X_matriz
    w = np.linalg.inv(w)
    w = w @ X_matriz_T
    w = w @ Y_vector

    return w
    pass