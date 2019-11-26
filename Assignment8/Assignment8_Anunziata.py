# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

ExternalFiles_folder=r"C:\Users\Angela\Desktop\Building Systems EEE\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFileName="consumption_5545.csv"
TemperatureFileName="Austin_weather_2014.csv"
IraddianceFileName="irradiance_2014_gen.csv"
path_consumptionFile=os.path.join(ExternalFiles_folder,ConsumptionFileName)
path_temperatureFile=os.path.join(ExternalFiles_folder,TemperatureFileName)
path_irradianceFile=os.path.join(ExternalFiles_folder,IraddianceFileName)

#IMPORTING CONSUMPTION + DATETIME (converting index in day time in order to extract time related features)
DF_consumption = pd.read_csv(path_consumptionFile, sep="," , index_col=0)
oldIndex_consumption = DF_consumption.index  
NewIndex_consumption=pd.to_datetime(oldIndex_consumption)
DF_consumption.index=NewIndex_consumption

#IMPORTING WEATHER DATA + DATETIME
DF_weather = pd.read_csv(path_temperatureFile, sep=";" , index_col=0)
oldIndex_weather= DF_weather.index
newIndex_weather=pd.to_datetime(oldIndex_weather)
DF_weather.index=newIndex_weather
   #I just need temperature
DF_temperature= DF_weather[["temperature"]]

#IMPORTING IRRADIANCE DATA + DATETIME
DF_irradianceSorce = pd.read_csv(path_irradianceFile, sep=";" , index_col=1)
DF_irradiance= DF_irradianceSorce[["gen"]] 
oldIndex_irradiance=DF_irradiance.index
newIndex_irradiance=pd.to_datetime(oldIndex_irradiance)
DF_irradiance.index=newIndex_irradiance
   #when is negative is zero
DF_irradiance.loc[DF_irradiance.loc[:,"gen"]<0,:]=0    # or    > ,"gen"] <   perchè ho solo una colonna


# Putting everything together: .join  
DF_joined= DF_consumption.join([DF_temperature,DF_irradiance])

# from Greenwich meridian to Austin meridian (-5 hours)
DF_joined["temperature"]=DF_joined.loc[:,"temperature"].shift(-5)


#PLOTTING
  #Subplots   (1st method subplots)
fig, axs = plt.subplots(3, 1)
fig.suptitle("SUBPLOTS", fontsize=18)

axs[0].plot(DF_joined["temperature"],"r")
axs[0].set_title("Temperature Plot")
axs[0].set_ylabel("Temp [degC]")

axs[1].plot(DF_joined["gen"],"g")
axs[1].set_title("Irradiance Plot")
axs[1].set_ylabel("Irradiance [W/m2]")

axs[2].plot(DF_joined["air conditioner_5545"],"b")
axs[2].set_title("Consumption Plot")
axs[2].set_ylabel("Consumption [W]")
axs[2].set_xlabel("Time")

plt.subplots_adjust(hspace=0.8)
plt.show()

  #Complete plot with normalized values
Temperature_normalized=((DF_joined["temperature"]-DF_joined["temperature"].min())/(DF_joined["temperature"].max()-DF_joined["temperature"].min())).to_frame()
Irradiance_normalized=((DF_joined["gen"]-DF_joined["gen"].min())/(DF_joined["gen"].max()-DF_joined["gen"].min())).to_frame()
Consumption_normalized=((DF_joined["air conditioner_5545"]-DF_joined["air conditioner_5545"].min())/(DF_joined["air conditioner_5545"].max()-DF_joined["air conditioner_5545"].min())).to_frame()

fig2=plt.figure()
plt.plot(Temperature_normalized,"r-.", label="Temperature")
plt.plot(Irradiance_normalized,"g--", label="Irradiance")  
plt.plot(Consumption_normalized,"b-", label="Consumption") 
plt.title("Normalized values", fontsize=18)
plt.xlabel("Time")
plt.legend()
plt.grid()

# FIRST WEEK OF JULY
DF_joined_normalized= Temperature_normalized.join([Irradiance_normalized,Consumption_normalized])
oldIndex_normalized=DF_joined_normalized.index
newIndex_normalized=pd.to_datetime(oldIndex_normalized)
DF_joined_normalized.index=newIndex_normalized
DF_joined_normalized_1week=DF_joined_normalized.loc["2014-07-01 00:00:00" : "2014-07-08 00:00:00"]
DF_joined_1week = DF_joined.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]

  # using pandas .plot (method 1)
fig3=DF_joined_normalized_1week.plot()
plt.grid()
plt.legend(['Temperature', 'Irradiance', 'Consumption'],loc="upper left")
plt.title("Normalized values, 1st WEEK JULY, Pandas", fontsize=18)
plt.xlabel("Time")
plt.show()

  # same using Matplotlib (method 2)
fig4=plt.figure()
plt.plot(DF_joined_normalized_1week["temperature"],"r-x", label="Temperature")
plt.plot(DF_joined_normalized_1week["gen"],"g-o", label="Irradiance")  
plt.plot(DF_joined_normalized_1week["air conditioner_5545"],"b-*", label="Consumption") 
plt.title("Normalized values, 1st WEEK JULY, Matplotlib", fontsize=18)
plt.xlabel("Time")
plt.legend(loc="upper left")
plt.grid()
plt.show()

  # subplots first week July   (2nd method subplots)
fig5= plt.figure()
plt.suptitle("SUBPLOTS 1st week July")

plt.subplot(311)
plt.plot(DF_joined_1week["temperature"])
plt.title("Temperature")
plt.ylabel("Temp [degC]")

plt.subplot(312)
plt.plot(DF_joined_1week["gen"])
plt.title("Irradiance")
plt.ylabel("Irradiance [W/m2]")

plt.subplot(313)
plt.plot(DF_joined_1week["air conditioner_5545"])
plt.title("Consumption")
plt.ylabel("Consumption [W]")
plt.xlabel("Time")
plt.rc("xtick", labelsize=7)

plt.subplots_adjust(hspace = 0.8)
plt.show()