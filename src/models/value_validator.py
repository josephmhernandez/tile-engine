
from models.bbox import Bbox
from models.coord import Coord
from models.map_style import MapStyle
from models.map_style import get_map_style_specifications
from models.pin import Pin
from typing import List
import logging

from models.print_format import PrintFormat


class ValueValidator:
    @staticmethod
    def extract_valid_bbox_value(bbox_values: list) -> Bbox:
        try:
            #TO DO: 
            # Validate Bbox values
            
            # Return Bbox value
            tl = Coord(bbox_values[0], bbox_values[1])
            br = Coord(bbox_values[2], bbox_values[3])
            context_bbox = Bbox(tl, br)
            return context_bbox
        except:
            raise ValueError("Could not convert bbox_values list to Bbox object")

    @staticmethod
    def extract_valid_map_style_value(map_style: str) -> dict:
        logging.info("extract map style specifications")
        # TO DO: Make this method call cleaner. pls. 
        rtn_style = get_map_style_specifications(map_style)
        return rtn_style 
        
    @staticmethod
    def extract_valid_print_dimension_value(print_dimension: str) -> PrintFormat:
        logging.info("extract print dimension")
        try: 
            print_format = PrintFormat[print_dimension]
        except Exception as e:
            logging.error("print_dimension couldn't be converted to correct PrintFormat:" + print_dimension)
            raise e

        return print_format

    @staticmethod
    def extract_valid_pins_value(pins: List[Pin]) -> List[Pin]:
        #TO DO
        #   - Validate each pin value 
        #       - Ensure that all coordinate pairs are inside the bbox
        #   - attach a hex color to each map style 
        #   - attach location of each pin file path
        # file path, color, coordinate points (lon, lat) 
        
        logging.info("Validating pin(s)")

        return pins

    @staticmethod
    def extract_valid_zoom_value(zoom: int) -> int:
        if(zoom > 15 or zoom < 8):
            logging.error("zoom is outside range [ ] : " + str(zoom))
            raise ValueError("zoom is outside range : ")
        
        return zoom 
        

    # @staticmethod
    # def validate_input_values(input_payload) -> bool:
    #     logging.info("Validating input payload values...")
    #     is_valid_input = True

    #     logging.info("Validating bbox value")
    #     if(not ValueValidator.is_valid_bbox_value(input_payload['bbox'])):
    #         is_valid_input = False
    #         logging.debug("bbox values aren't valid: {}".format(input_payload['bbox']))

    #     if(not ValueValidator.is_valid_map_style_value(input_payload['map_style'])):
    #         is_valid_input = False
    #         logging.debug("map style values aren't valid: {}".format(input_payload['map_style']))

    #     if(not ValueValidator.is_valid_print_dimension_value(input_payload['print_dimension'])):
    #         is_valid_input = False
    #         logging.debug("map dimesnion value isn't valid: {}".format(input_payload['print_dimension']))
        
    #     if(not ValueValidator.is_valid_pins_value(input_payload['pins'])):
    #         is_valid_input = False
    #         logging.debug("map pins values aren't valid")
            
    #     return is_valid_input

    