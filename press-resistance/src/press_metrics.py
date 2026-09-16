def cb_press_resistance_metric(event_data):
    cb_id_to_name_store = {}
    cb_press_resistance_metric_score = {}
    # Below ids are used to store the cb and the player the cb passes to so we can run checks. 
    cb_id = ""
    recipitent_id = ""
    for press_data in event_data:
        if press_data["type"]["name"] == "Pass":
            if press_data["position"]["name"] in ["Left Center Back", "Right Center Back", "Center Back"]:
                cb_id = press_data["player"]["id"]
                # recipient_id = press_data["pass"]["recipient"]["id"]
                player_name = press_data["player"]["name"]
                # We check if the keys already exists so that we don't overwrite them
                if player_name not in cb_id_to_name_store:
                    cb_id_to_name_store[player_name] = cb_id
                if cb_id not in cb_press_resistance_metric_score:
                    cb_press_resistance_metric_score[cb_id] = {"sucesfull_action": 0, "total_actions": 0}

                ## We remove any events that are not under preassure 
                if press_data.get("under_pressure") is not True:
                    continue
                ## If a pass has an outcome it is not a completed pass so we add a total_action count to the player 
                if press_data["pass"].get("outcome") != None:
                    cb_press_resistance_metric_score[cb_id]["total_actions"] += 1
                else:
                    cb_press_resistance_metric_score[cb_id]["total_actions"] += 1
                    print(f"Event point that started it: {press_data}")
                    outcome = recipient_tracking_data(event_data, press_data["id"], press_data["pass"]["recipient"]["id"], press_data["possession"])
                    if outcome == True:
                        cb_press_resistance_metric_score[cb_id]["sucesfull_action"] += 1
    print(cb_id_to_name_store)
    
    return cb_press_resistance_metric_score
    

def recipient_tracking_data(event, event_id, recipient_id, current_possession):
    ###Current issue:
    ### When looping through we get the event id we need.
    ### The while events is then performed on the passing event not recipient event
    ### so we skip over the while. But on the next event it hits the if block meaning we skip everything
    first_counter = 0 # Ensures we don't skip events following the CB passing
    print(f"cb made pass on possesion: {current_possession}")
    for events in event:
        if events["id"] != event_id and first_counter < 1:
            continue
        
        first_counter += 1 and events["possession"] == current_possession
        if events["player"]["id"] == recipient_id and events["type"].get("name") == "Pass":
            if events["possession"] == current_possession:# We ensure the stage of play is still the same as when the CB passed it - this needs refinement
                print(events)
                if events["pass"].get("outcome") == None:
                    print("Recipient has passed the ball")
                    print("--------------------------------")
                    return True
                else:
                    print("recipient has not carried on possesion")
                    print("-------------------------------------------")
                    return False

                
            else:
                print("another action happened - ignore for now")
                print("-----------------------------------------")

            
            first_counter = 0
        


