#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:43:23 2019

@author: bhagya
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

X=X[:,1:]

"""from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lb=LabelEncoder
#ohe=OneHotEncoder(categorical_features=[3])
ohe    = OneHotEncoder(categorical_features=[3],sparse=False)

#labels is categorical dataframe

encoded_columns  = ohe.fit_transform(X)

#join non categorical and categorical datasets after encoding

X = np.concatenate([scaled_columns, encoded_columns], axis=1)

#X=ohe.fit_transform(X).toarray()

from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(
    [('ohe', OneHotEncoder(sparse=False), [3]),],  # the column numbers I want to apply this to
    remainder='passthrough'  # This leaves the rest of my columns in place
)
X=ct.fit_transform(X)
from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(X)
X=svd.transform(X)

import scipy as sp
X=sp.sparse.hstack()
X = pd.convert_objects(convert_numeric=True)
 X=np.load(X).tolist()
 X=X.toarray()
 """
from sklearn.model_selection import train_test_split
X_tr,X_ts,Y_tr,Y_ts = train_test_split(X,Y,test_size=0.2)
"""
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_tr=sc_X.fit_transform(X_tr)
X_ts=sc_X.transform(X_ts)"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_tr,Y_tr)
import  statsmodels.formula.api as sm

X= np.append(arr=np.ones((50,1)).astype(int),values = X,axis=1 )

X_opt = X[:,[0,1,2,3,4,5]]

regr_ols=sm.OLS(endog=Y ,exog=X_opt).fit()
regr_ols.summary()

X_opt = X[:,[0,1,3,4,5]]

regr_ols=sm.OLS(endog=Y ,exog=X_opt).fit()
regr_ols.summary()

X_opt = X[:,[0,3,4,5]]

regr_ols=sm.OLS(endog=Y ,exog=X_opt).fit()
regr_ols.summary()

X_opt = X[:,[0,3,5]]

regr_ols=sm.OLS(endog=Y ,exog=X_opt).fit()
regr_ols.summary()

X_opt = X[:,[0,3]]

regr_ols=sm.OLS(endog=Y ,exog=X_opt).fit()
regr_ols.summary()

"""
import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)



Backward Elimination with p-values and Adjusted R Squared:

import statsmodels.formula.api as sm
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)O
"""