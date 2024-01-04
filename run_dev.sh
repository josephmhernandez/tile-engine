
# Start LocalStack then run tile enginer

# Kill any existing Docker containers running on the same port
# docker stop $(docker ps -q --filter "publish=4572")

# Start LocalStack with S3 service in detached mode
# docker run -d --rm -p 4572:4572 -e SERVICES=s3 localstack/localstack

# Give LocalStack some time to start up
# sleep 20

# localstack start -d --docker

# sleep 3


# docker run \
#   -e ENV='prod' \
#   -e MAP_INPUT="[{\"pinList\":[],\"center\":[32.7766642,-96.79698789999999],\"zoom\":9,\"orientation\":\"landscape\",\"textPrimary\":\"Dallas, TX\",\"textSecondary\":\"\",\"textCoordinates\":\"N 32°46'35.99\\\" W 96°47'49.16\\\"\",\"styling\":\"basic\",\"size\":\"_24_36_demo\",\"tileLayer\":\"modern-light\",\"bbox\":\"{\\\"_southWest\\\":{\\\"lat\\\":32.52597362010653,\\\"lng\\\":-97.24273681640626},\\\"_northEast\\\":{\\\"lat\\\":33.02478477990269,\\\"lng\\\":-96.35284423828126}}\",\"tileZoomOffset\":3,\"bgImgCode\":\"\",\"quantity\":1,\"description\":\"Map of Dallas, TX\",\"id\":\"eb267789-a25d-47f7-bb7d-b326c96291ab\",\"name\":\"Personalized Map\",\"unitPrice\":249.99,\"lineItemId\":[{\"id\":\"item_7RyWOwmK5nEa2V\",\"product_id\":\"prod_VKXmwDy717orgD\",\"name\":\"Personalized Map\",\"product_name\":\"Personalized Map\",\"sku\":null,\"permalink\":\"qNG91W\",\"quantity\":2,\"price\":{\"raw\":249.99,\"formatted\":\"249.99\",\"formatted_with_symbol\":\"$249.99\",\"formatted_with_code\":\"249.99 USD\"},\"line_total\":{\"raw\":499.98,\"formatted\":\"499.98\",\"formatted_with_symbol\":\"$499.98\",\"formatted_with_code\":\"499.98 USD\"},\"is_valid\":true,\"product_meta\":[],\"selected_options\":[],\"variant\":null,\"image\":{\"id\":\"ast_yA6nldR94goEWb\",\"url\":\"https://cdn.chec.io/merchants/47490/assets/CjaynbQmf8IB1ml3|text-close-up.jpg\",\"description\":null,\"is_image\":true,\"filename\":\"text-close-up.jpg\",\"file_size\":356984,\"file_extension\":\"jpg\",\"image_dimensions\":{\"width\":2000,\"height\":1000},\"meta\":[],\"created_at\":1679717075,\"updated_at\":1679717076},\"tax\":null}],\"isTransparentTextBlock\":true,\"text_styling_specs\":{\"id\":\"img-bg-black\",\"iconImg\":\"/tan-ocean.png\",\"url\":\"https://api.maptiler.com/maps/11489910-a9d8-4e58-a989-e00a490cf934/{z}/{x}/{y}.jpg?key=fLxXsh3K0MP3y21i3bJs\",\"isOverlay\":true,\"text\":{\"fontFamily\":{\"primary\":\"Semplicita\",\"secondary\":\"Semplicita\",\"coordinate\":\"Semplicita\"},\"size\":{\"primary\":\"24\",\"secondary\":\"12\",\"coordinate\":\"8\"},\"size_demo\":{\"primary\":\"8\",\"secondary\":\"4\",\"coordinate\":\"2\"},\"color\":{\"background\":\"#000000\",\"primary\":\"#FFFFFF\",\"secondary\":\"#FFFFFF\",\"coordinate\":\"#FFFFFF\"},\"color_transparent\":{\"background\":\"#0000\",\"primary\":\"#000000\",\"secondary\":\"#000000\",\"coordinate\":\"#000000\"},\"textBlock\":{\"padding\":\"8px\",\"rounded\":\"8px\",\"spacing\":\"1\"},\"text_block_demo\":{\"padding\":\"1px\",\"rounded\":\"3px\",\"spacing\":\"1\"}}},\"mapDimensionsIn\":{\"map_width\":36,\"map_height\":24,\"map_pixel_multiplier\":9}}]" \
#   --memory 10gb \
#   tile-engine:latest 

# Doesn't run yet  -----------------------------------------------------------------------------------------------------------------------------------------------------------
# to start localstack:

# docker compose up -d

# to create dynamo db table

aws --endpoint-url=http://localhost:4566 cloudformation deploy --stack-name cloudformation-example --template-file "cloudformation-example.yml"

# to list dynamo db tables

aws --endpoint-url=http://localhost:4566 dynamodb list-tables

# table count

aws --endpoint-url=http://localhost:4566 dynamodb describe-table --table-name ecommerce.digital-prints --query 'Table.ItemCount'

# set up localstack dynamo: 
# request id: req_eb267789-a25d-47f7-bb7d-b326c96291ab
aws --endpoint-url=http://localhost:4566 dynamodb put-item --table-name ecommerce.digital-prints --item '{"email": {"S": "josephmhernandez15@gmail.com"}, "requestId": {"S": "req_eb267789-a25d-47f7-bb7d-b326c96291ab"}, "orderStatus": {"S": "PENDING"}, "mapInput": {"S": "{\"pinList\":[],\"center\":[32.7766642,-96.79698789999999],\"zoom\":9,\"orientation\":\"landscape\",\"textPrimary\":\"Dallas, TX\",\"textSecondary\":\"\",\"textCoordinates\":\"N 99.16\\\"\",\"styling\":\"basic\",\"size\":\"_24_36_demo\",\"tileLayer\":\"modern-light\",\"bbox\":\"{\\\"_southWest\\\":{\\\"lat\\\":32.52597362010653,\\\"lng\\\":-97.24273681640626},\\\"_northEast\\\":{\\\"lat\\\":33.02478477990269,\\\"lng\\\":-96.35284423828126}}\",\"tileZoomOffset\":3,\"bgImgCode\":\"\",\"quantity\":1,\"description\":\"Map of Dallas, TX\",\"id\":\"eb267789-a25d-47f7-bb7d-b326c96291ab\",\"name\":\"Personalized Map\",\"unitPrice\":249.99,\"lineItemId\":[{\"id\":\"item_7RyWOwmK5nEa2V\",\"product_id\":\"prod_VKXmwDy717orgD\",\"name\":\"Personalized Map\",\"product_name\":\"Personalized Map\",\"sku\":null,\"permalink\":\"qNG91W\",\"quantity\":2,\"price\":{\"raw\":249.99,\"formatted\":\"249.99\",\"formatted_with_symbol\":\"$249.99\",\"formatted_with_code\":\"249.99 USD\"},\"line_total\":{\"raw\":499.98,\"formatted\":\"499.98\",\"formatted_with_symbol\":\"$499.98\",\"formatted_with_code\":\"499.98 USD\"},\"is_valid\":true,\"product_meta\":[],\"selected_options\":[],\"variant\":null,\"image\":{\"id\":\"ast_yA6nldR94goEWb\",\"url\":\"https://cdn.chec.io/merchants/47490/assets/CjaynbQmf8IB1ml3|text-close-up.jpg\",\"description\":null,\"is_image\":true,\"filename\":\"text-close-up.jpg\",\"file_size\":356984,\"file_extension\":\"jpg\",\"image_dimensions\":{\"width\":2000,\"height\":1000},\"meta\":[],\"created_at\":1679717075,\"updated_at\":1679717076},\"tax\":null}],\"isTransparentTextBlock\":true,\"text_styling_specs\":{\"id\":\"img-bg-black\",\"iconImg\":\"/tan-ocean.png\",\"url\":\"https://api.maptiler.com/maps/11489910-a9d8-4e58-a989-e00a490cf934/{z}/{x}/{y}.jpg?key=fLxXsh3K0MP3y21i3bJs\",\"isOverlay\":true,\"text\":{\"fontFamily\":{\"primary\":\"Semplicita\",\"secondary\":\"Semplicita\",\"coordinate\":\"Semplicita\"},\"size\":{\"primary\":\"24\",\"secondary\":\"12\",\"coordinate\":\"8\"},\"size_demo\":{\"primary\":\"8\",\"secondary\":\"4\",\"coordinate\":\"2\"},\"color\":{\"background\":\"#000000\",\"primary\":\"#FFFFFF\",\"secondary\":\"#FFFFFF\",\"coordinate\":\"#FFFFFF\"},\"color_transparent\":{\"background\":\"#0000\",\"primary\":\"#000000\",\"secondary\":\"#000000\",\"coordinate\":\"#000000\"},\"textBlock\":{\"padding\":\"8px\",\"rounded\":\"8px\",\"spacing\":\"1\"},\"text_block_demo\":{\"padding\":\"1px\",\"rounded\":\"3px\",\"spacing\":\"1\"}}},\"mapDimensionsIn\":{\"map_width\":36,\"map_height\":24,\"map_pixel_multiplier\":9}}"}}'

# create s3 bucket 
aws --endpoint-url=http://localhost:4566 s3 mb s3://tile-engine-resources

# add tile-engine-resources to s3 bucket
aws --endpoint-url=http://localhost:4566 s3 cp ./tile-engine-resources s3://tile-engine-resources --recursive