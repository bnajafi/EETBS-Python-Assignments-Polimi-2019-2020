# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plot


ExternalFiles_folder = r"C:\Users\Rafael Ferrato\Documents\CLASSES_Politecnico_Milano\Building_Systems\Data-driven_Building_simulation_Polimi_EETBS\Data"
ConspumtionFile = "consumption_5545.csv"
TemperatureFile = "Austin_weather_2014.csv"
IrradianceFile = "irradiance_2014_gen.csv"

path_ConsumptionFile = os.path.join(ExternalFiles_folder,ConspumtionFile)
path_TemperatureFile = os.path.join(ExternalFiles_folder,TemperatureFile)
path_IrradianceFile = os.path.join(ExternalFiles_folder,IrradianceFile)


# ## Importing and formating the consumption database


Consumption_DF = pd.read_csv(path_ConsumptionFile, sep = ",", index_col = 0)

Consumption_DF

# #### The program doesn't know this is a TIME STAMP on the INDEX! WE NEED TO MAKE IT UNDERSTAND!

Consumption_oldIndex = Consumption_DF.index
Consumption_newIndex = pd.to_datetime(Consumption_oldIndex) 

# the 'datetime' makes the program understant that the values are dates!
# Consumption_newIndex


# ### Now we assign our new index as the head:

Consumption_DF.index = Consumption_newIndex


# ### We can extract time related features from the table now!!

Consumption_DF_FirstWeekofJuly = Consumption_DF.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]
print Consumption_DF_FirstWeekofJuly


# ### Now let's PLOT!

get_ipython().magic(u'matplotlib notebook')

#Another way of doing the same thing up there, BUT BETTER! 

plot.close("all")
fig1 = Consumption_DF_FirstWeekofJuly.plot()
plot.xlabel("Time")         #Used to name the axis!
plot.ylabel("AC Consumption (W)") #Used to name the axis!

plot.legend(loc = "upper left") #Used to change where the the legend of the graph goes

plot.grid()                 #Used to add a grid to the figure!


# ## Importing Weather Related Files

Weather_DF = pd.read_csv(path_TemperatureFile, sep = ",", index_col = 0)
# Weather_DF

Weather_oldIndex = Weather_DF.index
Weather_newIndex = pd.to_datetime(Weather_oldIndex) # the 'datetime' makes the program understant that the values are dates!
Weather_newIndex = Weather_newIndex.tz_localize("UTC").tz_convert('America/Mexico_City').tz_localize(None)
Weather_DF.index = Weather_newIndex

#TO GET THE TEMPERATURES FROM THE WEATHER TABLE WE NEED TO CREATE A LIST OF LISTS:
# We get only the temperature column of the file and we will have the temperature for each day!

Temperature_DF = Weather_DF[["temperature"]]
# Temperature_DF.index


Temperature_DF_FirstWeekofJuly = Temperature_DF.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]
print Temperature_DF_FirstWeekofJuly

fig2 = Temperature_DF_FirstWeekofJuly.plot()
plot.xlabel("Time")         #Used to name the axis!
plot.ylabel("Temperature (F)") #Used to name the axis!

plot.legend(loc = "upper left") #Used to change where the the legend of the graph goes

plot.grid()                 #Used to add a grid to the figure!

Irradiance_Source = pd.read_csv(path_IrradianceFile, sep = ",", index_col=1)
Irradiance_DF = Irradiance_Source.loc[:,["gen"]]
Irradiance_DF.head(24)


Irradiance_oldIndex = Irradiance_DF.index
Irradiance_newIndex = pd.to_datetime(Irradiance_oldIndex) 

# the 'datetime' makes the program understant that the values are dates!
Irradiance_DF.index = Irradiance_newIndex


Irradiance_DF_FirstWeekofJuly = Irradiance_DF.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]
print Irradiance_DF_FirstWeekofJuly

fig3 = Irradiance_DF_FirstWeekofJuly.plot()
plot.xlabel("Time")         #Used to name the axis!
plot.ylabel("Irradiance (W)") #Used to name the axis!

plot.legend(loc = "upper left") #Used to change where the the legend of the graph goes

plot.grid()                 #Used to add a grid to the figure!


# SUBPLOTS

fig4 = plot.figure()
plot.subplot(3,1,1)
plot.plot(Consumption_DF_FirstWeekofJuly,color = "b")
plot.subplot(3,1,2)
plot.plot(Temperature_DF_FirstWeekofJuly,color = "r")
plot.subplot(3,1,3)
plot.plot(Irradiance_DF_FirstWeekofJuly,color = "k")

#JOIN ALL IN ONE TABLE

Joined_DF = Consumption_DF.join([Temperature_DF, Irradiance_DF])
# print Joined_DF

## GET RID OF THE NAN VALUES

Joined_DF = Joined_DF.dropna() 
# print Joined_DF


Joined_DF_FirstWeekofJuly = Joined_DF.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]

Joined_DF_FirstWeekofJuly

# Let's plot it!

fig5 = Joined_DF_FirstWeekofJuly.plot()
plot.xlabel("Time")
plot.grid()
plot.show()


#NORMALIZATION 

MaxValues = Joined_DF[['air conditioner_5545','temperature','gen']].max()
MinValues = Joined_DF[['air conditioner_5545','temperature','gen']].min()
Difference = MaxValues - MinValues
Normalized_Joined_DF = Joined_DF

Normalized_Joined_DF.loc[:,"air conditioner_5545"]=(Joined_DF.loc[:,"air conditioner_5545"]-MinValues['air conditioner_5545'])/Difference['air conditioner_5545']
Normalized_Joined_DF.loc[:,"temperature"]=(Joined_DF.loc[:,"temperature"]-MinValues['temperature'])/Difference['temperature']
Normalized_Joined_DF.loc[:,"gen"]=(Joined_DF.loc[:,"gen"]-MinValues['gen'])/Difference['gen']

print Normalized_Joined_DF

#GET FIRS WEEK OF JULY
Normalized_Joined_DF_FirstWeekofJuly = Normalized_Joined_DF.loc["2014-07-01 00:00:00":"2014-07-08 00:00:00"]

#PLOT

fig6 = Normalized_Joined_DF_FirstWeekofJuly.plot()
plot.xlabel("Time")
plot.grid()
plot.show()

