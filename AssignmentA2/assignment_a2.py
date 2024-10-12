from dataclasses import dataclass

from loguru import logger
import numpy as np


@dataclass
class Readings:

    '''Class that rapresent some readings
    '''

    timestamp: float
    adc: int

    def voltage(self):
        '''Return the converted value of the adc to the physical voltage
        '''
        return 1.69 * self.adc + 0.420


class VoltageData:
    
    '''Simple interface to a set of voltage readings.
    '''

    def __init__(self,timestaps,adcs):
        if len(timestaps) != len(adcs):
            raise IndexError("timestamps and adcs must be the same lenght")
        self.adcs = adcs
        self.timestaps = timestaps
        self._reading = [Readings(x,y) for (x,y) in zip(self.timestaps,self.adcs)]
        self._iterator = iter(self._reading)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self._iterator)

if __name__ == "__main__":
    adc_data = np.arange(0.,10.,1)
    timestamps_data = np.arange(0., 10.,1)
    for i in VoltageData(timestamps_data,adc_data):
        print(i)
