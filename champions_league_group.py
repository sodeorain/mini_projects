# create df , team name , matches played, matches won, matches drawn, matches lost, goals for, goals against, points 
import pandas as pd
import random



def run_matchday(table, fixtures_table):
    for i in range(1, 6):
        print(f"\nMatchday {i}")
        
        # First match
        home_team = random.randint(1, 4)
        away_team = random.choice([j for j in range(1, 5) if j != home_team])
        print(f"Team {home_team} vs. Team {away_team}")
        home_score = int(input(f"Team {home_team} score: "))
        away_score = int(input(f"Team {away_team} score: "))
        print(f"FT - Team {home_team} {home_score}:{away_score} Team {away_team}")
        update_stats(table, home_team, away_team, home_score, away_score)

        # Second match
        remaining_teams = [j for j in range(1, 5) if j not in [home_team, away_team]]
        home_team_2 = remaining_teams[0]
        away_team_2 = remaining_teams[1]
        print(f"Team {home_team_2} vs. Team {away_team_2}")
        home_score_2 = int(input(f"Team {home_team_2} score: "))
        away_score_2 = int(input(f"Team {away_team_2} score: "))
        print(f"FT - Team {home_team_2} {home_score_2}:{away_score_2} Team {away_team_2}")
        update_stats(table, home_team_2, away_team_2, home_score_2, away_score_2)
        
        record_fixtures(fixtures_table, home_team, away_team, home_team_2, away_team_2)
        print(fixtures_table)
        print("\nUpdated Table:")
        print(table)


def record_fixtures(fixtures_table, team1, team2, team3, team4):
    fixtures_table.loc[len(fixtures_table)] = [team1, team2]
    fixtures_table.loc[len(fixtures_table)] = [team3, team4]
    return fixtures_table



def update_stats(table, home_team, away_team, home_score, away_score):
    table.loc[table["Team"] == f"Team {home_team}", "Goals For"] += home_score
    table.loc[table["Team"] == f"Team {home_team}", "Goals Against"] += away_score
    table.loc[table["Team"] == f"Team {away_team}", "Goals For"] += away_score
    table.loc[table["Team"] == f"Team {away_team}", "Goals Against"] += home_score
    table.loc[table["Team"] == f"Team {home_team}", "Matches Played"] += 1
    table.loc[table["Team"] == f"Team {away_team}", "Matches Played"] += 1
    if home_score > away_score:
        table.loc[table["Team"] == f"Team {home_team}", "Points"] += 3
    elif home_score < away_score:
        table.loc[table["Team"] == f"Team {away_team}", "Points"] += 3
    else:
        table.loc[table["Team"] == f"Team {home_team}", "Points"] += 1
        table.loc[table["Team"] == f"Team {away_team}", "Points"] += 1
    table["Goal Difference"] = table["Goals For"] - table["Goals Against"]

    # Sort the table by Points and Goal Difference (descending)
    table.sort_values(by=["Points", "Goal Difference"], ascending=False, inplace=True)

        



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
    match_fixtures = pd.DataFrame(columns=["Home Team", "Away Team"])

    # Create the DataFrame
    df = pd.DataFrame(data)
    while True:
        run_matchday(df, match_fixtures)
          
play_game()



###########################
    # Update Matches Played
    #table.loc[table["Team"] == f"Team {home_team}", "Matches Played"] += 1
   # table.loc[table["Team"] == f"Team {away_team}", "Matches Played"] += 1

