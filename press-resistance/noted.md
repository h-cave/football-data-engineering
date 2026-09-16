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

other notes
pass have an "outcome" so you can tell if a pass was sucesfull or not - will be useful

An example of an event where Umtit wouldn't get a point. He passes under preassure. Jordi alba then performs an unsucesfull pass while still under preassure. 

```
 {
  "id" : "697e3b43-9edc-42e7-b917-9e82696d7c57",
  "index" : 32,
  "period" : 1,
  "timestamp" : "00:00:32.032",
  "minute" : 0,
  "second" : 32,
  "type" : {
    "id" : 30,
    "name" : "Pass"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "player" : {
    "id" : 5492,
    "name" : "Samuel Yves Umtiti"
  },
  "position" : {
    "id" : 5,
    "name" : "Left Center Back"
  },
  "location" : [ 10.7, 9.6 ],
  "duration" : 0.712604,
  "under_pressure" : true,
  "related_events" : [ "1ee7fd56-46e6-444c-8e14-53a9f3af3b7d", "e7dafc9e-c411-4c86-b7f4-27c96b7df0cb" ],
  "pass" : {
    "recipient" : {
      "id" : 5211,
      "name" : "Jordi Alba Ramos"
    },
    "length" : 8.809086,
    "angle" : -0.88187194,
    "height" : {
      "id" : 1,
      "name" : "Ground Pass"
    },
    "end_location" : [ 16.3, 2.8 ],
    "body_part" : {
      "id" : 38,
      "name" : "Left Foot"
    }
  }
}, {
  "id" : "e7dafc9e-c411-4c86-b7f4-27c96b7df0cb",
  "index" : 33,
  "period" : 1,
  "timestamp" : "00:00:32.745",
  "minute" : 0,
  "second" : 32,
  "type" : {
    "id" : 42,
    "name" : "Ball Receipt*"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "player" : {
    "id" : 5211,
    "name" : "Jordi Alba Ramos"
  },
  "position" : {
    "id" : 6,
    "name" : "Left Back"
  },
  "location" : [ 16.3, 2.8 ],
  "related_events" : [ "697e3b43-9edc-42e7-b917-9e82696d7c57" ]
}, {
  "id" : "09b4de4f-c877-4642-b78c-8c43a9f92ce8",
  "index" : 34,
  "period" : 1,
  "timestamp" : "00:00:32.745",
  "minute" : 0,
  "second" : 32,
  "type" : {
    "id" : 43,
    "name" : "Carry"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "player" : {
    "id" : 5211,
    "name" : "Jordi Alba Ramos"
  },
  "position" : {
    "id" : 6,
    "name" : "Left Back"
  },
  "location" : [ 16.3, 2.8 ],
  "duration" : 3.74199,
  "under_pressure" : true,
  "related_events" : [ "3771e62e-81c3-42d9-861a-5c7e5572993f", "8f9570cc-795c-4303-8b91-be78ca96ab7f", "e7dafc9e-c411-4c86-b7f4-27c96b7df0cb" ],
  "carry" : {
    "end_location" : [ 3.8, 2.8 ]
  }
}, {
  "id" : "8f9570cc-795c-4303-8b91-be78ca96ab7f",
  "index" : 35,
  "period" : 1,
  "timestamp" : "00:00:32.910",
  "minute" : 0,
  "second" : 32,
  "type" : {
    "id" : 17,
    "name" : "Pressure"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 207,
    "name" : "Valencia"
  },
  "player" : {
    "id" : 6583,
    "name" : "Carlos Soler Barragán"
  },
  "position" : {
    "id" : 12,
    "name" : "Right Midfield"
  },
  "location" : [ 101.0, 77.0 ],
  "duration" : 3.756225,
  "related_events" : [ "09b4de4f-c877-4642-b78c-8c43a9f92ce8", "3771e62e-81c3-42d9-861a-5c7e5572993f", "edfeb177-002d-4f3c-915c-b0ff0f36b300" ]
}, {
  "id" : "3771e62e-81c3-42d9-861a-5c7e5572993f",
  "index" : 36,
  "period" : 1,
  "timestamp" : "00:00:36.486",
  "minute" : 0,
  "second" : 36,
  "type" : {
    "id" : 30,
    "name" : "Pass"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "player" : {
    "id" : 5211,
    "name" : "Jordi Alba Ramos"
  },
  "position" : {
    "id" : 6,
    "name" : "Left Back"
  },
  "location" : [ 3.8, 2.8 ],
  "duration" : 0.179829,
  "under_pressure" : true,
  "related_events" : [ "723dc3cd-0ae9-41fd-baa0-a520b93ebe9e", "8f9570cc-795c-4303-8b91-be78ca96ab7f", "edfeb177-002d-4f3c-915c-b0ff0f36b300" ],
  "pass" : {
    "recipient" : {
      "id" : 5216,
      "name" : "Andrés Iniesta Luján"
    },
    "length" : 2.1213202,
    "angle" : 0.14189705,
    "height" : {
      "id" : 1,
      "name" : "Ground Pass"
    },
    "end_location" : [ 5.9, 3.1 ],
    "body_part" : {
      "id" : 38,
      "name" : "Left Foot"
    },
    "outcome" : {
      "id" : 9,
      "name" : "Incomplete"
    }
  }
}
```

{'id': '023826bd-5613-4f5a-82a4-926ebea2106d', 'index': 23, 'period': 1, 'timestamp': '00:00:20.290', 'minute': 0, 'second': 20, 'type': {'id': 30, 'name': 'Pass'}, 'possession': 3, 'possession_team': {'id': 217, 'name': 'Barcelona'}, 'play_pattern': {'id': 1, 'name': 'Regular Play'}, 'team': {'id': 217, 'name': 'Barcelona'}, 'player': {'id': 5213, 'name': 'Gerard Piqué Bernabéu'}, 'position': {'id': 3, 'name': 'Right Center Back'}, 'location': [34.8, 23.4], 'duration': 1.221624, 'under_pressure': True, 'related_events': ['0049b4d5-910d-4bfe-8ee9-97de93ae8b83', '72a81744-f231-4405-941d-476ecb40f396', 'd237f7b1-3183-4c39-915d-c22376297740'], 'pass': {'recipient': {'id': 5492, 'name': 'Samuel Yves Umtiti'}, 'length': 3.7589893, 'angle': -1.0714496, 'height': {'id': 2, 'name': 'Low Pass'}, 'end_location': [36.6, 20.1], 'type': {'id': 66, 'name': 'Recovery'}, 'aerial_won': True}}


NOte: At the moment my model only takes into account a player passing after recieving the ball from a CB. So if the reciever wins a free kick/shoots/gets a throw in or any action that isn't a shot my model doesn't account for it 
