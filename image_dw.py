import requests

image_url = "https://instagram.fdel1-4.fna.fbcdn.net/v/t51.2885-19/360036996_1414913875752953_7658540734379299855_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fdel1-4.fna.fbcdn.net&_nc_cat=105&_nc_ohc=YOGMgjRW_QcAX8Di1QT&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBCci15uCb6a7NDWFVv9F66AKvD5THskg9vzQehQL3Fcg&oe=64EED51A&_nc_sid=8b3546"
response = requests.get(image_url)

if response.status_code == 200:
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print("Failed to download image.")