#!/usr/bin/env/env python3
import boto3
import io
from io import BytesIO
from minio import Minio
from minio.error import S3Error

# Create the client
client = Minio('localhost:9000', access_key='minio', secret_key='miniosecret', secure=False)

if __name__ == "__main__":
    print("MinIO Client {}".format(client))
    buckets = client.list_buckets()
    for bucket in buckets:
        print(bucket.name, bucket.creation_date)
