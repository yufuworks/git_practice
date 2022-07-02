import urllib.request

response = urllib.request.urlopen('http://192.168.1.12/blog/wp-admin')

data = response.read()

print(data)