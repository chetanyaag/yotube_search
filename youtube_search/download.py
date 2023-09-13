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

    sql_query = "SELECT * FROM videos where is_downloaded_server=0 and garbage is null"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for result in results:
        try:
            video_id = result["youtube_video_id"]
            video_url = vi_url + video_id
            yt_video = YT(video_url)
            duration_seconds = yt_video.length
            file_name = video_id +".mp4"

            if duration_seconds > 90:
                raise Exception('large video duration')
                
            strm = yt_video.streams.get_by_resolution("720p")

            # strm.download("videos")
            strm.download("videos", file_name)

            sql_query = "UPDATE videos SET is_downloaded_server = 1 WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)
        except Exception as e:
            print(e)
            sql_query = "UPDATE videos SET garbage = '"+ str(e).replace("'", '') +"' WHERE id = "+ str(result['id'])
            print(sql_query)
            cursor.execute(sql_query)
    connection.commit()

except Exception as e:
    print(f"An error occurred: {str(e)}")
