# Tile Engine donwload, assemble, and print tiles into a large image file

# Input: 
# - BBox (EPSG:4326 projected coordinates) [float] size 4
# - Height (inches) of final picture
# - Width (inches) of final picture 
# - Size of tiles we want to download (256, 512, 1024) 

# Output: 
# - Tiff Image of map at high resolution > 300 dpi
from doctest import OutputChecker
from multiprocessing.dummy import Array
from optparse import Option
import sys

from pyparsing import Or
from models.value_validator import ValueValidator
import settings
import engine.engine_code as engine_code
from cgi import print_form
from stringprep import map_table_b2
from turtle import st
from typing import List
from models.coord import Coord
from engine.downloader import Downloader
from engine.assembler import Assembler
from models.bbox import Bbox
import numpy as np

import PIL.Image

from engine.validator import validate_payload

from models.icon import Icon
from models.map import Map
from models.pin import Pin
from models.print_format import PrintFormat
from models.border_style import Border

import logging 
from json import load
from schema import Schema, And, Use, Optional, SchemaError



def run_tile_engine(context) -> int:

    #Run Downloader
    logging.info("Running Downloader...")
    try: 
        new_grid = Downloader.generate_tile_lists(context)
    except Exception as e:
        logging.error("Downloader returned an error")
        logging.critical(e, exc_info=True)
        return engine_code.DOWNLOADER_FAILURE
    
    #Run Assembler (Border, style, wording, etc.) 
    logging.info("Running Assembler...")
    try:
        # Assemble map from downlaoded images
        logging.info("Assemble images")
        Assembler.assemble_image(folder_path=settings.TEMP_TILE_IMAGE_FOLDER, tile_grid=new_grid, output_img_name=settings.IMAGE_FILE_NAME)
        
        # Add pins to map
        logging.info("Add pins to map " + settings.IMAGE_FILE_NAME)
        if(context['pins'] != None):
            logging.info("Adding " + str(len(context['pins'])) + " pins to map image")
            Assembler.add_pins_to_map(context, input_path=settings.IMAGE_FILE_NAME, output_path=settings.IMAGE_FILE_NAME)
        else:
            logging.info("No pins to place on the image")
        
        # Add map style 
        logging.info("adding style to the map " + str(context['map_style']))
        if(context['map_style']['transparency'] is True):
            logging.info("Applying transparency effect to map")
            Assembler.add_transparency(img_path=settings.IMAGE_FILE_NAME, img_output_path=settings.IMAGE_FILE_NAME)
        else:
            logging.info("No transparency applied to map")

        logging.info("Adding text to the image")
        if('text' in context['map_style']):
            logging.info("Adding text " + str(context['map_style']['text']))
            Assembler.add_text(img_path=settings.IMAGE_FILE_NAME, out_path=settings.IMAGE_FILE_NAME, msg = context['map_style']['text'])
        else:
            logging.info("No text added to the image")

        # Add map border 
        logging.info("adding border to map")
        Assembler.add_border(map_style=context['map_style'], input_path=settings.IMAGE_FILE_NAME, output_path=settings.IMAGE_FILE_NAME)

    except Exception as e:
        logging.error("Assembler returned an error")
        logging.critical(e, exc_info=True)
        return engine_code.ASSEMBLER_FAILURE


    return engine_code.ENGINE_SUCCESS


def main(args) -> int: 
    #Return engine tile code. 
    #Set up logger
    logging.basicConfig(filename=settings.LOG_FILENAME, level=logging.INFO)
    
    #Validate payload
    logging.info("Validating payload...")
    context = validate_payload(args)

    #Run tile engine 
    logging.info("Running tile engine...")
    logging.info("tile-engine context: " + str(context))
    return run_tile_engine(context)

if __name__ == "__main__":
    """
    input: .json file for input_job_payload. TO DO: Specifications for input job payload
    output:
        success: 
            engine_status_code
            output_file_path location of final image 
        failure: 
            error_message
            engine_status_code
            logs_location

    """
    try: 
        code = main(sys.argv)
        logging.info("finished with Engine result code " + str(code))
    except Exception as e: 
        # Maybe this will always run? 
        logging.critical(e, exc_info=True)
        sys.exit(engine_code.ENGINE_FAILURE_CRITICAL)

    # Assembler.add_transparency("final_image.png")
    # print('starting border...')
    
    # Assembler.add_pins_to_map   

    # Assembler.add_text(img_path='out.png',out_path='out_text.png', msg=["MADHATTER", '- Washington DC -'])


    # context={}
    # context['api'] = "https://api.maptiler.com/maps/voyager/{z}/{x}/{y}@2x.png?key=PmIF6Ez34ROeDo7jJGuD#"
    # context['borders'] = [
    #     {'width':15, 'color':'#000000'},
    #     {'width':30, 'color':'#43ff6400'},
    #     {'width':30, 'color':'#000000'},
    #     {'width':100, 'color':'#43ff6400'}
    # ]
    # Assembler.add_border(map_style=context, input_path='out_text.png', output_path='out_border.png')





    # 1. Use BBox & size of tiles to get the List of tiles we want to download 
    # 2. Multi threaded download of tiles
    # 3. Assemble tiles on download completion
    # 4. Output tiff / Download tiff to device / store tiff somewhere? 
    
    # bbox = [-77.09690093994142,38.86042928143244,-76.97673797607423,38.95393580081098]


    ### USE THIS BBOX. 
    # tile_size = 0
    # # 1024 tiles. 
    # base_url = 'https://api.maptiler.com/maps/voyager/{z}/{x}/{y}@2x.png?key=msqCXSKnPannMXvUCPsn#' 

    # zoom = 15

    # bbox = [-77.07801818847658,38.859092581794336,-76.99562072753908,38.95527071579662]

    # ### USE THIS BBOX. 
    # map_box = Bbox(Coord(bbox[0], bbox[3]), Coord(bbox[2], bbox[1]))

    # new_grid = Downloader.generate_tile_lists(map_box, tile_size, base_url, zoom) 
    # print('new_grid')
    # print(new_grid)
    # Assembler.assemble_image('./src/tile_images/', new_grid, 'downloaded_image')

    # Assembler.crop_image(map_box, './downloaded_image.png', output_path="./cropped_image.png", zoom=zoom)


    # pin_1 = Pin(icon = Icon.HEART, location=Coord(-77.0369, 38.9072), digital_width=100, digital_height=100, color="hexCode")

    # map = Map(
    #     map_box=map_box, 
    #     tile_url=base_url, 
    #     print_format=PrintFormat.Canvas_24_36, 
    #     pins = pin_1,
    #     border_style=None,
    #     file_path="./cropped_image.png"
    #     )
    # Assembler.add_pin(map,'./w_the_pin.png', pin=pin_1)



    # # Test out border feature
    # Assembler.add_border(in_img,
    #         output_image='butterfly_border_indianred.jpg',
    #         border=100,
    #         color='indianred')


    # input_img = "w_the_pin.png"
    # output_img = "w_border_pin.png"

    # b1 = Border( width=100, color="#FF0000")
    # b21 = Border( width=1000, color="#0000FF")
    # b2 = Border( width=1000, color="#43ff6400")
    # b3 = Border( width=2000, color="#FF0000")
    # borders = [b1, b2, b3]
    # Assembler.add_border(input_path=input_img, output_path=output_img, borders=borders)