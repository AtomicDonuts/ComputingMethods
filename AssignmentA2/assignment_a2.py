# %%
from dataclasses import dataclass

from loguru import logger
import numpy as np
from scipy.interpolate import CubicSpline

# Da correggere tutti i typo di timestamp


@dataclass
class Reading:

    '''Class that rapresent some readings
    '''

    timestamp: float
    adc: int

    _CONVERSION_SLOPE = 1.420
    _CONVERSION_OFFSET = 0.690

    @staticmethod
    def _adc_to_voltage(adc):
        """Convertion function
        """
        return Reading._CONVERSION_SLOPE * adc + Reading._CONVERSION_OFFSET

    def voltage(self):
        """Convert ADC counts to a physical voltage (in V) using the convertion function.
        """
        return self._adc_to_voltage(self.adc)

    def __str__(self):
        return f"Timestamp: {self.timestamp}, ADC Value: {self.adc}, Voltage: {self.voltage()}"

    def __getitem__(self, index):
        _tuple = (self.timestamp, self.voltage())
        return _tuple[index]


class VoltageData:

    '''Simple interface to a set of voltage readings.
    '''
    # adc should not be exposed

    def __init__(self, timestamps, adcs):
        if len(timestamps) != len(adcs):
            raise IndexError("timestamps and adcs must be the same lenght")
        self.adcs = np.float64(adcs)
        self.timestamps = np.float64(timestamps)
        self._readings = [Reading(x, y)
                          for (x, y) in zip(self.timestamps, self.adcs)]
        self.voltages = np.float64([_list[1] for _list in self._readings])
        # self._iterator = iter(self._readings)

    @classmethod
    def from_path(cls, file_path):
        tryT = []
        tryA = []
        with open(file_path, "r") as text_file:
            for line in text_file:
                x, y = line.split()
                tryT.append(float(x))
                tryA.append(int(y))
        timestamps = np.float64(np.array(tryT))
        adc = np.float64(np.array(tryA))
        return cls(timestamps, adc)

    def __iter__(self):
        self._iterator = iter(self._readings)
        return self

    def __next__(self):
        pino = next(self._iterator)
        return np.array([pino[0], pino[1]])

    def __getitem__(self, index):
        return self._readings[index]

    def __len__(self):
        return len(self._readings)

    def __str__(self):
        _str = "index\t(timestamps,voltage)\n"
        for i, lines in enumerate(self._readings):
            # _str = _str + f"{i}\t{lines}\n"
            _str = _str + \
                f"Line#: {i} Timestamp: {lines[0]}, Voltage: {lines[1]}"
            if i < len(self._readings) - 1:
                _str = _str + "\n"
        return _str

    def __repr__(self):
        _rep = ""
        for i, lines in enumerate(self._readings):
            _rep = _rep + \
                f"VoltageData({i}"
            for j in lines:
                _rep = _rep + f",{j}"
            _rep = _rep + ")\n"
        return _rep

    def __call__(self,value):
        spline = CubicSpline(self.timestamps,self.adcs)
        return spline(value)

    def plot(self):
        pass


# %%
if __name__ == "__main__":
    adc_data = np.arange(0., 10., 1)
    timestamps_data = np.arange(0., 10., 1)
    pino = VoltageData(timestamps_data, adc_data)
    logger.info(
        "VoltageData is iterable, and its elements can be called with the [] notation")
    for i in pino:
        logger.info(f"{i}\t{i[0]}\t{i[1]}")
    gino = pino[3]
    logger.info(f"VoltageData[3] is {gino}")
    logger.info(f"The timestamp of element 3 of VoltageData"
                f"is {pino[3][0]} and its type is {type(pino[3][0])}")
    logger.info(f"VoltageData.timestamps is {pino.timestamps}"
                f"and its type is {type(pino.timestamps)}")
    logger.info(
        f"The third value of VoltageData.timestamp is {pino.timestamps[2]}")
    logger.info(
        f"VoltageData is sliceable, this are the even index terms {pino.timestamps[0::2]}")
    logger.info(f"Lenght of VoltageData is: {len(pino)}")
    logger.info("VoltageData is callable with reprs")
    logger.info(repr(pino))
    logger.info("VoltageData is callable with prints")
    logger.info(pino)
    logger.info("VoltageData can be generated from data file")
    gino = VoltageData.from_path("voltage.txt")
    logger.info(gino)
    logger.info("VoltageData is callable. VoltageData(x) return"\
                " the interpolated value of the voltage in x")
    logger.info(gino(3.2))


# %%
