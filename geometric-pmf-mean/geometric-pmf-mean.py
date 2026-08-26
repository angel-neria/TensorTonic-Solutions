import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    pmf = np.array([])
    expected_value = float(1/p)

    for i in range(len(k)):
        pmf = np.append(pmf, pow(1-p, k[i]-1)*p)

    geometric = {
        "pmf": pmf,
        "mean": expected_value
    }

    return geometric
    pass