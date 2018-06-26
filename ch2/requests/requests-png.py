import requests
r = requests.get("http://wikibook.co.kr/wikibook.png")

with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")