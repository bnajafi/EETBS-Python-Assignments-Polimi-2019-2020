
# coding: utf-8

# # Assignment 8

# In[11]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ### Importing consumption dataset

# In[12]:

ExternalFiles_folder=r"C:\Users\Valentina\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName="consumption_5545.csv"
TemperatureFileName="Austin_weather_2014.csv"
IrradianceFileName="irradiance_2014_gen.csv"
path_consumpionFile=os.path.join(ExternalFiles_folder,ConsumptionFileName)
path_temperatureFile=os.path.join(ExternalFiles_folder,TemperatureFileName)
path_irradianceFile=os.path.join(ExternalFiles_folder,IrradianceFileName)


# In[13]:

DF_consumption=pd.read_csv(path_consumpionFile, sep=',',index_col=0)
oldIndex_consumption = DF_consumption.index
NewParsedIndex=pd.to_datetime(oldIndex_consumption)
DF_consumption.index = NewParsedIndex
DF_consumption.head()


# ### Visualize the first two weeks of July of the dataset

# In[14]:

DF_consumption_FirstTwoWeeksOfJuly= DF_consumption.loc["2014-07-01 00:00:00":"2014-07-15 00:00:00",:] 
DF_consumption_FirstTwoWeeksOfJuly


# ### Let's plot it -->  using Matplotlib library

# In[15]:

get_ipython().magic(u'matplotlib notebook')


# In[16]:

fig1 = plt.figure()
plt.plot(DF_consumption_FirstTwoWeeksOfJuly)
plt.xlabel("Time")
plt.ylabel("AC power (W)")
plt.grid()
plt.show()


# ### Method two : plotting using Pandas --> using matplotlib indirectly
# 

# In[17]:

DF_consumption_FirstTwoWeeksOfJuly.plot()
plt.xlabel("Time")
plt.ylabel("AC power (W)")
plt.grid()
plt.legend(loc="upper left")  # per muovere l'indice in alto
plt.show()


# ### Importing the weather related datasets
# Since this dataset is big and we are interested only in temperature, we create a "sub-dataset"

# In[18]:

DF_weather=pd.read_csv(path_temperatureFile, sep=';',index_col=0)
oldIndex_weather = DF_weather.index
newPardedIndex_weather=pd.to_datetime(oldIndex_weather)
DF_weather.index=newPardedIndex_weather
DF_temperature = DF_weather.loc[:,["temperature"]]
DF_temperature


# Weather station provide us with the data in which the timestamp is in standard time zone (London), so we need to shift up the column
# 

# In[19]:

DF_temperature.loc[:,"temperature"]=DF_temperature.loc[:,"temperature"].shift(-5)
DF_temperature.head()


# In[20]:

DF_temperature_FirstTwoWeeksOfJuly = DF_temperature.loc["2014-07-01 00:00:00":"2014-07-15 00:00:00",:]
DF_temperature_FirstTwoWeeksOfJuly.head()


# ### Import Irradiance dataset

# In[21]:

DF_irradianceSource=pd.read_csv(path_irradianceFile, sep=';',index_col=1)
DF_irradiance= DF_irradianceSource[["gen"]] #means DF_irradiance= DF_irradianceSource.loc[:,["gen"]]
oldIndex_Irradiance = DF_irradiance.index
newIndex_Irradiance=pd.to_datetime(oldIndex_Irradiance)
DF_irradiance.index=newIndex_Irradiance
DF_irradiance.head()


# ### Convert into 0 the negative generated power values
# 

# In[22]:

DF_irradiance.loc[DF_irradiance.loc[:,"gen"]<0,:]=0
DF_irradiance.head()


# In[23]:

DF_IrradianceFirstTwoWeeksOfJuly = DF_irradiance.loc["2014-07-01 00:00:00":"2014-07-15 00:00:00",:]
DF_IrradianceFirstTwoWeeksOfJuly.head()


# ### Putting everything togheter : .join!

# In[24]:

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined_selected=DF_joined.loc["2014-07-01 00:00:00":"2014-07-15 00:00:00"]
DF_joined_selected.head()


# ### Creating 3 different plots

# In[25]:

fig,ax = plt.subplots(3)


# In[26]:

ax[0].plot(DF_consumption_FirstTwoWeeksOfJuly,"k-") # riempie solo il primo grafico dei due
ax[1].plot(DF_temperature_FirstTwoWeeksOfJuly, "b-") #riempie il secondo grafico
ax[2].plot(DF_IrradianceFirstTwoWeeksOfJuly, "g-")
ax[0].set_title("Consumption")
ax[1].set_title("Temperature")
ax[2].set_title("Irradiance")

# from the website of matplotlib
for ax in ax.flat:
    ax.set(xlabel='Time [h]')

for ax in fig.get_axes():
    ax.label_outer()
    
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9,hspace = 0.5)
fig


# ### Normalizing and a unique chart

# Normalize Consumption
# 

# In[29]:

DF_consumption_Min =DF_joined_selected.loc[:,"air conditioner_5545"].min()
DF_consumption_Min


# In[30]:

DF_consumption_Max = DF_joined_selected.loc[:,"air conditioner_5545"].max()
DF_consumption_Max


# In[31]:

DF_consumption_normalized= DF_joined_selected.loc[:,"air conditioner_5545"]/(DF_consumption_Max-DF_consumption_Min)
DF_consumption_normalized


# Normalizing Temperature
# 

# In[33]:

DF_temperature_Min =DF_joined_selected.loc[:,"temperature"].min()
DF_temperature_Max =DF_joined_selected.loc[:,"temperature"].max()
DF_temperature_normalized= DF_joined_selected.loc[:,"temperature"]/(DF_temperature_Max-DF_temperature_Min)
DF_temperature_normalized


# Normalize Irradiance

# In[34]:

DF_irradiance_Min =DF_joined_selected.loc[:,"gen"].min()
DF_irradiance_Max =DF_joined_selected.loc[:,"gen"].max()
DF_irradiance_normalized= DF_joined_selected.loc[:,"gen"]/(DF_irradiance_Max-DF_irradiance_Min)
DF_irradiance_normalized


# Plot

# In[39]:

plt.figure()
plt.title("Normalized values of the first two weeks of July")
plt.plot(DF_consumption_normalized, "k-", label="Consumption Air Conditioning")
plt.plot(DF_temperature_normalized, "b-", label="Temperature")
plt.plot(DF_irradiance_normalized, "g-", label="Irradiance")
plt.xlabel("Time")
plt.legend(loc="center")

