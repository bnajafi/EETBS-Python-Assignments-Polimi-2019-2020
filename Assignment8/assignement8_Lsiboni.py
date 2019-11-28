import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt 

files_folder = r"C:\Users\lorenzo\Desktop\somewhere"
consumption_file = "consumption_5545.csv"
temperature_file = "Austin_weather_2014.csv"
irradiance_file = "irradiance_2014_gen.csv"
path_consumption = os.path.join(files_folder,consumption_file)
path_temperature = os.path.join(files_folder,temperature_file)
path_irradiance = os.path.join(files_folder,irradiance_file)

# Consumption

DF_consumption = pd.read_csv(path_consumption,sep = ",", index_col = 0)
DF_weather = pd.read_csv(path_temperature,sep=";",index_col=0)
DF_irradiance_source = pd.read_csv(path_irradiance,sep=";",index_col=1)

old_index_consumption = DF_consumption.index
new_index_consumption = pd.to_datetime(old_index_consumption)
DF_consumption.index = new_index_consumption

DF_consumption_first_week_july = DF_consumption.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]  # first week of july

consumption_MAX = DF_consumption_first_week_july.max()
consumption_min = DF_consumption_first_week_july.min()

DF_consumption_NORMALIZED = (DF_consumption_first_week_july - consumption_min)/(consumption_MAX - consumption_min)

# Weather

old_index_weather = DF_weather.index
new_index_weather = pd.to_datetime(old_index_weather)
DF_weather.index = new_index_weather

DF_weather.loc[:,"temperature"]=DF_weather.loc[:,"temperature"].shift(-5)  # adjusting values according to time
DF_temperature = DF_weather[["temperature"]]   # because we need only the column of temperatures, in form of dataframe

DF_temperature_first_week_july = (DF_temperature.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"] - 32)/1.8
print(DF_temperature_first_week_july)

temperature_MAX = DF_temperature_first_week_july.max()
temperature_min = DF_temperature_first_week_july.min()

DF_temperature_NORMALIZED = (DF_temperature_first_week_july - temperature_min)/(temperature_MAX - temperature_min)
print(DF_temperature_NORMALIZED)

# Irradiance

DF_irradiance = DF_irradiance_source.loc[:,["gen"]]  # we need only this column

old_index_irradiance = DF_irradiance.index
new_index_irradiance = pd.to_datetime(old_index_irradiance)
DF_irradiance.index = new_index_irradiance

condition_negative =  DF_irradiance.loc[:,"gen"]<0
DF_irradiance.loc[condition_negative,"gen"]=0      #setting to zero negative values given by errors of measurement instruments

DF_irradiance_first_week_july = DF_irradiance.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]

irradiance_MAX = DF_irradiance_first_week_july.max()
irradiance_min = DF_irradiance_first_week_july.min()

DF_irradiance_NORMALIZED = (DF_irradiance_first_week_july - irradiance_min)/(irradiance_MAX - irradiance_min)

# PLOTS !

figure1, ax = plt.subplots()
ax = plt.gca()
DF_irradiance_NORMALIZED.plot(ax=ax)
DF_temperature_NORMALIZED.plot( color = "red", ax=ax )
DF_consumption_NORMALIZED.plot( color = "green", ax=ax ) # the labels will be the name of the columns

plt.xlabel("time")    
plt.ylabel("normalized values")
plt.title("Normalized plots of consumption/temperature/irradiance datasets")
plt.legend()

# SUBPLOTS!

ax = plt.gca()
figure2, ax = plt.subplots(3)
DF_irradiance_first_week_july.plot(color = "blue", ax = ax[0])   # the labels will be the name of the columns
DF_temperature_first_week_july.plot(color="red",ax = ax[1])
DF_consumption_first_week_july.plot(color = "green",ax = ax[2])

ax[0].set(xlabel="time", ylabel="irradiance")
ax[1].set(xlabel="time", ylabel="temperature")
ax[2].set(xlabel="time", ylabel="consumption")



whereToSaveMyFiles = r"C:\Users\lorenzo\Desktop\assignements Behzad"
figure1_Name = "my_figure1.png"
path_figure = os.path.join(whereToSaveMyFiles,figure1_Name)
figure1.savefig(path_figure)
figure2_Name = "my_figure2.png"
path_figure = os.path.join(whereToSaveMyFiles,figure2_Name)
figure2.savefig(path_figure)