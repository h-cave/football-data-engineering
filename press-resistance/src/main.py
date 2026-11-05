from loader import load_event_data, load_matches_data
from press_metrics import cb_press_resistance_metric
from formatter import score_formatter, id_to_name_conversion, data_cleaner
from data_format import generate_table

total_cb_press_score = dict()
total_id_to_name_dictionary = dict()
matches = [[9, 27],[2, 27], [11, 1], [11, 25]]
for match in matches:
    season = load_matches_data(match[0], match[-1])



    for matches in season:
        event_data = load_event_data(matches["match_id"])
        print("First loop")

        cb_press_metric_score, id_to_name_dictionary = cb_press_resistance_metric(event_data, matches["match_id"])

        # Update the id to name dictionary so we can format at the end
        total_id_to_name_dictionary.update(id_to_name_dictionary)
        # format the player score so we can keep count of score over mulptiplpe matches
        total_cb_press_score = score_formatter(total_cb_press_score, cb_press_metric_score)

# Format total_cb_press_score to add in the player names in replace of ID
id_to_name_conversion(total_cb_press_score, total_id_to_name_dictionary)

 # Clean the data so we only have players who have performed at least 50 actions
total_cb_press_score = data_cleaner(total_cb_press_score)

generate_table(total_cb_press_score)
