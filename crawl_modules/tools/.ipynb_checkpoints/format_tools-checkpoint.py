# tools.format_tools.py
import re


# Global regular expression compilation
xml_catch_re = re.compile('<.*?>')

def dict_list_to_string(arg_dict, sep=','):
    """
    Specifically made to create a parameter dictionary for the Youtube API
    Function that turns
    {'key' : [values]}
    into
    {'key' : 'value1,value2...'  }
    """
    return_dict = dict()
    for key, value in arg_dict.items():
        return_dict[key] = sep.join((map(str, value)))
    return return_dict

def nested_dict_to_dict(nested_dict):
    """
    Finds the value of the key in a nested dictionary.
    Does not unwrap values in list.
    """
    return_dict = dict()
    for key, value in recursive_items(nested_dict):
        return_dict[key] = value
    return return_dict
    
#https://stackoverflow.com/a/39234154
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)
            
def cherrypick_dict(dictionary, keys):
    """
    Receives dictionary and cherry picks key values.
    Returns dictionary with only keys in the keys list.
    """
    return_dict = dict()
    for key, value in dictionary.items():
        if key in keys:
            return_dict[key] = value
    return return_dict

def parse_xml_captions(string):
    """
    Takes all strings inside '<>'
    This allows separating only subtitles from
    xml based captions
    """
    global xml_catch_re
    return xml_catch_re.sub(r'', str(string))
    
    