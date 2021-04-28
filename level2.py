import pandas as pd

df = pd.read_csv('data/weatherAUS.csv')
pd.set_option('display.max_columns', 23)

print(df['Evaporation'].mean())

print(df['Evaporation'].fillna(df['Evaporation'].mean(),inplace=True)) #Replace the missing values with the average of evaporation 

print(df.dropna(axis='columns',how='any'))  #Drop the column which has null values

print(df.drop(columns='Date'))  #Drop the date column