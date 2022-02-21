

# TO DO: Make this parrallelized. Multi-thread approach to download tiles 

import this
import requests
import shutil
import mercantile
import math
from models.bbox import Bbox
from models.coord import Coord

class Downloader:

    @staticmethod
    def generate_tile_lists(map_bbox, tile_size, base_url, zoom):
        tl_tiles = mercantile.tile(float(map_bbox.top_left.lon), float(map_bbox.top_left.lat), zoom)
        br_tiles = mercantile.tile(float(map_bbox.bottom_right.lon), float(map_bbox.bottom_right.lat), zoom)

        x_tile_range = [tl_tiles.x,br_tiles.x]
        y_tile_range = [tl_tiles.y,br_tiles.y]

        # Loop over the tile ranges
        for i,x in enumerate(range(x_tile_range[0],x_tile_range[1]+1)):
            for j,y in enumerate(range(y_tile_range[0],y_tile_range[1]+1)):
                file_name = './src/tile_images/' + str(i) + '.' + str(j) + '.png'
                Downloader.download_tile(x, y, zoom, base_url, file_name)

        return [abs(x_tile_range[0] - x_tile_range[1])+1, abs(y_tile_range[0] - y_tile_range[1])+1]

    @staticmethod
    def download_tile(x, y, z, url, file_name):
        url = url.replace('{z}', str(z))
        url = url.replace('{x}', str(x))
        url = url.replace('{y}', str(y))
        
        # Call the URL to get the image back
        r = requests.get(
            url, 
            stream=True
        )

        if(r.status_code != 200):
            print('status code incorrect')
            print(r)

        # Next we will write the raw content to an image
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 


    def create_temp_tiles_folder(): 
        # TO DO:
        # - Checks to see if the folder exists
        # - Creates folder if it doesn't exist
        # - Clears contents in folder 
        print('TO DO: create_temp_tiles_folder')