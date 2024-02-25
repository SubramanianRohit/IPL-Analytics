import pandas as pd

#Dataframe from csv File 
df=pd.read_csv('all_matches.csv',low_memory=False)

#List All Seasons in the Dataframe
season=df['season'].unique()

#Boundaries in Power Play
sixer_pp = df['season'].isin(season) & (df['runs_off_bat']==6) & (df['ball']<5.7)
four_pp = df['season'].isin(season) & (df['runs_off_bat']==4) & (df['ball']>5.7)

#Boundaries in Middle Overs
sixer_mo = df['season'].isin(season) & (df['runs_off_bat']==6) & (df['ball']>5.7) & (df['ball']<16.7)
four_mo = df['season'].isin(season) & (df['runs_off_bat']==4) & (df['ball']>5.7) & (df['ball']<16.7)

#Boundaries in Death Overs
sixer_do = df['season'].isin(season) & (df['runs_off_bat']==6) & (df['ball']>16.7)
four_do = df['season'].isin(season) & (df['runs_off_bat']==4) & (df['ball']>16.7)

#Boundaries Grouped by Season
sixerpp_counts = df[sixer_pp].groupby(df['season']).size()
fourpp_counts = df[four_pp].groupby(df['season']).size()

sixermo_counts = df[sixer_mo].groupby(df['season']).size()
fourmo_counts = df[four_mo].groupby(df['season']).size()

sixerdo_counts = df[sixer_do].groupby(df['season']).size()
fourdo_counts = df[four_do].groupby(df['season']).size()

#Table Representing above data in 3 columns: Season, Sixers, Fours
new_table = {'Season': season, 'Sixers in Powerplay': sixerpp_counts, 'Fours in Powerplay': fourpp_counts, 'Sixers in Middle Overs': sixermo_counts, 'Fours in Middle Overs': fourmo_counts, 'Sixers in Death Overs': sixerdo_counts, 'Fours in Death Overs': fourdo_counts}

#Define dataframe 'bound' to summarize Boundaries
bound = pd.DataFrame(new_table)

#Show the boundaries Table 
bound