from src.metrics import analyse_shots, pass_data, corners, fouls

class TestMetrics:
    home_team = "Nantes"
    away_team = "Gazélec Ajaccio"
    event = [
    {
        "type" : {
            "id" : 16,
            "name" : "Shot"
        },
        "possession_team" : {
            "id" : 144,
            "name" : "Nantes"
        },
        "shot" : {
            "statsbomb_xg" : 0.26788074,
            "outcome" : {
              "id" : 97,
              "name" : "Goal"
            },
        }
    }, 
    {
        "type" : {
            "id" : 25,
            "name" : "Own Goal For"
        },
        "possession_team" : {
            "id" : 144,
            "name" : "Gazélec Ajaccio"
        },
    }
]
    pass_event_data = [
    {
        "type" : {
            "id" : 30,
            "name" : "Pass"
        },
        "possession_team" : {
          "id" : 29,
          "name" : "Gazélec Ajaccio"
        },
        "pass" : {
            "type" : {
                "id" : 65,
                "name" : "Kick Off"
            }
        },
    },
    {
        "type" : {
            "id" : 31,
            "name" : "Pass"
        },
        "possession_team" : {
        "id" : 144,
        "name" : "Nantes"
        },
        "play_pattern" : {
            "id" : 1,
            "name" : "Regular Play"
        },
        "pass" : {
            "recipient" : {
              "id" : 40222,
              "name" : "Laureano Bisan-Etame Mayer"
            }
        }
    },
    { 
    "type" : {
           "id" : 31,
           "name" : "Pass"
       },
       "possession_team" : {
       "id" : 144,
       "name" : "Nantes"
       },
       "play_pattern" : {
            "id" : 7,
            "name" : "From Goal Kick"
       },
       "pass" : {
            "type" : {
              "id" : 63,
              "name" : "Goal Kick"
            }
       }
    },
    {
      "type" : {
            "id" : 30,
            "name" : "Pass"
        },
        "play_pattern" : {
            "id" : 6,
            "name" : "From Counter"
        },
        "possession_team" : {
            "id" : 1,
            "name" : "Gazélec Ajaccio"
        },
        "pass" : {
            "recipient" : {
              "id" : 15512,
              "name" : "Sylvain Wiltord"
            }
        },
    },
]
    corner_data = [
    {
        "play_pattern" : {
            "id" : 2,
            "name" : "From Corner"
        },
        "pass" : {
            "type" : {
              "id" : 61,
              "name" : "Corner"
            },
          },
        "possession_team" : {
            "id" : 29,
            "name" : "Nantes"
        },
    },
    {
        "play_pattern" : {
            "id" : 2,
            "name" : "From Corner"
        }
    }
]
    foul_data = [
    {
        "type" : {
            "id" : 22,
            "name" : "Foul Committed"
        },
        "team" : {
            "id" : 1,
            "name" : "Gazélec Ajaccio"
        },
        "foul_committed" : {
            "card" : {
              "id" : 7,
              "name" : "Yellow Card"
            }
        }
    },
    {
        "type" : {
            "id" : 24,
            "name" : "Bad Behaviour"
        },
        "team" : {
            "id" : 764,
            "name" : "Nantes"
        },
        "foul_committed" : {
          "card" : {
                "id" : 6,
                "name" : "Second Yellow"
            }
        }
    }
]
    
    def test_fouls_data_returns_correct_dictionary_contents(self):
        expected_fouls_data = {
        "fouls_home_team": 1,
        "fouls_away_team": 1,
        "yellow_card_home_team": 1,
        "yellow_card_away_team": 1,
        "red_card_home_teams": 1,
        "red_card_away_teams": 0,
    }
        actual_fouls_data = fouls(self.home_team, self.away_team, self.foul_data)

        assert expected_fouls_data == actual_fouls_data
        
    def test_analyse_shots_returns_correct_directory_contents(self):
        expected_shots_data = {'total_home_team_shots': 1, 'total_away_team_shots': 0, 'home_team_xg_score': 0.26788074, 'away_team_xg_score': 0, 'home_team_goals': 1, 'away_team_goals': 1}
        shots_data = analyse_shots(self.home_team, self.away_team, self.event)

        assert expected_shots_data == shots_data

    def test_pass_data_returns_correct_dictionary_contents(self):
        expected_pass_data = {"passes": 4, "passes_in_open_play": 2, "total_home_team_passes": 2, "total_away_team_passes": 2, "open_play_passes_home_team": 1, "open_play_passes_away_team": 1}
        pass_data_recieved = pass_data(self.home_team, self.away_team, self.pass_event_data)

        assert expected_pass_data == pass_data_recieved

    def test_corner_data_returns_correct_dictionary_contents(self):
        expected_corner_data = {"home_team_corners": 1, "away_team_corners": 0}
        corner_data = corners(self.home_team, self.away_team, self.corner_data)

        assert expected_corner_data == corner_data


