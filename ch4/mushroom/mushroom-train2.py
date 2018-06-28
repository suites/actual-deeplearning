import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv('mushroom.csv', header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {'dic': {}, 'cnt': 0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]

        d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if v in attr['dic']:
            idx = attr['dic'][v]
        else:
            idx = attr['cnt']
            attr['dic'][v] = idx
            attr['cnt'] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print('정확도 =', ac_score)
print('리포트 =\n', cl_report)
