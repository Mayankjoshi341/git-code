
import pandas as pd
from logistic_reg import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X , y = data.data , data.target
x_train , x_test , y_train , y_test = train_test_split(X , y , test_size= 0.3)

clf = LogisticRegression(n_iters=200)
clf.fit(x_train , y_train)
y_pred = clf.predict(x_test)

acc = clf.accuracy(y_test , y_pred)