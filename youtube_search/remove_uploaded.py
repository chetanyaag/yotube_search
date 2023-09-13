import mysql.connector
import os

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

    sql_query = "SELECT * FROM videos where is_uploaded_s3=1 and is_deleted_server=0"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    file_path = os.path.join(os.getcwd() , "videos")

    for result in results:
        try:
            video_id = result["youtube_video_id"]
            file_name = video_id +".mp4"
            full_path = os.path.join(file_path, file_name)
            os.remove(full_path)
            sql_query = "UPDATE videos SET is_deleted_server=1 WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)
        except Exception as e:
            print(e)
        
            cursor.execute(sql_query)
    connection.commit()

except Exception as e:
    print(f"An error occurred: {str(e)}")