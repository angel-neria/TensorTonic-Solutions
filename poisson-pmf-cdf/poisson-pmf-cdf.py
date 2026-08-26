import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    #Cálculo de PMF:
    pmf = (math.exp(-lam)*lam**k)/(math.factorial(k))

    #Cálculo de CDF
    cdf = 0.0
    for i in range(k+1):
        cdf = cdf + (lam**i)/(math.factorial(i))
    cdf = cdf * math.exp(-lam)

    #Diccionario
    poisson = {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }

    return poisson
        
    pass