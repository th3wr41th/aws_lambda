from __future__ import print_function
import urllib
import datetime 
import boto3
from botocore.client import Config

def lambda_handler(event, context):
    date = datetime.datetime.today().strftime('%Y%m%d')
    url = "http://scientia.cloud/" + date + ".csv"
    urllib.urlretrieve(url, date + "info.csv")

    ACCESS_KEY_ID = 'test'
    ACCESS_SECRET_KEY = 'xxxxxxxxxxxxxxx'
    BUCKET_NAME = 'arch_mack'
    FILE_NAME = date + "info.csv";

    data = open('/tmp/' + FILE_NAME, 'r')

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    # Upload the File
    s3.Bucket(BUCKET_NAME).put(Key=FILE_NAME, Body=data, ACL='public-read')
