def get_match_metrics(home_team, away_team, event_data, match_id):
    ## This method will call all other metrics methods and will return a dict object e.g.
    ## total_home_shots: 5
    metrics = {
        "match_id": match_id,
        "home_team": home_team,
        "away_team": away_team, 
        "shot_data": analyse_shots(home_team, away_team, event_data),
        "pass_data": pass_data(home_team, away_team, event_data),
        "corener_data": corners(home_team, away_team, event_data)
    }
    
    return metrics

def analyse_shots(home_team, away_team, event_data):
    
    shots_data = {
            "total_home_team_shots": 0,
            "total_away_team_shots": 0,
            "home_team_xg_score": 0,
            "away_team_xg_score": 0,
            "home_team_goals": 0,
            "away_team_goals": 0
        }

    for shots in event_data:
        if shots['type']['name'] in ["Shot"]:
            if shots['possession_team']['name'] == home_team:
                shots_data["total_home_team_shots"] += 1
                shots_data["home_team_xg_score"] += shots['shot']['statsbomb_xg']
                if shots['shot']['outcome'].get('name') == 'Goal':
                    shots_data["home_team_goals"] += 1

            else:
                shots_data["total_away_team_shots"] += 1
                shots_data["away_team_xg_score"] += shots['shot']['statsbomb_xg']
                if shots['shot']['outcome'].get('name') == 'Goal':
                    shots_data["away_team_goals"] += 1

        ## We need a seperate if to check for own goals
        if shots['type']['name'] == "Own Goal For":
            if shots['possession_team']['name'] == home_team:
                shots_data["home_team_goals"] += 1
            else:
                shots_data["away_team_goals"] += 1

    return shots_data

def pass_data(home_team, away_team, event_data):

    pass_data = {
        "passes": 0,
        "passes_in_open_play": 0,
        "total_home_team_passes": 0,
        "total_away_team_passes": 0,
        "open_play_passes_home_team": 0,
        "open_play_passes_away_team": 0,
    }

    for data in event_data:
        if data['type']['name'] == "Pass":
            pass_data['passes'] += 1

            ## We check if the pass has come from a type that isn't "open play"
            if data['pass'].get("type", {}).get("name", None) in ["Goal Kick", "Corner", "Throw-in", "kick Off", "Free Kick"]:
                continue

            ## We check if the play_pattern is in "open play"
            if data['play_pattern']['name'] in ["Regular Play", "From Keeper", "From Goal Kick", "From Counter", "From Throw In"]:
                pass_data['passes_in_open_play'] += 1
                if data['possession_team']['name'] == home_team:
                    pass_data['open_play_passes_home_team'] += 1
                    pass_data['total_home_team_passes'] += 1
                else:
                    pass_data['open_play_passes_away_team'] += 1
                    pass_data['total_away_team_passes'] += 1
            else:
                if data['possession_team']['name'] == home_team:
                    pass_data['total_home_team_passes'] += 1
                else:
                    pass_data['total_away_team_passes'] += 1

    return pass_data

def corners(home_team, away_team, event_data):
    corners_data = {
        "home_team_corners": 0,
        "away_team_corners": 0
    }

    for corner in event_data:
        if corner['play_pattern']['name'] == "From Corner":
            if corner.get("pass", {}).get("type", {}).get("name", {}) == 'Corner':
                if corner['possession_team']['name'] == home_team:
                    corners_data['home_team_corners'] += 1
                else:
                    corners_data['away_team_corners'] += 1

    return corners_data
 
### These all need methods to create reusable code

# total_home_team_corners = [corner for corner in data[0:-1] if corner['type']['name'] == "Corner" and corner['possession_team']['name'] == home_team]
# total_away_team_corners = [corner for corner in data[0:-1] if corner['type']['name'] == "Corner" and corner['possession_team']['name'] == away_team]

# fouls_home_team = [fouls for fouls in data[0:-1] if fouls["type"].get('name') == "Foul Committed" and fouls['team']['name'] == home_team]
# fouls_away_team = [fouls for fouls in data[0:-1] if fouls["type"].get('name') == "Foul Committed" and fouls['team']['name'] == away_team]

# cards_home_team = [yellow_card for yellow_card in fouls_home_team if yellow_card.get('foul_committed') and yellow_card.get('foul_committed', "None").get('card')]
# cards_away_team = [yellow_card for yellow_card in fouls_away_team if yellow_card.get('foul_committed') and yellow_card.get('foul_committed', "None").get('card')]

# yellow_card_home_team = [card for card in cards_home_team if card.get("foul_committed")['card']['name'] in ["Yellow Card", "Second Yellow"]]
# yellow_card_away_team = [card for card in cards_away_team if card.get("foul_committed")['card']['name'] in ["Yellow Card", "Second Yellow"]]

# red_card_home_teams = [card for card in cards_home_team if card.get("foul_committed")['card']['name'] in ["Red Card", "Second Yellow"]]
# red_card_away_teams = [card for card in cards_away_team if card.get("foul_committed")['card']['name'] in ["Red Card", "Second Yellow"]]
