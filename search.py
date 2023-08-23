from pytube import YouTube as YT

vi = "https://www.youtube.com/shorts/Tta37KkWmUM"

video=YT(vi)
path_vid = "videos"
strm = video.streams.get_by_resolution("720p")
strm.download(path_vid)















# # from pytube import Search
# from pytube import YouTube



# # s= Search("kanha")

# # b = 0
# # for a  in s.results :
# #     stream = a.streams.get_highest_resolution()    
# #     path = 'video/video'+ str(b)+ ".mp4"
# #     stream.download(path)
# #     b = b + 1




# video_url = "https://www.youtube.com/watch?v=ERDypoAmLM8"
# yt = YouTube(video_url)
# # yt.streams.
# video = yt.streams.first()
# stream = yt.streams.get_highest_resolution()
# output_path = "videos/video.mp4"
# print(yt.bypass_age_gate)
# stream.download()
# video.download()