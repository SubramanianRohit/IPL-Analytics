#Program to create a Dataframe called Batters which lists every individual batter innings in IPL history and includes statistics like number of boundaries, balls faced, strike rate, boundary rate and dismissals. 

import pandas as pd
import numpy as np

df=pd.read_csv('all_matches.csv',low_memory=False)

# Your existing DataFrame
batters = df.groupby(['match_id', 'striker'])['runs_off_bat'].sum().reset_index()

# Add 'fours', 'sixers', 'balls', 'SR', 'BR', 'dismissal', and 'season' columns
batters = (
    batters
    .merge(df[df['runs_off_bat'] == 4].groupby(['match_id', 'striker']).size().reset_index(name='fours'), on=['match_id', 'striker'], how='left')
    .merge(df[df['runs_off_bat'] == 6].groupby(['match_id', 'striker']).size().reset_index(name='sixers'), on=['match_id', 'striker'], how='left')
    .merge(df.groupby(['match_id', 'striker']).size().reset_index(name='balls'), on=['match_id', 'striker'], how='left')
    .merge(df[df['wicket_type'].notna()].groupby(['match_id', 'striker'])['wicket_type'].first().reset_index(name='dismissal'), on=['match_id', 'striker'], how='left')
    .merge(df[['match_id', 'season']].drop_duplicates(), on='match_id', how='left')
)

# Fill NaN values with 0 for 'fours' and 'sixers', and with 'Not Out' for 'dismissal'
batters[['fours', 'sixers']] = batters[['fours', 'sixers']].fillna(0).astype(int)
batters['dismissal'] = batters['dismissal'].fillna('Not Out')

# Calculate 'SR' and 'BR'
batters['SR'] = (batters['runs_off_bat'] / batters['balls'] * 100).astype(int)
batters['BR'] = ((batters['fours'] + batters['sixers']) / batters['balls'] * 100).astype(int)

print(batters)