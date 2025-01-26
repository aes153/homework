from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    module = getattr(obj, "__module__", None)
    additional_properties = {}

    info = {
        "attributes": attributes,
        "methods": methods,
        "module": module,
        "additional_properties": additional_properties,
        "type": obj_type
    }

    return info


string_info = introspection_info('Hello')
pprint(string_info)

number_info = introspection_info(123)
pprint(number_info)