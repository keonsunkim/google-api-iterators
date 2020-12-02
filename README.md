# google-api-iterators
Easy data retreiver from multiple sources for gathering data.
Currently this package allows gathering following data.
* Google Map API
  * Place Text Search
  * Find Place Search
* Youtube
  * Youtube Comments 
  * Youtube Transcript
  * Youtube Video and Audio Files
  
## Google Map API
You can use it to retrieve and save google map data like the following code.

```python
from crawl_modules import GooglePlaceTextSearchAPI

API = 'Your API Key'
my_search = GooglePlaceTextSearchAPI(API)
return_data = my_search.search_with_params(set_sleeep_time = {'min': 1000, 'max : 2000}
                             params = {'query' : 'HaengDang-Dong', 'types' : 'restaurant}
                              )
```

  If you want to iterate through paginations, following code can serve as an example
  
```python
from crawl_modules import GooglePlaceTextSearchAPI
from google_api_iterator import GoogleMapAPITextSearchIterator

API = 'Your API Key'
my_search = GooglePlaceTextSearchAPI(API)

my_iterator = GoogleMapAPITextSearchIterator(
    my_search,
    set_sleep_time = {'min':1000, 'max':4000},
    params = {'query':'행당동', 'types':'restaurant'},
)

for result_page in my_iterator:
    print(result_page)
    # Additional code to save it in a separate file.

```
 
## Youtube Data
Retreiving youtube comments is similar to retreiving google map data.
Following code will return comments in the first page and save it in a file named ' test_youtube.csv'.
Also, if there is a file already named 'test_youtube.csv' it will automatically append data to the 
existing file.

```python
from crawl_modules import YoutubeAPICommentRetriever

youtube = YoutubeAPICommentRetriever(
                                     APIKey = API, 
                                     csv_file_directory = 'test_youtube.csv', 
                                     header = ['authorDisplayName', 'textDisplay', 'videoId', 'id', 'publishedAt', 'updatedAt'],
                                     )
return_data = youtube.search_with_params(set_sleep_time = {'min' : 1000, 'max' : 2000},
                                         params = {
                                          'part' : ['id', 'snippet', 'replies'],
                                          'videoId' : ['gIvxA9Y5iIY'],
                                          'maxResults' : [20],
                                          'textFormat' : ['plainText']
                                                  }
                                          )
```

Just like an easy made iterator used to retreive google map data, you can use the iterator.

```python
from crawl_modules import YoutubeAPICommentRetriever
from crawl_modules import YoutubeAPICommentIterator

youtube = YoutubeAPICommentRetriever(
                                     APIKey = API, 
                                     csv_file_directory = 'test_youtube.csv', 
                                     header = ['authorDisplayName', 'textDisplay', 'videoId', 'id', 'publishedAt', 'updatedAt'],
                                     )
                                     
youtube_iterator = YoutubeAPICommentIterator(youtube, 
                                           set_sleep_time = {'min':1000, 'max':2000},
                                           params = {
                                            'part' : ['id', 'snippet', 'replies'],
                                            'videoId' : ['gIvxA9Y5iIY'],
                                            'maxResults' : [20],
                                            'textFormat' : ['plainText']
                                            }
                                            )
                                            
for result in youtube_iterator:
  print(result)
  # unlike google map iterator, the iterator automatically saves data to the csv file.
```

