from loader import load_event_data, load_matches_data
from press_metrics import cb_press_resistance_metric
from formatter import score_formatter, id_to_name_conversion, data_cleaner

import pandas as pd 

#season = load_matches_data()
season = [3754059, 3754059]
total_cb_press_score = dict()
total_id_to_name_dictionary = dict()

for matches in season:
    #event_data = load_event_data(matches["match_id"])
    print("First loop")
    event_data = load_event_data(matches)

    cb_press_metric_score, id_to_name_dictionary = cb_press_resistance_metric(event_data)

    # Update the id to name dictionary so we can format at the end
    total_id_to_name_dictionary.update(id_to_name_dictionary)
    # format the player score so we can keep count of score over mulptiplpe matches
    total_cb_press_score = score_formatter(total_cb_press_score, cb_press_metric_score)

# Format total_cb_press_score to add in the player names in replace of ID
id_to_name_conversion(total_cb_press_score, total_id_to_name_dictionary)

# Clean the data so we only have players who have performed at least 50 actions
total_cb_press_score = data_cleaner(total_cb_press_score)

#load data into a DataFrame object:
df = pd.DataFrame(total_cb_press_score)

# Show every row
pd.set_option('display.max_rows', None)

# Show every column
pd.set_option('display.max_columns', None)

# Show the full text content inside cells (stops the ... inside a column)
pd.set_option('display.max_colwidth', None)

# Prevent the table from wrapping over multiple lines in terminal outputs
pd.set_option('display.width', None)

print(f"\nEND OF RUN:\n {df}")
