from dataclasses import dataclass

from models.icon import Icon
from models.coord import Coord

@dataclass
class Pin:
    icon: Icon # enum for pin icon type
    location: Coord # leaflet digital location (lon, lat)
    digital_width: int # leaflet digital pin size (pixels)  
    digital_height: int # leaflet digital pin size (pixels) 
    color: str # TO DO: color hex code 

    def __iter__(cls):
        return iter(cls.__name__)





    