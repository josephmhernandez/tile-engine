# We want all the map_style components to come as an input now from our UI.
# We don't want to have to store constants here so we dont have to update two places.
# Trying to delete this.
map_style = {
    "basic": {
        "borders": [
            {"width": 0, "color": "#FFFFFF"},
        ],
        "api": "https://api.maptiler.com/maps/voyager/{z}/{x}/{y}@2x.png?key=PmIF6Ez34ROeDo7jJGuD#",
        "primary_font": "Semplicita-Modern-Medium",
        "secondary_font": "Semplicita-Modern-Medium",
        "coordinate_font": "Semplicita-Modern-Medium",
        "text_color": "#000000",
        "_24_36": {
            "block_inches": 4.5,
            "dpi": 300,
            "primary_font_size": 450,
            "primary_text_block": 675,
            "secondary_font_size": 225,
            "secondary_text_block": 337,  # off by .5 pixel
            "coordinate_font_size": 150,
            "coordinate_text_block": 225,
        },
    }
}


# KEEP THIS BELOW
map_font_path = {
    "Semplicita": "src/fonts/Semplicita-Modern-Medium.otf",
}

# High resolution pins: 3800px x 3800px
map_pin_path = {
    "heart-black-white": "src/images/pins/pin-heart-black-white.png",
    "heart-white-black": "src/images/pins/pin-heart-white-black.png",
    "circle-white-black": "src/images/pins/pin-circle-white-black.png",
    "circle-black-white": "src/images/pins/pin-circle-black-white.png",
    "diamond-white-black": "src/images/pins/pin-diamond-white-black.png",
    "diamond-black-white": "src/images/pins/pin-diamond-black-white.png",
    "beach-black-white": "src/images/pins/pin-beach-black-white.png",
    "beach-white-black": "src/images/pins/pin-beach-white-black.png",
    "mountain-black-white": "src/images/pins/pin-mountain-black-white.png",
    "mountain-white-black": "src/images/pins/pin-mountain-white-black.png",
}

# 300 pixels per inch
MULTIPlIER = 300
