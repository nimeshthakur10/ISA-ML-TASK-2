import pandas as pd

df = pd.read_csv('data/weatherAUS.csv')

location= input()

filt = (df['Location'] == location)
print(df.loc[filt]) #display the data of particular location
