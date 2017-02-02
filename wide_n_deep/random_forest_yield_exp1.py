#!/usr/bin/python
# -*- coding: big5 -*-
# coding=Big5

# Feature Importance
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv("view_parameters_yield_mapping.csv", header=0, encoding = 'big5')
data.columns = ["�h�O�W��","�ƪO��","�̤p�u�|","�̤p�u�Z","�X�f���n",
                "��������","�����覡","�����t��","�������x","�n�����x",
                "E1�t�O","E1�u�O","�e�B�z","����","���}�v2"]
data["�̤p�u�|"].fillna(data["�̤p�u�|"].mean(), inplace=True)
data["�̤p�u�Z"].fillna(data["�̤p�u�Z"].mean(), inplace=True)
data["�X�f���n"].fillna(data["�X�f���n"].mean(), inplace=True)
data["�����t��"].fillna(data["�����t��"].mean(), inplace=True)
data.fillna("NAN")
feat_labels = data.columns[0:-1]

# Encode data columns
from sklearn.preprocessing import LabelEncoder
class_le1 = LabelEncoder()
class_le2 = LabelEncoder()
class_le3 = LabelEncoder()
class_le4 = LabelEncoder()
class_le5 = LabelEncoder()
class_le6 = LabelEncoder()
class_le7 = LabelEncoder()
class_le8 = LabelEncoder()
class_le9 = LabelEncoder()
class_le10 = LabelEncoder()
data["�h�O�W��"] = class_le1.fit_transform(data["�h�O�W��"])
data["�ƪO��"] = class_le2.fit_transform(data["�ƪO��"])
data["��������"] = class_le3.fit_transform(data["��������"])
data["�����覡"] = class_le4.fit_transform(data["�����覡"])
data["�������x"] = class_le5.fit_transform(data["�������x"])
data["�n�����x"] = class_le6.fit_transform(data["�n�����x"])
data["E1�t�O"] = class_le7.fit_transform(data["E1�t�O"])
data["E1�u�O"] = class_le8.fit_transform(data["E1�u�O"])
data["�e�B�z"] = class_le9.fit_transform(data["�e�B�z"])
data["����"] = class_le10.fit_transform(data["����"])

# Split trining data and testing data
X = data.iloc[:, 0:14]
y = data.iloc[:, 14:15]

from sklearn.model_selection import train_test_split
trX, teX, trY, teY = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Assessing Feature Importances with Random Forests
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=10000,
                                random_state=0,
                                n_jobs=-1)
forest.fit(trX, trY)
importances = forest.feature_importances_

indices = np.argsort(importances)[::-1]

for f in range(trX.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, 
                            feat_labels[indices[f]], 
                            importances[indices[f]]))

plt.title('Feature Importances')
plt.bar(range(trX.shape[1]), 
        importances[indices],
        color='lightblue', 
        align='center')

plt.xticks(range(trX.shape[1]), 
           feat_labels[indices], rotation=90)
plt.xlim([-1, trX.shape[1]])
plt.tight_layout()
#plt.savefig('./random_forest.png', dpi=300)
plt.show()



######### Part II #########
# -*- coding: big5 -*-
# coding=Big5
import numpy as np
import pandas as pd
# Import data
data = pd.read_csv("view_parameters_yield_mapping3.csv", header=0, encoding = 'big5')
data.columns = ["�h�O�W��","�ƪO��","�̤p�u�|","�̤p�u�Z","�X�f���n",
                "��������","�����覡","�����t��","�������x","�n�����x",
                "E1�t�O","E1�u�O","�e�B�z","����","���}�v2"]
data["�̤p�u�|"].fillna(data["�̤p�u�|"].mean(), inplace=True)
data["�̤p�u�Z"].fillna(data["�̤p�u�Z"].mean(), inplace=True)
data["�X�f���n"].fillna(data["�X�f���n"].mean(), inplace=True)
data["�����t��"].fillna(data["�����t��"].mean(), inplace=True)
#data["����"] = 'str' + data["����"].astype(str)
#data["�e�B�z"] = 'str' + data["�e�B�z"].astype(str)
data.fillna("NAN")
feat_labels = data.columns[0:-1]
# Encode data columns
from sklearn.preprocessing import LabelEncoder
class_le1 = LabelEncoder()
class_le2 = LabelEncoder()
class_le3 = LabelEncoder()
class_le4 = LabelEncoder()
class_le5 = LabelEncoder()
class_le6 = LabelEncoder()
class_le7 = LabelEncoder()
class_le8 = LabelEncoder()
class_le9 = LabelEncoder()
class_le10 = LabelEncoder()
data["�h�O�W��"] = class_le1.fit_transform(data["�h�O�W��"])
data["�ƪO��"] = class_le2.fit_transform(data["�ƪO��"])
data["��������"] = class_le3.fit_transform(data["��������"])
data["�����覡"] = class_le4.fit_transform(data["�����覡"])
data["�������x"] = class_le5.fit_transform(data["�������x"])
data["�n�����x"] = class_le6.fit_transform(data["�n�����x"])
data["E1�t�O"] = class_le7.fit_transform(data["E1�t�O"])
data["E1�u�O"] = class_le8.fit_transform(data["E1�u�O"])
data["�e�B�z"] = class_le9.fit_transform(data["�e�B�z"])
data["����"] = class_le10.fit_transform(data["����"])

# Split trining data and testing data
X = data.iloc[:, 0:14]
y = data.iloc[:, 14:15]

from sklearn.model_selection import train_test_split
trX, teX, trY, teY = train_test_split(
    X, y, test_size=0.2, random_state=0)

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=0)
clf = clf.fit(trX, trY)

import pydotplus 
dot_data = tree.export_graphviz(clf,
                                feature_names=["�h�O�W��","�ƪO��","�̤p�u�|","�̤p�u�Z",
                                            "�X�f���n","��������","�����覡","�����t��",
                                            "�������x","�n�����x","E1�t�O","E1�u�O",
                                            "�e�B�z","����"],
                                class_names=["A","B","C","D","E", "F"],
                                filled=True,
                                rounded=True,
                                special_characters=True,
                                out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("yields.pdf")

######### Part III #########
# -*- coding: big5 -*-
# coding=Big5
import numpy as np
import pandas as pd
# Import data
data = pd.read_csv("view_parameters_yield_mapping3.csv", header=0, encoding = 'big5')
data.columns = ["�h�O�W��","�ƪO��","�̤p�u�|","�̤p�u�Z","�X�f���n",
                "��������","�����覡","�����t��","�������x","�n�����x",
                "E1�t�O","E1�u�O","�e�B�z","����","���}�v2"]
data["�̤p�u�|"].fillna(data["�̤p�u�|"].mean(), inplace=True)
data["�̤p�u�Z"].fillna(data["�̤p�u�Z"].mean(), inplace=True)
data["�X�f���n"].fillna(data["�X�f���n"].mean(), inplace=True)
data["�����t��"].fillna(data["�����t��"].mean(), inplace=True)
#data["����"] = 'str' + data["����"].astype(str)
#data["�e�B�z"] = 'str' + data["�e�B�z"].astype(str)
data.fillna("NAN")
feat_labels = data.columns[0:-1]
# Encode data columns
from sklearn.preprocessing import LabelEncoder
class_le1 = LabelEncoder()
class_le2 = LabelEncoder()
class_le3 = LabelEncoder()
class_le4 = LabelEncoder()
class_le5 = LabelEncoder()
class_le6 = LabelEncoder()
class_le7 = LabelEncoder()
class_le8 = LabelEncoder()
class_le9 = LabelEncoder()
class_le10 = LabelEncoder()
data["�h�O�W��"] = class_le1.fit_transform(data["�h�O�W��"])
data["�ƪO��"] = class_le2.fit_transform(data["�ƪO��"])
data["��������"] = class_le3.fit_transform(data["��������"])
data["�����覡"] = class_le4.fit_transform(data["�����覡"])
data["�������x"] = class_le5.fit_transform(data["�������x"])
data["�n�����x"] = class_le6.fit_transform(data["�n�����x"])
data["E1�t�O"] = class_le7.fit_transform(data["E1�t�O"])
data["E1�u�O"] = class_le8.fit_transform(data["E1�u�O"])
data["�e�B�z"] = class_le9.fit_transform(data["�e�B�z"])
data["����"] = class_le10.fit_transform(data["����"])


# Split trining data and testing data
X = data.iloc[:, 0:14].as_matrix()
# To solve the error of Sci-kit learn pipeline returns indexError: 
# too many indices for array
y = data.iloc[:, 14:15].as_matrix().ravel()

from sklearn.model_selection import train_test_split
trX, teX, trY, teY = train_test_split(
    X, y, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import tree

pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=2)),
                    ('clf', LogisticRegression(random_state=1))])

pipe_lr.fit(trX, trY)
print('Test Accuracy: %.3f' % pipe_lr.score(teX, teY))
y_pred = pipe_lr.predict(teX)



######### Part IV K-fold cross-validation #########
# -*- coding: big5 -*-
# coding=Big5
from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=pipe_lr,
                         X=trX,
                         y=trY,
                         cv=10,
                         n_jobs=1)
print('CV accuracy scores: %s' % scores)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))

import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('clf', LogisticRegression(penalty='l2', random_state=0))])
train_sizes, train_scores, test_scores =\
                learning_curve(estimator=pipe_lr,
                               X=trX,
                               y=trY,
                               train_sizes=np.linspace(0.1, 1.0, 10),
                               cv=10,
                               n_jobs=1)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(train_sizes, train_mean,
         color='blue', marker='o',
         markersize=5, label='training accuracy')

plt.fill_between(train_sizes,
                 train_mean + train_std,
                 train_mean - train_std,
                 alpha=0.15, color='blue')

plt.plot(train_sizes, test_mean,
         color='green', linestyle='--',
         marker='s', markersize=5,
         label='validation accuracy')

plt.fill_between(train_sizes,
                 test_mean + test_std,
                 test_mean - test_std,
                 alpha=0.15, color='green')

plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.ylim([0.2, 1.0])
plt.tight_layout()
# plt.savefig('./figures/learning_curve.png', dpi=300)
plt.show()


#Addressing over- and underfitting with validation curves
######### Part IV K-fold cross-validation #########
# -*- coding: utf-8 -*-
from sklearn.model_selection import validation_curve

pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('clf', LogisticRegression(penalty='l2', random_state=0))])
param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
train_scores, test_scores = validation_curve(
                estimator=pipe_lr, 
                X=trX, 
                y=trY, 
                param_name='clf__C', 
                param_range=param_range,
                cv=10)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, 
         color='blue', marker='o', 
         markersize=5, label='training accuracy')

plt.fill_between(param_range, train_mean + train_std,
                 train_mean - train_std, alpha=0.15,
                 color='blue')

plt.plot(param_range, test_mean, 
         color='green', linestyle='--', 
         marker='s', markersize=5, 
         label='validation accuracy')

plt.fill_between(param_range, 
                 test_mean + test_std,
                 test_mean - test_std, 
                 alpha=0.15, color='green')

plt.grid()
plt.xscale('log')
plt.legend(loc='lower right')
plt.xlabel('Parameter C')
plt.ylabel('Accuracy')
plt.ylim([0.2, 1.0])
plt.tight_layout()
# plt.savefig('./figures/validation_curve.png', dpi=300)
plt.show()