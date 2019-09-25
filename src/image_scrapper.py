import requests
print(requests.get("https://www.google.com/search?q=messier+M2&tbm=isch&sa=X&biw=1920&bih=888").content.decode("latin-1"))
