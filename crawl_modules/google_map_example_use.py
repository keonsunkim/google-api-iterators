from google_map_api.api_modules import GooglePlaceTextSearchAPI

from google_api_iterator import GoogleMapAPITextSearchIterator



if __name__ == "__main__":
    API = 'Your API Key'
    my_search = GooglePlaceTextSearchAPI(API)

    my_iterator = GoogleMapAPITextSearchIterator(
        my_search,
        set_sleep_time = {'min':1000, 'max':4000},
        params = {'query':'행당동', 'types':'restaurant'},
    )

    num = 0

    for result_page in my_iterator:
        num += 1
        print(num)
        print(result_page)
