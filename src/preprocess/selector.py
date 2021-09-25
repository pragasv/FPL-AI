"""
The purpose of this code segment is to filter out the top 11 players based on points each week
Additionally conditions to max 3 players per team should be implemented together with position wise max capacity
"""

import pandas as pd

import data
from src.visualizer.visualize import pitch_view
from utils import *


# columns we are intrested in
COLUMNS = ['name', 'position', 'team', 'xP', 'assists', 'bonus', 'bps',
       'clean_sheets', 'creativity', 'element', 'fixture', 'goals_conceded',
       'goals_scored', 'ict_index', 'influence', 'minutes',
       'opponent_team', 'own_goals', 'penalties_missed', 'penalties_saved',
       'red_cards', 'saves', 'threat', 'total_points', 'transfers_balance',
       'transfers_in', 'transfers_out', 'was_home', 'yellow_cards']

df = pd.read_csv('data/2020-21/gws/gw1.csv')
df = df[COLUMNS]

df_forwards = pick_forwards(df)
df_midfielders = pick_midfielders(df)
df_defenders = pick_defenders(df)
df_keepers = pick_keepers(df)

forwards = df_forwards['name'].tolist()
midfields = df_midfielders['name'].tolist()
defenders = df_defenders['name'].tolist()
keepers = df_keepers['name'].tolist()


pitch_view(forwards, midfields, defenders, keepers)

## TODO: transform opponent_team code --> difficulty rating

