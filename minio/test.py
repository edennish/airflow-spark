
from boto3.session import Session

ACCESS_KEY="access"
SECRET_KEY="secret"
BUCKET_NAME="stage"
PREFIX="root"
MAX_FILES_READ=3
TOKEN = "token"

print("Creating the Session")
# Use Boto to connect to S3 and get a list of objects from a bucket
session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, aws_session_token=TOKEN)

print("Resources")
s3 = session.resource('s3')

print("Get Bucket")
# call S3 to list current buckets
my_bucket = s3.Bucket(BUCKET_NAME)

print("List")
index = 0
for s3_file in my_bucket.objects.filter(Prefix=PREFIX):
    if 'gz' in s3_file.key:
        index += 1
        print ("Found file: {file}".format(file=s3_file.key))
        if index == MAX_FILES_READ:
            break
        fileLocation = "s3a://{bucket}/{file}".format(bucket=BUCKET_NAME,file=s3_file.key)
        print ("file location: {loc}".format(loc=fileLocation))
        s3File = sc.textFile(fileLocation)
        print(s3File.count())
        print('\n')
