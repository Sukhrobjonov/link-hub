import urllib.request
import re

req = urllib.request.Request('https://www.google.com/search?q=yatoro+face+dota+2+portrait&tbm=isch', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
urls = re.findall(r'src="(https://encrypted-tbn0\.gstatic\.com/images([^"]+))"', html)

if urls:
    print("https://encrypted-tbn0.gstatic.com/images" + urls[0][1])
else:
    print("Not found")
