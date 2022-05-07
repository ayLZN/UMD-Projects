import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
from state_dict import abv_state
df = pd.read_csv('data/cleaned_climate_zones.csv')
#df = df.replace({'State': abv_state})
df['State'].map(abv_state)
zone1 = [] #1-2
zone2 = [] #2-3
zone3 = [] #3-4
zone4 = [] #4-5

for ind, row in df.iterrows():
    if 4 < row['CBECS Climate Zone'] <= 5:
        zone4.append(row['State'])
    if 3 < row['CBECS Climate Zone'] <= 4:
        zone3.append(row['State'])
    if 2 < row['CBECS Climate Zone'] <= 3:
        zone2.append(row['State'])
    elif 1 <= row['CBECS Climate Zone'] <= 2:
        zone1.append(row['State'])

print(zone1)