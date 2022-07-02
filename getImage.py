from email.mime import image
import urllib.request

url = "https://lh3.googleusercontent.com/a-/AOh14GgNyxdm1H_9Xtw1tjGoYCBbPUvrklLwuo6dtyv6=s96-c"
imagefile = "icon.jpg"

urllib.request.urlretrieve(url, imagefile)

print("File saved")
