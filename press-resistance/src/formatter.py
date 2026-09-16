def score_formatter(currunt_score, new_score):
    ## The current is the players score
    ## The new score is the most recent games score
    ## We check if the player is in the current score and if they are find their id and add the new score
    ## if they aren't we just add them in with the current score
    if bool(currunt_score) == False:
        currunt_score = new_score
    for key in new_score:
        if key in currunt_score:
            sucess_actions = new_score[key]["sucesfull_action"]
            total_actions = new_score[key]["total_actions"]
            currunt_score[key]["sucesfull_action"] += sucess_actions
            currunt_score[key]["total_actions"] += total_actions
        else:
            currunt_score[key] = new_score[key]
    print(f"CURRENT SCOIRE IN FORMATTER:{currunt_score}")
    return currunt_score


def id_to_name_conversion(fotmatted_event_data, id_to_name_data):
    print(f"formatted_data: {fotmatted_event_data}")
    print(f"id_to_name data: {id_to_name_data}")
    
    for player_id in id_to_name_data:
        ## go through the id_to_name dict
        # assign the name of an id to a player by creating a new entry in formatted dict
        # then delete the old id entry       
        player_name = id_to_name_data[player_id]
        fotmatted_event_data[player_name] = fotmatted_event_data[player_id]
        del fotmatted_event_data[player_id]

