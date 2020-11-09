import os

import json
import requests

import googleapiclient.discovery

from validator_functions import validate_parameters

class YoutubeAPIV3Base:

    api_service_name = "youtube"
    api_version = "v3"

    def __init__(self, APIKey, *args, **kwargs):

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self._apikey = APIKey
        self.searchobject = googleapiclient.discovery.build(
                            self.api_service_name,
                            self.api_version,
                            developerKey = self._apikey)
        self.return_data = None

    @classmethod
    def _validate_parameters(cls, params):
        """
        A pre-checking function to validate whether parameters meet the
        requirements of Youtube V3 API
        Functions made in validator_functions module.
        """
        validate_parameters(cls, params)

class YoutubeAPICommentRetriever(YoutubeAPIV3Base):
    """


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


    def __init__(self, APIKey, *args, **kwargs):
        super().__init__(APIKey, *args, **kwargs)


    def search_with_params(self, params, *args, **kwargs):
        #validate parameters
        self.validate_paramters(params)
        """
        Need to work here!
        """
        request = youtube.commentThreads().list()
        response = request.execute()
