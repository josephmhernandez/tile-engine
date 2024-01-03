# from datetime import date
# from io import BytesIO
# import logging
# import boto3

# class S3Writer:
#     def __init__(self, environment):
#         self.environment = environment
#         self.s3_client = None
#         self.bucket_name = 'maps'
        
#         logging.info('[S3Writer : __init__] Creating S3 resource client for environment: ' + self.environment)
#         if self.environment == 'local':
#             self.s3_client = boto3.client('s3',region_name='us-east-1', endpoint_url='http://localhost:4566')
#         elif self.environment == 'dev':
#             self.s3_client = boto3.client('s3',region_name='us-east-1', endpoint_url='http://localhost:4566')
#         elif self.environment == 'prod':
#             self.bucket_name = 'public-maps-map-your-memory'
#             self.s3_client = boto3.client('s3',region_name='us-east-1')

#     def write_to_s3(self, map_image_data, file_name):
#         # Write image data to localstack
#         logging.info("[S3Writer: write_to_localstack] Writing an image to S3")
     
#         # TO DO: get the time that the request was made from the UI. Help out with debugging.
#         today = date.today()
#         s3_key = today.strftime("%m-%d-%Y") + '/' + file_name
#         bucket_name = self.bucket_name
        
#         logging.info('[S3Writer: write_to_s3] Checking if bucket exists: ' + bucket_name)
#         try:
#             self.s3_client.head_bucket(Bucket=bucket_name)
#             logging.info('[S3Writer: write_to_s3] Bucket already exists')
#         except:
#             logging.info('[S3Writer: write_to_s3] Bucket does not exist. Creating bucket')
#             self.s3_client.create_bucket(Bucket=bucket_name)
        
        
#         # Save the PIL Image to a BytesIO object
#         image_stream = BytesIO()
#         map_image_data.save(image_stream, format='PNG')
#         image_stream.seek(0)

#         # Upload the image to S3
#         logging.info('[S3Writer: write_to_s3] Uploading image to S3 bucket: ' + bucket_name + ' with key: ' + s3_key)
#         self.s3_client.upload_fileobj(image_stream, bucket_name, s3_key)
    
#     def list_s3_objects(self):
#         # List all the objects in the bucket
#         for obj in self.s3_client.list_objects(Bucket=self.bucket_name)['Contents']:
#             logging.info('[S3Writer: write_to_s3] S3 object key: ' + obj['Key'])

    
