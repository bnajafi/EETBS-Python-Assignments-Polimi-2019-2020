# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os

externalfiles_folder="C:\Users\Hamed\Desktop\Behzad1"
consumptionfilename= "consumption_5545.csv"
temperaturefilename="Austin_weather_2014.csv"
irradiancefilename= "irradiance_2014_gen.csv"
path_consumptionfile=os.path.join(externalfiles_folder,consumptionfilename)
path_tempratureflie=os.path.join(externalfiles_folder,temperaturefilename)
path_irradiancefile=os.path.join(externalfiles_folder,irradiancefilename)

DF_consumption = pd.read_csv(path_consumptionfile,sep=",",index_col=0)
DF_weather = pd.read_csv(path_tempratureflie,sep=";",index_col=0)
DF_irradianceSource=pd.read_csv(path_irradiancefile,sep=";",index_col=1)

oldIndex_consumption=DF_consumption.index
NewParsedIndex=pd.to_datetime(oldIndex_consumption)
DF_consumption.index=NewParsedIndex
oldIndex_weather=DF_weather.index

newParsedIndex_weather=pd.to_datetime(oldIndex_weather)
DF_weather.index=newParsedIndex_weather

DF_temperature=DF_weather[["temperature"]]
DF_irradiance=DF_irradianceSource[["gen"]]
DF_irradiance.loc[DF_irradiance.loc[:,"gen"]<0,:]=0

DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
oldIndex_joined=DF_joined.index
newIndex_joined=pd.to_datetime(oldIndex_joined)
DF_joined.index=newIndex_joined

DF_joined_selected= DF_joined.loc["2014-07-01 00:00:00" : "2014-07-3 00:00:00"]

max_consumption=DF_joined_selected['air conditioner_5545'].max()
max_temperature=DF_joined_selected['temperature'].max()
max_irradiance=DF_joined_selected['gen'].max()
DF_joined_selected_norm=DF_joined_selected
DF_joined_selected_norm.loc[:,'air conditioner_5545']=DF_joined_selected_norm.loc[:,'air conditioner_5545']/max_consumption
DF_joined_selected_norm.loc[:,'temperature']=DF_joined_selected_norm.loc[:,'temperature']/max_temperature
DF_joined_selected_norm.loc[:,'gen']=DF_joined_selected_norm.loc[:,'gen']/max_irradiance

X_val=DF_joined_selected_norm.index
x = np.array(X_val)
consumption=DF_joined_selected_norm.iloc[:,0]
y1 = np.array(consumption)
temperature=DF_joined_selected_norm.iloc[:,1]
y2 = np.array(temperature)
irradiance=DF_joined_selected_norm.iloc[:,2]
y3 = np.array(irradiance)

fig, axs = plt.subplots(1)
fig.suptitle('Normalized Plot')

plt.plot(x, y1, ':', color='m', label='Consumption(W)')
plt.plot(x, y2, '-', color='y', label='Temperature(F)' )
plt.plot(x, y3, '-.', color='b', label='Irradiance(W/m^2)')
plt.legend()
plt.show()

