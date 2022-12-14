from cgi import print_form
from cmath import e
import enum
import logging
from tkinter import font
from typing import List
from xml.etree.ElementTree import PI
import PIL.Image
from PIL import ImageOps, ImageDraw, ImageFont
import math
import decimal
from pyparsing import Regex
from models.pin import Pin
import engine.engine_utils
from os import listdir
from os.path import isfile, join
from models.bbox import Bbox
from models.coord import Coord
import mercantile
import numpy as np
from regex import search
from models.border_style import Border
import numpy as np


class Assembler:
    @staticmethod
    def assemble_image(folder_path, tile_grid, output_img_name):
        # Given a folder path, concatenate the map image from these tile images.
        # tile_grid [x, y] Number of tiles in grid
        logging.info("assembling images from " + folder_path)
        logging.info("size of image " + str(tile_grid))
        # Make a list of the image names
        image_files = [folder_path + f for f in listdir(folder_path)]
        # Open the image set using pillow
        images = [PIL.Image.open(x) for x in image_files]

        # Calculate the number of image tiles in each direction
        edge_length_x = tile_grid[0]
        edge_length_y = tile_grid[1]

        # Find the final composed image dimensions
        width, height = images[0].size
        total_width = width * edge_length_x
        total_height = height * edge_length_y

        # Create a new blank image we will fill in
        composite = PIL.Image.new("RGB", (total_width, total_height))

        # Loop over the x and y ranges
        y_offset = 0
        for i in range(0, edge_length_x):
            x_offset = 0
            for j in range(0, edge_length_y):
                # Open up the image file and paste it into the composed
                # image at the given offset position
                tmp_img = PIL.Image.open(folder_path + str(i) + "." + str(j) + ".png")
                composite.paste(tmp_img, (y_offset, x_offset))
                x_offset += width  # Update the width
            y_offset += height  # Update the height

        # Save the final image
        composite.save("./" + output_img_name)
        logging.info("output image: " + output_img_name)

    @staticmethod
    def check_image_folder_exists(folder_path):
        # TO DO: Check the existance of folder and process error associated with this.
        print("TO DO: check image folder existance")

    @staticmethod
    def crop_image(map_box, img_path, output_path, zoom):
        logging.info(
            "cropping the image to the correct size. Input: "
            + img_path
            + "; Output: "
            + output_path
        )

        # Open Image
        img = PIL.Image.open(img_path)
        img_width, img_height = img.size

        # Create tile_box (it is larger than map box)
        tl_tile = mercantile.tile(
            float(map_box.top_left.lon), float(map_box.top_left.lat), zoom
        )
        br_tile = mercantile.tile(
            float(map_box.bottom_right.lon), float(map_box.bottom_right.lat), zoom
        )
        br_tile = mercantile.Tile(x=br_tile.x + 1, y=br_tile.y + 1, z=zoom)
        tl_coord = Coord(mercantile.ul(tl_tile).lng, mercantile.ul(tl_tile).lat)
        br_coord = Coord(mercantile.ul(br_tile).lng, mercantile.ul(br_tile).lat)
        tile_box = Bbox(tl_coord, br_coord)

        # Get difference between tile_box and map_box
        diff_left_degree = abs(tile_box.top_left.lon - map_box.top_left.lon)
        diff_top_degree = abs(tile_box.top_left.lat - map_box.top_left.lat)
        diff_right_degree = abs(tile_box.bottom_right.lon - map_box.bottom_right.lon)
        diff_bottom_degree = abs(tile_box.bottom_right.lat - map_box.bottom_right.lat)

        # Calculate percent change of diff and convert to pixels
        total_x_degree = abs(tile_box.top_left.lon - tile_box.bottom_right.lon)
        total_y_degree = abs(tile_box.top_left.lat - tile_box.bottom_right.lat)

        # Calculate pixel change
        pixel_diff_left = round((diff_left_degree / total_x_degree) * img.width)
        pixel_diff_right = round((diff_right_degree / total_x_degree) * img.width)
        pixel_diff_top = round((diff_top_degree / total_y_degree) * img.height)
        pixel_diff_bottom = round((diff_bottom_degree / total_y_degree) * img.height)

        # Crop Image. Save as output_path
        crop_payload = (
            0 + pixel_diff_left,
            0 + pixel_diff_top,
            img.width - pixel_diff_right,
            img.height - pixel_diff_bottom,
        )
        im1 = img.crop(crop_payload)

        logging.info("Save cropped image to " + output_path)
        im1.save(output_path)

    @staticmethod
    def add_pin(context, input_path: str, output_path: str, pin: Pin) -> None:
        # Input map path and pin DTO
        # Save map to output location with pin on map
        logging.info(context)
        # Open image
        map_img = PIL.Image.open(input_path)

        # Make sure map is expected size
        map_dim = engine.engine_utils.get_print_pixel_size(context["map_dimension"])
        map_img = map_img.resize(map_dim)

        logging.info("current map size: " + str(map_dim))

        # Open Pin image Pin utils
        pin_img = PIL.Image.open(engine.engine_utils.get_pin_image_path(pin))

        # Calculate location of pin on the map based on size of map image (pixels)
        (
            print_pin_location_x,
            print_pin_location_y,
        ) = engine.engine_utils.get_pin_location(
            map_box=context["bbox"], pin=pin, print_format=context["map_dimension"]
        )

        logging.info("pin location on print x: " + str(print_pin_location_x))
        logging.info("pin location on print y: " + str(print_pin_location_y))

        # Resize pin image
        new_pin_dim = engine.engine_utils.get_pin_size(context["map_dimension"], pin)
        logging.info("pin pixel size on map " + str(new_pin_dim))
        pin_img = pin_img.resize(new_pin_dim)

        # Place pin image on map
        map_img.paste(
            pin_img, (print_pin_location_x, print_pin_location_y), mask=pin_img
        )
        map_img.save("withPin.png")
        # Save map with pin saved as " + output_path)
        map_img.save(output_path)

    @staticmethod
    def add_pins_to_map(context, input_path: str, output_path: str) -> None:
        for p in context["pins"]:
            curr_pin = Pin(
                icon=p["icon"],
                location=p["location"],
                digital_height=p["digital_height"],
                digital_width=p["digital_width"],
                color=p["color"],
            )
            logging.info("adding pin: " + str(curr_pin))
            Assembler.add_pin(
                context, input_path=input_path, output_path=output_path, pin=curr_pin
            )

    @staticmethod
    def isHexColor(color: str) -> bool:
        return search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color)

    @staticmethod
    def add_border(map_style: dict, input_path: str, output_path: str):
        # If Input path and output path are the same the image will be overwritten
        # border width dimensions in pixels
        # fill is color value defined
        borders = map_style["borders"]
        if len(borders) == 0:
            logging.info("no borders to add to map")
            return

        img = PIL.Image.open(input_path).convert("RGBA")

        for border in borders:
            # if isinstance(border.width, int) and Assembler.isHexColor(border.color):
            img = ImageOps.expand(img, border=border["width"], fill=border["color"])
            # else:
            # print("hex code doesn't exist" +  str(border.width) + str(border.color))

        img.save(output_path)

    @staticmethod
    def add_transparency(img_path: str, img_output_path: str):
        # Transform picture to RGBA
        # calculate range of pixels to loop through and change transparency
        # calculatre the step of each pixel change
        # TO DO: Change .75 and .95 to inputs for fading.
        img = PIL.Image.open(img_path).convert("RGBA")

        arr = np.array(img)
        alpha = arr[:, :, 3]
        n = len(alpha)
        alpha[:] = np.interp(
            np.arange(n), [0, 0.75 * n, 0.95 * n, n], [255, 255, 0, 0]
        )[:, np.newaxis]
        img = PIL.Image.fromarray(arr, mode="RGBA")
        img.save(img_output_path)

    @staticmethod
    def add_text(img_path: str, out_path: str, msg: list):
        # TO DO: change this function to take in multiple messages and error check
        # better payload
        # Constants for positioning based off of how many messages in list.
        # Size of Font based on the number of characters in the message

        img = PIL.Image.open(img_path)

        width, height = img.size
        img = PIL.Image.open(img_path).convert("RGBA")
        draw = PIL.ImageDraw.Draw(img)
        myFont = ImageFont.truetype("src/fonts/texgyreadventor-regular.otf", 1100)
        # draw.textsize(msg, font=myFont)

        # Center the text
        w, h = draw.textsize(msg[0], font=myFont)
        draw.text(
            ((width - w) / 2, (height - h) * 0.94), msg[0], fill="black", font=myFont
        )

        myFont = ImageFont.truetype("src/fonts/texgyreadventor-regular.otf", 150)
        # Center the text
        w, h = draw.textsize(msg[1], font=myFont)
        draw.text(
            ((width - w) / 2, (height - h) * 0.97), msg[1], fill="black", font=myFont
        )

        img.save(out_path)
