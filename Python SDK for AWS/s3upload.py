import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIARBJW34Z4F5ILQN6S'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'cyient-avangrid'
FILE_NAME = 'D:\Energy Management Dashboard Project\VirtualizedApplicationsUserGuideAV.pdf'


data = open(FILE_NAME, 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# Image Uploaded
s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)

print ("Done")