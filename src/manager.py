from transform import NextdoorTransformer, SnapTransformer
from upload import S3Uploader


class Manager(object):
    def __init__(self, transformer, uploader):
        self._transformer = transformer
        self._uploader = uploader

    def run(self, data_loader):
        loaded_data = data_loader.load()
        transformed = self._transformer.transform(loaded_data)
        uploaded = self._uploader.upload(transformed)
        return uploaded


class ManagerFactory(object):
    def __init__(self, manager_type):
        if manager_type == 'SNAP':
            transformer = SnapTransformer()
            uploader = S3Uploader()
        elif manager_type == 'NEXTDOOR':
            transformer = NextdoorTransformer()
            uploader = S3Uploader()
        return Manager(transformer, uploader)
