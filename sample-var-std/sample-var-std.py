import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    mean = np.mean(x)
    n = len(x)
    
    X = x - mean
    X = np.power(X, 2)

    #varianza y desviación estándar
    var = 1/(n-1) * sum(X)
    std = np.sqrt(var)

    #resultados
    var_std = {
        "variance": float(var),
        "standard_deviation": float(std)
    }
    return var_std
    pass