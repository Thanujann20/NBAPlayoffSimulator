#!/usr/bin/env python
# coding: utf-8

# In[14]:


from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

team_stats = leaguedashteamstats.LeagueDashTeamStats(
    season="2024-25",      
    per_mode_detailed="PerGame",  
)

df = team_stats.get_data_frames()[0]
df_team_stats = df[['TEAM_NAME', 'PTS', 'FG_PCT','FG3_PCT',
       'FT_PCT', 'REB', 'AST', 'TOV', 'PLUS_MINUS' ]]

df_team_stats = df_team_stats.rename(columns={
    'TEAM_NAME': 'Team',
    'PTS': 'Points',
    'FG_PCT': 'FG%',
    '3P_PCT': '3P%',
    'FT_PCT' : 'FT%',
    'REB': 'Rebounds',
    'AST': 'Assists',
    'TOV': 'Turnovers',
    'PLUS_MINUS': '+/-'
})

df_team_stats['Team'] = df_team_stats['Team'].replace('LA Clippers', 'Los Angeles Clippers')

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/'
df_team_stats.to_csv(data_folder_path + 'team_stats.csv', index=False)



# In[ ]:





# In[ ]:




