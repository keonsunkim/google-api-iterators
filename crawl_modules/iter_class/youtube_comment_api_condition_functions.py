# iter_class.youtube_comment_api_condition_functions.py

# global imports
import json

def youtube_comment_api_result_list_empty_checker(iterator_instance):
    """
    If there is nothing in the results
    """
    if iterator_instance.index() == 0:
        pass
    elif not iterator_instance._searchobject.return_data.get('items', None):
        raise StopIteration


def youtube_api_next_page_token_checker(iterator_instance):
    """
    Stop iteration if there is no next_page_token!
    Let it flow when index is set at 0, since there is no data
    returned yet from the API!
    """
    if iterator_instance.index() == 0:
        pass
    elif iterator_instance._searchobject.return_data.get(
            'nextPageToken', None) == None:
        raise StopIteration
    else:
        pass
