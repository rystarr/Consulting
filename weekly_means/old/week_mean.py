import sys 
import pandas as pd 
import seaborn 
import matplotlib.pyplot as plt
# Read data in 
col_names = ['Date', 'WaveHeight', 'WavePeriod', 'WaveDir', 'WindSpd', 'WindDir']
file_name = 'test.txt'
data = pd.read_csv(file_name, names=col_names, index_col='Date')

data.plot()
plt.ylabel('Hourly Stats')
plt.show
