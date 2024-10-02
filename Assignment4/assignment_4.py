#!/usr/bin/python3

from loguru import logger
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):

    def __init__(self,x,y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        super().__init__(self._x, self._y)

    def _grid(self):
        return np.linspace(self._x.min(),self._x.max(),250)
    
    def plot(self):
        plt.scatter(self._x,self._y,color = "orange")
        grid_x = np.linspace(self._x.min(),self._x.max(),250)
        plt.plot(self._grid(),self(self._grid()))
    
    def normalizzation(self):
        return self.integral(self._x.min(),self._x.max())

    def _show_norm(self):
        plt.plot(self._grid(),[self.integral(self._x.min(),i) for i in self._grid()])

    def ppf(self):
        pass

def triang(x):
  """
  Funzione che calcola il valore di una funzione triangolare strettamente positiva.

  Args:
    x: Valore in input per cui calcolare la funzione.

  Returns:
    Il valore della funzione triangolare in corrispondenza di x.
  """

  # Condizioni per definire i tratti della funzione triangolare
  if x < 0 or x > 10:
    return 0
  elif x <= 5:
    return x / 5
  else:
    return (10 - x) / 5

def gauss(x, mu, sigma):
  """
  Calcola il valore di una gaussiana in un punto x, con media mu e deviazione standard sigma.

  Args:
    x: Valore in input per cui calcolare la gaussiana.
    mu: Media della distribuzione.
    sigma: Deviazione standard della distribuzione.

  Returns:
    Il valore della gaussiana in corrispondenza di x.
  """

  return (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-(x - mu)**2 / (2*sigma**2))

if __name__ == "__main__":
    data_x = np.linspace(0.,10.,6)
    #data_y = np.array([triang(i) for i in data_x])
    data_y = np.exp(data_x)
    pdf = ProbabilityDensityFunction(data_x,data_y)
    logger.info(pdf.normalizzation())
    pdf.plot()
    plt.show()
    pdf._show_norm()
    plt.show()