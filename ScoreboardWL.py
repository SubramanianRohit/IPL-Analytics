import pandas as pd
import numpy as np

df=pd.read_csv('all_matches.csv',low_memory=False)

#runs = runs off bat + extras
df['runs'] = df['runs_off_bat'] + df['extras']

#runs scored for each innings under each match id
runscored = df.groupby(['match_id', 'innings','batting_team'])['runs'].sum().reset_index()

#wickets taken for each innings under each match id
wickets = df.groupby(['match_id', 'innings'])['wicket_type'].count().reset_index()

#Combine the Wickets and Runs to show the scoreboard
scoreboard = pd.merge(runscored, wickets, on=['match_id', 'innings'])

#Determine the Winner and Loser for each Match ID based on the Runs scored 
scoreboard['result'] = np.where(scoreboard.groupby('match_id')['runs'].rank(ascending=False) == 1, 'W', 'L')

#Replace old team names
scoreboard=scoreboard.replace({'Rising Pune Supergiant':'Rising Pune Supergiants', 'Kings XI Punjab': 'Punjab Kings', 'Delhi Daredevils': 'Delhi Capitals', 'Deccan Chargers':'Sunrisers Hyderabad'})

#Count Number of Wins for each team
wins = scoreboard[scoreboard['result'] == 'W'].groupby('batting_team').size().reset_index(name='count')
wins.sort_values(by='count', ascending=False).reset_index(drop=True)

#Count Number of Games Played for each team
gp = scoreboard.groupby('batting_team').size().reset_index(name='gp')

#Merge Games Played into the wins table
wins=pd.merge(wins, gp, on='batting_team')

#Calculate Win Percentage and sort table by win percentage
wins['winp'] = ((wins['count']/wins['gp'])*100).round(0).astype(int)
wins.sort_values(by='winp', ascending=False).reset_index(drop=True)