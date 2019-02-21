# League-Analyzer

![League Logo](https://upload.wikimedia.org/wikipedia/fr/1/12/League_of_Legends_Logo.png)

Analyze games and statistics from the online MOBA game League of Legends


In this simply Python script you can download details from games without the need of setting an API. You can manipulate the data from tables and
create stastics.


## How the idea was born?

After numerous defeats while playing with my friends we wanted to see if there is a correlation between  our winrate and the day of week we are playing. We were having the perception that on Fridays we were losing way more than other days. 


Websites such as op.gg show you the latest games and we wanted to analyze maybe 1000s of them so that option was out.

We analyzed all ranked games since the beginning of **Season 8** until its end as available on their website (check link below)


## How it works?


1. Visit [this link where you can find all your historical games](https://matchhistory.eune.leagueoflegends.com/en/#match-history/EUW1/23004123)
2. Define your filters in the top side
3. Scroll until the bottom of the page (depening how many games you want to review you might need to hit page end multiple times)
4. Once the webpage displays all of your games right click and **save the html file**
5. Place the python file `league.py` in the same directory and change the following line
```file = open("Lubeto.html", "r", encoding="utf8", errors='ignore')```
replacing with the name of your file
6. Wait until the script is done and you will see a new cvs file in a structured way
7.For the rest, you can follow the Jupyter Notebook for an example of an analysis
8. Have fun :)


Necessary libraries:
 * Pandas
 * BeautifulSoup
 * Mathplotlib
 
