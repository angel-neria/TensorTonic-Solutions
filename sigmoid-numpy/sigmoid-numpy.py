import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    #caso 1: x es una lista
    if(type(x) == list):
        X = np.array(x)
        sigma_X = 1.0 / (1.0 + np.exp(-X)) #sigmoid(x)
        return sigma_X
        
    #caso 2: x no es una lista 
    else:
        sigma_X = 1.0/(1.0+np.exp(-x)) #sigmoid(x)
        return sigma_X
    pass