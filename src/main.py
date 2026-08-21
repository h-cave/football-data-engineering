from loader import load_matches_data, load_event_data
from metrics import get_match_metrics
from summary import game_summary

import time
start_time = time.time()
## Load the match
match_event_ids = load_matches_data()


# Load the event
for matches in match_event_ids:
    event_data = load_event_data(matches["match_id"])
    home_team = matches["home_team"]["home_team_name"]
    away_team = matches["away_team"]["away_team_name"]
    match_data = get_match_metrics(home_team, away_team, event_data, matches["match_id"])
    game_summary_output = game_summary(match_data)
    print(game_summary_output)

print(f"--- {time.time() - start_time} seconds ---")

