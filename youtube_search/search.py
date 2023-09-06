from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey='AIzaSyD5bZRMzYLh8JoMp2wjDN2ODftSl_SFhB8')

keyword_to_search = 'makan chor'

search_response = youtube.search().list(
    q=keyword_to_search,
    type='video',
    videoDuration='short',
    order='relevance',
    part='snippet',
    maxResults=10
).execute()