from datetime import timedelta

def minutes_played(event, player_id):
    starting_lineup = []
    for minutes_played in event:
        strating_lineup_check = "Not Done"
        if minutes_played["index"] == 1:
            #print(minutes_played["tactics"]["lineup"])
            for player in minutes_played["tactics"]["lineup"]:
                if player["player"]["id"] == player_id:
                    #print("PLAYER IN STARTING XI")
                    #print(f"PLAYER DATA: {player}")
                    print('')
                else:
                    #find_when_player_came_on(event, player_id)
                    continue
        # Issue here, we dont check when a player comes on to the pitch. So there played minutes is alwasy the minutes they cam off. 
        # This should be minutes they came off minus the minutes they missed. 
        # so, a player come on on the 80th minute. there play time should be minute they came off (or game end) - time they came on. 
        # if game lasts until 95th minute their play time will be 95 - 80 = 15 minutes
        if minutes_played.get("player", {}).get("id", {}) == player_id:

        
            if minutes_played.get("foul_committed", {}).get("card", {}).get("name") == ["Second Yellow", "Red Card"]:
                played_minutes = f"{minutes_played['minute']}: {minutes_played['second']}"

                return played_time_format(played_minutes)

            if minutes_played.get("type", {}).get("name", {}) in ["Substitution", "Player Off"]:
                if minutes_played.get("substitution", {}).get("replacement", {}).get("id") == player_id:
                    continue
                played_minutes = f"{minutes_played['minute']}: {minutes_played['second']}"

                return played_time_format(played_minutes)

        elif minutes_played["period"] == 2 and minutes_played["type"]["name"] == "Half End":
            
            played_minutes = f"{minutes_played['minute']}: {minutes_played['second']}"

            return played_time_format(played_minutes)
        else:
            continue



def played_time_format(played_minutes):

    # 1. Split and convert to integers
    minutes, seconds = map(int, played_minutes.split(":"))

    # 2. Create a timedelta object
    duration = timedelta(minutes=minutes, seconds=seconds)

    return duration.total_seconds()



###Events that cause a player to leave the field
# type: Player Off
# type: substitution
# foul_committed - card: Second Yellow