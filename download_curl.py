import urllib.request
url = 'https://liquipedia.net/commons/images/thumb/0/07/Yatoro_TI10.jpg/600px-Yatoro_TI10.jpg'
req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.64.1', 'Referer': 'https://liquipedia.net/'})
data = urllib.request.urlopen(req).read()
if len(data) > 5000:
    with open('static/yatoro.jpg', 'wb') as f:
        f.write(data)
    print('Downloaded correctly!')
else:
    print('Failed length check, length:', len(data))
