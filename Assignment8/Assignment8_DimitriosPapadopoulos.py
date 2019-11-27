#assignment 8 
#plots of July

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os 

ExternalFiles_Folder= r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\Data-driven_Building_simulation_Polimi_EETBS-master\Data"

ConsumptionFileName="consumption_5545.csv"
TemperatureFileName="Austin_weather_2014.csv"
IrradianceFileName="irradiance_2014_gen.csv"
path_ConsumptionFileName=os.path.join(ExternalFiles_Folder,ConsumptionFileName)
path_TemperatureFileName=os.path.join(ExternalFiles_Folder,TemperatureFileName)
path_IrradianceFileName=os.path.join(ExternalFiles_Folder,IrradianceFileName)

DF_consumption= pd.read_csv(path_ConsumptionFileName, sep=",", index_col=0)

oldindex_consumption= DF_consumption.index
NewParsedIndex=pd.to_datetime(oldindex_consumption)
DF_consumption.index=NewParsedIndex

DF_consumption_July=DF_consumption.loc["2014-07-01 00:00:00":"2014-08-01 00:00:00"]

fig1=plt.figure()
plt.plot(DF_consumption_July)
plt.xlabel("Time")
plt.ylabel("power cons (W)")
plt.grid()
plt.show()


DF_weather=pd.read_csv(path_TemperatureFileName, sep=";", index_col=0)

oldindex_weather= DF_weather.index
newParshedIndex_weather=pd.to_datetime(oldindex_weather)
newParshedIndex_weather=newParshedIndex_weather.tz_localize("UTC").tz_convert('America/Mexico_City').tz_localize(None)
DF_weather.index=newParshedIndex_weather

DF_temperature=DF_weather[["temperature"]]
DF_temperature_July=DF_temperature.loc["2014-07-01 00:00:00":"2014-08-01 00:00:00"]

fig2=plt.figure()
plt.plot(DF_temperature_July)
plt.xlabel("Time")
plt.ylabel("Temp")
plt.grid()
plt.show()

DF_IrradianceSource=pd.read_csv(path_IrradianceFileName, sep=";", index_col=1)
DF_irradiance=DF_IrradianceSource[["gen"]]
oldIndex_irradiance=DF_irradiance.index
newIndex_irradiance=pd.to_datetime(oldIndex_irradiance)


DF_irradiance.index=newIndex_irradiance


DF_irradiance.loc[DF_irradiance.loc[:,"gen"]<0.0,:]=0.0

DF_irradiance_July=DF_irradiance.loc["2014-07-01 00:00:00":"2014-08-01 00:00:00"]

fig3=plt.figure()
plt.plot(DF_irradiance_July)
plt.xlabel("Time")
plt.ylabel("Irradiance")
plt.grid()
plt.show()

DF_joined=DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined_July=DF_joined.loc["2014-07-01 00:00:00":"2014-08-01 00:00:00"]
DF_joined_clean=DF_joined_July.dropna() 

sumofcons=DF_joined_clean["air conditioner_5545"]
sumodtemp=DF_joined_clean["temperature"]
sumofgen=DF_joined_clean["gen"]



minaric=min(DF_joined_clean["air conditioner_5545"])
maxairc=max(DF_joined_clean["air conditioner_5545"])

mintemp=min(DF_joined_clean["temperature"])
maxtemp=max(DF_joined_clean["temperature"])

mingen=min(DF_joined_clean["gen"])
maxgen=max(DF_joined_clean["gen"])

DF_normal=DF_joined_clean
DF_normal["air conditioner_5545"]=(DF_joined_clean["air conditioner_5545"]-minaric)/(maxairc-minaric)
DF_normal["temperature"]=(DF_joined_clean["temperature"]-mintemp)/(maxtemp-mintemp)
DF_normal["gen"]=(DF_joined_clean["gen"]-mingen)/(maxgen-mingen)

fig4=plt.figure()
plt.plot(DF_joined)
plt.xlabel("Time")
plt.ylabel("Values")
plt.grid()
plt.show()

fig5=plt.figure()
plt.plot(DF_normal)
plt.xlabel("Time")
plt.ylabel("Normalized_Values")
plt.grid()
plt.show()

