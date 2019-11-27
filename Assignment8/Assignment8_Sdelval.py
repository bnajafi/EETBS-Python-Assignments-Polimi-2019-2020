# -*- coding: utf-8 -*-
#Assignment N°8
#Importing part
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Searching for the files 
Loc1=r"C:\Users\Santi\Desktop\MoS Politecnico di Milano\3 Semestre\Building Systems\Data-driven_Building_simulation_Polimi_EETBS\Data"
os.chdir(Loc1)
os.getcwd()

ConsumptionF="consumption_5545.csv"
TemperatureF="Austin_weather_2014.csv"
IrradianceF="irradiance_2014_gen.csv"
path_C=os.path.join(Loc1,ConsumptionF)
path_T=os.path.join(Loc1,TemperatureF)
path_I=os.path.join(Loc1,IrradianceF)

#Data framing the files
DFC= pd.read_csv(path_C, sep=",", index_col=0)
print(DFC)

DFT=pd.read_csv(path_T, sep=";" , index_col=0)
print(DFT)

DFI=pd.read_csv(path_I, sep=";" , index_col=1)
print(DFI)

#Converting indexes into real time stamps
DFC.index=pd.to_datetime(DFC.index)
print(DFC.index)

DFT.index=pd.to_datetime(DFT.index)
print(DFT.index)

DFI.index=pd.to_datetime(DFI.index)
print(DFI.index)

#Defining the dataframe for the first week
DFC_firstweek=DFC.loc["2014-07-01 00:00:00" : "2014-07-07 00:00:00", :]
print(DFC_firstweek)

DFT.loc[:,"temperature"]=DFT.loc[:,"temperature"].shift(-5)
DFT_firstweek=DFT.loc["2014-07-01 00:00:00" : "2014-07-07 00:00:00", "temperature"]
print(DFT_firstweek)

DFIgen=DFI.loc[:,["gen"]]
DFIgen.loc[DFIgen.loc[:,"gen"]<0,]=0
print(DFIgen)
DFI.loc[:,"gen"]=DFIgen
DFI_firstweek=DFI.loc["2014-07-01 00:00:00" : "2014-07-07 00:00:00", "gen"]
print(DFI_firstweek)

#Plotting-sub plots(first week of July)
get_ipython().magic(u'matplotlib notebook')
plt.figure()
fig, ax = plt.subplots(3)
ax[0].plot(DFC_firstweek,"r")
ax[0].set(xlabel="Time",ylabel="AC Power (W)")
ax[0].set_title("AC power consumption in the first week of July")
ax[1].plot(DFT_firstweek,"g")
ax[1].set(xlabel="Time",ylabel="Temperature (F)")
ax[1].set_title("Temperature variation in the first week of July")
ax[2].plot(DFI_firstweek,"b")
ax[2].set(xlabel="Time",ylabel="Generation (W)")
ax[2].set_title("Generation produced during the first week of July") 

#Normalising the data
#Temperature
DFTj=DFT.loc[:,"temperature"]
MaxT=DFTj.max()
print(MaxT)


#AC consumption
DFCj=DFC.loc[:,"air conditioner_5545"]
MaxC=DFCj.max()
print(MaxC)


#Irradiance
DFIj=DFI.loc[:,"gen"]
MaxI=DFIj.max()
print(MaxI)


#Regrouping Dataframes and plotting simultaneously
DF=DFC.join([DFT,DFI])
DF=DF.loc[:,["temperature","gen","air conditioner_5545"]]
DF=DF.loc["2014-07-01 00:00:00" : "2014-07-07 00:00:00",:]
DF.loc[:,"temperature"]=DF.loc[:,"temperature"]/MaxT
DF.loc[:,"gen"]=DF.loc[:,"gen"]/MaxI
DF.loc[:,"air conditioner_5545"]=DF.loc[:,"air conditioner_5545"]/MaxC
print(DF)

plt.figure()
ax=plt.gca()
DF.plot(kind="line",y="temperature",color="red",ax=ax)
DF.plot(kind="line",y="gen",color="blue",ax=ax)
DF.plot(kind="line",y="air conditioner_5545",color="green",ax=ax)
plt.xlabel("Time")
plt.ylabel("AC Power (W)  /  Temperature(F)  /  Generation(W)")
plt.title("Variation in parameters through the first week of July")
plt.legend(loc="upper left")
plt.grid()
plt.show()

clear
