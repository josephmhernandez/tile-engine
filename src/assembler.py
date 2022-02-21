
import PIL.Image
import math
import decimal
from os import listdir
from os.path import isfile, join
from bbox import Bbox
from coord import Coord
import mercantile
import numpy as np
class Assembler:

    @staticmethod
    def assemble_image(folder_path, tile_grid, output_img_name):
        # Given a folder path, concatenate the map image from these tile images. 
        # tile_grid [x, y] Number of tiles in grid 

        # Make a list of the image names   
        image_files = [folder_path + f for f in listdir(folder_path)]
        # Open the image set using pillow
        images = [PIL.Image.open(x) for x in image_files]

        # Calculate the number of image tiles in each direction
        edge_length_x = tile_grid[0]
        edge_length_y = tile_grid[1]

        # Find the final composed image dimensions  
        width, height = images[0].size
        total_width = width*edge_length_x
        total_height = height*edge_length_y

        # Create a new blank image we will fill in
        composite = PIL.Image.new('RGB', (total_width, total_height))
        
        # Loop over the x and y ranges
        y_offset = 0
        for i in range(0,edge_length_x):
            x_offset = 0
            for j in range(0,edge_length_y):
                # Open up the image file and paste it into the composed
                # image at the given offset position
                tmp_img = PIL.Image.open(folder_path + str(i) + '.' + str(j) + '.png')
                composite.paste(tmp_img, (y_offset,x_offset))
                x_offset += width # Update the width
            y_offset += height # Update the height
        
        # Save the final image
        composite.save('./' + output_img_name + '.png')


        

    @staticmethod
    def check_image_folder_exists(folder_path):
        # TO DO: Check the existance of folder and process error associated with this. 
        print("TO DO: check image folder existance")


    @staticmethod
    def crop_image(map_box, img_path, output_path, zoom):

        # Open Image
        img = PIL.Image.open(img_path)
        img_width, img_height = img.size

        # Create tile_box (it is larger than map box) 
        tl_tile = mercantile.tile(float(map_box.top_left.lon), float(map_box.top_left.lat), zoom)
        br_tile = mercantile.tile(float(map_box.bottom_right.lon), float(map_box.bottom_right.lat), zoom)
        br_tile = mercantile.Tile(x = br_tile.x+1, y = br_tile.y+1 , z = zoom)
        tl_coord = Coord(mercantile.ul(tl_tile).lng, mercantile.ul(tl_tile).lat)
        br_coord = Coord(mercantile.ul(br_tile).lng, mercantile.ul(br_tile).lat)
        tile_box = Bbox(tl_coord, br_coord)

        # Get difference between tile_box and map_box
        diff_left_degree = abs(tile_box.top_left.lon - map_box.top_left.lon)
        diff_right_degree = abs(tile_box.bottom_right.lon - map_box.bottom_right.lon)
        diff_top_degree = abs(tile_box.top_left.lat - map_box.top_left.lat)
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
        crop_payload = (0 + pixel_diff_left, 0 + pixel_diff_top, img.width - pixel_diff_right, img.height - pixel_diff_bottom)
        im1 = img.crop(crop_payload)

        im1.save(output_path)

