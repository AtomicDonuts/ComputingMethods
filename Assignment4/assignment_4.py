#!/usr/bin/python3
"""
Probability Density Function module developed for the Computing Methods course
"""

from loguru import logger
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    """
    Probability Density Function for a given set of points via scipy InterpolatedUnivariateSplie

    Parameters:
            x : (N,), array_like

            y : (N,), array_like
    """

    def __init__(self, x, y):
        """
        Constructor mmodule

        Parameters:
            x : (N,), array_like

            y : (N,), array_like
        """
        spline = InterpolatedUnivariateSpline(x, y)
        self.norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / self.norm
        super().__init__(self._x, self._y)

    def _grid(self):
        """
        return a dense set of point for plots in the self._x domain
        """
        return np.linspace(self._x.min(), self._x.max(), 1000)

    def normalizzation(self):
        """
        return the normalizzation of the pdf, expected value is 1.
        """
        return self.integral(self._x.min(), self._x.max())

    def _cumulative(self, val):
        """
        return cpf of the pdf evalueted in val
        Parameters:
                val: float
        """
        return self.integral(self._x.min(), val)

    def _a_cumulative(self):
        """
        return an array of the cpf in the given domain of self._x
        """
        return [self._cumulative(i) for i in self._grid()]

    def ppf(self,val):
        """
        return ppf of the pdf evalueted in val
        Parameters:
                val: float
        """
        prob2 = InterpolatedUnivariateSpline(self._a_cumulative(),self._grid())
        return prob2(val)

    def _a_ppf(self):
        """
        return an array of the ppf in the given domain of self._x
        """
        return [self.ppf(y) for y in np.linspace(0., 1., 100)]

    def random(self):
        """
        reutrn a pseudo-random number according to the pdf
        """
        return self.ppf(np.random.random())

    def plot_pdf(self):
        """
        plot of the input set of points and the interpoleted spline
        """
        plt.scatter(self._x, self._y, color="orange")
        plt.plot(self._grid(), self(self._grid()))

    def plot_cumulative(self):
        """
        plot of the cpf of the pdf
        """
        plt.plot(self._grid(), [self._cumulative(i) for i in self._grid()])

    def plot_ppf(self):
        """
        plot of the cpf of the pdf
        """
        plt.plot(np.linspace(0., 1., 100),self._a_ppf())

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

def gauss(val, mu_val, sigma):
    """
    Calcola il valore di una gaussiana in un punto x, con media mu e deviazione standard sigma.

    Args:
            x: Valore in input per cui calcolare la gaussiana.
            mu: Media della distribuzione.
            sigma: Deviazione standard della distribuzione.

    Returns:
            Il valore della gaussiana in corrispondenza di x.
    """

    return (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-(val - mu_val)**2 / (2*sigma**2))

def some_tests():
    """
    some useless tests
    """
    _rand_numb = np.random.random()
    logger.debug(f"RE: {np.abs(np.abs(np.cos(_rand_numb))/pdf.norm - pdf(_rand_numb))/100.}")
    logger.debug(f"Value of pdf in {_rand_numb}: {pdf(_rand_numb)}")

if __name__ == "__main__":
    data_x = np.linspace(0., 10., 30)
    # data_y = np.array([triang(i) for i in data_x])
    # data_y = np.array([gauss(i,5,1) for i in data_x])
    data_y = np.abs(np.cos(data_x))
    pdf = ProbabilityDensityFunction(data_x, data_y)
    logger.info(pdf.normalizzation())
    pdf.plot_pdf()
    plt.show()
    pdf.plot_cumulative()
    plt.show()
    pdf.plot_ppf()
    plt.show()
    plt.hist([pdf.random() for i in range(0,10000)],bins = 40)
    plt.show()
    some_tests()
    