#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import regex as re

stats_folder_path = "./Stats/"
east_st = pd.read_csv(stats_folder_path + "standings_e.csv")
west_st = pd.read_csv(stats_folder_path + "standings_w.csv")
east_so = pd.read_csv(stats_folder_path + "sos_e.csv")
west_so = pd.read_csv(stats_folder_path + "sos_w.csv")

east_st["Team"] = east_st["Team"].apply(lambda x: re.sub(r"\s*\(\d+\)", "", x).strip())
east_merged = east_st.merge(east_so, on="Team", how='outer')
west_st["Team"] = west_st["Team"].apply(lambda x: re.sub(r"\s*\(\d+\)", "", x).strip())
west_merged = west_st.merge(west_so, on="Team", how='outer')

numeric_columns_east = east_merged.select_dtypes(include=['float64', 'int64']).columns
east_merged[numeric_columns_east] = east_merged[numeric_columns_east].fillna(east_merged[numeric_columns_east].mean())
numeric_columns_west = west_merged.select_dtypes(include=['float64', 'int64']).columns
west_merged[numeric_columns_west] = west_merged[numeric_columns_west].fillna(west_merged[numeric_columns_west].mean())

east_merged["Projected wins"] = round(((82 - (east_merged["W"] + east_merged["L"])) * east_merged['W/L%'] - east_merged['SOS'] * 0.5) + east_merged['W'])
west_merged["Projected wins"] = round(((82 - (west_merged["W"] + west_merged["L"])) * west_merged['W/L%'] - west_merged['SOS'] * 0.5) + west_merged['W'])

sorted_east = east_merged.sort_values(by='Projected wins', ascending=False)
sorted_west = west_merged.sort_values(by='Projected wins', ascending=False)

sorted_east['Seed'] = range(1, 16)
sorted_west['Seed'] = range(1, 16)

sorted_east.to_csv(stats_folder_path + "updated_standings_e.csv", index=False)
sorted_west.to_csv(stats_folder_path + "updated_standings_w.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




