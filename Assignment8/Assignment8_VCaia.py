#Assignment 8:Valentina Caia

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


#Creating the pathes for external files to be imported

ExternalFiles_folder =  r"C:\Users\User\Desktop\clonefolder\Data-driven_Building_simulation_Polimi_EETBS\Data"

ConsumptionFileName = "consumption_5545.csv"
TemperatureFileName = "Austin_weather_2014.csv"
IrradianceFileName = "irradiance_2014_gen.csv"

path_ConsumptionFile = os.path.join(ExternalFiles_folder, ConsumptionFileName)
path_TemperatureFile = os.path.join(ExternalFiles_folder, TemperatureFileName)
path_IrradianceFile = os.path.join(ExternalFiles_folder, IrradianceFileName)

#Importing datasets
DF_Consumption = pd.read_csv(path_ConsumptionFile, sep = ",", index_col = 0)
DF_Weather = pd.read_csv(path_TemperatureFile, sep =";", index_col = 0)
DF_IrradianceSource = pd.read_csv(path_IrradianceFile, sep=";", index_col = 1)


#Converting the index to real timestamps

OldIndex_consumption = DF_Consumption.index
NewParsedIndex_consumption = pd.to_datetime(OldIndex_consumption)
print(NewParsedIndex_consumption)
DF_Consumption.index = NewParsedIndex_consumption

OldIndex_weather = DF_Weather.index
NewParsedIndex_weather = pd.to_datetime(OldIndex_weather)
NewParsedIndex_weather = NewParsedIndex_weather.tz_localize("UTC").tz_convert('America/Mexico_City').tz_localize(None) #since it was localized in UTC (Greenwich) we need to remove the time zone and convert it for the Mexico City
print(NewParsedIndex_weather)
DF_Weather.index = NewParsedIndex_weather
print(DF_Weather.columns)

OldIndex_irradiance = DF_IrradianceSource.index
NewParsedIndex_irradiance = pd.to_datetime(OldIndex_irradiance)
DF_IrradianceSource.index = NewParsedIndex_irradiance
print(DF_IrradianceSource.index)


#Visualizing a part of the dataset (limited time: first week of July 2014)

DF_Consumption_FirstWeekOfJuly = DF_Consumption.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"] 
print(DF_Consumption_FirstWeekOfJuly)

DF_Temperature = DF_Weather[["temperature"]] 
print(DF_Temperature)
DF_Temperature_FirstWeekOfJuly = DF_Temperature.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00"]
print(DF_Temperature_FirstWeekOfJuly)

DF_Irradiance = DF_IrradianceSource[["gen"]]
DF_Irradiance.loc[DF_Irradiance.loc[:, "gen"] < 0, :] = 0  #converting them to zero
DF_Irradiance_FirstWeekOfJuly = DF_Irradiance.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00"]
print(DF_Irradiance_FirstWeekOfJuly)


#Plotting the extracted sub-dataset (Method one: Matplotlib library)
Figure_1 = plt.figure()
plt.plot(DF_Consumption_FirstWeekOfJuly)
plt.xlabel("Time")
plt.ylabel("AC Power [W]")
plt.grid()
plt.show()


#Plotting the extracted sub-dataset (Method two: Pandas) - best way

Figure1 = plt.figure()
DF_Consumption_FirstWeekOfJuly.plot()
plt.xlabel("Time")
plt.ylabel("AC Power [W]")
plt.grid()
plt.legend(loc = "upper center")
plt.show()

Figure2 = DF_Temperature_FirstWeekOfJuly.plot()
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.grid()
plt.show()

Figure3 = DF_Irradiance_FirstWeekOfJuly.plot()
plt.xlabel("Time")
plt.ylabel("Irradiance")
plt.grid()
plt.show()


#Putting everythnig together
DF_joinedFirstWeekOfJuly = DF_Consumption_FirstWeekOfJuly.join([DF_Temperature_FirstWeekOfJuly, DF_Irradiance_FirstWeekOfJuly])
print(DF_joinedFirstWeekOfJuly.head(12))


#Creating subplots
fig,ax = plt.subplots(3)
ax[0].plot(DF_Consumption_FirstWeekOfJuly, "g")
ax[1].plot(DF_Temperature_FirstWeekOfJuly, "r--")
ax[2].plot(DF_Irradiance_FirstWeekOfJuly, "b-")

#Putting titles on the subplots
ax[0].set_title("AC Consumption")
ax[1].set_ylabel("Temperature")
ax[2].set_ylabel("Irradiance")



#Normalization

ValueMaximum = DF_joinedFirstWeekOfJuly[['air conditioner_5545', 'temperature', 'gen']].max()
ValueMinimum = DF_joinedFirstWeekOfJuly[['air conditioner_5545', 'temperature', 'gen']].min()
Difference_MaxMin = ValueMaximum - ValueMinimum
DF_NormalizedforFirstWeekOfJuly = DF_joinedFirstWeekOfJuly

DF_NormalizedforFirstWeekOfJuly.loc[:, "air conditioner_5545"] = (DF_joinedFirstWeekOfJuly.loc[:, "air conditioner_5545"] - ValueMinimum['air conditioner_5545']) / Difference_MaxMin['air conditioner_5545']
DF_NormalizedforFirstWeekOfJuly.loc[:, "temperature"] = (DF_joinedFirstWeekOfJuly.loc[:, "temperature"] - ValueMinimum['temperature']) / Difference_MaxMin['temperature']
DF_NormalizedforFirstWeekOfJuly.loc[:, "gen"] = (DF_joinedFirstWeekOfJuly.loc[:, "gen"] - ValueMinimum['gen']) / Difference_MaxMin['gen']

NormalFigure = DF_NormalizedforFirstWeekOfJuly.plot()
plt.xlabel("Time")
plt.grid()
plt.show()
