from loader import load_event_data
from press_metrics import cb_press_resistance_metric
total_score = []
event_data = load_event_data(9880)
cb_press_metric_score = cb_press_resistance_metric(event_data)

print(cb_press_metric_score)
total_score.append(cb_press_metric_score)
print(total_score)
