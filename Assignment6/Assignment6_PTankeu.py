#!/usr/bin/env python
# coding: utf-8

# #### Assignment 6

# In[1]:


import pandas as pd
import os


# In[2]:


resistances_names = ["R_outside","R_woodB","R_fiberboard","R_glass","R_Woodstud","R_gypsum","R_inside"]
resistances_types = ["conv","cond","cond","cond","cond","cond","conv"]
resistances_Rval_standard = [0.03,0.14,0.23,0.7,0.63,0.079,0.12]
resistances_L_standard=  [None,0.013,0.013,0.025,0.09,0.013,None]
resistances_L= [None,0.013,0.013,0.09,0.09,0.013,None]
resistances_RValues=[0,0,0,0,0,0,0]
resistance_lists =[resistances_types,resistances_Rval_standard,resistances_L_standard,resistances_L,resistances_RValues]


# In[4]:


resistances_DF = pd.DataFrame(resistance_lists, index=["type","R_Standard","L_stand","L","R_value"],columns=["R_outside","R_woodB","R_fiberboard","R_glass","R_Woodstud","R_gypsum","R_inside"])
resistances_DF=resistances_DF.transpose()
resistances_DF


# In[7]:


os.chdir(r"C:\Users\philt\OneDrive - Politecnico di Milano\LECTURES\Building Systems\Codes")
os.getcwd()


# In[8]:


resistances_DF.to_excel("Data_Assignment6.xlsx")


# In[10]:


File_location = r"C:\Users\philt\OneDrive - Politecnico di Milano\LECTURES\Building Systems\Codes"
Name_of_file = "Data_Assignment6.xlsx"
file_path = os.path.join(File_location,Name_of_file)
file_path


# In[19]:


def R_val_calculator(length):
    resistances_DF.loc[resistances_DF.loc[:,"type"] == "cond","R_value"] = resistances_DF.loc[:,"R_Standard"]*(resistances_DF.loc[:,"L"]/resistances_DF.loc[:,"L_stand"])
    resistances_DF.loc[resistances_DF.loc[:,"type"] == "conv","R_value"] = resistances_DF.loc[:,"R_Standard"]
    
resistances_DF.loc[:,:].apply(R_val_calculator)


# In[20]:


resistances_DF


# In[25]:


R_tot_wood = sum(resistances_DF.loc[:,"R_value"])-resistances_DF.loc["R_glass","R_value"]
R_tot_glass = sum(resistances_DF.loc[:,"R_value"])-resistances_DF.loc["R_Woodstud","R_value"]
    
U_tot_glass = 1.0/R_tot_glass
U_tot_wood = 1.0/R_tot_wood

U_tot_wall = 0.25*U_tot_wood +0.75*U_tot_glass
A_wall_net = 0.8*50*2.5
T_indoor= 22
T_outdoor = -2
Q_wall = round((U_tot_wall*A_wall_net*(T_indoor-T_outdoor)),4)


# In[26]:


print(f"The total heat loss is {Q_wall} W")

