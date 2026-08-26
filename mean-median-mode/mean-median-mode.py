from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x.sort() #importante para la mediana
    
    #Cálculo de media
    media = 0
    for i in range(len(x)):
        media = media + x[i]
    media = media/len(x)

    #Cálculo de mediana
    if(len(x)%2 == 0):
        mediana = (x[int(len(x)/2)-1] + x[int(len(x)/2)])/2 #indices comienzan en 0
    else:
        mediana = x[int(np.floor(len(x)/2))] #no le sumamos 1 porque los índices comienzan en 0

    #Cálculo de moda
    frecuencias = Counter(x)
    temp = 0
    moda = 0
    for keys in frecuencias.keys():
        if frecuencias[keys] > temp:
            temp = frecuencias[keys]
            moda = keys

    #Diccionario
    results = {
        "mean": float(media),
        "median": float(mediana),
        "mode": float(moda)
    }
    return results
    pass