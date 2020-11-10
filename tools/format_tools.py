# tools.format_tools.py

def dict_list_to_string(arg_dict, sep=','):
    """
    Specifically made to create a parameter dictionary for the Youtube API
    Function that turns
    {'key' : [values]}
    into
    {'key' : 'value1,value2...'  }
    """
    for key, value in arg_dict.items():
        arg_dict[key] = sep.join((map(str, value)))
    return arg_dict
