from dataclasses import dataclass

from loguru import logger
import numpy as np

# Da correggere tutti i typo di timestamp


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

    # C'è un modo per tenersi sia questa cosa qui, che gli array?
    def __str__(self):
        return f"Timestamp: {self.timestamp}, ADC Value: {self.adc}, Voltage: {self.voltage()}"

    def __getitem__(self, index):
        _tuple = (self.timestamp, self.voltage())
        return _tuple[index]


class VoltageData:

    '''Simple interface to a set of voltage readings.
    '''
    # adc should not be exposed

    def __init__(self, timestaps, adcs):
        if len(timestaps) != len(adcs):
            raise IndexError("timestamps and adcs must be the same lenght")
        self.adcs = np.float64(adcs)
        self.timestaps = np.float64(timestaps)
        self._readings = [Readings(x, y)
                          for (x, y) in zip(self.timestaps, self.adcs)]
        self.voltages = np.float64([_list[1] for _list in self._readings])
        # self._iterator = iter(self._readings)

    def from_path(self, file_path):
        tryT = []
        tryA = []
        with open(file_path,"r") as text_file:
            for line in text_file:
                x,y = line.split("\t")
                tryT.append(float(x))
                tryA.append(float(y))
        self._timestamps_2 = np.float64(np.array(tryT))
        self._adc_2 = np.float64(np.array(tryA))

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
            _str = _str + f"{i}\t{(str(lines[0]),str(lines[1]))}"
            if i < len(self._readings) - 1:
                _str = _str + "\n"
            # fix this shit with some real function^
        return _str

    def __call__(self):
        pass

    def plot(self):
        pass


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
    logger.info(f"VoltageData.timestamps is {pino.timestaps}"
                f"and its type is {type(pino.timestaps)}")
    logger.info(
        f"The third value of VoltageData.timestamp is {pino.timestaps[2]}")
    logger.info(
        f"VoltageData is sliceable, this are the even index terms {pino.timestaps[0::2]}")
    logger.info(f"{len(pino)}")
    logger.info("VoltageData is callable with prints")
    print(pino)
    gino = VoltageData(timestamps_data, adc_data)
    gino.from_path("voltage.txt")
    print(gino._adc_2,gino._timestamps_2)
