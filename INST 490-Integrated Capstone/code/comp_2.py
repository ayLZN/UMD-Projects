import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

climate_zone_df = pd.read_csv('data/cleaned_climate_zones.csv')
Energy_census = pd.read_csv('data/Energy Census and Economic Data US 2010-2014.csv')
final_df = climate_zone_df.sort_values(by=['CBECS Climate Zone'], ascending=True)


# Creating a subset of the dataframe based on the index.
zone1 = final_df.iloc[0:19] #1-2
zone2 = final_df.iloc[19:32] #2-3
zone3 = final_df.iloc[32:40] #3-4
zone4 = final_df.iloc[40:46] #4-5
zone5 = final_df.iloc[46:] # 5+

# Creating a list of the states in each climate zone.
Zone1_states = zone1['State'].to_list()
Zone2_states = zone2['State'].to_list()
Zone3_states = zone3['State'].to_list()
Zone4_states = zone4['State'].to_list()
Zone5_states = zone5['State'].to_list()

# Creating a subset of the dataframe based on the index.
zone1_subset = Energy_census.loc[Energy_census['StateCodes'].isin(Zone1_states)]
zone2_subset = Energy_census.loc[Energy_census['StateCodes'].isin(Zone2_states)]
zone3_subset = Energy_census.loc[Energy_census['StateCodes'].isin(Zone3_states)]
zone4_subset = Energy_census.loc[Energy_census['StateCodes'].isin(Zone4_states)]
zone5_subset = Energy_census.loc[Energy_census['StateCodes'].isin(Zone5_states)]



new_df = pd.DataFrame(zone1_subset.mean().to_dict(),index=[zone1_subset.index.values[-1]])

# Creating a new dataframe with the mean of each column in the dataframe.
df2 = pd.DataFrame(zone2_subset.mean().to_dict(),index=[zone2_subset.index.values[-1]])
df3 = pd.DataFrame(zone3_subset.mean().to_dict(),index=[zone3_subset.index.values[-1]])
df4 = pd.DataFrame(zone4_subset.mean().to_dict(),index=[zone4_subset.index.values[-1]])
df5 = pd.DataFrame(zone5_subset.mean().to_dict(),index=[zone5_subset.index.values[-1]])
new_df = new_df.append((df2,df3,df4,df5), ignore_index= True)

idx = 0
new_col = [1, 2, 3, 4, 5]
new_df.insert(loc=idx, column='Zones', value=new_col)

print(new_df)

# Plotting the dataframe with the x axis being the zones and the y axis being the total electricity consumption.
ax =new_df.plot(x="Zones", y=['TotalC2010', 'TotalC2011', 'TotalC2012', 'TotalC2013', 'TotalC2014'], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Electricity Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.show()