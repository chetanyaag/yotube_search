
# TASK 1 -> MAKE A GET REQUEST

import requests

instagram_id = "17841460279593500"
token = "EAACL2GIQVx4BO1QHLzZCPasga3ylZCoHLZC03VwHnbHIuRlncB7YGtdRyNOdYoRjot0pPWK8CyKezZAZAiZAbEhlBhJelqyDpDSY0GpRgHRZBHmoVTQxukITrqvZCxc0azn51RIa1y6GZCglUSaVUgV960a4bwC5olqiwOEngpTYcx98KhFTZAukthskx7ZCLt44EFK"

url = "https://graph.facebook.com/v17.0/{}/media?access_token={}".format(instagram_id, token)
g_url = "https://graph.facebook.com/v17.0/"
# r = requests.get(url)

# print(r.json())

def post_image(caption='', image_url='',instagram_account_id='',access_token=''):
    url = g_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['image_url'] = image_url
    response = requests.post(url, params=param)
    response = response.json()
    print(response)
    return response

# nw_res =   post_image("testgraph", "image.jpg", instagram_id, token)
# cretae_id = nw_res["id"]

def publish_container(creation_id = '',instagram_account_id='',access_token=''):
    url = g_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    print(response)
    return response

# publish_container(cretae_id, instagram_id, token)

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

# nw_res = post_video('https://instagram-video.s3.ap-south-1.amazonaws.com/image1.mp4', "लड्डू गोपाल घर में हैं तो 5 नियम ध्यान रखें  Laddu gopal ki puja karne ke fayde sanyasidham laddu", instagram_id, token)
# create_id = nw_res["id"]

def publish_container(creation_id = '',instagram_account_id='',access_token=''):
    url = g_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    print(response)
    return response

publish_container("18098763121345491", instagram_id, token)