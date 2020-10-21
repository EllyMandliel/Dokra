class RecorderSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(RecorderSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FunctionWrapper(metaclass=RecorderSingleton):

    def __getitem__(self, item):
        return_type = None
        if isinstance(item, slice):
            return_type = item.stop
            item = item.start
        if callable(item):
            return WrappedFunction(item, return_type)


class WrappedFunction:

    def __init__(self, function, return_type=None):
        self.function = function
        self.__annotations__ = {'return': return_type}

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
