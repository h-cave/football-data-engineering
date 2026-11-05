from minutes_played_data import minutes_played

def cb_press_resistance_metric(event_data, match_id):
    cb_id_to_name_store = {}
    cb_press_resistance_metric_score = {}
    # Below ids are used to store the cb and the player the cb passes to so we can run checks. 
    cb_id = ""
    recipitent_id = ""
    for press_data in event_data:
        if press_data["type"]["name"] == "Pass":
            if press_data["position"]["name"] in ["Left Center Back", "Right Center Back", "Center Back"]:
                
                cb_id = press_data["player"]["id"]
                player_name = press_data["player"]["name"]
                # We check if the keys already exists so that we don't overwrite them
                if player_name not in cb_id_to_name_store:
                    cb_id_to_name_store[cb_id] = player_name
                if cb_id not in cb_press_resistance_metric_score:
                    match_total_minutes = f"{event_data[-1]["minute"]}:{event_data[-1]["second"]}"
                    seconds_played = minutes_played(match_total_minutes, cb_id, match_id)
                    cb_press_resistance_metric_score[cb_id] = {"sucesfull_action": 0, "total_actions": 0, "seconds_played": seconds_played, "actions_per_90": 0, "sucessfull_actions_per_90": 0, "0_15_yard_pass": 0, "16_to_30_yard_pass": 0, "31_plus_yard_pass": 0}

                    
                ## We skip any events that are not under preassure 
                if press_data.get("under_pressure") is not True:
                    continue
                ## If a pass has an outcome it is not a completed pass so we add a total_action count to the player 
                if press_data["pass"].get("outcome") != None:
                    cb_press_resistance_metric_score = update_passing_disatance(press_data, cb_id, cb_press_resistance_metric_score)
                    cb_press_resistance_metric_score[cb_id]["total_actions"] += 1
                else:
                    # we add a total action and call recipient_tracking_data to se if the recipient retains possesion
                    cb_press_resistance_metric_score = update_passing_disatance(press_data, cb_id, cb_press_resistance_metric_score)
                    cb_press_resistance_metric_score[cb_id]["total_actions"] += 1
                    # Pass through all events and the event id. 
                    # Pass through the recipient of the CBs pass
                    # And the current possesion in which the CB made the pass
                    outcome = recipient_tracking_data(event_data, press_data["id"], press_data["pass"]["recipient"]["id"], press_data["possession"])
                    if outcome == True:
                        cb_press_resistance_metric_score[cb_id]["sucesfull_action"] += 1
        
    return cb_press_resistance_metric_score, cb_id_to_name_store
    
def recipient_tracking_data(event, event_id, recipient_id, current_possession):
    ### takes all event and event id. Circle through until we find the CB passing event
    ### The counter is used so that we don't continue over the actions after we find the correct ID. Allowing us to see if the recipient has reatined/passed the ball
    ### Circle through until the recipient passes the ball and then check that the pass is made within the same possesion
    ### This stops situations in which the cirepient may make a pass unrelated to the CBs pass (could do with refinement)
    ### Then check if the recipients pass has a outcome or not to detemine if they suceeded
    first_counter = 0

    for events in event:
        if events["id"] != event_id and first_counter < 1:
            continue
        
        first_counter += 1
        
        if events.get("player", {}).get("id") == recipient_id and events["type"].get("name") == "Pass":
            if events["possession"] == current_possession:# We ensure the stage of play is still the same as when the CB passed it - this needs refinement
            
                if events["pass"].get("outcome") == None:
                    return True
                else:
                    return False

            else:
                print("another action happened - ignore for now")
                print("-----------------------------------------")

            
            first_counter = 0

def update_passing_disatance(event, player_id, current_player_score):
    print("EVENT")
    print(event)
    pass_length = event["pass"].get("length")
    if pass_length <= 15:
        current_player_score[player_id]["0_15_yard_pass"] += 1
    elif pass_length > 15 and pass_length <= 30:
        current_player_score[player_id]["16_to_30_yard_pass"] += 1
    else:
        current_player_score[player_id]["31_plus_yard_pass"] += 1

    return current_player_score