#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:10:44 2019

@author: bhagya
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values



from sklearn.model_selection import train_test_split
X_tr,X_ts,Y_tr,Y_ts = train_test_split(X,Y,test_size=1/3,random_state=0)

"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_tr=sc_X.fit_transform(X_tr)
X_ts=sc_X.transform(X_ts)"""

from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(X_tr,Y_tr)

y_pred = regressor.predict(X_ts)

plt.scatter(X_tr,Y_tr,color='red')
plt.plot(X_tr,regressor.predict(X_tr),color='blue')
#plt.plot(X_tr,Y_tr,color='green')
plt.title('salary vs experience(Training set)')
plt.xlabel('experience')
plt.ylaber('salary')
plt.show()

plt.scatter(X_ts,Y_ts,color='red')
plt.plot(X_ts,y_pred,color='blue')
plt.plot(X_tr,regressor.predict(X_tr),color='green')
#plt.plot(X_tr,Y_tr,color='green')
plt.title('salary vs experience(Trest set)')
plt.xlabel('experience')
plt.ylaber('salary')
plt.show()