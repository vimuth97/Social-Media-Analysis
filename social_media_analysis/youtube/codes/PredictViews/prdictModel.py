# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:16:02 2020

@author: user
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import random


data = pd.read_csv('Datasets/datapredictviews.csv')
data = data.iloc[:,:].values
random.shuffle(data)
random.shuffle(data)
random.shuffle(data)


def normalize(x_train):
    for column in range(x_train.shape[1]):
        avg = sum(x_train[:,column])/x_train.shape[0]
        datarange = (max(x_train[:,column]) - min(x_train[:,column]))
        for data in range(0,x_train.shape[0]):
            x_train[data,column] = float(x_train[data,column] - avg)/datarange            
    return x_train


#normalizedData = normalize(data)

y1 = data[:,1]
y2 = data[:,2]

x = data[:,3:]

#print("labels",labels)

#print("test",x_test)
#sys.exit()
#imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

features = x

X_train, X_test, y1_train, y1_test = train_test_split(features, y1, test_size=0.3,random_state=1)
reg = linear_model.LinearRegression()
reg.fit(X_train, y1_train)


X_train, X_test, y2_train, y2_test = train_test_split(features, y2, test_size=0.3,random_state=1)
reg2 = linear_model.LinearRegression()
reg2.fit(X_train, y2_train)


print('Coefficients: \n', reg.coef_) 
print('Coefficients: \n', reg2.coef_) 
 

#print('Variance score: {}'.format(reg.score(X_test, y1_test)))
#print('Variance score: {}'.format(reg.score(X_test, y2_test)))

## setting plot style 
#plt.style.use('fivethirtyeight') 
  
## plotting residual errors in training data 
#plt.scatter(reg.predict(X_train), reg.predict(X_train) - y1_train, 
 #           color = "green", s = 10, label = 'Train data') 
  
## plotting residual errors in test data 
#plt.scatter(reg.predict(X_test), reg.predict(X_test) - y1_test, 
#            color = "blue", s = 10, label = 'Test data') 
  
## plotting line for zero residual error 
#plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 8) 
  
## plotting legend
#plt.legend(loc = 'upper right') 
  
## plot title 
#plt.title("Residual errors") 
  
## function to show plot 
#plt.show()
 