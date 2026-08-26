from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    X = sorted(x) #importante para la mediana
    n = len(x)

    #Cálculo de la media
    media = sum(X)/len(X)

    #Cálculo de la mediana
    if(len(X)%2 == 0):
        mediana = (X[(n // 2) - 1] + X[n//2])/2
    else:
        mediana = X[n//2]

    #Cálculo de la moda
    frecuencias = Counter(X)
    moda = 0.0
    temp = 0
    for keys in frecuencias.keys():
        if(frecuencias[keys] > temp):
            temp = frecuencias[keys]
            moda = keys #También se puede hacer moda = Counter(x).most_common(1)[0][0]

    #Diccionario
    results = {
        "mean": float(media),
        "median": float(mediana),
        "mode": float(moda)
    }
    return results
    pass