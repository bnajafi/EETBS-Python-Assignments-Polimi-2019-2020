import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

ExternalFiles_folder = r"C:\Users\fabri\Dropbox\Polimi\3rd Semester\Building Systems\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName = "consumption_5545.csv"
TemperatureFileName = "Austin_weather_2014.csv"
IrradianceFileName = "irradiance_2014_gen.csv"
path_consumptionFile = os.path.join(ExternalFiles_folder , ConsumptionFileName)
path_TemperatureFile = os.path.join(ExternalFiles_folder , TemperatureFileName)
path_IrradianceFile = os.path.join(ExternalFiles_folder , IrradianceFileName)

DF_consumption = pd.read_csv(path_consumptionFile , sep = "," , index_col = 0)
DF_weather = pd.read_csv(path_TemperatureFile , sep = ";" , index_col = 0)
DF_IrradianceSource = pd.read_csv(path_IrradianceFile , sep = ";" , index_col = 1)

oldIndex_consumption = DF_consumption.index
NewParsedIndex =  pd.to_datetime(oldIndex_consumption)
DF_consumption.index = NewParsedIndex
DF_consumption_FirstWeekOfJuly = DF_consumption.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]

oldIndex_weather = DF_weather.index
NewParsedIndex_weather = pd.to_datetime (oldIndex_weather)
DF_weather.index = NewParsedIndex_weather

oldIndex_Irradiance = DF_IrradianceSource.index 
NewParsedIndex_Irradiance = pd.to_datetime (oldIndex_Irradiance)
DF_IrradianceSource.index = NewParsedIndex_Irradiance


DF_temperature = DF_weather[["temperature"]]
DF_temperature.loc[: , "temperature"]=DF_temperature.loc[: , "temperature"].shift(-6)
DF_temperature_FirstWeekOfJuly = DF_temperature.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]

DF_Irradiance = DF_IrradianceSource[["gen"]]
DF_Irradiance.loc[DF_Irradiance.loc[: , "gen"]<0 ,:]=0
DF_Irradiance_FirstWeekOfJuly = DF_Irradiance.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]


Xaxis=DF_Irradiance_FirstWeekOfJuly.index
Yaxis1=DF_consumption_FirstWeekOfJuly.loc[:,"air conditioner_5545"]
Yaxis2=DF_temperature_FirstWeekOfJuly.loc[:,"temperature"]
Yaxis3=DF_Irradiance_FirstWeekOfJuly.loc[:,"gen"]

fig,ax = plt.subplots(3)
ax[0].plot(Xaxis,Yaxis1)
ax[1].plot(Xaxis,Yaxis2)
ax[2].plot(Xaxis,Yaxis3)

ax[0].set_ylabel('AC Consumption [W]')
ax[1].set_ylabel('Temperature')
ax[2].set_ylabel('Irradiance')


DF_joined_FirstWeekOfJuly = DF_consumption_FirstWeekOfJuly.join ([DF_temperature_FirstWeekOfJuly , DF_Irradiance_FirstWeekOfJuly])
MaxValues_FirstWeekOfJuly = DF_joined_FirstWeekOfJuly[['air conditioner_5545','temperature','gen']].max()
MinValues_FirstWeekOfJuly = DF_joined_FirstWeekOfJuly[['air conditioner_5545','temperature','gen']].min()
DifValues_FirstWeekOfJuly=MaxValues_FirstWeekOfJuly-MinValues_FirstWeekOfJuly
DF_Normalized_FirstWeekOfJuly = DF_joined_FirstWeekOfJuly
# Now let's normalize everything in order to plot everything together

DF_Normalized_FirstWeekOfJuly.loc[:,"air conditioner_5545"]=(DF_joined_FirstWeekOfJuly.loc[:,"air conditioner_5545"]-MinValues_FirstWeekOfJuly['air conditioner_5545'])/DifValues_FirstWeekOfJuly['air conditioner_5545']
DF_Normalized_FirstWeekOfJuly.loc[:,"temperature"]=(DF_joined_FirstWeekOfJuly.loc[:,"temperature"]-MinValues_FirstWeekOfJuly['temperature'])/DifValues_FirstWeekOfJuly['temperature']
DF_Normalized_FirstWeekOfJuly.loc[:,"gen"]=(DF_joined_FirstWeekOfJuly.loc[:,"gen"]-MinValues_FirstWeekOfJuly['gen'])/DifValues_FirstWeekOfJuly['gen']

fig4 = DF_Normalized_FirstWeekOfJuly.plot()
plt.xlabel("Time")
plt.grid()
plt.show()

