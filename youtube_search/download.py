from pytube import YouTube as YT
import mysql.connector
video_id = "8ERbrByKLBk"
vi_url = r"https://www.youtube.com/shorts/"


try:
    connection = mysql.connector.connect(
        host='127.0.0.1', 
        user='chetanya',
        password='password',
        port=3306
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor(dictionary=True)

    new_database = "botverse"
    cursor.execute(f"USE {new_database}")

    sql_query = "SELECT * FROM videos where is_downloaded_server=0"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for result in results:
        video_id = result["youtube_video_id"]
        video_url = vi_url + video_id
        yt_video = YT(video_url)
        duration_seconds = yt_video.length
        file_name = video_id +".mp4"

        if duration_seconds > 90:
            # raise Exception('large video duration')
            continue

    
        strm = yt_video.streams.get_by_resolution("720p")

        # strm.download("videos")
        strm.download("videos", file_name)

except Exception as e:
    print(f"An error occurred: {str(e)}")
