import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)

Energy_census = pd.read_csv('data/Energy Census and Economic Data US 2010-2014.csv')
df = pd.read_csv('data/cleaned_climate_zones.csv')
#df['State'].map(abv_state)

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

merger = pd.DataFrame([])

for ind,row in Energy_census.iterrows():
    if row['StateCodes'] in zone1:
        merger = merger.append(pd.DataFrame({
            'Zone': 1,
            'State': row['StateCodes']
        }, index=[0]), ignore_index = True)
    if row['StateCodes'] in zone2:
        merger = merger.append(pd.DataFrame({
            'Zone' : 2,
            'State': row['StateCodes']
        }, index=[0]), ignore_index = True)
    if row['StateCodes'] in zone3:
        merger = merger.append(pd.DataFrame({
            'Zone': 3,
            'State': row['StateCodes']
        }, index = [0]), ignore_index = True)
    elif row['StateCodes'] in zone4:
        merger = merger.append(pd.DataFrame({
            'Zone' : 4,
            'State': row['StateCodes']
        }, index=[0]), ignore_index=True)

merger = merger.merge(Energy_census, left_on='State', right_on='StateCodes', how='left')
merger = merger.drop(['StateCodes', 'State_x', 'State_y', 'Region', 'Division', 'Coast', 'Great Lakes', 'TotalC10-11', 'TotalC11-12', 'TotalC12-13', 'TotalC13-14', 'TotalP10-11', 'TotalP11-12', 'TotalP12-13', 'TotalP13-14', 'TotalE10-11', 'TotalE11-12', 'TotalE12-13', 'TotalE13-14', 'TotalPrice10-11', 'TotalPrice11-12', 'TotalPrice12-13', 'TotalPrice13-14'
], axis=1)
merger = merger.groupby(['Zone']).mean()

#print(merger)


a  = np.arange(0,len(merger.columns)) // 5*5
merger = merger.groupby(a, axis=1).mean().round(2)

merger.columns =['Total Energy Consumption',
'Total Energy Production',
'Total Energy Expenditures',
'Total Energy Average Price',
'Total Biomass Consumption',
'Total Coal Consumption' ,
'Total Coal Production' ,
'Total Coal Expenditures' ,
'Total Coal Average Price' ,
'Total Electricity Consumption',
'Total Electricity Expenditures',
'Total Electricity Average Price' ,
'Total Fossil Fuels Consumption',
'Total Geothermal Energy Net Generation',
'Total Hydropower Consumption' ,
'Total Hydropower Net Generation',
'Total Natural Gas Consumption' ,
'Total Natural Gas Expenditures',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this',
'Delete this']

merger = merger.drop(['Delete this'], axis=1)


idx = 0
new_col = [1, 2, 3, 4]
merger.insert(loc=idx, column='Zones', value=new_col)
print(merger)


ax = merger.plot(x="Zones", y=['Total Biomass Consumption', 'Total Coal Consumption', 'Total Electricity Consumption', 'Total Fossil Fuels Consumption', 'Total Hydropower Consumption', 'Total Natural Gas Consumption'], kind="bar", figsize=(9, 10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set(xlabel='Total Consumption by Zones', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_consumption_by_zone.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()

ax = merger.plot(x="Zones", y=['Total Energy Production', 'Total Coal Production'], kind="bar", figsize=(9, 10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set(xlabel='Total Production by Zones', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_production_by_zone.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()

ax = merger.plot(x="Zones", y=['Total Energy Expenditures', 'Total Coal Expenditures', 'Total Electricity Expenditures', 'Total Natural Gas Expenditures'], kind="bar", figsize=(9, 10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set(xlabel='Total Expenditures by Zones', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_expenditures_by_zone.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()

ax = merger.plot(x="Zones", y=['Total Energy Average Price','Total Coal Average Price', 'Total Electricity Average Price'], kind="bar", figsize=(9, 10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.set(xlabel='Total Average Price by Zones', ylabel='Price')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Vis/total_average_price_by_zone.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()
