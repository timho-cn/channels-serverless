import os
from src.manager import ManagerFactory
'''
Parse partner_id argument
Use partner_id to decide which manager to create
Buffer S3 file (or load entirely into memory because we have to transform?)
'''

S3_BUCKET = os.getenv('S3_BUCKET')
S3_KEY = f'<some_datestring>/feed.json'


def lambda_handler(event, context):
    partner_id = event['partner_id']
    manager = ManagerFactory(partner_id)
    manager.run()
