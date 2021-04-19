def download_file_from_s3(bucket: str, key: str):
    print(f'Downloading S3 file: s3://{bucket}/{key}')
    return 'some_data'


def upload_file_to_s3(bucket: str, key: str, file):
    print(f'Uploading S3 file to s3://{bucket}/{key}')
