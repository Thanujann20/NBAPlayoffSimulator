#!/usr/bin/env python
# coding: utf-8

# In[127]:

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from Simulation.playIn import get_team_stats, simulate_game


def simulate_bracket(east, west, team_stats, opp_stats):
    
    east_teams = east.iloc[:8]['Team'].tolist()
    west_teams = west.iloc[:8]['Team'].tolist()
    
    east_team_stats = [get_team_stats(team, team_stats, opp_stats)[0] for team in east.iloc[:8]['Team']]
    east_opp_stats = [get_team_stats(team, team_stats, opp_stats)[1] for team in east.iloc[:8]['Team']]
    
    west_team_stats = [get_team_stats(team, team_stats, opp_stats)[0] for team in west.iloc[:8]['Team']]
    west_opp_stats = [get_team_stats(team, team_stats, opp_stats)[1] for team in west.iloc[:8]['Team']]

    # Round 1 (1v8, 4v5, 2v6, 2v7)
    print("\n---------First Round---------")
    east_1_winner = simulate_game(east_team_stats[0], east_team_stats[7], east_opp_stats[0], east_opp_stats[7])
    east_2_winner = simulate_game(east_team_stats[3], east_team_stats[4], east_opp_stats[3], east_opp_stats[4])
    east_3_winner = simulate_game(east_team_stats[2], east_team_stats[5], east_opp_stats[2], east_opp_stats[5])
    east_4_winner = simulate_game(east_team_stats[1], east_team_stats[6], east_opp_stats[1], east_opp_stats[6])
    
    west_1_winner = simulate_game(west_team_stats[0], west_team_stats[7], west_opp_stats[0], west_opp_stats[7])
    west_2_winner = simulate_game(west_team_stats[3], west_team_stats[4], west_opp_stats[3], west_opp_stats[4])
    west_3_winner = simulate_game(west_team_stats[2], west_team_stats[5], west_opp_stats[2], west_opp_stats[5])
    west_4_winner = simulate_game(west_team_stats[1], west_team_stats[6], west_opp_stats[1], west_opp_stats[6])

    # Conference SemiFinals 
    print("\n---------Conference Semi Finals---------")
    east_round1_winners = [east_1_winner[0], east_2_winner[0], east_3_winner[0], east_4_winner[0]]
    west_round1_winners = [west_1_winner[0], west_2_winner[0], west_3_winner[0], west_4_winner[0]]

    east_indices = [east_teams.index(team) for team in east_round1_winners]
    west_indices = [west_teams.index(team) for team in west_round1_winners]
    
    east_1vs2_winner = simulate_game(east_team_stats[east_indices[0]], east_team_stats[east_indices[1]], east_opp_stats[east_indices[0]], east_opp_stats[east_indices[1]])
    east_3vs4_winner = simulate_game(east_team_stats[east_indices[2]], east_team_stats[east_indices[3]], east_opp_stats[east_indices[2]], east_opp_stats[east_indices[3]])
    
    west_1vs2_winner = simulate_game(west_team_stats[west_indices[0]], west_team_stats[west_indices[1]], west_opp_stats[west_indices[0]], west_opp_stats[west_indices[1]])
    west_3vs4_winner = simulate_game(west_team_stats[west_indices[2]], west_team_stats[west_indices[3]], west_opp_stats[west_indices[2]], west_opp_stats[west_indices[3]])

    # Conference Finals
    print("\n---------Conference Finals---------")
    east_round2_winners = [east_1vs2_winner[0], east_3vs4_winner[0]]
    west_round2_winners = [west_1vs2_winner[0], west_3vs4_winner[0]]

    east_indices = [east_teams.index(team) for team in east_round2_winners]
    west_indices = [west_teams.index(team) for team in west_round2_winners]
    
    east_winner = simulate_game(east_team_stats[east_indices[0]], east_team_stats[east_indices[1]], east_opp_stats[east_indices[0]], east_opp_stats[east_indices[1]])
    west_winner = simulate_game(west_team_stats[west_indices[0]], west_team_stats[west_indices[1]], west_opp_stats[west_indices[0]], west_opp_stats[west_indices[1]])
    
    # Finals
    print("\n---------NBA Finals---------")
    east_rep = east_teams.index(east_winner[0])
    west_rep = west_teams.index(west_winner[0])

    champion = simulate_game(east_team_stats[east_rep], west_team_stats[west_rep], east_opp_stats[east_rep], west_opp_stats[west_rep])
    return champion[0]

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/' 

east_st = pd.read_csv(data_folder_path + "east_playoffs.csv")
west_st = pd.read_csv(data_folder_path + "west_playoffs.csv")
team_stats = pd.read_csv(data_folder_path + "team_stats.csv")
opp_stats = pd.read_csv(data_folder_path + "opp_stats.csv")

champion = simulate_bracket(east_st, west_st, team_stats, opp_stats)
print(f"The {champion} have won the NBA Finals!")


# In[ ]:





# In[ ]:




