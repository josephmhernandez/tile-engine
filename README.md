# tile-engine

pipenv run python3 main.py test/inputs/seattle-lights.json

# Commands

pipenv shell # Activate virtual environment

# Check for vulnerabilities

pipenv check

# Run Tests

pytest

# Run Test with Logs outputted to console / whereever

pytest --log-cli-level=INF

# Run Specific Test

pytest test_mod.py::TestClass::test_method
pytest test/assembler_test.py::TestAssembler::test_add_text_all_blocks

# Run the application

pipenv run python3 main.py test/inputs/
RUN WITH LOGS TO CONSOLE:
Comment out line in logging.basicCongig in main.py

# Local Configuraiton Changes

Download images zip folder
Change BG_FOLDER_PATH (src/constants/bg_images.py) to the location locally of the unzipped bg images

# Pipenv guide: https://realpython.com/pipenv-guide/

# Organize ouput files:

Let's put all output files into a folder called temp_output/
Name files based off of their assembler / downloader step name
Steps:

1. Downloader - download the tiles
2. Assembler - assemble-tiles to one image
3. Assembler - crop-image to the bbox
4. Assembler - add-pin to the image
5. TransparencyTransformer - Adds transparency to the tile layer. Adds image as background.
6. Assembler - add-style to the map image (transparency etc.)
7. Assembler - add-text to the image
8. Assembler - add-border to the image

TO DO List:

1. Ctrl shift I thing to automatically fix spacing stuff.
2. Clean up import so that they don’t have \*. Only import functions
3. Exception Handling
4. Logging
5. Result Codes
6. Validating Engine inputs
7. Strong typing / hybrid? Not sure? Research pros and cons. Might not be worth doing.
8. Unit Testing - PyTest
9. Integration Testing
10. Acceptance Testing
11. Delete images we downloaded once we are done with them. Clean up functions for each engine call (assembler, downloader, etc.)
12. Bbox edge cases: lon and lat across prime meridian /equator. How are those handled.
13. Think of better way to separate engine_utils into multiple utils.

14. FIll in ValueValidator Class

<!-- LocalStack Docker -->

# to start localstack:

docker compose up -d

# to create dynamo db table

aws --endpoint-url=http://localhost:4566 cloudformation deploy --stack-name cloudformation-example --template-file "cloudformation-example.yml"

# to list dynamo db tables

aws --endpoint-url=http://localhost:4566 dynamodb list-tables

# table count

aws --endpoint-url=http://localhost:4566 dynamodb describe-table --table-name ecommerce.digital-prints --query 'Table.ItemCount'

# insert item to table

aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name ecommerce.digital-prints --item '{"email":{"S":"josephmhernandez15@gmail.com"},"requestId":{"S":"req_eb267789-a25d-47f7-bb7d-b326c96291"},"orderStatus":{"S":"PENDING"},"orderedOn":{"S":"2016-06-02T12:53:14.924Z"},"emailStatus":{"S":"PENDING"},"mapInput":{"S": "{\"pinList\":[],\"center\":[32.7766642,-96.79698789999999],\"zoom\":9,\"orientation\":\"landscape\",\"textPrimary\":\"Dallas, TX\",\"textSecondary\":\"\",\"textCoordinates\":\"N 32°46'35.99\\\" W 96°47'49.16\\\"\",\"styling\":\"basic\",\"size\":\"\_24_36_demo\",\"tileLayer\":\"modern-light\",\"bbox\":\"{\\\"\_southWest\\\":{\\\"lat\\\":32.52597362010653,\\\"lng\\\":-97.24273681640626},\\\"\_northEast\\\":{\\\"lat\\\":33.02478477990269,\\\"lng\\\":-96.35284423828126}}\",\"tileZoomOffset\":3,\"bgImgCode\":\"\",\"quantity\":1,\"description\":\"Map of Dallas, TX\",\"id\":\"eb267789-a25d-47f7-bb7d-b326c96291ab\",\"name\":\"Personalized Map\",\"unitPrice\":249.99,\"lineItemId\":[{\"id\":\"item_7RyWOwmK5nEa2V\",\"product_id\":\"prod_VKXmwDy717orgD\",\"name\":\"Personalized Map\",\"product_name\":\"Personalized Map\",\"sku\":null,\"permalink\":\"qNG91W\",\"quantity\":2,\"price\":{\"raw\":249.99,\"formatted\":\"249.99\",\"formatted_with_symbol\":\"$249.99\",\"formatted_with_code\":\"249.99 USD\"},\"line_total\":{\"raw\":499.98,\"formatted\":\"499.98\",\"formatted_with_symbol\":\"$499.98\",\"formatted_with_code\":\"499.98 USD\"},\"is_valid\":true,\"product_meta\":[],\"selected_options\":[],\"variant\":null,\"image\":{\"id\":\"ast_yA6nldR94goEWb\",\"url\":\"https://cdn.chec.io/merchants/47490/assets/CjaynbQmf8IB1ml3|text-close-up.jpg\",\"description\":null,\"is_image\":true,\"filename\":\"text-close-up.jpg\",\"file_size\":356984,\"file_extension\":\"jpg\",\"image_dimensions\":{\"width\":2000,\"height\":1000},\"meta\":[],\"created_at\":1679717075,\"updated_at\":1679717076},\"tax\":null}],\"isTransparentTextBlock\":true,\"text_styling_specs\":{\"id\":\"img-bg-black\",\"iconImg\":\"/tan-ocean.png\",\"url\":\"https://api.maptiler.com/maps/11489910-a9d8-4e58-a989-e00a490cf934/{z}/{x}/{y}.jpg?key=fLxXsh3K0MP3y21i3bJs\",\"isOverlay\":true,\"text\":{\"fontFamily\":{\"primary\":\"Semplicita\",\"secondary\":\"Semplicita\",\"coordinate\":\"Semplicita\"},\"size\":{\"primary\":\"24\",\"secondary\":\"12\",\"coordinate\":\"8\"},\"size_demo\":{\"primary\":\"8\",\"secondary\":\"4\",\"coordinate\":\"2\"},\"color\":{\"background\":\"#000000\",\"primary\":\"#FFFFFF\",\"secondary\":\"#FFFFFF\",\"coordinate\":\"#FFFFFF\"},\"color_transparent\":{\"background\":\"#0000\",\"primary\":\"#000000\",\"secondary\":\"#000000\",\"coordinate\":\"#000000\"},\"textBlock\":{\"padding\":\"8px\",\"rounded\":\"8px\",\"spacing\":\"1\"},\"text_block_demo\":{\"padding\":\"1px\",\"rounded\":\"3px\",\"spacing\":\"1\"}}},\"mapDimensionsIn\":{\"map_width\":36,\"map_height\":24,\"map_pixel_multiplier\":9}}"}}'
