import urllib.request
import re

url = "https://html.duckduckgo.com/html/?q=yatoro+dota+2+face+close+up"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
matches = re.findall(r'src="(//external-content\.duckduckgo\.com/[^"]+)"', html)

if matches:
    # Just take the first image
    img_url = "https:" + matches[0]
    req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
    with open('static/yatoro.jpg', 'wb') as f:
        f.write(urllib.request.urlopen(req_img).read())
    print("Success")
else:
    print("No images found")
