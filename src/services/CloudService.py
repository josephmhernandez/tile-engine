
import json
import logging
import boto3
from datetime import date
from io import BytesIO
import src.constants.aws_constants as aws_constants
from boto3.dynamodb.conditions import Key

class CloudService: 
  # Class that reads data from dynamo database 

    def __init__(self, environment):
        self.environment = environment
        self.dynamodb_client = None
        self.s3_client = None
        self.table_name = 'ecommerce.digital-prints'
        self.bucket_name = "maps"
        self.map_location = None
        
        logging.info('[CloudService : __init__] Creating Dynamo resource client for environment: ' + self.environment)
        if self.environment == 'local':
            self.dynamodb_client = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:4566')
            self.s3_client = boto3.client('s3',region_name='us-east-1', endpoint_url='http://localhost:4566')
        elif self.environment == 'dev':
            self.dynamodb_client = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:4566')
            self.s3_client = boto3.client('s3',region_name='us-east-1', endpoint_url='http://localhost:4566')
        elif self.environment == 'prod':
            self.bucket_name = 'public-maps-map-your-memory'
            self.dynamodb_client = boto3.resource('dynamodb', region_name='us-east-2')
            self.s3_client = boto3.client('s3',region_name='us-east-1')
    
    def get_map(self, request_id):
        # Get map from dynamo
        logging.info('[CloudService: get_map] Getting map from dynamo with id: ' + request_id)
        table = self.dynamodb_client.Table(self.table_name)
        response = table.get_item(
            Key={
                # 'orderStatus': aws_constants.PENDING_STATUS,
                'requestId': request_id
            }
        )
        logging.info('[CloudService: get_map] Dynamo response: ' + str(response))
        # response = table.query(
        #     IndexName='requestId-index',
        #     KeyConditionExpression=Key('requestId').eq(request_id)
        # )

        # convert dynamo response to mapInput
        payload = json.loads(response['Item']['mapInput'])
        
        return payload, response['Item']['email']

    def update_record(self, email, request_id):
        # Update record in dynamo
        logging.info('[CloudService: update_record] Updating record in dynamo with id: ' + request_id)
        table = self.dynamodb_client.Table(self.table_name)
        response = table.update_item(
            Key={
                # 'orderStatus': aws_constants.PENDING_STATUS,
                'requestId': request_id
            },
            UpdateExpression="set orderStatus = :s, mapLocation = :l",
            ExpressionAttributeValues={
                ':s': aws_constants.COMPLETED_STATUS,
                ':l': self.map_location
            },
            ReturnValues="UPDATED_NEW"
        )
        logging.info('[CloudService: update_record] Update response: ' + str(response))
        return response

    def write_to_s3(self, map_image_data, file_name):
        # Write image data to localstack
        logging.info("[CloudService: write_to_localstack] Writing an image to S3")
     
        # TO DO: get the time that the request was made from the UI. Help out with debugging.
        today = date.today()
        s3_key = today.strftime("%m-%d-%Y") + '/' + file_name
        bucket_name = self.bucket_name

        self.map_location = 'https://' + bucket_name + '.s3.amazonaws.com/' + s3_key
        
        logging.info('[CloudService: write_to_s3] Checking if bucket exists: ' + bucket_name)
        try:
            self.s3_client.head_bucket(Bucket=bucket_name)
            logging.info('[CloudService: write_to_s3] Bucket already exists')
        except:
            logging.info('[CloudService: write_to_s3] Bucket does not exist. Creating bucket')
            self.s3_client.create_bucket(Bucket=bucket_name)
        
        
        # Save the PIL Image to a BytesIO object
        image_stream = BytesIO()
        map_image_data.save(image_stream, format='PNG')
        image_stream.seek(0)
        
        # Upload the image to S3
        logging.info('[CloudService: write_to_s3] Uploading image to S3 bucket: ' + bucket_name + ' with key: ' + s3_key)
        self.s3_client.upload_fileobj(image_stream, bucket_name, s3_key)
    
    def list_s3_objects(self):
        # List all the objects in the bucket
        for obj in self.s3_client.list_objects(Bucket=self.bucket_name)['Contents']:
            logging.info('[CloudService: write_to_s3] S3 object key: ' + obj['Key'])
