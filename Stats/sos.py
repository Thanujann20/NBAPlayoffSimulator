#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

url = 'https://www.basketball-reference.com/friv/playoff_prob.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

east_sos = soup.find(id='all_projected_standings_e')
west_sos = soup.find(id='all_projected_standings_w')
east_sos_str = str(east_sos)
west_sos_str = str(west_sos)

east_s = StringIO(east_sos_str)
east_df = pd.read_html(east_s)[0]
west_s = StringIO(west_sos_str)
west_df = pd.read_html(west_s)[0]
east_cleaned = east_df[[('Unnamed: 1_level_0', 'Eastern Conference'), ('Unnamed: 6_level_0', 'rSOS')]]
west_cleaned = west_df[[('Unnamed: 1_level_0', 'Western Conference'), ('Unnamed: 6_level_0', 'rSOS')]]

east_cleaned.columns = ['Team', 'SOS']
east_cleaned = east_cleaned.dropna()
west_cleaned.columns = ['Team', 'SOS']
west_cleaned = west_cleaned.dropna()

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/' 

east_cleaned.to_csv(data_folder_path + 'sos_e.csv', index=False)
west_cleaned.to_csv(data_folder_path + 'sos_w.csv', index=False)




# In[ ]:





# In[ ]:




