import urllib.request
import re
import os

req = urllib.request.Request('https://liquipedia.net/dota2/Yatoro', headers={'User-Agent': 'curl/7.64.1', 'Referer': 'https://liquipedia.net/'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Look for the Infobox main image
    match = re.search(r'src="(/commons/images/thumb/[^"]+/(?:[0-9]+px-)?[^"]+Yatoro[^"]*\.jpg)"', html, re.IGNORECASE)
    if match:
        img_url = "https://liquipedia.net" + match.group(1).replace('&amp;', '&')
        print("Found:", img_url)
        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'curl/7.64.1', 'Referer': 'https://liquipedia.net/dota2/Yatoro'})
        data = urllib.request.urlopen(img_req).read()
        with open('static/yatoro.jpg', 'wb') as f:
            f.write(data)
        print("Saved size:", len(data))
    else:
        print("Regex match failed")
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        imgs = [img['src'] for img in soup.find_all('img') if 'Yatoro' in img.get('src','')]
        print("Possible images:", imgs)
except Exception as e:
    print(e)
