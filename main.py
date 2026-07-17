import json

open_data_path = "/home/harry/projects/open-data/data"

def which_team_passed(data):
    if data['possession_team']['name'] == "Everton":
            return 'Everton'
    else:
        return 'Arsenal'

with open(f"{open_data_path}/events/3749493.json", "r") as file:
    data = json.load(file)

records = 0
passes = 0
passes_in_open_play = 0
total_everton_passes = 0
total_arsenal_passes = 0
open_play_passes_everton = 0
open_play_passes_arsenal = 0
for data in data:
    records += 1
    print(f"data: {data}")
    # print(f"Record {records}: {data['type']['name']}")
    if data['type']['name'] == "Pass":
        passes += 1
        team = which_team_passed(data)
        if data['play_pattern']['name'] in ["Regular Play", "From Keeper"]:
            passes_in_open_play += 1
            if team == 'Everton':
                open_play_passes_everton += 1
            else:
                open_play_passes_arsenal += 1
        else:
            if team == 'Everton':
                total_everton_passes += 1
            else:
                total_arsenal_passes += 1
        






print ("#########RECORDS#########")
print(f"Total Records: {records}")
print(f"Total Passes: {passes}")
print(f"Everton Passes: {total_everton_passes}")
print(f"Arsenal Passes: {total_arsenal_passes}")
print(f"Passes in Open Play: {passes_in_open_play}")
print(f"Open Play Passes Everton: {open_play_passes_everton}")
print(f"Open Play Passes Arsenal: {open_play_passes_arsenal}")
print ("#########data#########")
print(f"LENGTH:{len(data)}")
print(data)
print("Data type")
print(type(data))


res = next(iter(data))
print(f"First record: {res}")
