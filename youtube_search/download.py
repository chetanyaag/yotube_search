from pytube import YouTube as YT

video_id = "8ERbrByKLBk"
vi_url = r"https://www.youtube.com/shorts/"
video_url = vi_url + video_id

try:
    print(video_url)
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
