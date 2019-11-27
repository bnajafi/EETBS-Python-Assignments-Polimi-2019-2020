
# coding: utf-8

# ## ASSIGNMENT 7
# Fill the Windows table

# In[3]:

import os
import numpy as np
import pandas as pd
Folder_whereThoseTablesAre = r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies\ASSIGNMENT 7\TABLES_RFL"
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)



# # Calculate IAC

# In[4]:

name_file_IAC_Cl="IAC_cl.csv"
path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0)
IAC_cl_DF


# In[5]:

def IAC_CL_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,IntShadingType]
    return IAC_cl_value


# In[6]:

# apply to the all dataframe
window_DF.loc[:,"IAC_cl"]=window_DF.apply(IAC_CL_finder, axis=1)
window_DF.loc[:,"IAC_cl"]


# IAC = 1 + (IAC_Cl -1) * closeNess

# In[7]:

window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)
window_DF.loc[:,"IAC"]=1.0 + (window_DF.loc[:,"IAC_cl"]-1)*(window_DF.loc[:,"IntShading_closeness"])


# # Calculate Area

# In[8]:

window_DF.loc[:,"Area"]=window_DF.loc[:,'width']*window_DF.loc[:,'Height']
window_DF


# # Calculate FFs

# In[9]:

window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)
def FFs_finder(row):
    direction = row["Direction"]
    name_file_FFs="FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre,name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0)
    FFs_value = FFs_DF.loc[direction,"SingleFamilyDetached"]
    return FFs_value


# In[12]:

window_DF.loc[:,"FFs"]=window_DF.apply(FFs_finder, axis=1)
window_DF.loc[:,"FFs"]


# # Calculate SLF

# In[13]:

window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)

def SLF_finder(row):
    name_file_SLF="SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0)
    direction = row["Direction"]
    SLF_value = SLF_DF.loc[direction,"45"]
    return (SLF_value)

window_DF.loc[:,"SLF"]=window_DF.apply(SLF_finder, axis=1)
window_DF.loc[:,"SLF"]


# # F_shd

# In[14]:

fshd=(window_DF["SLF"]*window_DF["Doh"]-window_DF["Xoh"])/window_DF["Height"]
fshd.loc["south-Fixed"]=1.0
fshd.loc["south-Operable"]=1.0
window_DF.loc[:,"Fshd"]=fshd
window_DF.loc[:,"Fshd"]


# # Beam Irradiance

# In[16]:

def Beam_finder(row):
    direction=row["Direction"]
    name_file_beam = "BeamIrradiance.csv"
    path_file_beam = os.path.join(Folder_whereThoseTablesAre,name_file_beam)
    Beam_DF= pd.read_csv(path_file_beam, sep=";", index_col=0, header=0)  
    Beam_value = Beam_DF.loc[direction,"45"]
    return(Beam_value )

window_DF.loc[:,"ED"]=window_DF.apply(Beam_finder, axis=1)
window_DF.loc[:,"ED"]


# In[17]:

def Diffuse_finder(row):
    direction=row["Direction"]
    name_file_Diffuse = "DiffuseIrradiance.csv"
    path_file_Diffuse = os.path.join(Folder_whereThoseTablesAre,name_file_Diffuse)
    Diffuse_DF= pd.read_csv(path_file_Diffuse, sep=";", index_col=0, header=0)
    Diffuse_value = Diffuse_DF.loc[direction,"45"]
    return(Diffuse_value)

window_DF.loc[:,"Ed"]=window_DF.apply(Diffuse_finder, axis=1)
window_DF.loc[:,"Ed"]


# # Compute PXI

# In[18]:

window_DF.loc[:,"PXI"]=window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+(1.0-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"])
window_DF.loc[:,"PXI"]


# # Modify tables

# In[19]:

name_file_modifiedWindows="window_modified_Vbocchi.csv"
path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows) 
window_DF.to_csv(path_file_modifiedwindows,sep=";")
path_file_modifiedwindows_excel=os.path.join(Folder_whereThoseTablesAre,"window_modified_Vbocchi.xlsx")
window_DF.to_excel(path_file_modifiedwindows_excel)


# In[ ]:




# In[ ]:



