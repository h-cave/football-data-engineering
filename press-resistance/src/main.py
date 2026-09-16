from loader import load_event_data, load_matches_data
from press_metrics import cb_press_resistance_metric
from formatter import score_formatter, id_to_name_conversion


la_liga_matches = load_matches_data()

total_cb_press_score = dict()
total_id_to_name_dictionary = dict()
barcelona_matches = [303532, 303377, 16086, 16231, 303479]#[303532, 303479, 303377]

for matches in la_liga_matches:
    print(f"THIS IS MATCH: {matches}")
    event_data = load_event_data(matches["match_id"])
    cb_press_metric_score, id_to_name_dictionary = cb_press_resistance_metric(event_data)

    # Update the id to name dictionary so we can format at the end
    total_id_to_name_dictionary.update(id_to_name_dictionary)
    # format the player score so we can keep count of score over mulptiplpe matches
    total_cb_press_score = score_formatter(total_cb_press_score, cb_press_metric_score)
  


print(f"total id_to_name dict: {total_id_to_name_dictionary}")
formatted_total_cb_press_score = id_to_name_conversion(total_cb_press_score, total_id_to_name_dictionary)

print(f"END OF RUN: {total_cb_press_score}")
