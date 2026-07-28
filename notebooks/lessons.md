### KeyError and .get

Today when getting yellow cards from the data I was running into KeyError. I was doing;
```
yellow_cards_home_team = [yellow_card for yellow_card in data[0:-1] if yellow_card['foul_committed']['card']['name'] in yellow_card and yellow_card['possession_team']['name'] == home_team]
```
This was giving Key error as foul_comitted doesn't alwasy exist and if it does fould_committed doesn't always contain card and/or name 

the fix, .get() this returns None if the key isn't in the dict not and error. 
This returns the entire data event if .get('foul_committed) is in the event. This means I have the entire data to then play with top get the info I need

```
yellow_cards_home_team = [yellow_card for yellow_card in data[0:-1] if yellow_card.get('foul_committed') and yellow_card['possession_team']['name'] == home_team]
```


Further learning. Some data contains just 
`'type': {'id': 22, 'name': 'Foul Committed'}`
where as other data contains 
`'foul_committed': {'card': {'id': 7, 'name': 'Yellow Card'}}}`
at the end. 

As a foul can be comitted withou a card I assume. 


`{'id': '3caad328-66b5-4a08-ba4d-3189c9a64cbd', 'index': 2668, 'period': 2, 'timestamp': '00:33:54.006', 'minute': 78, 'second': 54, 'type': {'id': 22, 'name': 'Foul Committed'}, 'possession': 168, 'possession_team': {'id': 1, 'name': 'Arsenal'}, 'play_pattern': {'id': 1, 'name': 'Regular Play'}, 'team': {'id': 29, 'name': 'Everton'}, 'player': {'id': 40287, 'name': 'Tie Li'}, 'position': {'id': 15, 'name': 'Left Center Midfield'}, 'location': [87.8, 3.5], 'duration': 0.0, 'related_events': ['b9627cdf-8934-4e95-b534-cd4d7717524f'], 'foul_committed': {'card': {'id': 7, 'name': 'Yellow Card'}}}`