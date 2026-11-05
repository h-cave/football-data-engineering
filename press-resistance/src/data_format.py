import numpy as np
import streamlit as st
import pandas as pd
from formatter import seconds_to_minutes

def generate_table(cb_press_score):
    headings = []
    pressing_action =[]
    passing_distance = []
    index = 0
    for data in cb_press_score:
        minutes_played = round(seconds_to_minutes(cb_press_score[data].get("seconds_played")), 2)
        
        headings.append([data, cb_press_score[data].get("sucesfull_action"), cb_press_score[data].get("total_actions"), minutes_played, cb_press_score[data].get("actions_per_90"), cb_press_score[data].get("sucessfull_actions_per_90"), cb_press_score[data].get("completion_percentage"), cb_press_score[data].get("0_15_yard_pass"), cb_press_score[data].get("16_to_30_yard_pass"), cb_press_score[data].get("31_plus_yard_pass"), cb_press_score[data].get("0_15_yard_pass_per_90"), cb_press_score[data].get("16_to_30_yard_pass_per_90"), cb_press_score[data].get("31_plus_yard_pass_per_90")])
        pressing_action.append([data, cb_press_score[data].get("sucesfull_action"), cb_press_score[data].get("total_actions"), minutes_played, cb_press_score[data].get("actions_per_90"), cb_press_score[data].get("sucessfull_actions_per_90"), cb_press_score[data].get("completion_percentage")])
        passing_distance.append([data, cb_press_score[data].get("0_15_yard_pass"), cb_press_score[data].get("16_to_30_yard_pass"), cb_press_score[data].get("31_plus_yard_pass"), cb_press_score[data].get("0_15_yard_pass_per_90"), cb_press_score[data].get("16_to_30_yard_pass_per_90"), cb_press_score[data].get("31_plus_yard_pass_per_90")])
        index += 1

    
    tab1, tab2, tab3 = st.tabs(["All CB Press data", "Pressing actions", "Passing distance"])
    with tab1:
        all_data = np.array(headings)
        np.array(all_data).reshape(index, 13)
        df = pd.DataFrame(all_data, columns=["player_name", "sucesfull_action", "total_actions", "minutes_played", "actions_per_90", "sucessfull_actions_per_90", "completion_percentage", "0_15_yard_pass", "16_to_30_yard_pass", "31_plus_yard_pass", "0_15_yard_pass_per_90", "16_to_30_yard_pass_per_90", "31_plus_yard_pass_per_90"])
        st.dataframe(df.style.highlight_max(axis=0))
    with tab2:
        pressing_actions = np.array(pressing_action)
        np.array(pressing_actions).reshape(index, 7)
        tab2_df = pd.DataFrame(pressing_actions, columns=["player_name", "sucesfull_action", "total_actions", "minutes_played", "actions_per_90", "sucessfull_actions_per_90", "completion_percentage"])
        st.dataframe(tab2_df.style.highlight_max(axis=0))
    with tab3:
        passing_distance = np.array(passing_distance)
        np.array(passing_distance).reshape(index, 7)
        tab3_df = pd.DataFrame(passing_distance, columns=["player_name", "0_15_yard_pass", "16_to_30_yard_pass", "31_plus_yard_pass", "0_15_yard_pass_per_90", "16_to_30_yard_pass_per_90", "31_plus_yard_pass_per_90"])
        st.dataframe(tab3_df.style.highlight_max(axis=0))

    