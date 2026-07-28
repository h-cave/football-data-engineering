import json

open_data_path = "/home/harry/projects/open-data/data"

def which_team_passed(data):
    if data['possession_team']['name'] == "Everton":
            return 'Everton'
    else:
        return 'Arsenal'

with open(f"{open_data_path}/events/3749493.json", "r") as file:
    data = json.load(file)

home_team = data[0]["team"]["name"]
away_team = data[1]["team"]["name"]

records = 0
passes = 0
passes_in_open_play = 0

total_away_team_passes = 0
total_home_team_passes = 0

open_play_passes_away_team = 0
open_play_passes_home_team = 0

total_home_team_shots = [shot for shot in data[0:-1] if shot['type']['name'] == "Shot" and shot['possession_team']['name'] == home_team]
total_away_team_shots = [shot for shot in data[0:-1] if shot['type']['name'] == "Shot" and shot['possession_team']['name'] == away_team]

home_team_xg_score = sum([shot['shot'].get('statsbomb_xg') for shot in total_home_team_shots])
away_team_xg_score = sum([shot['shot'].get('statsbomb_xg') for shot in total_away_team_shots])

home_team_goals = [shot['shot']['outcome'].get('name') == 'Goal' for shot in total_home_team_shots]
away_team_goals = [shot['shot']['outcome'].get('name') == 'Goal' for shot in total_away_team_shots]

total_home_team_corners = [corner for corner in data[0:-1] if corner['type']['name'] == "Corner" and corner['possession_team']['name'] == home_team]
total_away_team_corners = [corner for corner in data[0:-1] if corner['type']['name'] == "Corner" and corner['possession_team']['name'] == away_team]

fouls_home_team = [fouls for fouls in data[0:-1] if fouls["type"].get('name') == "Foul Committed" and fouls['team']['name'] == home_team]
fouls_away_team = [fouls for fouls in data[0:-1] if fouls["type"].get('name') == "Foul Committed" and fouls['team']['name'] == away_team]

cards_home_team = [yellow_card for yellow_card in fouls_home_team if yellow_card.get('foul_committed') and yellow_card.get('foul_committed', "None").get('card')]
cards_away_team = [yellow_card for yellow_card in fouls_away_team if yellow_card.get('foul_committed') and yellow_card.get('foul_committed', "None").get('card')]

yellow_card_home_team = [card for card in cards_home_team if card.get("foul_committed")['card']['name'] in ["Yellow Card", "Second Yellow"]]
yellow_card_away_team = [card for card in cards_away_team if card.get("foul_committed")['card']['name'] in ["Yellow Card", "Second Yellow"]]

red_card_home_teams = [card for card in cards_home_team if card.get("foul_committed")['card']['name'] in ["Red Card", "Second Yellow"]]
red_card_away_teams = [card for card in cards_away_team if card.get("foul_committed")['card']['name'] in ["Red Card", "Second Yellow"]]


for data in data:
    records += 1
    #print(f"data: {data}")
    #print(f"Record {records}: {data['type']['name']}")
    if data['type']['name'] == "Pass":
        passes += 1
        team = which_team_passed(data)
        if data['play_pattern']['name'] in ["Regular Play", "From Keeper"]:
            passes_in_open_play += 1
            if team == away_team:
                open_play_passes_away_team += 1
                total_away_team_passes += 1
            else:
                open_play_passes_home_team += 1
                total_home_team_passes += 1
        else:
            if team == away_team:
                total_away_team_passes += 1
            else:
                total_home_team_passes += 1

# print("XG")

#print("Goals")

# # print(away_team_xg_score)
# print(home_team_xg_score)
# print(away_team_xg_score)
# print("hots")
# print(total_home_team_shots)
# print(total_away_team_shots)
# print("fouls_home_team")      
# print(fouls_home_team)

# print("cards Arsenal")
# print(cards_home_team)

# print(f"yellow cards {home_team}")
# print(yellow_card_home_team)

# print(f"yellow cards {away_team}")
# print(yellow_card_away_team)

# print(len(cards_home_team))
# print(len(cards_away_team))
# print("fouls_away_team")
# print(fouls_away_team)

#print(f"red card: {red_card_away_teams}")



print(f"""
============================================
Match Summary
============================================
Home Team: {home_team}
Away Team: {away_team}

Total Evnts: {records}

XG
-----------------
{home_team} XG: {home_team_xg_score}
{away_team} XG: {away_team_xg_score}

Goals
-----------------
{home_team} Goals: {home_team_goals.count(True)}
{away_team} Goals: {away_team_goals.count(True)}

Passed
-----------------
{home_team} Passes: {total_home_team_passes}
{away_team} Passes: {total_away_team_passes}

Open Play Passes
-----------------
{home_team} Open Play Passes: {open_play_passes_home_team}
{away_team} Open Play Passes: {open_play_passes_away_team}

Total Passes
-----------------
Total Passes: {passes}

Shots
-----------------
{home_team} Shots: {len(total_home_team_shots)}
{away_team} Shots: {len(total_away_team_shots)}

Corners
-----------------
{home_team} Corners: {len(total_home_team_corners)}
{away_team} Corners: {len(total_away_team_corners)}

Fouls Committed
-----------------
{home_team} Fouls Committed: {len(fouls_home_team)}
{away_team} Fouls Committed: {len(fouls_away_team)}

Yellow Cards
-----------------
{home_team} Yellow Cards: {len(yellow_card_home_team)}
{away_team} Yellow Cards: {len(yellow_card_away_team)}

Red Cards
-----------------
{home_team} Red Cards: {len(red_card_home_teams)}
{away_team} Red Cards: {len(red_card_away_teams)}
"""
)


# print ("#########RECORDS#########")
# print(f"Total Records: {records}")
# print(f"Total Passes: {passes}")
# print(f"Everton Passes: {total_everton_passes}")
# print(f"Arsenal Passes: {total_arsenal_passes}")
# print(f"Passes in Open Play: {passes_in_open_play}")
# print(f"Open Play Passes Everton: {open_play_passes_everton}")
# print(f"Open Play Passes Arsenal: {open_play_passes_arsenal}")
# print ("#########data#########")
# print(f"LENGTH:{len(data)}")
# print(data)
# print("Data type")
# print(type(data))


# res = next(iter(data))
# print(f"First record: {res}")
