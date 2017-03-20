import sys
import requests
import json
from PIL import Image
from io import BytesIO
import os
import subprocess
import datetime
#Read args
username = sys.argv[1]

api_key = sys.argv[2]
#build the URL from the username
print(datetime.datetime.now().time())
print("username:" + username)
print("api_key: " + api_key)
print("Try and get that url thing")
lastfm = requests.get("http://ws.audioscrobbler.com/" +
        "2.0/?method=user.getrecenttracks&user=" + username +
        "&api_key=" + api_key + "&format=json")
print("lastfm response is: " + str(lastfm.status_code))
info = lastfm.json()
#parse the json
imageUrl = info["recenttracks"]["track"][0]["image"][3]["#text"]
print("Image url: " + imageUrl)
#Query for the picture
picture = requests.get(imageUrl)
try:
    image = Image.open(BytesIO(picture.content))
except IOError:
    print("Could not parse the url")
    exit()
#Save the picture locally and set it as background
try:
    image.save('/home/tpanetti/.logs/image.png',image.format);
except IOError:
    print("Could not save file")
    exit()
subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri","file:///home/tpanetti/.logs/image.png"])
print("looks like everything was sucessful")
