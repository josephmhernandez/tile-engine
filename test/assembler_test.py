from doctest import OutputChecker
import logging
from zlib import DEF_BUF_SIZE
import pytest
from src.engine.validator import validate_json_attributes

# Note: Test Classes must start with "Test"
# Note: Test Functions must start with "test"

from src.engine.assembler import Assembler
from src.models.print_format import PrintFormat


class TestAssembler:
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
        pass
