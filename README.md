A series of tools to analyze data for every IPL game. Data retrieved from cricsheet.org. 
The data carries 22 characteristics for every ball bowled. Most files below are dedicated to developing useful stats from these ball-by-ball datapoints. 

1. Boundaries by Phase of Play.py generates dataframes to track team batting by powerplay, middle overs and death overs and provides a skeleton for similar phase-based analysis for other characteristics down the road 
2. ScoreboardWL.py generates the score for both teams and determines who won or lost the game. This enables further computations to determine win percentages and predictions.
3. Batters.py generates a list of every batting innings ever in the IPL listing every batter from every season, and includes second degree stats like number of balls faced, strike rate, boundary rate, dismissal type, etc.
4. Batters_compare.py allows comparison of 3 user-picked batters and their stats by season. Best way to visualize the progress made by an up and coming player versus veterans.
5. BattersbySeason.py compiles match by match info to generate a dataframe that lists every batter's season long stats across every IPL season. Allows for further analysis by filtering and sorting for min and max thresholds across various primary and secondary statistics.  
