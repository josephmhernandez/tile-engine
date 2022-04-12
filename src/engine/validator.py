
import logging 
from json import load
from schema import Schema, And, Use, Optional, SchemaError

from models.value_validator import ValueValidator
from models.icon import Icon
from models.map import Map
from models.pin import Pin
from models.print_format import PrintFormat
from models.border_style import Border


def validate_schema(input_payload_dict: dict):
    err_list = []
    payload_schema = Schema({
        'bbox': And(Use(list)),
        'map_style': And(Use(str)),
        'print_dimension': And(Use(str)),
        'zoom': And(Use(int)),
        Optional('pins'): And(Use(list))
    })

    logging.info("validating schema...")
    try:
        if(not payload_schema.validate(input_payload_dict)):
            logging.info("Dictionary input doesn't match expected schema")
            err_list.append("Cannot validate dictionary schema")
    except Exception as e:
        logging.debug("Error thrown while validating input payload schema.")
        logging.error(e, exc_info=True)
        err_list.append(str(e))

    return err_list


def validate_payload(args) -> str:
    # return context obejct for tile-engine
    context = {}
    logging.info("length of args " + str(len(args)))

    if(len(args) != 2):
        logging.error("incorrect number of args. Pass input json file name as arg")
        raise AttributeError("Incorrect number of args")
    
    #Pre Validate input payload
    with open(args[1], 'r') as f:
        logging.info("reading json file: " + str(f))
        input_payload = load(f)
    
        if(input_payload == None):
            logging.debug("Input Args are None")
            raise AttributeError("Input Args are None")

        logging.info("Prevalidate payload schema...")
        validation_error_list = validate_schema(input_payload_dict=input_payload)

        if(len(validation_error_list) > 0):
            logging.debug("Error list not empty")
            logging.error("Error(s) validating payload: " + len(validation_error_list) + " errors")
            raise SchemaError(validation_error_list.to_string())

    # TO DO: 
    #   - Validate BBox values 
    #   - Validate map_style as one of the pre-specified styles
    #   - Validate print_dimension as one of the pre-specified print dimensions
    #   - Validate pins 

    #Validate values of json attributes
    try:
        context['bbox'] = ValueValidator.extract_valid_bbox_value(input_payload['bbox'])
        context['map_style'] = ValueValidator.extract_valid_map_style_value(input_payload['map_style'])
        context['map_dimension'] = ValueValidator.extract_valid_print_dimension_value(input_payload['print_dimension'])
        context['zoom'] = ValueValidator.extract_valid_zoom_value(input_payload['zoom'])
        # Optional Elements
        if('pins' in input_payload):
            context['pins'] = ValueValidator.extract_valid_pins_value(input_payload['pins'])
        else: 
            context['pins'] = None
    except Exception as e:
        logging.error("This is an error that wasn't caught in the ValueValidator...")
        logging.error(e, exc_info=True)
        raise ValueError("This is an error that wasn't caught in the ValueValidator...")

        
    return context
