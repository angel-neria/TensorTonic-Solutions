import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    distancia = 0.0
    
    if(len(x) != len(y)):
        print("error: las dos listas deben ser del mismo tamaño")
        return -1
    else:
        for i in range(len(x)):
            distancia = distancia + (x[i] - y[i])**2
        distancia = np.sqrt(distancia)
        return distancia
    pass