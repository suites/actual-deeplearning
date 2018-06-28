import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.grid_search import GridSearchCV

train_csv = pd.read_csv('./train.csv')
test_csv = pd.read_csv('./t10k.csv')

train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:577]
test_label = train_csv.ix[:, 0]
test_data = train_csv.ix[:, 1:577]
print('학습 데이터의 수 =', len(train_label))

params = [
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma':[0.001, 0.0001]}
]

clf = GridSearchCV(svm.SVC(), params, n_jobs=-1)
clf.fit(train_data, train_label)
print('학습기 =', clf.best_estimator_)

pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print('정답률 =', ac_score)
