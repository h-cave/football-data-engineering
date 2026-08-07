from loader import load_matches_data, load_event_data
from metrics import get_match_metrics

import time
start_time = time.time()
## Load the match
match_event_ids = load_matches_data()

# event_data = load_event_data(3754217)
# match_data = get_match_metrics("Chelsea", "Arsenal", event_data)
# # print(match_data)

# Load the event
for matches in match_event_ids:
    event_data = load_event_data(matches["match_id"])
    home_team = matches["home_team"]["home_team_name"]
    away_team = matches["away_team"]["away_team_name"]
    print(matches["match_id"])
    match_data = get_match_metrics(home_team, away_team, event_data, matches["match_id"])
    print(match_data)
    # Call a method in metrics. This method will call all the metrics methods and return a Dict object with the key values being the metrics. 

print(f"--- {time.time() - start_time} seconds ---")

# Calculate the metrics


# print the summary