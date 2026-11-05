import json

open_data_path = "/Users/harryc/projects/open-data/data"


def load_matches_data(matches, match_file):
    ### Used to get the match_id within matches
    with open(f"{open_data_path}/matches/{matches}/{match_file}.json", "r") as file:
        data = json.load(file)
    return data


def load_event_data(event_id):
    ### Used to get the event data.
    ### Event id is retrieved from load_matches_data
    with open(f"{open_data_path}/events/{event_id}.json", "r") as file:
        data = json.load(file)
    return data

def load_lineups_data(match_id):
    # Used to retrieve lineup information used to determine playing time
    with open(f"{open_data_path}/lineups/{match_id}.json", "r") as file:
        data = json.load(file)
    return data
