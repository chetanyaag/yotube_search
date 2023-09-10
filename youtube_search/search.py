from googleapiclient.discovery import build
import mysql.connector
import json

try:
    connection = mysql.connector.connect(
            host='127.0.0.1', 
            user='chetanya',
            password='password',
            port=3306
        )
    
    if connection.is_connected()==False:
        raise ValueError("not connected")

    cursor = connection.cursor()
    youtube = build('youtube', 'v3', developerKey='AIzaSyD5bZRMzYLh8JoMp2wjDN2ODftSl_SFhB8')

    keyword_to_search = 'makan chor'

    search_response = youtube.search().list(
        q=keyword_to_search,
        type='video',
        videoDuration='short',
        order='relevance',
        part='snippet',
        maxResults=5
    ).execute()


    for i in search_response['items']:
        video_title = i["snippet"]["title"]
        video_id = i["id"]["videoId"]
        json_text = json.dumps(i)
        sql_query = "INSERT INTO videos (title, youtube_video_id, youtube_raw_response) VALUES (?, ?, ?);"
        # Execute the query with the provided values
        cursor.execute(sql_query, (video_title, video_id, json_text))

    connection.commit()
except Exception as e:
    print(e)







# https://developers.google.com/youtube/v3/docs/search
# youtube = build('youtube', 'v3', developerKey='AIzaSyD5bZRMzYLh8JoMp2wjDN2ODftSl_SFhB8')

# keyword_to_search = 'makan chor'

# search_response = youtube.search().list(
#     q=keyword_to_search,
#     type='video',
#     videoDuration='short',
#     order='relevance',
#     part='snippet',
#     maxResults=1
# ).execute()


# ################################
# #TODO save this data in database make download flag to 0

# for i in search_response['items']:
#     print(i, end="\n\n") 