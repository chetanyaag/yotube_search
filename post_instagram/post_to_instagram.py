import requests
import mysql.connector
import os
import time
instagram_id = "17841460279593500"
token = "EAACL2GIQVx4BO1QHLzZCPasga3ylZCoHLZC03VwHnbHIuRlncB7YGtdRyNOdYoRjot0pPWK8CyKezZAZAiZAbEhlBhJelqyDpDSY0GpRgHRZBHmoVTQxukITrqvZCxc0azn51RIa1y6GZCglUSaVUgV960a4bwC5olqiwOEngpTYcx98KhFTZAukthskx7ZCLt44EFK"
url = "https://graph.facebook.com/v17.0/{}/media?access_token={}".format(instagram_id, token)
g_url = "https://graph.facebook.com/v17.0/"

def post_video(video_url='',caption='',instagram_account_id='',access_token=''):
    url = g_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['video_url'] = video_url
    param['media_type'] = 'VIDEO'
    param['thumb_offset'] = '10'
    response = requests.post(url, params=param)
    response = response.json()
    print(response)
    return response


def publish_container(creation_id = '',instagram_account_id='',access_token=''):
    url = g_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    print(response)
    return response

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

    sql_query = "SELECT * FROM videos where is_downloaded_server=1 and is_uploaded_instagram=0"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    index = 0
    for result in results[:3]:
        index = index + 1
        if index >1:
            break
        try:
            video_url_s3 = r"https://instagram-video.s3.ap-south-1.amazonaws.com/" + result["youtube_video_id"]+".mp4"
            post_video_response = post_video(video_url_s3, result["title"], instagram_id, token)
            creation_id = post_video_response["id"]
            print(post_video_response)
            time.sleep(5)
            sql_query = "UPDATE videos SET instagram_container_id = "+str(creation_id)+" WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)
            post_container_response = publish_container(creation_id, instagram_id, token)
            print(post_container_response)
            instagram_published_id = post_container_response['id']
            sql_query = "UPDATE videos SET instagram_published_id = "+str(instagram_published_id)+" WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)
            sql_query = "UPDATE videos SET is_uploaded_instagram =1 WHERE id = "+ str(result['id'])
            cursor.execute(sql_query)
        except Exception as e:
            print(e)
    connection.commit()

except  Exception as e:
    print(e)