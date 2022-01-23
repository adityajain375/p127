from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url)

soup = bs(page.text,'html.parser')

table = soup.find('table')

tempList = []
rows= table.find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

starNames = []
distance= []
mass = []
radius = []

for i in range(1,len(tempList)):
    starNames.append(tempList[i][1])
    distance.append(tempList[i][3])
    mass.append(tempList[i][5])
    radius.append(tempList[i][6])

df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius)),columns=['star name','distance','mass','radius'])
print(df2)
df2.to_csv('brightStars.csv')
