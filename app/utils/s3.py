import boto3
from flask import current_app

def get_s3_client():
    return boto3.client(
        's3',
        region_name='us-east-1',
        endpoint_url='http://localstack:4566',  # Nombre del servicio en Docker
        aws_access_key_id='test',
        aws_secret_access_key='test'
    )