from googleapiclient.discovery import build
# https://developers.google.com/youtube/v3/docs/search
youtube = build('youtube', 'v3', developerKey='AIzaSyD5bZRMzYLh8JoMp2wjDN2ODftSl_SFhB8')

keyword_to_search = 'makan chor'

search_response = youtube.search().list(
    q=keyword_to_search,
    type='video',
    videoDuration='short',
    order='relevance',
    part='snippet',
    maxResults=1
).execute()


################################
#TODO save this data in database make download flag to 0

for i in search_response['items']:
    print(i, end="\n\n") 