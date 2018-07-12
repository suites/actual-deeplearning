import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

fp = codecs.open('BEXX0003.txt', 'r', encoding='utf-16')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text')
text = body.getText()

twitter = Twitter()
word_dic = {}
lines = text.split('\n')
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == 'Noun':
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print('{0}({1}) '.format(word, count), end='')
