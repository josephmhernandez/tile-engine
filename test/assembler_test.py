import logging
import pytest
from PIL import Image
import os
import glob
from src.style_constants import map_style_text
from src.engine.assembler import Assembler
from src.models.print_format import PrintFormat
from src.engine.validator import validate_json_attributes

# Note: Test Classes must start with "Test"
# Note: Test Functions must start with "test"


class TestAssembler:
    @pytest.fixture()
    def setup_takedown(self):
        # Setup
        print("yo")
        yield
        # Tear Down

        # Remove all files from test_tile_images folder
        # TO DO: Remove all files from test/test_tile_images folder

        # Remove all files from /temp_output folder
        print("temp_output delete")
        files = glob.glob("/temp_output/*.png")
        for f in files:
            os.remove(f)
        pass

    def test_simple(self):
        print("running test_simple")
        assert 2 + 2 != 1

    def test_pin_in_correct_place(self):
        logging.info("Running test_pin_in_correct_place")
        # Image name where tiles have been assembled and has been cropped to the correct size
        assembled_cropped_image = "test/assembler_unit_test_attachments/cropped_dc.png"
        output_file = "test_pin_in_correct_place.png"
        # Define parameters
        context = {
            "bbox": [
                -77.07801818847658,
                38.95527071579662,
                -76.99562072753908,
                38.859092581794336,
            ],
            "map_style": "debug_default_map",
            "print_dimension": "Canvas_24_36",
            "zoom": 15,
            "pins": [
                {
                    "icon": "heart",
                    "location": [-77.043443, 38.909629],
                    "digital_width": 50,
                    "digital_height": 50,
                    "color": "#000000",
                }
            ],
        }

        context = validate_json_attributes(context)

        Assembler.add_pins_to_map(
            context=context,
            input_path=assembled_cropped_image,
            output_path="test/assembler_unit_test_attachments/" + output_file,
        )

        # new grid size 8, 12

        logging.info("finished test_pin_in_correct_place; Output file:" + output_file)
        assert True

    def test_add_text_all_blocks(self):
        logging.info("running test add_text")
        assembled_cropped_image = "test/assembler_unit_test_attachments/cropped_dc.png"
        map_img = Image.open(assembled_cropped_image)
        logging.info(f"size of the image: {map_img.size}")

        img_path = assembled_cropped_image
        out_path = "temp_output/"
        text = {
            "primary": "Washington, DC",
            "secondary": "United States",
            "coordinate": "38.9072° N, 77.0369° W",
        }
        frame_size = "_24_36"
        style = "basic"
        Assembler.add_text(
            img_path=img_path,
            out_path=out_path,
            text=text,
            frame_size=frame_size,
            style=style,
        )

        prim_img = Image.open("temp_output/primary-text.png")
        sec_img = Image.open("temp_output/secondary-text.png")
        coord_img = Image.open("temp_output/coordinate-text.png")
        final_img = Image.open("temp_output/all-text.png")
        all_text_w_padding = Image.open("temp_output/all-text-updown.png")

        logging.info(f"size of the primary image: {prim_img.size}")
        logging.info(f"size of the secondary image: {sec_img.size}")
        logging.info(f"size of the coordinate image: {coord_img.size}")
        logging.info(f"size of the final image: {final_img.size}")
        logging.info(f"size of the final image w padding: {all_text_w_padding.size}")

        # Assert that each image generated is the correct size
        assert (
            map_style_text[style][frame_size]["primary_text_block"] == prim_img.size[1]
        )
        assert (
            map_style_text[style][frame_size]["secondary_text_block"] == sec_img.size[1]
        )
        assert (
            map_style_text[style][frame_size]["coordinate_text_block"]
            == coord_img.size[1]
        )

        assert (
            map_style_text[style][frame_size]["block_inches"]
            * map_style_text[style][frame_size]["dpi"]
            == all_text_w_padding.size[1]
        )

        # Clean up temp_output folder
        pass
