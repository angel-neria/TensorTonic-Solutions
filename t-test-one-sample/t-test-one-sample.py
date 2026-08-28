import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    n = len(x)
    X = np.array(x)
    mean = np.mean(X)

    X_centrada = X - mean
    X_centrada2 = np.power(X_centrada, 2)

    
    #Cálculo de la desviación
    s = np.sqrt(sum(X_centrada2)/(n-1))

    #Cálculo del estadístico t
    t = (mean - mu0)/(s/np.sqrt(n))

    return float(t)
    
    pass