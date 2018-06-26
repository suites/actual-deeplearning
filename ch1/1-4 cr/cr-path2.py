from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print(urljoin(base, "/hoge.html"))
print(urljoin(base, "http://otherExample.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))