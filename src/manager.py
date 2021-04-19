from src.transform.transform import NextdoorTransformer, SnapTransformer
from src.upload.upload import SnapUploader, NextDoorUploader


class Manager(object):
    def __init__(self, transformer, uploader):
        self._transformer = transformer
        self._uploader = uploader

    def run(self, data):
        transformed = self._transformer.transform(data)
        uploaded = self._uploader.upload(transformed)
        return uploaded


def manager_factory(manager_type: Manager):
    if manager_type == 'SNAP':
        transformer = SnapTransformer()
        uploader = SnapUploader()
    elif manager_type == 'NEXTDOOR':
        transformer = NextdoorTransformer()
        uploader = NextDoorUploader()
    return Manager(transformer, uploader)
