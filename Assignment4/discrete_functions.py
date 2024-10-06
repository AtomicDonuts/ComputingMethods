def func(x):
    """
    random bullshit go!
    """
    lel = 0
    if x <= 0:
        lel = 0
    elif x > 0 and x < 2:
        lel = 1.5 * x
    elif x >= 2 and x < 4:
        lel = -x + 5
    elif x >= 4 and x < 5:
        lel = x - 3
    elif x >= 5 and x < 8:
        lel = 2./3. * x - 4./3.
    elif x >= 8 and x < 10:
        lel = -2*x + 20
    else:
        lel = 0
    return lel


def triang(val):
    """
    Funzione che calcola il valore di una funzione triangolare strettamente positiva.

    Args:
            x: Valore in input per cui calcolare la funzione.

    Returns:
            Il valore della funzione triangolare in corrispondenza di x.
    """
    # Condizioni per definire i tratti della funzione triangolare
    result = 0
    if val < 0 or val > 10:
        result = 0
    elif val <= 5:
        result = val / 5
    else:
        result = (10 - val) / 5
    return result
