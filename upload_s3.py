from __future__ import print_function
import urllib
import datetime 
import boto3
from botocore.client import Config

def lambda_handler(event, context):

    """Make a variable containing the date format based on YYYYYMMDD"""
    cur_dt = datetime.datetime.today().strftime('%Y%m%d')

    """Make a variable containing the url and current date based on the variable
    cur_dt"""
    dls = "http://11.11.111.111/XL/" + cur_dt + ".xlsx"
    urllib.urlretrieve(dls, cur_dt + "test.xls")

    ACCESS_KEY_ID = 'Abcdefg'
    ACCESS_SECRET_KEY = 'hijklmnop+6dKeiAByFluK1R7rngF'
    BUCKET_NAME = 'my-bicket'
    FILE_NAME = cur_dt + "test.xls";

    data = open('/tmp/' + FILE_NAME, 'wb')

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    # Uploaded File
    s3.Bucket(BUCKET_NAME).put(Key=FILE_NAME, Body=data, ACL='public-read')
