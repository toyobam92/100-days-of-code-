import pandas as pd

states_game = pd.read_csv("50_states.csv")
all_states = states_game["state"]
list_states = all_states.to_list()
print(list_states)