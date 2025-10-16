import numpy as np
import pandas as pd

df=pd.read_csv(r"C:\Users\VAIBHAVI\Desktop\Python\dataset\weatherAUS.csv",encoding="utf-8")
print('size of weather data frame os : ',df.shape)
print(df[0:5]) # to print first 5 rows
#data preprocessing
print(df.count().sort_values())# to print count of non null values in each column 

df=df.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','Date'])#dropping columns withlarge number of null values and irrelevant  columns
print(df.shape)

#get rid of  of all null values in dataframe
df=df.dropna(how='any')
print(df.shape)

#remove outliers from df we are  using z score to detect and remove the outliers
from scipy import stats
z=np.abs(stats.zscore(df._get_numeric_data()))
print(z)
df=df[(z<3).all(axis=1)]
print(df.shape)

#Lets deal with the categorial columns now
#simply change yes/no to 1/0 for RainToday andd RainTommorrow columns
df['RainToday']=df['RainToday'].replace({'No':0,'Yes':1}).astype(int)
df['RainTomorrow']=df['RainTomorrow'].replace({'No':0,'Yes':1}).astype(int)

#see unique values and convert them to  int using pd.getDummies()
categorical_columns=['WindGustDir','WindDir3pm','WindDir9am']
for col in categorical_columns:
    print(np.unique(df[col]))
#transform the categorial columns to int
df=pd.get_dummies(df,columns=categorical_columns)
print(df.iloc[4:9])

#next step is to standardize theb data -using min max scaler
from sklearn import preprocessing
scaler=preprocessing.MinMaxScaler()
scaler.fit(df)
df=pd.DataFrame(scaler.transform(df),index=df.index ,columns=df.columns)
print(df.iloc[4:10])

#Exploratory data analysis (it will help us to select the best features that influence the target variable)
from sklearn.feature_selection import SelectKBest,chi2
X=df.loc[:,df.columns!='RainTomorrow']
y=df['RainTomorrow']
selector=SelectKBest(chi2,k=3)
selector.fit(X,y)
X_new=selector.transform(X)
print(X.columns[selector.get_support(indices=True)])#top 3 columns that influence the target variable

#Lets get hold of the important  features and assign them to x
df=df[['Humidity3pm','Rainfall','RainToday','RainTomorrow']]
X=df[['Humidity3pm']] #lets use only one feature HUmidity3pm
y=df[['RainTomorrow']]

#Data Modelling
#Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

#calculating the  accuracy and the time taken  by the classifier
t0=time.time()
#Data splicing
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
clf_logreg=LogisticRegression(random_state=0)
#Building the model using training dataset
clf_logreg.fit(x_train,y_train)

#Evaluating the model using testing data set
y_pred=clf_logreg.predict(x_test)
score=accuracy_score(y_test,y_pred)

#printing the accuracy and the time taken by the classifier
print('Accuracy using Logistic Regression:' ,score)
print('Time taken using Logistic Regression:',time.time()-t0)