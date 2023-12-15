# File for background image constants. This is where we will store the url's of the background images. They'll be on local disk for now. Leaving space for a "api" url in the future when we switch up the arhitecture and run remotely.
# BG_FOLDER_PATH is the path your bg images are stored.
BG_FOLDER_PATH = {
    "local": "/Users/joseph/Documents/workspace/bg_images",
}

# BG_IMG_URL_MAP is a dictionary with Image Codes as keys and a dictionary and locatio of the images as values of the size selected.
# usa: Image Code
# 2_3: Size Code
# local: Local path to the image
# api: Remote path to the image (future s3 bucket)
BG_IMG_URL_MAP = {
    "usa-flag": {
        "2_3": {
            "local": "/usa/2_3_usa_large.png",
            "api": "",
        }
    },
    "usa-flag-rippled": {
        "2_3": {
            "local": "/usa/2_3_usa_large_rippled.png",
            "api": "",
        }
    },
    "alabama-flag": {"2_3": {"local": "/alabama/2_3_alabama_large.png", "api": ""}},
    "alabama-flag-rippled": {
        "2_3": {"local": "/alabama/2_3_alabama_large_rippled.png", "api": ""}
    },
    "alaska-flag": {"2_3": {"local": "/alaska/2_3_alaska_large.png", "api": ""}},
    "alaska-flag-rippled": {
        "2_3": {"local": "/alaska/2_3_alaska_large_rippled.png", "api": ""}
    },
    "arizona-flag": {"2_3": {"local": "/arizona/2_3_arizona_large.png", "api": ""}},
    "arizona-flag-rippled": {
        "2_3": {"local": "/arizona/2_3_arizona_large_rippled.png", "api": ""}
    },
    "arkansas-flag": {"2_3": {"local": "/arkansas/2_3_arkansas_large.png", "api": ""}},
    "arkansas-flag-rippled": {
        "2_3": {"local": "/arkansas/2_3_arkansas_large_rippled.png", "api": ""}
    },
    "california-flag": {
        "2_3": {"local": "/california/2_3_california_large.png", "api": ""}
    },
    "california-flag-rippled": {
        "2_3": {"local": "/california/2_3_california_large_rippled.png", "api": ""}
    },
    "colorado-flag": {"2_3": {"local": "/colorado/2_3_colorado_large.png", "api": ""}},
    "colorado-flag-rippled": {
        "2_3": {"local": "/colorado/2_3_colorado_large_rippled.png", "api": ""}
    },
    "connecticut-flag": {
        "2_3": {"local": "/connecticut/2_3_connecticut_large.png", "api": ""}
    },
    "connecticut-flag-rippled": {
        "2_3": {"local": "/connecticut/2_3_connecticut_large_rippled.png", "api": ""}
    },
    "delaware-flag": {"2_3": {"local": "/delaware/2_3_delaware_large.png", "api": ""}},
    "delaware-flag-rippled": {
        "2_3": {"local": "/delaware/2_3_delaware_large_rippled.png", "api": ""}
    },
    "florida-flag": {"2_3": {"local": "/florida/2_3_florida_large.png", "api": ""}},
    "florida-flag-rippled": {
        "2_3": {"local": "/florida/2_3_florida_large_rippled.png", "api": ""}
    },
    "georgia-flag": {"2_3": {"local": "/georgia/2_3_georgia_large.png", "api": ""}},
    "georgia-flag-rippled": {
        "2_3": {"local": "/georgia/2_3_georgia_large_rippled.png", "api": ""}
    },
    "hawaii-flag": {"2_3": {"local": "/hawaii/2_3_hawaii_large.png", "api": ""}},
    "hawaii-flag-rippled": {
        "2_3": {"local": "/hawaii/2_3_hawaii_large_rippled.png", "api": ""}
    },
    "idaho-flag": {"2_3": {"local": "/idaho/2_3_idaho_large.png", "api": ""}},
    "idaho-flag-rippled": {
        "2_3": {"local": "/idaho/2_3_idaho_large_rippled.png", "api": ""}
    },
    "illinois-flag": {"2_3": {"local": "/illinois/2_3_illinois_large.png", "api": ""}},
    "illinois-flag-rippled": {
        "2_3": {"local": "/illinois/2_3_illinois_large_rippled.png", "api": ""}
    },
    "indiana-flag": {"2_3": {"local": "/indiana/2_3_indiana_large.png", "api": ""}},
    "indiana-flag-rippled": {
        "2_3": {"local": "/indiana/2_3_indiana_large_rippled.png", "api": ""}
    },
    "iowa-flag": {"2_3": {"local": "/iowa/2_3_iowa_large.png", "api": ""}},
    "iowa-flag-rippled": {
        "2_3": {"local": "/iowa/2_3_iowa_large_rippled.png", "api": ""}
    },
    "kansas-flag": {"2_3": {"local": "/kansas/2_3_kansas_large.png", "api": ""}},
    "kansas-flag-rippled": {
        "2_3": {"local": "/kansas/2_3_kansas_large_rippled.png", "api": ""}
    },
    "kentucky-flag": {"2_3": {"local": "/kentucky/2_3_kentucky_large.png", "api": ""}},
    "kentucky-flag-rippled": {
        "2_3": {"local": "/kentucky/2_3_kentucky_large_rippled.png", "api": ""}
    },
    "louisiana-flag": {
        "2_3": {"local": "/louisiana/2_3_louisiana_large.png", "api": ""}
    },
    "louisiana-flag-rippled": {
        "2_3": {"local": "/louisiana/2_3_louisiana_large_rippled.png", "api": ""}
    },
    "maine-flag": {"2_3": {"local": "/maine/2_3_maine_large.png", "api": ""}},
    "maine-flag-rippled": {
        "2_3": {"local": "/maine/2_3_maine_large_rippled.png", "api": ""}
    },
    "maryland-flag": {"2_3": {"local": "/maryland/2_3_maryland_large.png", "api": ""}},
    "maryland-flag-rippled": {
        "2_3": {"local": "/maryland/2_3_maryland_large_rippled.png", "api": ""}
    },
    "massachusetts-flag": {
        "2_3": {"local": "/massachusetts/2_3_massachusetts_large.png", "api": ""}
    },
    "massachusetts-flag-rippled": {
        "2_3": {
            "local": "/massachusetts/2_3_massachusetts_large_rippled.png",
            "api": "",
        }
    },
    "michigan-flag": {"2_3": {"local": "/michigan/2_3_michigan_large.png", "api": ""}},
    "michigan-flag-rippled": {
        "2_3": {"local": "/michigan/2_3_michigan_large_rippled.png", "api": ""}
    },
    "minnesota-flag": {
        "2_3": {"local": "/minnesota/2_3_minnesota_large.png", "api": ""}
    },
    "minnesota-flag-rippled": {
        "2_3": {"local": "/minnesota/2_3_minnesota_large_rippled.png", "api": ""}
    },
    "mississippi-flag": {
        "2_3": {"local": "/mississippi/2_3_mississippi_large.png", "api": ""}
    },
    "mississippi-flag-rippled": {
        "2_3": {"local": "/mississippi/2_3_mississippi_large_rippled.png", "api": ""}
    },
    "missouri-flag": {"2_3": {"local": "/missouri/2_3_missouri_large.png", "api": ""}},
    "missouri-flag-rippled": {
        "2_3": {"local": "/missouri/2_3_missouri_large_rippled.png", "api": ""}
    },
    "montana-flag": {"2_3": {"local": "/montana/2_3_montana_large.png", "api": ""}},
    "montana-flag-rippled": {
        "2_3": {"local": "/montana/2_3_montana_large_rippled.png", "api": ""}
    },
    "nebraska-flag": {"2_3": {"local": "/nebraska/2_3_nebraska_large.png", "api": ""}},
    "nebraska-flag-rippled": {
        "2_3": {"local": "/nebraska/2_3_nebraska_large_rippled.png", "api": ""}
    },
    "nevada-flag": {"2_3": {"local": "/nevada/2_3_nevada_large.png", "api": ""}},
    "nevada-flag-rippled": {
        "2_3": {"local": "/nevada/2_3_nevada_large_rippled.png", "api": ""}
    },
    "newHampshire-flag": {
        "2_3": {"local": "/newHampshire/2_3_newHampshire_large.png", "api": ""}
    },
    "newHampshire-flag-rippled": {
        "2_3": {"local": "/newHampshire/2_3_newHampshire_large_rippled.png", "api": ""}
    },
    "newJersey-flag": {
        "2_3": {"local": "/newJersey/2_3_newJersey_large.png", "api": ""}
    },
    "newJersey-flag-rippled": {
        "2_3": {"local": "/newJersey/2_3_newJersey_large_rippled.png", "api": ""}
    },
    "newMexico-flag": {
        "2_3": {"local": "/newMexico/2_3_newMexico_large.png", "api": ""}
    },
    "newMexico-flag-rippled": {
        "2_3": {"local": "/newMexico/2_3_newMexico_large_rippled.png", "api": ""}
    },
    "newYork-flag": {"2_3": {"local": "/newYork/2_3_newYork_large.png", "api": ""}},
    "newYork-flag-rippled": {
        "2_3": {"local": "/newYork/2_3_newYork_large_rippled.png", "api": ""}
    },
    "northCarolina-flag": {
        "2_3": {"local": "/northCarolina/2_3_northCarolina_large.png", "api": ""}
    },
    "northCarolina-flag-rippled": {
        "2_3": {
            "local": "/northCarolina/2_3_northCarolina_large_rippled.png",
            "api": "",
        }
    },
    "northDakota-flag": {
        "2_3": {"local": "/northDakota/2_3_northDakota_large.png", "api": ""}
    },
    "northDakota-flag-rippled": {
        "2_3": {"local": "/northDakota/2_3_northDakota_large_rippled.png", "api": ""}
    },
    "ohio-flag": {"2_3": {"local": "/ohio/2_3_ohio_large.png", "api": ""}},
    "ohio-flag-rippled": {
        "2_3": {"local": "/ohio/2_3_ohio_large_rippled.png", "api": ""}
    },
    "oklahoma-flag": {"2_3": {"local": "/oklahoma/2_3_oklahoma_large.png", "api": ""}},
    "oklahoma-flag-rippled": {
        "2_3": {"local": "/oklahoma/2_3_oklahoma_large_rippled.png", "api": ""}
    },
    "oregon-flag": {"2_3": {"local": "/oregon/2_3_oregon_large.png", "api": ""}},
    "oregon-flag-rippled": {
        "2_3": {"local": "/oregon/2_3_oregon_large_rippled.png", "api": ""}
    },
    "pennsylvania-flag": {
        "2_3": {"local": "/pennsylvania/2_3_pennsylvania_large.png", "api": ""}
    },
    "pennsylvania-flag-rippled": {
        "2_3": {"local": "/pennsylvania/2_3_pennsylvania_large_rippled.png", "api": ""}
    },
    "rhodeIsland-flag": {
        "2_3": {"local": "/rhodeIsland/2_3_rhodeisland_large.png", "api": ""}
    },
    "rhodeIsland-flag-rippled": {
        "2_3": {"local": "/rhodeIsland/2_3_rhodeisland_large_rippled.png", "api": ""}
    },
    "southCarolina-flag": {
        "2_3": {"local": "/southCarolina/2_3_southCarolina_large.png", "api": ""}
    },
    "southCarolina-flag-rippled": {
        "2_3": {
            "local": "/southCarolina/2_3_southCarolina_large_rippled.png",
            "api": "",
        }
    },
    "southDakota-flag": {
        "2_3": {"local": "/southDakota/2_3_southDakota_large.png", "api": ""}
    },
    "southDakota-flag-rippled": {
        "2_3": {"local": "/southDakota/2_3_southDakota_large_rippled.png", "api": ""}
    },
    "tennessee-flag": {
        "2_3": {"local": "/tennessee/2_3_tennessee_large.png", "api": ""}
    },
    "tennessee-flag-rippled": {
        "2_3": {"local": "/tennessee/2_3_tennessee_large_rippled.png", "api": ""}
    },
    "texas-flag": {"2_3": {"local": "/texas/2_3_texas_large.png", "api": ""}},
    "texas-flag-rippled": {
        "2_3": {"local": "/texas/2_3_texas_large_rippled.png", "api": ""}
    },
    "utah-flag": {"2_3": {"local": "/utah/2_3_utah_large.png", "api": ""}},
    "utah-flag-rippled": {
        "2_3": {"local": "/utah/2_3_utah_large_rippled.png", "api": ""}
    },
    "vermont-flag": {"2_3": {"local": "/vermont/2_3_vermont_large.png", "api": ""}},
    "vermont-flag-rippled": {
        "2_3": {"local": "/vermont/2_3_vermont_large_rippled.png", "api": ""}
    },
    "virginia-flag": {"2_3": {"local": "/virginia/2_3_virginia_large.png", "api": ""}},
    "virginia-flag-rippled": {
        "2_3": {"local": "/virginia/2_3_virginia_large_rippled.png", "api": ""}
    },
    "washington-flag": {
        "2_3": {"local": "/washington/2_3_washington_large.png", "api": ""}
    },
    "washington-flag-rippled": {
        "2_3": {"local": "/washington/2_3_washington_large_rippled.png", "api": ""}
    },
    "westVirginia-flag": {
        "2_3": {"local": "/westVirginia/2_3_westVirginia_large.png", "api": ""}
    },
    "westVirginia-flag-rippled": {
        "2_3": {"local": "/westVirginia/2_3_westVirginia_large_rippled.png", "api": ""}
    },
    "wisconsin-flag": {
        "2_3": {"local": "/wisconsin/2_3_wisconsin_large.png", "api": ""}
    },
    "wisconsin-flag-rippled": {
        "2_3": {"local": "/wisconsin/2_3_wisconsin_large_rippled.png", "api": ""}
    },
    "wyoming-flag": {"2_3": {"local": "/wyoming/2_3_wyoming_large.png", "api": ""}},
    "wyoming-flag-rippled": {
        "2_3": {"local": "/wyoming/2_3_wyoming_large_rippled.png", "api": ""}
    },
}

# Convert actual size of the map to ratio size for bg image lookup in BG_IMG_URL_MAP
BG_SIZE_RATIO = {
    "_24_36": "2_3",
}
