import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template, request
from Simulation.playIn import simulate_bracket, get_play_in_teams
from Simulation.playOffs import simulate_bracket as simulate_playoffs

import pandas as pd # type: ignore

app = Flask(__name__)

data_folder_path = '/Users/thanujann/Documents/code/NBApredictor/Data/'
east_st = pd.read_csv(data_folder_path + "east_playoffs.csv")
west_st = pd.read_csv(data_folder_path + "west_playoffs.csv")
team_stats = pd.read_csv(data_folder_path + "team_stats.csv")
opp_stats = pd.read_csv(data_folder_path + "opp_stats.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/playin', methods=['GET'])
def playin():
    #east, west = simulate_playin(east_st, west_st, team_stats, opp_stats)
    east_st = pd.read_csv(data_folder_path + "updated_standings_e.csv")
    west_st = pd.read_csv(data_folder_path + "updated_standings_w.csv")
    
    east_playIn = get_play_in_teams(east_st)
    west_playIn = get_play_in_teams(west_st)
    return render_template('playin.html', east_playIn=east_playIn, west_playIn=west_playIn)  

@app.route('/playoffs')
def playoffs():
    return render_template('playoffs.html')

if __name__ == "__main__":
    app.run(debug=True)
