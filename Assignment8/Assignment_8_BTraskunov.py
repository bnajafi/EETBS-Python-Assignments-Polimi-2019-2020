import os
import pandas as pd
import matplotlib.pyplot as plt 

ExternalFiles_folder = r"C:\Users\Class2018\OneDrive - Politecnico di Milano\Master Class Materials\Semester 3\Building Systems\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConspumtionFile = "consumption_5545.csv"
TemperatureFile = "Austin_weather_2014.csv"
IrradianceFile = "irradiance_2014_gen.csv"

path_ConsumptionFile = os.path.join(ExternalFiles_folder,ConspumtionFile)
path_TemperatureFile = os.path.join(ExternalFiles_folder,TemperatureFile)
path_IrradianceFile = os.path.join(ExternalFiles_folder,IrradianceFile)

Consumption_DF = pd.read_csv(path_ConsumptionFile, sep = ",", index_col = 0)

Consumption_oldIndex = Consumption_DF.index
Consumption_newIndex = pd.to_datetime(Consumption_oldIndex)

Consumption_DF.index = Consumption_newIndex

DF_weather = pd.read_csv(path_TemperatureFile,sep=";", index_col=0)

oldIndex_weather = DF_weather.index
newParsedIndex_weather = pd.to_datetime(oldIndex_weather)
DF_weather.index=newParsedIndex_weather

DF_temperature = DF_weather[["temperature"]]

DF_irradianceSource = pd.read_csv(path_IrradianceFile, sep = ";", index_col = 1)
DF_irradiance = DF_irradianceSource.loc[:,["gen"]]

oldIndex_irradiance = DF_irradiance.index
newIndex_irradiance = pd.to_datetime(oldIndex_irradiance)
DF_irradiance.index = newIndex_irradiance

conditionNegative =DF_irradiance.loc[:,"gen"]<0
DF_irradiance.loc[conditionNegative,"gen"]=0

DF_joined = Consumption_DF.join([DF_temperature,DF_irradiance])

DF_joined.loc[:,"temperature"].shift(-5)

maxval=DF_joined.max()
minval=DF_joined.min()

DF_joined.loc[:,"air conditioner_5545"] = (DF_joined.loc[:,"air conditioner_5545"]-minval[0])/(maxval[0]-minval[0])
DF_joined.loc[:,"temperature"] = (DF_joined.loc[:,"temperature"]-minval[1])/(maxval[1]-minval[1])
DF_joined.loc[:,"gen"] = (DF_joined.loc[:,"gen"]-minval[2])/(maxval[2]-minval[2])

fig1 = plt.figure()
plt.plot(DF_joined)
plt.xlabel = ("Time")
plt.ylabel = ("Variable Value")
plt.grid()
plt.legend(loc="upper left")
plt.show()

plt.savefig('/Users/Class2018/OneDrive - Politecnico di Milano/Master Class Materials/Semester 3/Building Systems/Assignment8(Part1).png')

fig2 = DF_joined.plot(subplots=True)
plt.xlabel = ("Time")
plt.ylabel = ("Normalized Values")
plt.grid()
plt.show

plt.savefig('/Users/Class2018/OneDrive - Politecnico di Milano/Master Class Materials/Semester 3/Building Systems/Assignment8(Part2).png')
