# create df , team name , matches played, matches won, matches drawn, matches lost, goals for, goals against, points 

import pandas as pd
import random

def run_matchday(table):
    for i in range(1,6):
        print(f"Matchday {i}")
        home_team = random.randint(1, 4)
        away_team = random.choice([i for i in range(1, 5) if i != home_team])
        print(f"Team {home_team} vs. Team {away_team}")
        home_team_score = input(f"Team {home_team} score: ")
        away_team_score = input(f"Team {away_team} score: ")
        print(f"FT - Team {home_team} {home_team_score}:{away_team_score} Team {away_team} ")
        table.loc[table["Team"] == f"Team {home_team}", "Goals For"] += home_team_score
        table.loc[table["Team"] == f"Team {away_team}", "Goals Against"] += away_team_score
        home_team_second_match = random.choice([i for i in range(1, 5) if i != home_team and i != away_team])
        away_team_second_match = random.choice([i for i in range(1, 5) if i != home_team and i != away_team and i!= home_team_second_match])
        print(f"Team {home_team_second_match} vs. Team {away_team_second_match}")
        home_team_second_match_score = input(f"Team {home_team_second_match} score: ")
        away_team_second_match_score = input(f"Team {away_team_second_match} score: ")
        print(f"FT - Team {home_team_second_match} {home_team_second_match_score}:{away_team_second_match_score} Team {away_team_second_match} ")
        table.loc[table["Team"] == f"Team {home_team_second_match}", "Goals For"] += home_team_second_match_score
        table.loc[table["Team"] == f"Team {away_team_second_match}", "Goals Against"] += away_team_second_match_score
        return table


def play_game():
    data = {
    "Team": ["Team 1", "Team 2", "Team 3", "Team 4"],
    "Matches Played": [0, 0, 0, 0],
    "Matches Won": [0, 0, 0, 0],
    "Matches Drawn": [0, 0, 0, 0],
    "Matches Lost": [0, 0, 0, 0],
    "Goals For": [0, 0, 0, 0],
    "Goals Against": [0, 0, 0, 0],
    "Goal Difference": [0, 0, 0, 0],
    "Points": [0, 0, 0, 0]
}
    # Create the DataFrame
    df = pd.DataFrame(data)
    while True:
          run_matchday(df)
          
play_game()



