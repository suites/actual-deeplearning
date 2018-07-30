import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import urllib.request

import os, re, json, random

# 마르코프 체인 딕셔너리 만들기
def make_dic(words):
    tmp = ['@']
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3:
            continue
        if len(tmp) > 3:
            tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == '.':
            tmp = ['@']
            continue
    return dic

# 딕셔너리에 데이터 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if w1 not in dic:
        dic[w1] = {}
    if w2 not in dic[w1]:
        dic[w1][w2] = {}
    if w3 not in dic[w1][w2]:
        dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

def make_sentence(dic):
    ret = []
    if '@' not in dic:
        return 'no dic'
    top = dic['@']
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == '.':
            break
        w1, w2 = w2, w3
    ret = ''.join(ret)

    params = urllib.parse.urlencode({
        '_callback': '',
        'q': ret
    })

    data = urllib.request.urlopen('https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?' + params)
    data = data.read().decode('utf-8')[1:-2]
    data = json.loads(data)
    data = data['message']['result']['html']
    data = soup = BeautifulSoup(data, 'html.parser').getText()

    return data


def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

toji_file = 'toji.txt'
dict_file = 'markov-toji.json'
if not os.path.exists(dict_file):
    fp = codecs.open('BEXX0003.txt', 'r', encoding='utf-16')
    soup = BeautifulSoup(fp, 'html.parser')
    body = soup.select_one('body > text')
    text = body.getText()
    text = text.replace('…', '')

    twitter = Twitter()
    malist = twitter.pos(text, norm=True)
    words = []
    for word in malist:
        if word[1] not in ['Punctuation']:
            words.append(word[0])
        if word[0] == '.':
            words.append(word[0])
    dic = make_dic(words)
    json.dump(dic, open(dict_file, 'w', encoding='utf-8'))
else:
    dic = json.load(open(dict_file, 'r'))

for i in range(3):
    s = make_sentence(dic)
    print(s)
    print('---')