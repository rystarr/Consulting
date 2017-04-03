
# coding: utf-8

# In[41]:

#Import 
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns; seaborn.set()


# In[42]:

col_names = ['Date', 'WaveHeight', 'WavePeriod', 'WaveDir', 'WindSpd', 'WindDir']
file_name = 'test_data.txt'
data = pd.read_csv(file_name, names=col_names, index_col='Date', parse_dates=True)


# In[43]:

data['WaveHeight'].plot()
plt.ylabel('Hourly Stats')
plt.show


# In[45]:

weekly = data['WaveHeight'].resample('W').mean()
plt.figure(figsize=(15,5))
weekly.plot(style=['-'])
plt.ylabel('Weekly Wave Height')


# In[47]:

#Index data by year 
#weekly.to_csv('test.txt', index=True, header=False, sep=',')



# In[48]:

#Plot Avg Weeks
#sns.set()
#fig, ax = plt.subplots(figsize=(20,10))
#pd.pivot_table(data, index=['Week'],columns=['Year'], values=['WaveHeight']).plot(ax=ax, legend=False)


# In[ ]:



