# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:13:00 2019

@author: sajid ali
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
### importing data set
externalfiles_folder = r"D:\data\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConsumptionFilesname="consumption_5545.csv"
TempertaureFilename="Austin_weather_2014.csv"
IrradianceFilename="irradiance_2014_gen.csv"

##importind consumption,generation from pv plant,
path_ConsumptionFile=os.path.join(externalfiles_folder,ConsumptionFilesname)
path_TemperatureFile=os.path.join(externalfiles_folder,TempertaureFilename)
path_IrradianceFilename=os.path.join(externalfiles_folder,IrradianceFilename)

DF_Consumption = pd.read_csv(path_ConsumptionFile,sep=",",index_col=0)
## coverting Date and time index
oldIndex_consumption = DF_Consumption.index
NewparsedIndex= pd.to_datetime(oldIndex_consumption )
NewparsedIndex
DF_Consumption.index = NewparsedIndex
DF_Consumption

DF_weather = pd.read_csv(path_TemperatureFile,sep=";",index_col=0)
oldindex_weather = DF_weather.index
newparsedindex_weather = pd.to_datetime(oldindex_weather)
DF_weather.index = newparsedindex_weather
DF_weather

DF_irrandiancesource = pd.read_csv(path_IrradianceFilename,sep=";",index_col=1)
oldindex_irrandiance = DF_irradiance.index
newindex_irrandiance = pd.to_datetime(oldindex_irrandiance)
DF_irradiance.index = newindex_irrandiance
DF_irradiance

DF_Consumption
DF_temperature = DF_weather.loc[:,["temperature"]]
DF_irradiance = DF_irrandiancesource.loc[:,["gen"]]

DF_joined = DF_Consumption.join([DF_temperature,DF_irradiance])
DF_joined.index

#fig,ax =plt.subplots(2) # fig is the whole frame i which  wea re
#ax[0].plot(DF_joined.index,DF_joined.loc[:,["temperature"]],"-c")
#ax[1].plot(DF_joined.index,DF_joined.loc[:,["gen"]],"--ob")

Firstweek_july_temp=DF_joined.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00","temperature"]
Firstweek_july_gen=DF_joined.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00","gen"]
Firstweek_july_consumption=DF_joined.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00","air conditioner_5545"]

plt.figure(1)
fig,ax =plt.subplots(3) # fig is the whole frame i which  wea re
ax[0].plot(Firstweek_july_temp,"-c",label="temp")
ax[1].plot(Firstweek_july_gen,"--c",label="gen")
ax[2].plot(Firstweek_july_consumption,"--b",label="consumption")
plt.xlabel("Time")
plt.legend(loc="upper right")
plt.grid()
plt.show()
#######
DF_Newdata = pd.DataFrame(DF_joined.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00",:],columns=["air conditioner_5545","temperature","gen"])
##### creating colum for normalize values
DF_Newdata.loc[:,"norm_temp"]=0
DF_Newdata.loc[:,"norm_gen"]=0
DF_Newdata.loc[:,"norm_consumption"]=0
DF_Newdata.loc[DF_Newdata.loc[:,"gen"]<0,"gen"]=0
#### to calculate max and mini following step
consumption_july=DF_Newdata.loc[:,"air conditioner_5545"]
temp_july = DF_Newdata.loc[:,"temperature"]
gen_july = DF_Newdata.loc[:,"gen"]
####### normalizing the values 
DF_Newdata.loc[:,"norm_temp"]=(DF_Newdata.loc[:,"temperature"]-temp_july.min())/(temp_july.max()-temp_july.min())
DF_Newdata.loc[:,"norm_gen"]=(DF_Newdata.loc[:,"gen"]-gen_july.min())/(gen_july.max()-gen_july.min())
DF_Newdata.loc[:,"norm_consumption"]=(DF_Newdata.loc[:,"air conditioner_5545"]-consumption_july.min())/(consumption_july.max()-gen_july.min())
##### draw a graph

 #plot graph with normalize values
plt.figure()
plt.plot(DF_Newdata.loc[:,"norm_temp"],"-r",label="temp")
plt.plot(DF_Newdata.loc[:,"norm_gen"],"-g",label="gen")
plt.plot(DF_Newdata.loc[:,"norm_consumption"],"-b",label="consumption")
plt.xlabel("Time")
plt.legend(loc="upper right")
plt.grid()
plt.show()
save =r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone"
file_name = "assiginment8_SALI.png"
path_join =os.path.join(save,file_name)
fig.savefig(path_join)