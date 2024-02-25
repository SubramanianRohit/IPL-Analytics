#From the batters df, compile stats of every batter over every season to result in a dataframe that lists all full season stats for every batter that has played in the IPL, filter data by thresholds and generate scatterplots for key stats 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


#Batter By Season batbs
batbs = batters.groupby(['striker', 'season']).agg({
    'match_id': 'count',
    'runs_off_bat': 'sum',
    'fours': 'sum',
    'sixers': 'sum',
    'balls': 'sum',
    'SR': 'mean',
    'BR': 'mean',
    'dismissal': lambda x: (x != 'not out').sum()
}).reset_index()

batbs['SR'] = batbs['SR'].astype(int)
batbs['BR'] = batbs['BR'].astype(int)

print(batbs)

#Objective 2: Filter batters by season data for historical markers by applying balls faced, strike rate and boundary rate thresholds

balls_t = int(input("Please enter the Balls Faced Threshold:"))
SR_t = int(input ("Please enter the Strike Rate Threshold:"))
BR_t = int(input ("Please enter the Boundary Rate Threshold:"))


f_batbs = batbs[(batbs['balls'] >= balls_t) & (batbs['SR'] > SR_t) & (batbs['BR'] > BR_t)]
batbs_sorted = f_batbs.sort_values('runs_off_bat', ascending=False)

print(batbs_sorted)

#Objective 3: Seek Threshold from user and scatterplot between two variables and include a regression line 
balls_t = int(input("Enter the minimum number of runs for the scatterplot: "))

f_batbs = batbs[batbs['runs_off_bat'] >= balls_t]

plt.scatter(f_batbs['BR'], f_batbs['dismissal'])

# Calculate the coefficients for the regression line
m, b = np.polyfit(f_batbs['BR'], f_batbs['dismissal'], 1)

# Add the regression line to the plot
plt.plot(f_batbs['BR'], m*f_batbs['BR'] + b, color='red')

plt.title('Scatter plot between Dismissals and Boundary Rate')
plt.xlabel('BR')
plt.ylabel('Dismissal')
plt.show()