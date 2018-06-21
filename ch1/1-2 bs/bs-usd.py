from bs4 import BeautifulSoup
import urllib.request as req

url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

usd_price = soup.select_one("a.head.usd > div > span.value").string
jpy_price = soup.select_one("a.head.jpy > div > span.value").string

print('usd/krw=', usd_price)
print('jpy/krw=', jpy_price)
