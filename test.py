from youtube_api.api_modules import YoutubeAPICommentRetriever

API = 'Your API Key'

youtube = YoutubeAPICommentRetriever(API)

youtube.search_with_params(
    params = {
    'part' : ['id', 'replies'],
    'videoId' : ['AidknPJdu3I'],
    'maxResults' : [5],
    'textFormat' : ['plainText']
    }
)
