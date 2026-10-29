def score_formatter(currunt_score, new_score):
    ## The current is the players score
    ## The new score is the most recent games score
    ## We check if the player is in the current score and if they are find their id and add the new score
    ## if they aren't we just add them in with the current score
    for key in new_score:
        if key in currunt_score:
            sucess_actions = new_score[key]["sucesfull_action"]
            total_actions = new_score[key]["total_actions"]
            seconds_played = new_score[key]["seconds_played"]
            currunt_score[key]["sucesfull_action"] += sucess_actions
            currunt_score[key]["total_actions"] += total_actions
            currunt_score[key]["seconds_played"] += seconds_played

            # Maybe move this to outside when all matches are completed. 
            # currunt_score[key]["actions_per_90"] += (total_actions * 5400) / seconds_played
            # currunt_score[key]["sucessfull_actions_per_90"] += (sucess_actions * 5400) / seconds_played
        else:
            currunt_score[key] = new_score[key]
    return currunt_score


def id_to_name_conversion(fotmatted_event_data, id_to_name_data):
    for player_id in id_to_name_data:
        ## go through the id_to_name dict
        # assign the name of an id to a player by creating a new entry in formatted dict
        # then delete the old id entry       
        player_name = id_to_name_data[player_id]
        fotmatted_event_data[player_name] = fotmatted_event_data[player_id]
        del fotmatted_event_data[player_id]

def data_cleaner(cb_press_score):
    print("DATA CLEANER")
    print(cb_press_score)
    for player_data in cb_press_score.copy():
        if cb_press_score[player_data].get("total_actions") < 50:
            del cb_press_score[player_data]
    return cb_press_score