from bs4 import BeautifulSoup
fp = open("books.html", encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

sel = lambda q: print(soup.select_one(q).string)
sel("#nu") # id로 찾는 방법
sel("li#nu") # id와 tag로 찾는 방법
sel("ul > li#nu") # 부모 tag로 id와 tag로 찾는 방법
sel("#bible #nu") # id로 아래의 id를 찾는 방법
sel("#bible > #nu") # id 끼리 부모자식 관계를 나타낸것
sel("ul#bible > li#nu") #
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)