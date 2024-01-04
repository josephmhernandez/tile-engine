
# Start LocalStack then run tile engine from command line. 

# Kill any existing Docker containers running on the same port
docker stop $(docker ps -q --filter "publish=4572")

# Start LocalStack with S3 service in detached mode
docker run -d --rm -p 4572:4572 -e DEBUG=1 -e SERVICES=s3 localstack/localstack

# docker run -it localstack/localstack:latest


# localstack start

# Give LocalStack some time to start up
sleep 10

pipenv run python3 main.py test/inputs/image-bg/12-4/dallas-landscape-white.json 
