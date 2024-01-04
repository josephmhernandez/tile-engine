import uuid

# Engine Properties
IMAGE_FILE_NAME = "all_skate_image.png"
TEMP_TILE_IMAGE_FOLDER = "./temp/tile_images/" + str(uuid.uuid4()) + "/"


# Tile properties
TILE_URL = ""
TILE_API_KEY = ""

# Dynamo DB


# Logging
LOG_FILENAME = "logs.log"


# xxxxxx for unit testing -> delete folder after each unit test
# temp_output is used to store output at each engine step if flag is set.

# Create random folder name for each run of the engine.
# This is to avoid conflicts when running multiple engines at the same time.
TEMP = "temp/"
TEMP_OUTPUT = TEMP + 'temp_output/'
TEMP_TILE_IMAGE = TEMP + 'tile_images/'
TEMP_OUTPUT_FOLDER = TEMP + 'temp_output/' + str(uuid.uuid4()) + "/"

TEMP_TEXT_OUTPUT_FOLDER = TEMP_OUTPUT_FOLDER + "temp_text/"
TEMP_PIN_OUTPUT_FOLDER = TEMP_OUTPUT_FOLDER + "temp_pin/"

TEMP_RESIZED_OUTPUT = TEMP_OUTPUT_FOLDER + "main-resized.png"

# Controls the Editing of the Map / Poster. Need the map resized before we add
#   text / borders / effects so these things are not distored.
DPI = 300
