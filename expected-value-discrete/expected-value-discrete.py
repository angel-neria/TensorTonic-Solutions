import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    esperanza = 0.0
    
    if(len(x) != len(p)):
        print("error")
    else:
        for i in range(len(x)):
            esperanza = esperanza + x[i]*p[i]
            
    return esperanza
    pass