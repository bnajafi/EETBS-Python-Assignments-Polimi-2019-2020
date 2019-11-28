import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


ConsumptionFileName = "consumption_5545.csv"
TemperatureFileName = "Austin_weather_2014.csv"
IrradianceFileName = "irradiance_2014_gen.csv"
ExternalFiles_folder = r"C:\Users\david\Desktop\ERASMUS\2_POLIMI\1_SEMESTER\Building Systems\3_My assignments\Data\Data"

path_consumptionFile = os.path.join(ExternalFiles_folder , ConsumptionFileName)
path_TemperatureFile = os.path.join(ExternalFiles_folder , TemperatureFileName)
path_IrradianceFile = os.path.join(ExternalFiles_folder , IrradianceFileName)

#Read Windows_DF csv
DF_consumption = pd.read_csv(path_consumptionFile , sep = "," , index_col = 0)
DF_weather = pd.read_csv(path_TemperatureFile , sep = ";" , index_col = 0)
DF_IrradianceSource = pd.read_csv(path_IrradianceFile , sep = ";" , index_col = 1)

#converting the index to real timestamps
#Consumption
oldIndex_consumption = DF_consumption.index
NewParsedIndex =  pd.to_datetime(oldIndex_consumption)
DF_consumption.index = NewParsedIndex
#Weather
oldIndex_weather = DF_weather.index
NewParsedIndex_weather = pd.to_datetime (oldIndex_weather)
DF_weather.index = NewParsedIndex_weather
#Irradiance
oldIndex_Irradiance = DF_IrradianceSource.index 
NewParsedIndex_Irradiance = pd.to_datetime (oldIndex_Irradiance)
DF_IrradianceSource.index = NewParsedIndex_Irradiance

#Consumption
#visualizing a part of the dataset (for a limited time)
DF_consumption_1stWeekOfJuly = DF_consumption.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]

consumption_MAX = DF_consumption_1stWeekOfJuly.max()
consumption_min = DF_consumption_1stWeekOfJuly.min()
Dif_con = consumption_MAX - consumption_min
DF_consumption_Normalized = (DF_consumption_1stWeekOfJuly - consumption_min)/Dif_con

#Weather
#visualizing a part of the dataset (for a limited time)
DF_temperature = DF_weather[["temperature"]]# in this way it is  a dataframe !
DF_temperature.loc[: , "temperature"]=DF_temperature.loc[: , "temperature"].shift(-6)
DF_temperature_FirstWeekOfJuly = DF_temperature.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]

temperature_MAX = DF_temperature_FirstWeekOfJuly.max()
temperature_min = DF_temperature_FirstWeekOfJuly.min()
Dif_tem = temperature_MAX - temperature_min
DF_temperature_Normalized = (DF_temperature_FirstWeekOfJuly - temperature_min)/Dif_tem

#Irradiance
DF_Irradiance = DF_IrradianceSource[["gen"]]# in this way it is  a dataframe !
DF_Irradiance.loc[DF_Irradiance.loc[: , "gen"]<0 ,:]=0#Those negative values are actually zero, I should convert all of them to zero 
DF_Irradiance_FirstWeekOfJuly = DF_Irradiance.loc["2014-07-01 00:00:00 ":"2014-07-08 00:00:00 "]

irradiance_MAX = DF_Irradiance_FirstWeekOfJuly.max()
irradiance_min = DF_Irradiance_FirstWeekOfJuly.min()
Dif_irr = irradiance_MAX - irradiance_min
DF_irradiance_Normalized = (DF_Irradiance_FirstWeekOfJuly - irradiance_min)/Dif_irr

#plot
fig_1, ax = plt.subplots()
DF_irradiance_Normalized.plot(ax=plt.gca(),color = "yellow")
DF_temperature_Normalized.plot( color = "red", ax=plt.gca())
DF_consumption_Normalized.plot( color = "green", ax=plt.gca()) # the labels will be the name of the columns

plt.xlabel("time")    
plt.ylabel("normalized values")
plt.legend()
plt.title("Consumption,temperature and irradiance data")

#subplots
fig_2,ax = plt.subplots(3)
Xaxis=DF_Irradiance_FirstWeekOfJuly.index

ax[0].plot(Xaxis,DF_consumption_Normalized.loc[:,"air conditioner_5545"],color = "green")
ax[1].plot(Xaxis,DF_temperature_Normalized.loc[:,"temperature"],color = "red")
ax[2].plot(Xaxis,DF_irradiance_Normalized.loc[:,"gen"],color = "yellow")

ax[0].set(xlabel="time", ylabel=" consumption")
ax[1].set(xlabel="time", ylabel="temperature")
ax[2].set(xlabel="time", ylabel="irradiance")

#Save
whereToSaveMyFiles = r"C:\Users\david\Desktop\ERASMUS\2_POLIMI\1_SEMESTER\Building Systems\3_My assignments"
fig1= "figure1.png"
path_figure = os.path.join(whereToSaveMyFiles,fig1)
fig_1.savefig(path_figure)
fig2 = "figure2.png"
path_figure = os.path.join(whereToSaveMyFiles,fig2)
fig_2.savefig(path_figure)



