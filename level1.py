import pandas as pd

df = pd.read_csv('data\weatherAUS.csv')
pd.set_option('display.max_columns', 23)

print(df['MaxTemp'].mean() ) #Average Maximum Temperature
print(df['MinTemp'].mean() ) #Average Minimum Temperature

filt = (df['Location'] == 'Cobar')

print(df.loc[filt]['MaxTemp'].mean()) #Average Maximum Temperature in the Location Cobar

print(145460 - df['Sunshine'].count()) #count of null value in the column → Sunshine
print(145460 - df['Evaporation'].count()) #count of null value in the column →  Evaporation