#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

url = 'https://www.basketball-reference.com/leagues/NBA_2025_standings.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
soup.find('div', class_='section_heading assoc_confs_standings_E').decompose()
soup.find('div', class_='footer no_hide_long').decompose()

east_standings = soup.find(id='all_confs_standings_E')
west_standings = soup.find(id='all_confs_standings_W')
east_standings_str = str(east_standings)
west_standings_str = str(west_standings)

east = StringIO(east_standings_str)
east_df = pd.read_html(east)[0]
west = StringIO(west_standings_str)
west_df = pd.read_html(west)[0]

cleaned_e = east_df.loc[:, :'PA/G']
cleaned_w = west_df.loc[:, :'PA/G']
cleaned_e.rename(columns={'Eastern Conference': 'Team'}, inplace=True)
cleaned_w.rename(columns={'Western Conference': 'Team'}, inplace=True)

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/'

cleaned_e.to_csv(data_folder_path + 'standings_e.csv', index=False)
cleaned_w.to_csv(data_folder_path + 'standings_w.csv', index=False)


# In[ ]:





# In[ ]:




