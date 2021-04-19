class SnapTransformer(object):
    def transform(self, data):
        print(f'Snap transformed {data}')
        return True


class NextdoorTransformer(object):
    def transform(self, data):
        print(f'Nextdoor transformed {data}')
        return True
