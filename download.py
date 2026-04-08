import os
import urllib.request

os.makedirs('static', exist_ok=True)
url = "https://liquipedia.net/commons/images/thumb/4/4b/Yatoro_2025_Team_Spirit.jpg/600px-Yatoro_2025_Team_Spirit.jpg"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://liquipedia.net/'
})
with open('static/yatoro.jpg', 'wb') as f:
    f.write(urllib.request.urlopen(req).read())
print("Downloaded")
