import json

open_data_path = "/home/harry/projects/open-data/data"

def load_event_data(event_id):
    ### Used to get the event data.
    ### Event id is retrieved from load_matches_data
    with open(f"{open_data_path}/events/{event_id}.json", "r") as file:
        data = json.load(file)
    return data
