import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp = codecs.open('BEXX0003.txt', 'r', encoding='utf-16')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text')
text = body.getText()

twiter = Twitter()
results = []
lines = text.split('\n')
for line in lines:
    malist = twiter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ['josa', 'Eomi', 'Punctuation']:
            r.append(word[0])
    rl = (' '.join(r)).strip()
    results.append(rl)
    print(rl)

wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('toji.model')
print('ok')
