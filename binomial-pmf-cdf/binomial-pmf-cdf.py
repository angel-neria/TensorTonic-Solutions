import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    pmf = 0.0
    cdf = 0.0

    #cálculo de pmf y cdf
    pmf = math.comb(n,k) * pow(p, k) * pow(1-p, n-k)
    for i in range(0,k):
        cdf = cdf + math.comb(n,i) * pow(p, i) * pow(1-p, n-i)
    cdf = cdf + pmf

    #diccionario
    dict_pmf_cdf ={
        "pmf": float(pmf),
        "cdf": float(cdf)
    }
    return dict_pmf_cdf
    pass