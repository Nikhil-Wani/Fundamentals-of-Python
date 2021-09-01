import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIARBJW34Z4F5ILQN6S'
ACCESS_SECRET_KEY = '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'

# S3 Connect
s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.delete_object(Bucket='cyient-avangrid', Key='life-support-1630400034.json')

print ("Done")