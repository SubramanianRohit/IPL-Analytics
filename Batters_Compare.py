#Program to compare 3 batters and their stats by Season 

#First run Batters.py

import pandas as pd
import numpy as np


# Prompt the user for three partial batter names
partial_name1 = input("Please enter part of the first batter's name: ")
partial_name2 = input("Please enter part of the second batter's name: ")
partial_name3 = input("Please enter part of the third batter's name: ")

# Filter the 'batters' DataFrame for the given partial batter names
batter_stats1 = batters[batters['striker'].str.contains(partial_name1, case=False, na=False)]
batter_stats2 = batters[batters['striker'].str.contains(partial_name2, case=False, na=False)]
batter_stats3 = batters[batters['striker'].str.contains(partial_name3, case=False, na=False)]

# Group by 'season' and 'striker', and calculate the total statistics for the batters
season_stats1 = batter_stats1.groupby(['season', 'striker']).agg({
    'runs_off_bat': 'sum',
    'fours': 'sum',
    'sixers': 'sum',
    'balls': 'sum',
    'dismissal': lambda x: (x != 'Not Out').sum()
}).reset_index()

season_stats2 = batter_stats2.groupby(['season', 'striker']).agg({
    'runs_off_bat': 'sum',
    'fours': 'sum',
    'sixers': 'sum',
    'balls': 'sum',
    'dismissal': lambda x: (x != 'Not Out').sum()
}).reset_index()

season_stats3 = batter_stats3.groupby(['season', 'striker']).agg({
    'runs_off_bat': 'sum',
    'fours': 'sum',
    'sixers': 'sum',
    'balls': 'sum',
    'dismissal': lambda x: (x != 'Not Out').sum()
}).reset_index()

# Calculate 'SR' and 'BR'
for stats in [season_stats1, season_stats2, season_stats3]:
    stats['SR'] = (stats['runs_off_bat'] / stats['balls'] * 100).astype(int)
    stats['BR'] = ((stats['fours'] + stats['sixers']) / stats['balls'] * 100).astype(int)

print(season_stats1)
print(season_stats2)
print(season_stats3)