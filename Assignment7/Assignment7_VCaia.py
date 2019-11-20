#Assignment7: Valentina Caia

import os

import pandas as pd

Folder_WhereIwas = os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\User\Desktop\clonefolder\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles\Tables"

name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre, name_file_windows) 

window_DF = pd.read_csv(path_file_windows, sep = ";", index_col = 0, header=0) 
print(window_DF)

window_DF.columns
window_DF.index

window_DF['Area'] = window_DF['width'] * window_DF['Height']
print(window_DF['Area'])


name_file_IAC_Cl = "IAC_cl.csv"
path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre, name_file_IAC_Cl) 
IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep = ";", index_col = 1, header = 0) 

def IAC_cl_finder_DrapesDarkClosed(windowID):
    IntShadingType = "DrapesDarkClosed"
    name_file_IAC_Cl = "IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre, name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep = ";", index_col = 1, header = 0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID, IntShadingType]
    return value_IAC_cl
print(IAC_cl_DF.index)

window_DF.loc[:,"IAC_cl"] = window_DF.loc[:,"Window_ID"].apply(IAC_cl_finder_DrapesDarkClosed) #gli assegno i valori
print(window_DF.loc[:,"IAC_cl"])


def IAC_cl_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl = "IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre, name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep = ";", index_col = 1, header = 0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID, IntShadingType]
    return value_IAC_cl

window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_cl_finder, axis = 1)
print(window_DF.loc[:,"IAC_cl"]) 

window_DF.loc[:, "IAC"] = 1.0 + (window_DF.loc[:,"IAC_cl"] -1 ) * window_DF.loc[:,"IntShading_closeness"] 
print(window_DF.loc[:, "IAC"])


name_file_BeamIrradiance = "BeamIrradiance.csv"
path_file_BeamIrradiance = os.path.join(Folder_whereThoseTablesAre, name_file_BeamIrradiance) 
BeamIrradiance_DF = pd.read_csv(path_file_BeamIrradiance, sep = ";", index_col = 1, header = 0) 

window_DF.loc[:,"Latitude"] = "45"
print(window_DF)

direction = window_DF.loc[:,"Direction"]
latitude = "45"
def BeamIrradiance_find(x):
    direction = x["Direction"]
    Deg = latitude
    name_file_BeamIrradiance = "BeamIrradiance.csv"
    path_file_BeamIrradiance = os.path.join(Folder_whereThoseTablesAre, name_file_BeamIrradiance) 
    BeamIrradiance_DF = pd.read_csv(path_file_BeamIrradiance, sep = ";", index_col = 0, header = 0) 
    value_BeamIrradiance = BeamIrradiance_DF.loc[direction,Deg]
    return value_BeamIrradiance
window_DF.loc[:,"ED"] = window_DF.apply(BeamIrradiance_find, axis=1)
print(window_DF.loc[:,"ED"]) 


def DiffuseIrradiance_find(x):
    direction = x["Direction"]
    Deg = latitude
    name_file_DiffuseIrradiance = "DiffuseIrradiance.csv"
    path_file_DiffuseIrradiance = os.path.join(Folder_whereThoseTablesAre, name_file_DiffuseIrradiance) 
    DiffuseIrradiance_DF = pd.read_csv(path_file_DiffuseIrradiance, sep = ";", index_col = 0, header = 0) 
    value_DiffuseIrradiance = DiffuseIrradiance_DF.loc[direction,Deg]
    return value_DiffuseIrradiance
window_DF.loc[:,"Ed"] = window_DF.apply(DiffuseIrradiance_find, axis=1)
print(window_DF.loc[:,"Ed"])


def FFs_finder(x):
    direction = x["Direction"]
    Fam = "SingleFamilyDetached"
    name_file_FFs = "FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre, name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep = ";", index_col = 0, header = 0) 
    value_FFs = FFs_DF.loc[direction,Fam]
    return value_FFs
window_DF.loc[:,"FFs"] = window_DF.apply(FFs_finder, axis=1)
print(window_DF.loc[:,"FFs"])


def SLF_finder(x):
    direction = x["Direction"]
    Deg = latitude
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre, name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep = ";", index_col = 0, header = 0) 
    value_SLF = SLF_DF.loc[direction,Deg]
    return value_SLF
window_DF.loc[:,"SLF"] = window_DF.apply(SLF_finder, axis=1)
print(window_DF.loc[:,"SLF"])


def Fshd_finder(x):
    SLF = x["SLF"]
    Doh = x["Doh"]
    Xoh = x["Xoh"]
    h = x["Height"]
    Fshad = (SLF*Doh-Xoh)/h
    Fshd = min(1,max(Fshad,0))
    return Fshd
window_DF.loc[:,"Fshd"] = window_DF.apply(Fshd_finder, axis=1)
print(window_DF.loc[:, "Fshd"])

window_DF.loc[:, "PXI"] = (window_DF.loc[:,"Tx"] * (window_DF.loc[:,"Ed"] + ((1 - window_DF.loc[:,"Fshd"]) * window_DF.loc[:,"ED"])))
print(window_DF.loc[:, "PXI"])


name_modified_windows = "window_modified.csv"
path_modified_windows = os.path.join(Folder_whereThoseTablesAre,name_modified_windows) 
window_DF.to_csv(path_modified_windows,sep=";")
path_modified_windows_excel = os.path.join(Folder_whereThoseTablesAre, "window_modified.xlsx") 
window_DF.to_excel(path_modified_windows_excel)
path_modified_windows_webpage = os.path.join(Folder_whereThoseTablesAre, "window_modified.html") 
window_DF.to_html(path_modified_windows_webpage)
