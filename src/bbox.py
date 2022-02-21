
from unicodedata import decimal
from coord import Coord
import decimal
import numpy
class Bbox:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __sub__(self, other):
        tl_lon = decimal.Decimal(self.top_left.lon - other.top_left.lon)
        tl_lat = decimal.Decimal(self.top_left.lat - other.top_left.lat)
        br_lon = decimal.Decimal(self.bottom_right.lon - other.bottom_right.lon)
        br_lat = decimal.Decimal(self.bottom_right.lat - other.bottom_right.lat)

        # return Bbox(Coord(tl_lon, tl_lat), Coord(br_lon, br_lat))
        return numpy.array([tl_lon, tl_lat, br_lon, br_lat])

    def lat_lon_print(self):
        print("" + str(self.top_left.lat) + "," + str(self.top_left.lon) + "," + str(self.bottom_right.lat) + "," + str(self.bottom_right.lon) + "") 


    def __repr__(self):
        return "[(lon: " + str(self.top_left.lon) + ", lat: " + str(self.top_left.lat) + "), (lon: " + str(self.bottom_right.lon) + ", lat: " + str(self.bottom_right.lat) + ")]" 


    def __str__(self):
        return "[(lon: " + str(self.top_left.lon) + ", lat: " + str(self.top_left.lat) + "), (lon: " + str(self.bottom_right.lon) + ", lat: " + str(self.bottom_right.lat) + ")]" 

    
    # TO DO: Support multiple constructors wiht __init__(self, *args):
    # def __init__(self, south, west, north, east):
    #     self.top_left = Coord(south, west)
    #     self.bottom_right = Coord(north, east)
