import sklearn

#How can we modify this code so it doesn’t do that? Set header to "None."
import pandas
data=pandas.read_csv("iris.data", header=None)
print(data)

#Could you use this to predict the type of iris based on the lengths of different flower parts? Yes, but it 
#What iris can easily be identified? Blue
#What two are hard to tell apart? Why? Green and orange, because their is a lot of overlap between them.
import matplotlib.pyplot as plt
import seaborn as sns # visualization
sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
plt.show()

import numpy as np
data=np.array(data)

X=data[:,0:4] #This gets all the rows and only the first 4 columns.
y=data[:,4]
print(X.shape) #(150,4)
print(y.shape) #(150,)

#How did you verify this? By comparing the shuffled x and y columns.
#What is random_state? A seed the program uses to randomized sets.
#How could it be useful? It makes the tests repeatable because it shuffles the same way every time.
from sklearn.utils import shuffle
X,y=shuffle(X,y,random_state=0)

trainX=X[:120]
trainy=y[:120]
testX=X[120:]
testy=y[120:]

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[5,5], max_iter = 2000,random_state=0)
clf.fit(trainX, trainy)

#On a piece of paper, see if you can draw out your network and label the weights.
print(clf.coefs_)

prediction=clf.predict(testX)

#What do these numbers mean? They are the percentage of how many of the pediction the NN got correct.
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

from sklearn.model_selection import cross_validate
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)











