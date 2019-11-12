
# coding: utf-8

# ## Assignment 6

# In[5]:

import pandas as pd


# In[6]:

resistances_names = ["R_outside","R_woodB","R_fiberboard","R_glass","R_Woodstud","R_gypsum","R_inside"]
resistances_types = ["conv","cond","cond","cond","cond","cond","conv"]
resistances_Rval_standard = [0.03,0.14,0.23,0.7,0.63,0.079,0.12]
resistances_L_standard=  [None,0.013,0.013,0.025,0.09,0.013,None]
resistances_L= [None,0.013,0.013,0.09,0.09,0.013,None]
resistances_RValues=[0,0,0,0,0,0,0]
resistance_lists =[resistances_types,resistances_Rval_standard,resistances_L_standard,resistances_L,resistances_RValues]


# In[7]:

resistances_DF = pd.DataFrame(resistance_lists, index=["type","R_Standard","L_stand","L","R_value"],columns=["R_outside","R_woodB","R_fiberboard","R_glass","R_Woodstud","R_gypsum","R_inside"])
resistances_DF=resistances_DF.transpose()


# ##### Computing the R values

# In[8]:

resistances_DF.loc[resistances_DF["type"]=="cond","R_value"] = resistances_DF.loc[resistances_DF["type"]=="cond","R_Standard"]*resistances_DF.loc[resistances_DF["type"]=="cond","L"]/resistances_DF.loc[resistances_DF["type"]=="cond","L_stand"]
resistances_DF.loc[resistances_DF["type"]=="conv","R_value"] = resistances_DF.loc[resistances_DF["type"]=="conv","R_Standard"]


# ###### Computing R_tot_wood and R_tot_glass

# In[9]:

R_tot_wood = sum(resistances_DF.loc[:,"R_value"])-resistances_DF.loc["R_glass","R_value"]
R_tot_glass = sum(resistances_DF.loc[:,"R_value"])-resistances_DF.loc["R_Woodstud","R_value"] 


# In[10]:

def Utot(input_value):
  output_value = 1.0/input_value
  return output_value
U_tot_wood = Utot(R_tot_wood)
U_tot_glass = Utot(R_tot_glass)
U_tot_wall = 0.25*U_tot_wood+0.75*U_tot_glass
R_tot_wall = round((1/U_tot_wall),4)
print('The total wall unit resistance is ' + str(R_tot_wall)+ ' °C/W.m^2')


# In[11]:

resistances_DF


# ##### Computing rate of heat loss through wall

# In[12]:

T_inside= 22
T_outside = -2
wall_perimeter = 50
wall_heigth = 2.5
GF = 0.2
A_tot_wall = wall_perimeter*wall_heigth
A_actual=A_tot_wall*(1-GF)
Q=round((U_tot_wall*A_actual*(T_inside-T_outside)),4)
print("The rate of heat loss through the wall is "+ str(Q)+ " W")



# ###### Exporting table of Results

# In[13]:

import os


# In[14]:

resistances_DF


# In[15]:

import os
os.chdir(r"C:\Users\philt\OneDrive - Politecnico di Milano\LECTURES\Building Systems")
os.getcwd()
resistances_DF.to_csv("DataFrame.csv")



# In[ ]:



