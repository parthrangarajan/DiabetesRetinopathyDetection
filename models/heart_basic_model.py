import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data= pd.read_csv("heart_disease_data\heart_disease_health_indicators_BRFSS2015.csv")
print(data.head())

data.drop(['Education', 'Income', 'PhysHlth', 'MentHlth'], axis = 1, inplace = True)
X = data.loc[:, data.columns != 'HeartDiseaseorAttack']
y = data.loc[:, data.columns == 'HeartDiseaseorAttack']

from imblearn.over_sampling import SMOTE

os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns

os_data_X,os_data_y=os.fit_resample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['HeartDiseaseorAttack'])

data_final_vars=data.columns.values.tolist()
y=['HeartDiseaseorAttack']
X=[i for i in data if i not in y]
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
rfe = RFE(logreg)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
data_X= data[X]
data_y= data[y]
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#TESTING
pred_Xtest1= logreg.predict(X_test.iloc[0].values.reshape(1, -1).tolist())
print(pred_Xtest1)
print(y_test.iloc[0])