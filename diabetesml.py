import sklearn
import sklearn.ensemble
import sklearn.datasets
import sklearn.linear_model
import sklearn.tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d=pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\diabetes.csv")
y=d['Species']
d=d.drop(['Species'],axis=1)
x=d
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(clf.feature_importances_)
