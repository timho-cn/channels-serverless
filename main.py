import os
from src.constant import S3_BUCKET, S3_KEY
from src.manager import manager_factory
from src.utils.utils import download_file_from_s3

'''
Parse partner_id argument
Use partner_id to decide which manager to create
Buffer S3 file (or load entirely into memory because we have to transform?)
'''

'''
Downloading S3 file outside of handler because AWS billing cycles do not apply to init logic
This may need to be moved under handler if channels service needs to dynamically determine S3_BUCKET/S3_KEY
'''
data = download_file_from_s3(S3_BUCKET, S3_KEY)


def lambda_handler(event, context):
    partner_id = event['partner_id']
    manager = manager_factory(partner_id)
    manager.run(data)
