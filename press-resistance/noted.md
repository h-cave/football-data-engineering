## How to find who plays where?
Two places
1. There is a starting lineup which gives players position - limitation if the player moves in game I won't know if i just use this
2. For each action a player does it gives a "position - I think this can be used to determin player position

## How to tell if a pass is under preassure?
There is a "under_preassure" tag. This can be checked to see if the player is under preassure (true or false). Will need to check the "pass" for aerial_won as I don't want to count headers as part of my model. 
Note - the type preassure are the defending team preassuring. Can probably ignore this. 

##Potential steps
-Loop through event. Find type == "Pass".
- Check if the position is one of Left Centre Back or Right Center Back.
- If it is, store player name into a dictionary - this stores the players and will be used to keep score
```
centre_back = {
  player-id: 0
  player-id: 0
}
```
- then check is `"under_pressure" == True` if not ignore
- then check if the pass outcome was "Incomplete"/“Injury Clearance”/“Out”/“Pass Offside”/Unknown” - if any of these are present then the pass did not reach it's target.
- If the pass was sucesfull. We need to get that players name. This is in pass - reciepient - name. 
- In v1 I will save this to a local dictionary for player id and name but PersistDict library could be used going forward
- then need to circle through the event data while the possession_team and player are the same as retrieved in the step above. 
- When we find a type name "pass" from the player that recieved the ball, we check if the outcome is "incomplete".

V1 assumption: Once the recipient loses possession, the CB's press-resistance sequence is considered unsuccessful, even if the recipient subsequently regains possession.




