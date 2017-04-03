import sys 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#File
col_names = ['Date', 'WaveHeight']
filename = 'allyears.txt'

data = pd.read_csv(filename, names=col_names, index_col='Date', parse_dates=True)

data['Year'] = data.index.year
data['Week'] = data.index.week

five_yr = data['2010':'2015']
#30yr = data['1979':'2009']
piv = pd.pivot_table(five_yr, index=['Week'],columns=['Year'], values=['WaveHeight'])
print piv 
#File 2
col_two = ['Week', 'WaveHeight Average','Period','WaveDir', 'WindSpd', 'WindDir']
filename2 = 'weekly_avg.txt'
data2 = pd.read_csv(filename2, names=col_two, index_col='Week')


sns.set()
fig, ax = plt.subplots(figsize=(20,10))
pd.pivot_table(data, index=['Week'],columns=['Year'], values=['WaveHeight']).plot(ax=ax, legend=False)
plt.plot(data2['WaveHeight Average'], color='k', linestyle='-')

#plt.figure(figsize=(15,5))
#piv.plot()
plt.title('Average Weekly Wave Heights')
plt.ylabel('Wave Height (m)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
plt.savefig('all_years.png')
