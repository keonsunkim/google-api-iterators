# iter_class.google_map_api_condition_functions.py

# global imports
import json

def google_map_api_result_list_empty_checker(iterator_instance):
    """
    If there is nothing in the results
    """
    if iterator_instance.index() == 0:
        pass
    elif not iterator_instance._searchobject.return_data.get('results', None):
        raise StopIteration


def google_map_api_next_page_token_checker(iterator_instance):
    """
    Stop iteration if there is no next_page_token!
    Let it flow when index is set at 0, since there is no data
    returned yet from the API!
    """
    if iterator_instance.index() == 0:
        pass
    elif iterator_instance._searchobject.return_data.get(
            'next_page_token', None) == None:
        raise StopIteration
    else:
        pass
