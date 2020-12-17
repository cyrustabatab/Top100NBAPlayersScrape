import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.cbssports.com/nba/news/nba-top-100-player-rankings-lebron-james-holds-off-kawhi-giannis-for-no-1-no-rookies-make-list/'
response = requests.get(url)


soup = BeautifulSoup(response.text,'html.parser')



names = soup.find_all('span',class_='player-name')
teams = soup.find_all('span',class_='player-position')

df = pd.DataFrame(columns=['name','team','position'])
df.index.name = 'rank'
for i,(name,team) in enumerate(zip(names,teams)):
    rank = i + 1

    name = name.getText().strip()
    team = team.getText().strip()
    position = team[-2:]
    team = team[:-2]


    df.loc[rank] = [name,team,position]


df.to_csv("top100.csv")


