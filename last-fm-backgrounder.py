import sys
import requests
import json
from PIL import Image
from io import BytesIO
import os
import subprocess

#Read args
username = sys.argv[1]

api_key = sys.argv[2]
#build the URL from the username

lastfm = requests.get("http://ws.audioscrobbler.com/" +
        "2.0/?method=user.getrecenttracks&user=" + username +
        "&api_key=" + api_key + "&format=json")
info = lastfm.json()
#parse the json
imageUrl = info["recenttracks"]["track"][0]["image"][3]["#text"]

#Query for the picture
picture = requests.get(imageUrl)
try:
    image = Image.open(BytesIO(picture.content))
except IOError:
    exit()
#Save the picture locally and set it as background
image.save('image.png',image.format);
path = os.getcwd() + r'/image.png'
subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri","file://"+path])
