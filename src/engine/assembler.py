from cgi import print_form
from cmath import e
import enum
import logging
from tkinter import font
from typing import List
from xml.etree.ElementTree import PI
from PIL import ImageOps, ImageDraw, ImageFont, Image
import math
import decimal
from pyparsing import Regex
from src.models.pin import Pin
import src.engine.engine_utils
from os import listdir
from os.path import isfile, join
from src.models.bbox import Bbox
from src.models.coord import Coord
import mercantile
import numpy as np
from regex import search
from src.models.border_style import Border
import numpy as np
from src.style_constants import map_style, map_font_path, map_pin_path
import settings


class Assembler:
    @staticmethod
    def assemble_image(folder_path, tile_grid, output_img_name, verbose=False):
        # Given a folder path, concatenate the map image from these tile images.
        # tile_grid [x, y] Number of tiles in grid
        logging.info("assembling images from " + folder_path)
        logging.info("size of image " + str(tile_grid))
        # Make a list of the image names
        image_files = [folder_path + f for f in listdir(folder_path)]
        # Open the image set using pillow
        images = [Image.open(x) for x in image_files]

        # Calculate the number of image tiles in each direction
        edge_length_x = tile_grid[0]
        edge_length_y = tile_grid[1]

        # Find the final composed image dimensions
        width, height = images[0].size
        total_width = width * edge_length_x
        total_height = height * edge_length_y

        # Create a new blank image we will fill in
        composite = Image.new("RGB", (total_width, total_height))

        # Loop over the x and y ranges
        y_offset = 0
        for i in range(0, edge_length_x):
            x_offset = 0
            for j in range(0, edge_length_y):
                # Open up the image file and paste it into the composed
                # image at the given offset position
                tmp_img = Image.open(folder_path + str(i) + "." + str(j) + ".png")
                composite.paste(tmp_img, (y_offset, x_offset))
                x_offset += width  # Update the width
            y_offset += height  # Update the height

        # Save the final image
        composite.save("./" + output_img_name)
        if verbose:
            logging.info(f"saving assembled image to {settings.TEMP_OUTPUT_FOLDER}")
            composite.save(settings.TEMP_OUTPUT_FOLDER + "assemble-tiles.png")
        logging.info("output image: " + output_img_name)

    @staticmethod
    def check_image_folder_exists(folder_path):
        # TO DO: Check the existance of folder and process error associated with this.
        print("TO DO: check image folder existance")

    @staticmethod
    def crop_image(map_box, img_path, output_path, zoom, verbose=False):
        logging.info(
            "cropping the image to the correct size. Input: "
            + img_path
            + "; Output: "
            + output_path
        )

        # Open Image
        img = Image.open(img_path)
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
        if verbose:
            logging.info(f"saving cropped image to {settings.TEMP_OUTPUT_FOLDER}")
            im1.save(settings.TEMP_OUTPUT_FOLDER + "crop-to-bbox.png")
        im1.save(output_path)

    @staticmethod
    def add_pin(
        context,
        input_path: str,
        output_path: str,
        pin: Pin,
        verbose: bool = False,
        id: int = 69,
    ) -> None:
        # Input map path and pin DTO
        # Save map to output location with pin on map
        logging.info(f"map context: {context}")
        # Open image
        map_img = Image.open(input_path)

        # Make sure map is expected size
        # map_dim = src.engine.engine_utils.get_print_pixel_size(context["map_dimension"])
        # map_img = map_img.resize(map_dim)
        map_dim = map_img.size
        logging.info("current map size: " + str(map_dim))

        # Open Pin image Pin utils
        pin_img = Image.open(map_pin_path[pin.icon])
        # pin_img = Image.open(src.engine.engine_utils.get_pin_image_path(pin))

        # Calculate location of pin on the map based on size of map image (pixels)
        (
            print_pin_location_x,
            print_pin_location_y,
        ) = src.engine.engine_utils.get_pin_location(
            context, pin, map_dim_pixel=map_dim
        )
        # trying to delete this
        #     map_box=context["bbox"],
        #     pin=pin,
        #     map_dim_pixel=map_dim,
        #     print_format=context["size"],
        # )

        logging.info("pin location on print x: " + str(print_pin_location_x))
        logging.info("pin location on print y: " + str(print_pin_location_y))

        # Resize pin image
        # hererjekrje;l
        new_pin_dim = src.engine.engine_utils.get_pin_size(context, pin, map_dim)
        logging.info("pin pixel size on map " + str(new_pin_dim))
        pin_img = pin_img.resize(new_pin_dim)

        # Place pin image on map
        map_img.paste(
            pin_img, (print_pin_location_x, print_pin_location_y), mask=pin_img
        )
        if verbose:
            logging.info(f"saving map with pin to {settings.TEMP_PIN_OUTPUT_FOLDER}")
            map_img.save(
                settings.TEMP_PIN_OUTPUT_FOLDER + "add-pin-" + str(id) + ".png"
            )

        # Save map with pin saved as " + output_path)
        map_img.save(output_path)

    @staticmethod
    def add_pins_to_map(
        context, input_path: str, output_path: str, verbose: bool = False
    ) -> None:
        id = 0
        for p in context["pins"]:
            print("pin")
            print(p)
            curr_pin = Pin(
                icon=p["style"],
                location=[p["position"]["lng"], p["position"]["lat"]],
                digital_height=p["size"],
                digital_width=p["size"],
                color=p["color"] if "color" in p else "#000000",
            )
            logging.info("adding pin: " + str(curr_pin))
            Assembler.add_pin(
                context,
                input_path=input_path,
                output_path=output_path,
                pin=curr_pin,
                verbose=verbose,
                id=id,
            )
            id += 1

    @staticmethod
    def isHexColor(color: str) -> bool:
        return search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color)

    @staticmethod
    def add_border(
        map_style: dict, input_path: str, output_path: str, verbose: bool = False
    ):
        # If Input path and output path are the same the image will be overwritten
        # border width dimensions in pixels
        # fill is color value defined
        borders = map_style["borders"]
        if len(borders) == 0:
            logging.info("no borders to add to map")
            return

        img = Image.open(input_path).convert("RGBA")

        for border in borders:
            # if isinstance(border.width, int) and Assembler.isHexColor(border.color):
            img = ImageOps.expand(img, border=border["width"], fill=border["color"])
            # else:
            # print("hex code doesn't exist" +  str(border.width) + str(border.color))

        if verbose:
            logging.info(f"saving map with border to {settings.TEMP_OUTPUT_FOLDER}")
            img.save(settings.TEMP_OUTPUT_FOLDER + "add-border.png")
        img.save(output_path)

    @staticmethod
    def add_transparency(img_path: str, img_output_path: str, verbose: bool = False):
        # Transform picture to RGBA
        # calculate range of pixels to loop through and change transparency
        # calculatre the step of each pixel change
        # TO DO: Change .75 and .95 to inputs for fading.
        img = Image.open(img_path).convert("RGBA")

        arr = np.array(img)
        alpha = arr[:, :, 3]
        n = len(alpha)
        alpha[:] = np.interp(
            np.arange(n), [0, 0.75 * n, 0.95 * n, n], [255, 255, 0, 0]
        )[:, np.newaxis]
        img = Image.fromarray(arr, mode="RGBA")
        if verbose:
            logging.info(
                f"saving map with transparency to {settings.TEMP_PIN_OUTPUT_FOLDER}"
            )
            img.save(settings.TEMP_OUTPUT_FOLDER + "add-transparency.png")
        img.save(img_output_path)

    @staticmethod
    def create_image(size, bgColor, message, font, fontColor):
        """
        Creates an image block with the given message
        """
        W, H = size
        image = Image.new("RGB", size, bgColor)
        draw = ImageDraw.Draw(image)
        _, _, w, h = draw.textbbox((0, 0), message, font=font)
        draw.text(((W - w) / 2, (H - h) / 2), message, font=font, fill=fontColor)
        return image

    @staticmethod
    def concatenate_images_v(img1, img2, img3=None):
        """
        Concatenates two images vertically
        """
        dst = Image.new("RGB", (max(img1.width, img2.width), img1.height + img2.height))
        dst.paste(img1, (0, 0))
        dst.paste(img2, (0, img1.height))

        if img3:
            logging.debug("concatenating 3 images")
            rtnImg = Image.new(
                "RGB", (max(dst.width, img3.width), dst.height + img3.height)
            )
            rtnImg.paste(dst, (0, 0))
            rtnImg.paste(img3, (0, dst.height))
            return rtnImg
        else:
            logging.debug("concatenating 2 images")
            return dst

    @staticmethod
    def add_text(
        img_path: str,
        out_path: str,
        text: dict,
        frame_size: str,
        style: str,
        verbose: bool = False,
    ):
        # TO DO: change this function to take in multiple messages and error check
        # Constants for positioning based off of how many messages in dict.
        # img_path: path to image to add text to
        # out_path: path to save image with text
        # frame_size: _24_36
        """
        img_path: "path/to/image.png"
        out_path: "path/to/output.png"
        frame_size: _24_36
        text = {
            "primary": "LargeText",
            "secondary": "MediumText",
            "coordinate": "DelimitedDegreeMinutesSecondsWDirection",
        }
        style: "basic"
        """

        # Total size of image block
        map_img = Image.open(img_path)
        map_width, map_height = map_img.size

        # Not sure if we switch map width the beginning etc
        width = map_width
        logging.debug(f"text block width will be: {width}")

        # Generate the primary, secondary, coordinate text blocks
        primary_img = None
        secondary_img = None
        coordinate_img = None

        style_dict = map_style[style]
        text_size_dict = style_dict[frame_size]
        if text["primary"] and text["primary"] != "":
            logging.debug(f'primary text found: {text["primary"]}')
            primary_font = ImageFont.truetype(
                map_font_path[style_dict["primary_font"]],
                text_size_dict["primary_font_size"],
            )
            primary_img = Assembler.create_image(
                (width, text_size_dict["primary_text_block"]),
                "white",
                text["primary"],
                primary_font,
                "black",
            )
            if verbose:
                logging.info(
                    f"saving primary text block to {settings.TEMP_TEXT_OUTPUT_FOLDER}"
                )
                primary_img.save(settings.TEMP_TEXT_OUTPUT_FOLDER + "primary-text.png")

        if text["secondary"] and text["secondary"] != "":
            logging.debug(f'secondary text found: {text["secondary"]}')
            secondary_font = ImageFont.truetype(
                map_font_path[style_dict["secondary_font"]],
                text_size_dict["secondary_font_size"],
            )
            secondary_img = Assembler.create_image(
                (width, text_size_dict["secondary_text_block"]),
                "white",
                text["secondary"],
                secondary_font,
                "black",
            )
            if verbose:
                logging.info(
                    f"saving secondary text block to {settings.TEMP_TEXT_OUTPUT_FOLDER}"
                )
                secondary_img.save(
                    settings.TEMP_TEXT_OUTPUT_FOLDER + "secondary-text.png"
                )

        if text["coordinate"] and text["coordinate"] != "":
            logging.debug(f'coordinate text found: {text["coordinate"]}')
            coordinate_font = ImageFont.truetype(
                map_font_path[style_dict["coordinate_font"]],
                text_size_dict["coordinate_font_size"],
            )
            coordinate_img = Assembler.create_image(
                (width, text_size_dict["coordinate_text_block"]),
                "white",
                text["coordinate"],
                coordinate_font,
                "black",
            )
            if verbose:
                logging.info(
                    f"saving coordinate text block to {settings.TEMP_TEXT_OUTPUT_FOLDER}"
                )
                coordinate_img.save(
                    settings.TEMP_TEXT_OUTPUT_FOLDER + "coordinate-text.png"
                )

        if primary_img is None and secondary_img is None and coordinate_img is None:
            logging.debug(
                "all text blocks are None, no text to add. Something might be wrong."
            )
            return

        final_img = None
        if primary_img is None:
            if secondary_img is None:
                final_img = coordinate_img
            else:
                if coordinate_img is None:
                    final_img = secondary_img
                else:
                    # Append secondary and coordinate
                    final_img = Assembler.concatenate_images_v(
                        secondary_img, coordinate_img
                    )
        else:
            if secondary_img is None:
                if coordinate_img is None:
                    final_img = primary_img
                else:
                    # Append primary and coordinate
                    final_img = Assembler.concatenate_images_v(
                        primary_img, coordinate_img
                    )
            else:
                # Append primary and secondary
                final_img = Assembler.concatenate_images_v(primary_img, secondary_img)
                if coordinate_img:
                    # Append primary and secondary and coordinate
                    final_img = Assembler.concatenate_images_v(
                        final_img, coordinate_img
                    )

        if verbose:
            logging.info(
                f"saving final text block to {settings.TEMP_TEXT_OUTPUT_FOLDER}"
            )
            final_img.save(settings.TEMP_TEXT_OUTPUT_FOLDER + "all-text.png")

        # Add padding to text block image to match the style specifications: (block_inches * dpi)
        final_width, final_height = final_img.size
        padding_total = (
            int(text_size_dict["block_inches"] * text_size_dict["dpi"]) - final_height
        )

        # Add padding to the text block image north and south image.
        img_updown = ImageOps.expand(
            final_img,
            border=(0, int(padding_total / 2), 0, int(padding_total / 2)),
            fill="white",
        )
        logging.debug(f"padding total: {padding_total}, final height: {final_height}")

        # Add padding to south of image if there is left over space. (shouldnt be off by more than a pixel)
        if padding_total % 2 != 0:
            img_updown = ImageOps.expand(img_updown, border=(0, 0, 0, 1), fill="white")
        logging.debug(f"final text block size: {img_updown.size}")

        if verbose:
            logging.info(
                f"saving final text block with padding to {settings.TEMP_TEXT_OUTPUT_FOLDER}"
            )
            img_updown.save(settings.TEMP_TEXT_OUTPUT_FOLDER + "add-text-w-padding.png")

        img_updown.save(out_path)
