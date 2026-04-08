import urllib.request
import re

try:
    req = urllib.request.Request('https://liquipedia.net/dota2/Yatoro', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'src="(/commons/images/thumb/[^"]+Yatoro[^"]+/\d+px-[^"]+\.jpg)"', html)
    if matches:
        print("https://liquipedia.net" + matches[0])
    else:
        print("Not found")
except Exception as e:
    print(e)
