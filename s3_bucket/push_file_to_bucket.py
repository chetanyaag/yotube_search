import boto3
import mysql.connector
import os
try:
    s3 = boto3.client('s3', aws_access_key_id='AKIARG3UQKCMZAXUXG76', aws_secret_access_key='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', region_name='us-west-1')

    # Upload the image to a specific bucket
    bucket_name = 'instagram-video'

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

    sql_query = "SELECT * FROM videos where is_downloaded_server=1 and is_uploaded_s3=0"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    video_folder = '/home/ubuntu/youtube/yotube_search/youtube_search/videos'
    for result in results:
        try:
            video_id = result["youtube_video_id"]
            file_name = file_name = video_id +".mp4"
            file_path = os.path.join(video_folder, file_name)
            s3.upload_file(file_path, bucket_name, file_name)
            sql_query = "UPDATE videos SET is_uploaded_s3 = 1 WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)

        except Exception as e:
            print(e)
    connection.commit()
   
    # file_path = r'videos/Krishna Makhan Chor Song Cover  THE 9TEEN shorts.mp4'
    
except Exception as e:

    print(e)

# bucket_url = f"https://{bucket_name}.s3.amazonaws.com/"
# image_url = f"{bucket_url}image.jpg"