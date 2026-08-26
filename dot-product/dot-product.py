import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    prod_punto = 0.0
    
    if (len(x) != len(y)):
        print("error")
        return -9999
    else:
        for i in range(len(x)):
            prod_punto = prod_punto + x[i]*y[i]
        return prod_punto
    pass