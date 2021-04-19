from src.utils.utils import upload_file_to_s3


class S3Uploader(object):
    def __init__(self, bucket, key):
        self.bucket = bucket
        self.key = key

    def upload(self, data):
        upload_file_to_s3(self.bucket, self.key, data)
        print(f'uploaded {data}')
        return True


class SnapUploader(S3Uploader):
    def __init__(self):
        print('Initializing SnapUploader object')
        super().__init__('SnapS3Bucket', 'SnapS3Key')


class NextDoorUploader(S3Uploader):
    def __init__(self):
        print('Initializing NextDoorUploader object')
        super().__init__('NextDoorS3Bucket', 'NextDoorS3Key')
