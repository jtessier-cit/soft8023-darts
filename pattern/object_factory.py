# generic object factory
class ObjectFactory:
    def __init__(self):
        # dictionary to register a builder key/method
        self._builders = {}

    # add a builder to the dictionary of builders
    # key = object type
    # builder = builder class
    def register_builder(self, key, builder):
        self._builders[key] = builder

    # return a builder
    def create(self, key, **kwargs):
        # get the builder class from the key/object type
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)