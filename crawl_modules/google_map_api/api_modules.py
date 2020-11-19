#google_map_api.api_modules.py

import json
import requests

class GooglePlaceAPIBase:

    def __init__(self, APIKey, *args, **kwargs):
        self._apikey = APIKey
        self.return_data = None

    @classmethod
    def validate_parameters(cls, params):
        """
        A pre-checking function to validate whether parameters meet the
        requirements of google place API

        Since each API has different rules, this classmethod only checks required parameters.
        It will return the number of unchecked required parameters.
        Additional exception rule checking can be carried out in respective child model class methods.
        """
        required_params_num = len(cls.required_parameters)

        for key, value in params.items():
            if key in cls.required_parameters:
                required_params_num -= 1
            elif key in cls.legitimate_parameters:
                pass
            else:
                raise ValueError(f'Your parameter key : {key} is not valid')

        return required_params_num


class GoogleFindPlaceSearchAPI(GooglePlaceAPIBase):

    required_parameters = ('input', 'inputtype')
    legitimate_parameters = ('language', 'fields', 'locationbias')

    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    def __init__(self, APIKey, *args, **kwargs):
        super().__init__(APIKey, args, kwargs)

    def search_with_params(self, params, *args, **kwargs):

        #add APIKey in kwarg parameters!
        params.update({'key' : self._apikey})
        self.return_data = requests.get(self.url, params=params).json()
        return self.return_data


class GooglePlaceTextSearchAPI(GooglePlaceAPIBase):

    required_parameters = ('query', )
    legitimate_parameters = ('region', 'location', 'radius', 'language',
                             'minprice', 'maxprice', 'opennow', 'pagetoken',
                             'types')
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


    def __init__(self, APIKey, *args, **kwargs):
        super().__init__(APIKey, args, kwargs)

    @classmethod
    def validate_paramters(cls, params):
        required_params_num = super().validate_parameters(params)

        # check for winning parameters that allow API use!
        # such as query and types, page_token...
        if required_params_num > 0:
            if 'pagetoken' in params:
                pass
            else:
                raise ValueError('Are you trying to use "page_token" in your parameters? Some parameter is missing')

    def search_with_params(self, params, *args, **kwargs):
        #validate parameters first!
        self.validate_parameters(params)

        #add APIKey!
        params.update({'key' : self._apikey})
        self.return_data = requests.get(self.url, params=params).json()
        return self.return_data
