import os

import json
import requests

import googleapiclient.discovery

class YoutubeAPIV3Base:

    def __init__(self, APIKey, *args, **kwargs):

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "YOUR_API_KEY"


        self._apikey = APIKey
        self.return_data = None

    @classmethod
    def validate_parameters(cls, params):
        """
        A pre-checking function to validate whether parameters meet the
        requirements of Youtube V3 API

        Since each API has different rules, this classmethod only checks required parameters.
        It will return the number of unchecked required parameters.
        Additional exception rule checking can be carried out in respective child model class methods.
        """
        required_params_num = len(cls.required_parameters)

        for key, value in params.items():
            if key in cls.required_parameters:
                required_params_num == 1
            elif key in cls.legitimate_parameters:
                pass
            else:
                raise ValueError(f'Yout parameter key : {key} is not valid')

        return required_params_num

class YoutubeAPICommentRetriever(YoutubeAPIV3Base):

    url = "https://www.googleapis.com/youtube/v3/commentThreads"

    def __init__(self, *args, **kwargs):
        self._

    @classmethod
    def validate_paramters(csl, params):
