import math

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    log_list = []
    for x in values:
        log_list.append(math.log(x+1))

    return log_list
    pass