from instascrape import Reel, Profile
import requests
# create a Reel object using the reel's URL
reel = Reel("https://www.instagram.com/reel/CrOH69cAQdW/")
# 5764516643%3AwHACqmeGDwDU33%3A27%3AAYcC2cH9fOrM8bDXql_LXotK7HHyjA1kYQX39jc4Wg
# 5764516643:wHACqmeGDwDU33:27:AYcC2cH9fOrM8bDXql_LXotK7HHyjA1kYQX39jc4Wg
# initialize the Reel object with data

SESSIONID = "5764516643%3AwHACqmeGDwDU33%3A27%3AAYcC2cH9fOrM8bDXql_LXotK7HHyjA1kYQX39jc4Wg"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

reel.scrape(headers=headers)

# get the video URL
video_url = reel.video_url

# download the video using the video URL
# add desired file path and name to save the video
with open("filename.mp4", "wb") as file:
    response = requests.get(video_url)
    file.write(response.content)

