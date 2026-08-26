def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    columnas = []
    m = len(data)
    n = len(data[0])

    #matriz transpuesta
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(data[j][i])
        columnas.append(temp) 

    #máximo y mínimo por columna
    lista_max = []
    lista_min = []
    for columna in columnas:
        max = columna[0]
        min = columna[0]
        for i in range(m):
            if(columna[i] > max):
                max = columna [i]
            if(columna[i] < min):
                min = columna[i]
        lista_max.append(max)
        lista_min.append(min)

    #Estandarización:
    for i in range(m):
        for j in range(n):
            if(lista_max[j] !=lista_min[j]):
                data[i][j] = (data[i][j] - lista_min[j])/(lista_max[j]-lista_min[j])
            else:
                data[i][j] = 0
    return data
        
    pass