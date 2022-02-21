# Tile Engine donwload, assemble, and print tiles into a large image file

# Input: 
# - BBox (EPSG:4326 projected coordinates) [float] size 4
# - Height (inches) of final picture
# - Width (inches) of final picture 
# - Size of tiles we want to download (256, 512, 1024) 

# Output: 
# - Tiff Image of map at high resolution > 300 dpi

from models.coord import Coord
from engine.downloader import Downloader
from engine.assembler import Assembler
from models.bbox import Bbox

import PIL.Image

if __name__ == "__main__":
    # 1. Use BBox & size of tiles to get the List of tiles we want to download 
    # 2. Multi threaded download of tiles
    # 3. Assemble tiles on download completion
    # 4. Output tiff / Download tiff to device / store tiff somewhere? 
    
    bbox = [-77.09690093994142,38.86042928143244,-76.97673797607423,38.95393580081098]

    tile_size = 0
    # 1024 tiles. 
    base_url = 'https://api.maptiler.com/maps/voyager/{z}/{x}/{y}@2x.png?key=msqCXSKnPannMXvUCPsn#' 

    zoom = 15

    map_box = Bbox(Coord(bbox[0], bbox[3]), Coord(bbox[2], bbox[1]))

    new_grid = Downloader.generate_tile_lists(map_box, tile_size, base_url, zoom) 
    print('new_grid')
    print(new_grid)
    Assembler.assemble_image('./src/tile_images/', new_grid, 'downloaded_image')

    Assembler.crop_image(map_box, './downloaded_image.png', output_path="./cropped_image.png", zoom=zoom)



