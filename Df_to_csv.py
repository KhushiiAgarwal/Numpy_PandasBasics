import pandas as pd 
import numpy as np
pers_data = {'name': ['Asha', 'Radha', 'Kamal', 'Divy', 'Anjali'],'height': [ 5.5, 5, np.nan, 5.9, np.nan], 'age': [11, 23, 22, 33, 22]} 
labels = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(pers_data , index=labels) 
print("Persons whose height not known:") 
print(df[df['height'].isnull()])
print('Dataframe')
print(df.to_csv('C:\\Users\\lab-pc\\AppData\\Local\\Programs\\Python\\pp1.csvpp1.csv' ,names=[‘name’,’age’,’height’],index=False ,skiprows=[1])) #Ensure correct path where a new csv can be created
df1=pd.read_csv('C:\\Users\\lab-pc\\AppData\\Local\\Programs\\Python\\pp1.csvpp1.csv')# Ensure the path is same
print(df1['age'])
print(df1)
print(df1['age'].max())
