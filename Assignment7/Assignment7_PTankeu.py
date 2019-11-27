#!/usr/bin/env python
# coding: utf-8

# In[95]:


import os
import pandas as pd


# In[96]:


Folder_of_interest = r"C:\Users\philt\OneDrive\Desktop\Data Folder"
Windows_DF= pd.read_csv("windows_file.csv",sep=",",index_col=0,header=0)
Windows_DF


# In[97]:


latitude = "45"
deltaT_cool = 7.9
deltaT_heat = 24.9
DR_cooling = 11.9
U_operable = 2.87
U_fixed = 2.84
SHGC_operable = 0.46
SHGC_fixed = 0.54


# In[98]:


def FFs_calculator(HouseType):
    
    House_Type = "SingleFamilyDetached"
    FF_path_file = os.path.join(Folder_of_interest,"FFs.csv")
    FF_DF = pd.read_csv(FF_path_file,sep=";",index_col=0,header=0)
    FF_value = FF_DF.loc[HouseType,House_Type]
    return FF_value


# In[99]:


Windows_DF.loc[:,"FFs"]=Windows_DF.loc[:,"Direction"].apply(FFs_calculator)


# In[100]:


def SLF_calculator(variable):
    path_file_SLF = os.path.join(Folder_of_interest,"SLF.csv")
    SLF_DF = pd.read_csv(path_file_SLF, sep=";",index_col=0,header=0)
    Value_SLF = SLF_DF.loc[variable,latitude]
    return Value_SLF
Windows_DF.loc[:,"SLF"] = Windows_DF.loc[:,"Direction"].apply(SLF_calculator)


# In[101]:


def IrradianceBeam_Find(var):
    path_irradiance = os.path.join(Folder_of_interest,"BeamIrradiance.csv")
    irradiance_DF =pd.read_csv(path_irradiance, sep = ";", index_col = 0, header =0)
    ED_value = irradiance_DF.loc[var,latitude]
    return ED_value
Windows_DF.loc[:,"ED"] = Windows_DF.loc[:,"Direction"].apply(IrradianceBeam_Find)
Windows_DF  


# In[105]:


Windows_DF.loc[Windows_DF.iloc[:,5]=="Fixed", "U"] = U_fixed
Windows_DF.loc[Windows_DF.iloc[:,5]=="Operable", "U"] = U_operable
Windows_DF.loc[Windows_DF.iloc[:,5]=="Fixed", "SHGC"] = SHGC_fixed
Windows_DF.loc[Windows_DF.iloc[:,5]=="Operable", "SHGC"] = SHGC_operable
Windows_DF.loc[:,"HF"]=Windows_DF.loc[:,"U"]*deltaT_heat
Windows_DF


# In[107]:


def diffuse(var):
    diffuse_path = os.path.join(Folder_of_interest,"DiffuseIrradiance.csv")
    diffuse_DF = pd.read_csv(diffuse_path,sep=";", index_col=0,header=0)
    Ed_value = diffuse_DF.loc[var,latitude]
    return Ed_value
Windows_DF.loc[:,"Ed"]=Windows_DF.loc[:,"Direction"].apply(diffuse)


# In[115]:


Windows_DF.loc[:,"Fshd"] = Windows_DF.loc[:,"SLF"]*Windows_DF.loc[:,"Doh"]-Windows_DF.loc[:,"Xoh"]
Windows_DF.loc[Windows_DF.loc[:,"Fshd"]>1,"Fshd"]=1


# In[119]:


Windows_DF.loc[:,"PXI"] = Windows_DF.loc[:,"Tx"]*(Windows_DF.loc[:,"Ed"]+(1-Windows_DF.loc[:,"Fshd"])*Windows_DF.loc[:,"ED"])
Windows_DF


# In[123]:


Windows_DF.loc[:,"Q heating"] = Windows_DF.loc[:,"HF"]*Windows_DF.loc[:,"Area"]
Windows_DF.loc[:,"Q heating"]


# In[125]:


Windows_DF.loc[:,"CF"]= Windows_DF.loc[:,"U"]*(deltaT_cool-
0.46*DR_cooling)+Windows_DF.loc[:,"PXI"]*Windows_DF.loc[:,"SHGC"]*Windows_DF.loc[:,"IAC"]*Windows_DF.loc[:,"FFs"]


# In[129]:


Windows_DF.loc[:,"Qcooling"] = Windows_DF.loc[:,"CF"]*Windows_DF.loc[:,"Area"]


# In[130]:


window_name = "windows_file.xlsx"
Path_window = os.path.join(Folder_of_interest,window_name)
Windows_DF.to_excel(Path_window)

