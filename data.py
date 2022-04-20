import pandas as pd 

data = pd.read_csv('out_steve.csv')

print((data.loc[data["name"] == cur, "race"]).tolist()[0])