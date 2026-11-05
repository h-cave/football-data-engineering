from loader import load_lineups_data

###Events that cause a player to leave the field
# type: Player Off
# type: substitution
# foul_committed - card: Second Yellow

def minutes_played(end_of_game_time, player_id, match_id):
    lineup_data = load_lineups_data(match_id)
    for played_minutes in lineup_data:
        for lineup in played_minutes["lineup"]:
            if lineup["player_id"] == player_id:
                if not lineup["positions"]:
                    continue
            
                player_dismissed = False
                dismisal_time = ""
                
                for time in lineup["cards"]:
                    if time["card_type"] in  ["Red Card", "Second Yellow"]:
                        dismisal_time = time["time"]
                        player_dismissed = True
                        return get_player_minutes(lineup["positions"],  end_of_game_time, dismisal_time)
                if player_dismissed == False:
                    return get_player_minutes(lineup["positions"], end_of_game_time)
    print('')


def get_player_minutes(player_positions,  end_game_time, dismisal_time=""):
    game_time = {
        "from": "",
        "to": ""
    }
    print(end_game_time)

    if len(player_positions) > 1:
        if dismisal_time:
            game_time["to"] = dismisal_time
            print("PLAYER DISMISSED")
            game_time["from"] = player_positions[0].get("from")
        else:
            game_time["from"] = player_positions[0].get("from")
            game_time["to"] = player_positions[-1].get("to")

    else:
        game_time["from"] = player_positions[0].get("from")
        game_time["to"] = player_positions[0].get("to")

    
    if not game_time["to"]:
        game_time["to"] = end_game_time

    return calculate_playing_time(game_time)


def calculate_playing_time(playing_time):
    # Split and convert to seconds directly inline
    start_seconds = int(playing_time["from"].split(':')[0]) * 60 + int(playing_time["from"].split(':')[1])
    end_seconds = int(playing_time["to"].split(':')[0]) * 60 + int(playing_time["to"].split(':')[1])

    # Calculate the difference in seconds
    duration_seconds = end_seconds - start_seconds

    return duration_seconds
    
    
    
##Plan
# pass the game id through to minutes played - DONE
# pass the end of the second half through to minutes played to gather the end time of the second half from the event data - DONE
# load up the linups event
# find the players from - to metrics. Note, if a players position is an empty list, they did not play
# If a players "position" list is greater than 1 it means they played in more than one position. In these circumstances i will get the from time in index 0 and the to time in index -1 to work out total playeing time.
# Note, if a player gets a red card then the positions list isn't always correct. For sake of this use the time in the cards list to indicate when the player left the pitch and the from in the positions list to indicate when they came on
# If their to metric is null - this becomes the passed through end of match timedelta
# if their start time is "00:00" and end time null - they played the entire game, give them the end of second half minutes time
# if there start time is "00:00" and end time is not null work out difference between the times
# if their starting time is not "00:00" and end time is null work out the difference, should be able to make this a function used for above to. 