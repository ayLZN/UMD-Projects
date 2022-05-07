import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
import matplotlib.pyplot as plt
import plotly.express as px


# Reading the csv file and then dropping the columns that are not needed. Then it is grouping the data by state and then
# resetting the index.
state_df = pd.read_csv('data/CBECS climate zones by county - CBECS Climate Zones.csv')
state_df = state_df.drop(['County', 'NOAA Climate Division (Number)', 'NOAA Climate Division (Name)'], axis=1)
state_df = state_df.groupby(['State']).mean()
state_df = state_df.reset_index()
state_df.to_csv('data/cleaned_climate_zones.csv', index=False)
print(state_df['CBECS Climate Zone'].describe())

# This is creating a choropleth map of the United States. It is using the state_df dataframe to create the map.
fig = px.choropleth(state_df,  # Input Pandas DataFrame
                   locations="State",  # DataFrame column with locations
                   color="CBECS Climate Zone",  # DataFrame column with color values
                   hover_name="State", # DataFrame column hover info
                   locationmode = 'USA-states') # Set to plot as US States
fig.update_layout(
   title_text = 'State Rankings', # Create a Title
   geo_scope='usa',  # Plot only the USA instead of globe
)
fig.write_image("Vis/cbecs.png")


df = pd.read_csv('data/Five_states.csv')

Totalc = df.loc[:4]


ax =Totalc.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Energy Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_energy_production.png', bbox_extra_artists=(ax,), bbox_inches='tight')

Totalp = df.loc[15:18]


ax =Totalp.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total energy average price', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_energy_average_price.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()


HydroC = df.loc[92:95]

ax =HydroC.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Hydropower Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_hydropower_consumption.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()


ElecE = df.loc[62:65]
ax =ElecE.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Electricity Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_electricity_consumption.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()




