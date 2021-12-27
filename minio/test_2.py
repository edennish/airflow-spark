import boto3
from botocore.client import Config

ACCESS_KEY="access"
SECRET_KEY="secret"
BUCKET_NAME="stage"

print("Creating the Session")
s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY,
                    #config=Config(signature_version='s3v4'),
                    #region_name='us-east-1'
                    )

print("Get Bucket")
my_bucket = s3.Bucket(BUCKET_NAME)

print("List")
index = 0
for s3_file in my_bucket.objects.all():
    print ("Found file: {file}".format(file=s3_file))
    print('\n')
