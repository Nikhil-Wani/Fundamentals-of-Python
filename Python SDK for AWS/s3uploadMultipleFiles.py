import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIARBJW34Z4F5ILQN6S'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'cyient-avangrid'
local_file = r'D:\Energy Management Dashboard Project\Docs\xls'

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)   

for filename in os.listdir(local_file):
    path = r'{}\{}'.format(local_file, filename)
    data = open(path, 'rb')

# Image Uploaded
    s3.Bucket(BUCKET_NAME).put_object(Key=path, Body=data)
    print ("Done")