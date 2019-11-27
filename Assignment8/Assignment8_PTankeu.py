
# coding: utf-8

# In[1]:

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

Folder_I_save = r"C:\Users\philt\OneDrive\Desktop\Data Folder"
file_name = "DF_assignment_8.csv"
file_path= os.path.join(Folder_I_save,file_name)
DF_interest = pd.read_csv(file_path,sep=",",index_col=0)


# In[3]:

old_index =DF_interest.index
NewParsed_index = pd.to_datetime(old_index)
DF_interest.index=NewParsed_index


# In[4]:

Data_first_week_of_july = DF_interest.loc['2014-07-01 00:00:00':'2014-07-08 00:00:00',:]


# In[5]:

Temp_First_week_July = Data_first_week_of_july.loc[:,"temperature"]
air_condition_first_week_july = Data_first_week_of_july.loc[:,"air conditioner_5545"]
gen_first_week_july = Data_first_week_of_july.loc[:,"gen"]


# In[6]:

get_ipython().magic(u'matplotlib notebook')


# In[7]:

fig, ax=plt.subplots(3,sharex=True)
ax[0].plot(air_condition_first_week_july, "-r")
ax[1].plot(Temp_First_week_July,"-b")
ax[2].plot(gen_first_week_july, "-g")


# In[8]:

max_temp = Temp_First_week_July.max()
min_temp= Temp_First_week_July.min()
gen_max = gen_first_week_july.max()
gen_min = gen_first_week_july.min()
air_max = air_condition_first_week_july.max()
air_min = air_condition_first_week_july.min()


# In[9]:

Data_first_week_of_july.loc[:,"normalised temp"] = (Data_first_week_of_july.loc[:,"temperature"]-min_temp)/(max_temp -min_temp)
Data_first_week_of_july.loc[:,"air_cond_norm"] =(Data_first_week_of_july.loc[:,"air conditioner_5545"]-air_min)/(air_max-air_min)
Data_first_week_of_july.loc[:,"gen_norm"]=(Data_first_week_of_july.loc[:,"gen"]-gen_min)/(gen_max-gen_min)


# In[10]:

Data_first_week_of_july


# In[11]:

Normal_temp = Data_first_week_of_july.loc[:,"normalised temp"]
Gen_Norm = Data_first_week_of_july.loc[:,"gen_norm"]
Air_Norm = Data_first_week_of_july.loc[:,"air_cond_norm"]


# In[17]:

plt.figure()
plt.plot(Normal_temp, "-g", label = "Normalised Temperature")
plt.plot(Gen_Norm, "-.r",label="Normalised Gen")
plt.plot(Air_Norm,"--k", label="Normalised AC")
plt.legend(loc="upper right")
plt.grid()

