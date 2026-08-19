###Summary will return a dict summary of the game. The data will be passed from main which gets it from metrics.py

def game_summary(match_data):
    print(f"""

    ==========================================================
    score: {match_data["home_team"]}: {match_data["shot_data"]["home_team_goals"]} - {match_data["shot_data"]["away_team_goals"]} :{match_data["away_team"]}

    total passes: {match_data["pass_data"]["passes"]}
    open play passes: {match_data["pass_data"]["passes_in_open_play"]}
    ==========================================================
    Home team: {match_data["home_team"]}     -       Away team: {match_data["away_team"]}
    ========================================================== 

    Shot data:              
    goals: {match_data["shot_data"]["home_team_goals"]}                   -     {match_data["shot_data"]["away_team_goals"]}  
    total_shots: {match_data["shot_data"]["total_home_team_shots"]}            -      {match_data["shot_data"]["total_away_team_shots"]}
    xg_score: {match_data["shot_data"]["home_team_xg_score"]}     -     {match_data["shot_data"]["away_team_xg_score"]}
    
    Pass data:
    total_passes: {match_data["pass_data"]["total_home_team_passes"]}           -      {match_data["pass_data"]["total_away_team_passes"]}
    passes_in_open_play: {match_data["pass_data"]["open_play_passes_home_team"]}     -     {match_data["pass_data"]["open_play_passes_away_team"]}

    Corner data:
    total_corners: {match_data["corner_data"]["home_team_corners"]}     -     {match_data["corner_data"]["away_team_corners"]}
    
    Foul data:
    total_fouls: {match_data["foul_data"]["fouls_home_team"]}     -     {match_data["foul_data"]["fouls_away_team"]}
    yellow_cards: {match_data["foul_data"]["yellow_card_home_team"]}     -     {match_data["foul_data"]["yellow_card_away_team"]}
    red_cards: {match_data["foul_data"]["red_card_home_teams"]}     -     {match_data["foul_data"]["red_card_away_teams"]}
    ==========================================================
    """)