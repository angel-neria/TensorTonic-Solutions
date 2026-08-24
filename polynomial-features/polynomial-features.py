def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    lista_potencias = []
    
    for i in range(len(values)):
        lista_temp = []
        for j in range(degree + 1):
            lista_temp.append(pow(values[i], j))
        lista_potencias.append(lista_temp)

    return lista_potencias
    pass