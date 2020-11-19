# os import
import os

# standard library imports
import json

# third party imports
import requests
import googleapiclient.discovery

# local imports
from mixins import CSVSaveMixin

from .validator_functions import validate_youtube_api_parameters
from .parser import youtube_comment_data_parser
from tools import dict_list_to_string

class YoutubeAPIBase:
    """
    Base Youtube API class only made to be extended through inheritance.
    """
    api_service_name = "youtube"


    def __init__(self, APIKey, version = 'v3', *args, **kwargs):

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
        self._apikey = APIKey
        self.searchobject = googleapiclient.discovery.build(
                            self.api_service_name,
                            version,
                            developerKey = self._apikey)
        self.api_version = version
        self.return_data = None
        
        super(YoutubeAPIBase, self).__init__(*args, **kwargs)


    @classmethod
    def validate_parameters(cls, params):
        """
        A pre-checking function to validate whether parameters meet the
        requirements of Youtube V3 API
        Functions made in validator_functions module.
        """
        validate_youtube_api_parameters(cls, params)

class YoutubeAPICommentRetriever(YoutubeAPIBase, CSVSaveMixin):
    """
    A class to make easy of youtube comment retrieval.

    Parameters are set from the rules given in the below website.
    "https://developers.google.com/youtube/v3/docs/commentThreads/
    list?apix_params=%7B%22part%22%3A%5B%22id%22%2C%22snippet%22%5D%7D"
    """

    required_parameters = {
        'part' : {'required_type' : str, 'values' : ['id', 'replies', 'snippet']},
    }
    filter_parameters = {
        'allThreadRelatedToChannelId' : {'required_type' : str},
        'channelId' : {'required_type' : str},
        'id' : {'required_type' : str},
        'videoId' : {'required_type' : str}
    }
    optional_parameters = {
        'maxResults' : {
                        'required_type' : int,
                        'values' : [i for i in range(1, 101)]
                        },
        'moderationStatus' : {
                              'required_type' : str,
                              'values' : ['heldForReview, likelySpam', 'published']
                              },
        'order' : {'required_type' : str, 'values' : ['time', 'relevance']},
        'pageToken' : {'required_type' : str},
        'textFormat' : {'required_type' : str, 'values' : ['html', 'plainText']}
    }
    
    _parser_function = youtube_comment_data_parser


    def __init__(self, APIKey, *args, **kwargs):
        
        print(kwargs)
        super(YoutubeAPICommentRetriever, self).__init__(APIKey, *args, **kwargs)


    def search_with_params(self, params, *args, **kwargs):
        """
        Search function that accepts parameters. However parameters must be in
        following syntax
        { 'parameter name' : [values], ... }
        """
        #validate parameters
        self.validate_parameters(params)

        request = self.searchobject.commentThreads().list(
            **dict_list_to_string(params)
        )
        self.return_data = request.execute()
        self.save()
        return self.return_data
    
    def check(self):
        print(self.header)