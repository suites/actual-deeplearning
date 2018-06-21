import urllib.request as request
import urllib.parse as parse
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stdId': '109'
}
params = parse.urlencode(values)

url = API + "?" + params
print('url=', url)

data = request.urlopen(url).read()
text = data.decode('utf-8')
print(text)