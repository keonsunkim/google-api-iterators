import json

from google_map_api.api_modules import GooglePlaceTextSearchAPI
from iter_class.base_iterator import BaseIterator

from iter_class.google_map_api_condition_functions import next_page_token_checker,\
                                            google_map_api_result_list_empty_checker



class GoogleMapAPITextSearchIterator(BaseIterator):
    """
    An Iterator object to iterate through the API class module.
    With an API class instance attached to the iterator, we can iterate through
    search results with pagination.


    GoogleMapSearch = APISearchIterator(someAPIclass instance)
    Ex) for page in GoogleMapSearch: ...

    Before Every iteration, the iterator class sleeps for 4 seconds to abide by google's
    request rules!
    """

    cls_stop_condition_functions = [
                                    next_page_token_checker,
                                    google_map_api_result_list_empty_checker
                                    ]

    def __init__(self, SearchObject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._searchobject = SearchObject
        self._params = kwargs.get('params', None)


    def __iter__(self):
        return self

    def __next__(self):
        super().__next__()
        if self.index() == 1:
            print(self._params)
            return self._searchobject.search_with_params(params=self._params)
        return self._searchobject.search_with_params(
            params = {'pagetoken' : self._searchobject.return_data.get('next_page_token')}
        )
