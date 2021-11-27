import csv
import pandas as pd

file_1 = "stars.csv"
file_2 = "scrapper_2.csv"

d1 = []
d2 = []

with open(file_1, 'r', encoding = "utf8") as f:
    reader = csv.reader(f)
    d1 = list(reader)
    
with open(file_2, 'r', encoding = "utf8") as f:
    reader = csv.reader(f)
    d2 = list(reader)
    
h1 = d1[0]
h2 = d2[0]

h = h1 + h2

p_d = []

for i in d1:
    p_d.append(i)
    
for i in d2:
    p_d.append(i)
    
with open("main.csv", "w", encoding = "utf8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(h)
        csvwriter.writerows(p_d)
        
df = pd.read_csv('main.csv')
df.tail(8)