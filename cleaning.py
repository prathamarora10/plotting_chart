import pandas as pd
import csv

df = pd.read_csv('main.csv')
print(df.shape)

del df['name']
del df['distance']
del df['mass']
del df['radius']

print(df.shape)

df.to_csv('final.csv')