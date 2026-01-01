import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class LogisticRegression:

    def __init__(self, lr = 0.001 , n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.losses = []
    def fit(self , X ,y):
        n_samples , n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_model = np.dot(X , self.weights) + self.bias
            predicteds = sigmoid(linear_model)

            dw = (1/n_samples) * np.dot(X.T , (predicteds - y))
            db = (1/n_samples) * np.sum(predicteds - y)

            self.weights = self.weights - self.lr * dw 
            self.bias = self.bias - self.lr * db

            losss = - (1/n_samples) * np.sum(y* np.log(predicteds + 1e-9) + (1-y )* np.log(1 - predicteds + 1e-9))
            self.losses.append(losss)


    def predict(self , X ):
        linear_model = np.dot(X , self.weights) + self.bias
        predicteds = sigmoid(linear_model)
        y_predicted = [1 if i >= 0.5 else 0 for i in predicteds]
        return np.array(y_predicted)
    
    def accuracy(self , y_true , y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        print("Accuracy : " , accuracy)
    
        

# testing the binary classification model 

from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

data = load_breast_cancer()
X , y = data.data , data.target
x_train , x_test , y_train , y_test = train_test_split(X , y , test_size= 0.3)

clf = LogisticRegression(0.01,1000)
clf.fit(x_train , y_train)
y_pred = clf.predict(x_test)

clf.accuracy(y_test , y_pred)

# Plotting the loss over iterations
plt.plot(range(len(clf.losses)), clf.losses)
plt.title("Training Loss over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Loss (Cost)")
plt.show()


