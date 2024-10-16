#!/usr/bin/python3
"""
Probability Density Function module developed for the Computing Methods course
"""

from loguru import logger
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import discrete_functions as df


class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    """
    Probability Density Function for a given set of points via scipy InterpolatedUnivariateSplie

    Parameters:
            x : (N,), array_like

            y : (N,), array_like
    """

    def __init__(self, x, y, _w=None, _bbox=[None, None], _k=3, _ext=0, _check_finite=False):
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
        super().__init__(self._x, self._y, w=_w, bbox=_bbox,
                         k=_k, ext=_ext, check_finite=_check_finite)

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

    def ppf(self, val):
        """
        return ppf of the pdf evalueted in val
        Parameters:
                val: float
        """
        prob2 = InterpolatedUnivariateSpline(
            self._a_cumulative(), self._grid())
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

    def a_random(self, dim):
        """
        return a n-dimentional array of pseudo-random number according to the pdf

        Parameters:
                dim: int
                    the dimention od the array
        """
        pino = np.random.rand(dim)
        return pdf.ppf(pino)

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
        plt.plot(np.linspace(0., 1., 100), self._a_ppf())


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


if __name__ == "__main__":
    data_x = np.linspace(0., 10., 30)
    # data_y = np.array([df.triang(i) for i in data_x])
    # data_y = np.array([gauss(i,5,1) for i in data_x])
    data_y = np.array([df.func(i) for i in data_x])
    # data_y = np.abs(np.cos(data_x))
    pdf = ProbabilityDensityFunction(data_x, data_y)
    logger.info(pdf.normalizzation())
    pdf.plot_pdf()
    plt.show()
    pdf.plot_cumulative()
    plt.show()
    pdf.plot_ppf()
    plt.show()
    # plt.hist([pdf.random() for i in range(0, 10000)], bins=40)
    plt.hist(pdf.a_random(10000), bins=40)
    plt.show()
