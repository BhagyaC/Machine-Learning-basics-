#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:11:17 2019

@author: bhagya
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values



from sklearn.model_selection import train_test_split
X_tr,X_ts,Y_tr,Y_ts = train_test_split(X,Y,test_size=0.2)

"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_tr=sc_X.fit_transform(X_tr)
X_ts=sc_X.transform(X_ts)"""