from bs4 import BeautifulSoup
import pandas as pd

file = open("Lubeto.html", "r", encoding="utf8", errors='ignore')
soup = BeautifulSoup(file.read(), "html.parser")

#Dates
dates_list = []
for date in soup.body.find_all('span', {'class': 'date-duration-date'}):
	dates_list.append(date.string)
#print(dates_list)


#Show visible info in the table
# games = soup.body.find_all('li', {'class': 'game-summary'}, limit=50)
# for game in games:
# 	#print(game.text.split()[14])
# 	print(game.text.split())
# 	champ_list.append(game.text.split()[1]) #split string
# print(champ_list)

#Show vicotry class
wins = []
for div in soup.body.findAll('div', {'class': 'date-duration'}):
    child = div.next_sibling
    wins.append(child.attrs['class'][0])

#Champ names
champions = []
for champ in soup.body.find_all('div', {'class': 'champion-nameplate-name'}):
	champions.append(champ.text)
#print(champions)

s1 = pd.Series(champions)
s2 = pd.Series(wins)
s3 = pd.Series(dates_list)

df=pd.DataFrame()
df['champs']=s1
df['wins'] = s2
df['dates']= s3

df.to_csv('league_lubeto.csv')