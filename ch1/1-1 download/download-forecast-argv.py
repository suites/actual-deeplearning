import sys
import urllib.request as request
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-arvg <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stdId': regionNumber
}
params = parse.urlencode(values)

url = API + "?" + params
print('url=', url)

data = request.urlopen(url).read()
text = data.decode('utf-8')
print(text)