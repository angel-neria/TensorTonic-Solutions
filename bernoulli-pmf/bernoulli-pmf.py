import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = np.array([])
    for i in range(len(x)):
        if(x[i] == 0):
            pmf = np.append(pmf, 1-p)
        else:
            pmf = np.append(pmf, p)

    mean = float(p)
    variance = float(p*(1-p))
    bernoulli = {
        "pmf": pmf,
        "mean": mean,
        "variance": variance
    }
    return bernoulli
    pass