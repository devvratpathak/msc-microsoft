import numpy as np
import pandas as pd
import os
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestRegressor, VotingRegressor
import seaborn as sns
import xgboost as xgb
from xgboost import XGBClassifier, XGBRegressor
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from catboost import CatBoostClassifier
os.getcwd()




df=pd.read_csv("he.csv")
df3=pd.read_csv("he.csv")
target=df3['Medical Condition']
X=df

a=LabelEncoder()
df['Gender']=a.fit_transform(df['Gender'])
df['Blood_Type']=a.fit_transform(df['Blood Type'])
df['Test_Results']=a.fit_transform(df['Test Results'])
df.drop(['Blood Type','Medication','Test Results'],axis=1,inplace=True)


df.drop(['Name','Date of Admission','Doctor','Hospital','Insurance Provider','Billing Amount',
        'Room Number','Admission Type','Discharge Date'],axis=1,inplace=True)

target=y=df['Medical Condition']
df.drop(['Medical Condition'],axis=1,inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.2, random_state=42)


rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
catboost_classifier = CatBoostClassifier(iterations=100, learning_rate=0.1, verbose=False)

rf_classifier.fit(X_train, y_train)
catboost_classifier.fit(X_train, y_train)

ensemble_model1 = VotingClassifier(estimators=[('Random Forest', rf_classifier), ('CatBoost', catboost_classifier)], voting='soft')  

ensemble_model1.fit(X_train, y_train)

column_names = ['Age', 'Gender', 'Blood_Type', 'Test_Results']

user_input = []

for column in column_names:
    user_input.append(float(input(f"Enter value for {column}: ")))

input_df = pd.DataFrame([user_input], columns=column_names)

input_values = input_df.values.reshape(1, -1)

ensemble_model100 = ensemble_model1.predict(input_values)

print("Medical Condition:", ensemble_model100[0])


