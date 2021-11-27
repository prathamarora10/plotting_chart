from bs4 import BeautifulSoup as bs

import pandas as pd
import csv
import requests

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(START_URL)
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')
temp_list = []
table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
star_name = []
star_dist = []
star_mass = []
star_radius = []

for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][0])
    star_dist.append(temp_list[i][5])
    star_mass.append(temp_list[i][7])
    star_radius.append(temp_list[i][8])
    
df = pd.DataFrame(list(zip(star_name, star_dist, star_mass, star_radius)), columns = ["name", "distance", "mass", "radius"])
df.to_csv('stars.csv')