from dataclasses import dataclass
from typing import List

from mercantile import Bbox
from models.border_style import BorderStyle

from models.pin import Pin
from models.print_format import PrintFormat

@dataclass
class Map:
    map_box : Bbox # lng lat box of ui map
    tile_url : str # tile url w/ style 
    print_format : PrintFormat # Size of print
    pins : Pin # List of pins on print
    border_style : BorderStyle # TO DO: Style of Border on print 
    file_path : str # Path to file  