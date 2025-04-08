#!/usr/bin/env python
# coding: utf-8

# In[269]:


import pandas as pd # type: ignore
import random

def get_play_in_teams(df):
    return [row for index, row in df.iterrows() if 6 < row['Seed'] < 11]

def get_team_stats(team_name, team_stats, opp_stats):
    return (
        team_stats[team_stats["Team"] == team_name].iloc[0],
        opp_stats[opp_stats["Team"] == team_name].iloc[0]
    )

def simulate_bracket(east_playIn, west_playIn, team_stats, opp_stats):
    #7vs8 - winner is 7th seed, loser plays winner of 9vs10 to get 8th seed. Single game elimination 
    
    team_7, team_8, team_9, team_10 = east_playIn[0]['Team'], east_playIn[1]['Team'], east_playIn[2]['Team'], east_playIn[3]['Team']
    wteam_7, wteam_8, wteam_9, wteam_10 = west_playIn[0]['Team'], west_playIn[1]['Team'], west_playIn[2]['Team'], west_playIn[3]['Team']

    team_7_stats, team_7_opp_stats = get_team_stats(team_7, team_stats, opp_stats)
    team_8_stats, team_8_opp_stats = get_team_stats(team_8, team_stats, opp_stats)
    team_9_stats, team_9_opp_stats = get_team_stats(team_9, team_stats, opp_stats)
    team_10_stats, team_10_opp_stats = get_team_stats(team_10, team_stats, opp_stats)
    wteam_7_stats, wteam_7_opp_stats = get_team_stats(wteam_7, team_stats, opp_stats)
    wteam_8_stats, wteam_8_opp_stats = get_team_stats(wteam_8, team_stats, opp_stats)
    wteam_9_stats, wteam_9_opp_stats = get_team_stats(wteam_9, team_stats, opp_stats)
    wteam_10_stats, wteam_10_opp_stats = get_team_stats(wteam_10, team_stats, opp_stats)

    east_seven_seed, east_7v10_loser = simulate_game(team_7_stats, team_8_stats, team_7_opp_stats, team_8_opp_stats)
    
    west_seven_seed, west_7v10_loser = simulate_game(wteam_7_stats, wteam_8_stats, wteam_7_opp_stats, wteam_8_opp_stats)
    
    east_9v10_winner, elim = simulate_game(team_9_stats, team_10_stats, team_9_opp_stats, team_10_opp_stats)
    west_9v10_winner, elim2 = simulate_game(wteam_9_stats, wteam_10_stats, wteam_9_opp_stats, wteam_10_opp_stats)

    if east_7v10_loser == team_8 and east_9v10_winner == team_9:
        east_eight_seed, elim3 = simulate_game(team_8_stats, team_9_stats, team_8_opp_stats, team_9_opp_stats)
    elif east_7v10_loser == team_8 and east_9v10_winner == team_10:
        east_eight_seed, elim3 = simulate_game(team_8_stats, team_10_stats, team_8_opp_stats, team_10_opp_stats)
    elif east_7v10_loser == team_7 and east_9v10_winner == team_9:
        east_eight_seed, elim3 = simulate_game(team_7_stats, team_9_stats, team_7_opp_stats, team_9_opp_stats)
    else :
        east_eight_seed, elim3 = simulate_game(team_7_stats, team_10_stats, team_7_opp_stats, team_10_opp_stats)
    
    if west_7v10_loser == wteam_8 and west_9v10_winner == wteam_9:
        west_eight_seed, elim3 = simulate_game(wteam_8_stats, wteam_9_stats, wteam_8_opp_stats, wteam_9_opp_stats)
    elif west_7v10_loser == wteam_8 and west_9v10_winner == wteam_10:
        west_eight_seed, elim3 = simulate_game(wteam_8_stats, wteam_10_stats, wteam_8_opp_stats, wteam_10_opp_stats)
    elif west_7v10_loser == wteam_7 and west_9v10_winner == wteam_9:
        west_eight_seed, elim3 = simulate_game(wteam_7_stats, wteam_9_stats, wteam_7_opp_stats, wteam_9_opp_stats)
    else:
        west_eight_seed, elim3 = simulate_game(wteam_7_stats, wteam_10_stats, wteam_7_opp_stats, wteam_10_opp_stats)
    
    east_playoffs = (east_st[['Team', 'Seed']]).loc[0:7]
    east_playoffs.loc[6, 'Team'] = east_seven_seed
    east_playoffs.loc[7, 'Team'] = east_eight_seed
    west_playoffs = (west_st[['Team', 'Seed']]).loc[0:7]
    west_playoffs.loc[6, 'Team'] = west_seven_seed
    west_playoffs.loc[7, 'Team'] = west_eight_seed

    east_playoffs = east_playoffs[['Team', 'Seed']].to_dict(orient='records')  
    west_playoffs = west_playoffs[['Team', 'Seed']].to_dict(orient='records')

    return east_playoffs, west_playoffs
    
    
def simulate_game(team1_stats, team2_stats, team1_opp_stats, team2_opp_stats) :
    team1_score = 1 # home court advantage
    team2_score = 0
    
    # Fewer team turnovers is better, as well as forcing more opponent turovers
    if team1_stats["Turnovers"] > team2_stats["Turnovers"] :
        team2_score+=1
    else :
        team1_score+=1

    if team1_opp_stats["Opponent Turnovers"] > team2_opp_stats["Opponent Turnovers"] :
        team1_score+=1
    else :
        team2_score+=1
        
    team1_stats_new = team1_stats.drop(['Team', 'Turnovers'])
    team2_stats_new = team2_stats.drop(['Team', 'Turnovers'])
    team1_opp_stats_new = team1_opp_stats.drop(['Team', 'Opponent Turnovers'])
    team2_opp_stats_new = team2_opp_stats.drop(['Team', 'Opponent Turnovers'])
    
    for stat1, stat2 in zip(team1_stats_new.values, team2_stats_new.values):  
        if stat1 > stat2:
            team1_score += 1
        elif stat1 < stat2:
            team2_score += 1
    for stat1, stat2 in zip(team1_opp_stats_new.values, team2_opp_stats_new.values):  
        if stat1 < stat2:
            team1_score += 1
        elif stat1 > stat2:
            team2_score += 1
            
    total_score = team1_score + team2_score
    team1_chance = team1_score / total_score  
    team2_chance = team2_score / total_score 
    
    rand = random.random()  
    if team1_chance > rand:
        print(team1_stats.iloc[0] + " defeat " + team2_stats.iloc[0])
        return(team1_stats.iloc[0], team2_stats.iloc[0])
    else:
        print(team2_stats.iloc[0] + " defeat " + team1_stats.iloc[0])
        return(team2_stats.iloc[0], team1_stats.iloc[0])

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/' 

east_st = pd.read_csv(data_folder_path + "updated_standings_e.csv")
west_st = pd.read_csv(data_folder_path + "updated_standings_w.csv")
team_stats = pd.read_csv(data_folder_path + "team_stats.csv")
opp_stats = pd.read_csv(data_folder_path + "opp_stats.csv")

east_playIn = get_play_in_teams(east_st)
west_playIn = get_play_in_teams(west_st)

east, west = simulate_bracket(east_playIn, west_playIn, team_stats, opp_stats)

east_df = pd.DataFrame(east)  
west_df = pd.DataFrame(west) 

east_df.to_csv(data_folder_path + 'east_playoffs.csv', index=False)
west_df.to_csv(data_folder_path + 'west_playoffs.csv', index=False)


# In[ ]:





# In[ ]:




