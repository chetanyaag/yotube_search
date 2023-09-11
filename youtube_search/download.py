from pytube import YouTube as YT
import mysql.connector
video_id = "8ERbrByKLBk"
vi_url = r"https://www.youtube.com/shorts/"
video_url = vi_url + video_id

try:
    connection = mysql.connector.connect(
        host='127.0.0.1', 
        user='chetanya',
        password='password',
        port=3306
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor()

    new_database = "botverse"
    cursor.execute(f"USE {new_database}")

    sql_query = "SELECT * FROM videos where is_downloaded_server=0"
    result = cursor.execute(sql_query)
    results = result.fetchall()

    yt_video = YT(video_url)
    duration_seconds = yt_video.length
    print(duration_seconds)
    #check if video's duration is larger than 90 sec
    # if duration_seconds > 90:
    #     raise Exception('large video duration')
    
    #check if video already downloaded
    # if "condition" :
    #     raise Exception('Video already downloaded')
    
    strm = yt_video.streams.get_by_resolution("720p")

    strm.download("videos")
    # strm.download("videos", "filename")

except Exception as e:
    print(f"An error occurred: {str(e)}")
