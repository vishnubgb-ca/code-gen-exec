
import os
import boto3

def download_file_from_s3(bucket, file_name):
    s3 = boto3.client("s3", 
                      aws_access_key_id=os.getenv("aws_access_key_id"),
                      aws_secret_access_key=os.getenv("aws_secret_access_key"),
                      region_name=os.getenv("region"))

    try:
        s3.download_file(bucket, file_name, file_name)
        print("File downloaded successfully")
    except Exception as e:
        print("Error occurred while downloading file: ", e)

download_file_from_s3(os.getenv("bucket"), "Training.zip")
