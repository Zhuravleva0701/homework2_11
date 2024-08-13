import inspect
from pprint import pprint


def introspection_info(obj):
    result = {'type': type(obj).__name__, 'attributes': [], 'methods': [], 'module': inspect.getmodule(obj)}
    for i in dir(obj):
        if callable(getattr(obj, i)):
            result['methods'].append(i)
        else:
            result['attributes'].append(i)

    return result


number_info = introspection_info(42)
print(number_info)