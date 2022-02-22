

from pickletools import long1
import decimal
import numpy as np
class Coord:
    def __init__(self, lon, lat):
        self.lon = decimal.Decimal(lon)
        self.lat = decimal.Decimal(lat)

    def __sub__(self, other):
        diff_log = decimal.Decimal(abs(self.lon - other.lon))
        diff_lat = decimal.Decimal(abs(self.lat - other.lat))

        return np.array([diff_log, diff_lat])
