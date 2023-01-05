# We want all the map_style components to come as an input now from our UI.
# We don't want to have to store constants here so we dont have to update two places.
# Trying to delete this.
# map_style = {
#     "basic": {
#         "borders": [
#             {"width": 0, "color": "#FFFFFF"},
#         ],
#         "api": "https://api.maptiler.com/maps/voyager/{z}/{x}/{y}@2x.png?key=PmIF6Ez34ROeDo7jJGuD#",
#         "primary_font": "Semplicita-Modern-Medium",
#         "secondary_font": "Semplicita-Modern-Medium",
#         "coordinate_font": "Semplicita-Modern-Medium",
#         "text_color": "#000000",
#         "_24_36": {
#             "block_inches": 4.5,
#             "dpi": 300,
#             "primary_font_size": 450,
#             "primary_text_block": 675,
#             "secondary_font_size": 225,
#             "secondary_text_block": 337,  # off by .5 pixel
#             "coordinate_font_size": 150,
#             "coordinate_text_block": 225,
#         },
#     }
# }


# KEEP THIS BELOW
map_font_path = {
    "Semplicita": "src/fonts/Semplicita-Modern-Medium.otf",
}

map_pin_path = {
    "heart-black-white": "src/images/pins/heart-pin-square-black-white.png",
    "heart-white-black": "src/images/pins/heart-pin-square-white-black.png",
    "circle-white-black": "src/images/pins/circle-pin-square-white-black.png",
    "circle-black-white": "src/images/pins/circle-pin-square-black-white.png",
    "diamond-white-black": "src/images/pins/diamond-pin-square-white-black.png",
    "diamond-black-white": "src/images/pins/diamond-pin-square-black-white.png",
}

# 300 pixels per inch
MULTIPlIER = 300
