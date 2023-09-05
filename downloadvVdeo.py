# AIzaSyCbM9s8tI1nF6_oA_CxB42EkQBHE4AbSKM


from googleapiclient.discovery import build
from pytube import YouTube as YT
# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey='AIzaSyD5bZRMzYLh8JoMp2wjDN2ODftSl_SFhB8')

# Search for YouTube Shorts
search_response = youtube.search().list(
    q='makan chor',
    type='video',
    videoDuration='short',
    order='relevance',
    part='snippet',
    maxResults=10
).execute()

vi_url = r"https://www.youtube.com/shorts/"


# Process the search results
for item in search_response['items']:
    try:
        url1 = vi_url + item['id']['videoId']
        video=YT(url1)
        strm = video.streams.get_by_resolution("720p")
    
        strm.download("videos")
    except Exception as e:
        print(e) 

