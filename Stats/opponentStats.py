#!/usr/bin/env python
# coding: utf-8

# In[16]:


from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

opp_stats = leaguedashteamstats.LeagueDashTeamStats(
    measure_type_detailed_defense="Opponent", 
    season="2024-25", 
    per_mode_detailed="PerGame"
)
df = opp_stats.get_data_frames()[0]
df_opponent_stats = df[['TEAM_NAME', 'OPP_PTS', 'OPP_FG_PCT','OPP_FG3_PCT',
       'OPP_FT_PCT', 'OPP_REB','OPP_AST', 'OPP_TOV']]

df_opponent_stats = df_opponent_stats.rename(columns={
    'TEAM_NAME': 'Team',
    'OPP_PTS': 'Opponent Points',
    'OPP_FG_PCT': 'Opponent FG%',
    'OPP_3P_PCT': 'Opponent 3P%',
    'OPP_FT_PCT' : 'Opponent FT%',
    'OPP_REB': 'Opponent Rebounds',
    'OPP_AST': 'Opponent Assists',
    'OPP_TOV': 'Opponent Turnovers'
})

df_opponent_stats['Team'] = df_opponent_stats['Team'].replace('LA Clippers', 'Los Angeles Clippers')

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/'

df_opponent_stats.to_csv(data_folder_path + 'opp_stats.csv', index=False)


# In[ ]:




