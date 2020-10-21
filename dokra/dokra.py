from Dokra.utils import identity
from Dokra.wrapper import WrappedFunction, FunctionWrapper


class Dokra:

    def __new__(cls, func=None, *args, **kwargs):
        if not func:
            return FunctionWrapper()
        return Dokra.decorate(func)

    @staticmethod
    def decorate(func):
        wrapped_annotations = {key: value for key, value in dict(func.__annotations__).items() if is_middleware(value)}
        if 'return' in wrapped_annotations:
            endware_type = wrapped_annotations.pop('return')
            endware = endware_type
        else:
            endware = identity

        def wrapper(*args, **kwargs):
            full_kwargs = {
                **{arg_name: arg_value for arg_name, arg_value in zip(func.__code__.co_varnames, args)},
                **kwargs
            }
            patched_kwargs = {
                key: wrapped_annotations.get(key, identity)(value) for key, value in full_kwargs.items()
            }
            return endware(func(**patched_kwargs))

        return wrapper

    def __call__(self):
        pass


def is_middleware(f):
    return isinstance(f, WrappedFunction)
