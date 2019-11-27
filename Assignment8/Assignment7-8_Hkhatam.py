import os
import pandas as pd
import numpy as np
Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\Hamed\Desktop\Behzad1"
os.chdir(Folder_whereThoseTablesAre)
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)
path_file_excel = os.path.join(Folder_whereThoseTablesAre,"windows.xlsx")
window_DF.to_excel(path_file_excel)
window_DF.loc[:,"Area"]=window_DF.loc[:,"Height"]*window_DF.loc[:,"width"]
def IAC_cl_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID,IntShadingType]
    return value_IAC_cl
window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_cl_finder,axis=1)

window_DF.loc[:, "IAC"] = 1.0 + (window_DF.loc[:,"IAC_cl"] -1 )* window_DF.loc[:,"IntShading_closeness"]

Familytype = raw_input("Enter Familytype : ")
def FFs_finder(Direction):
    name_file_FFs="FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre,name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0) 
    value_FFs = FFs_DF.loc[Direction,Familytype]
    return value_FFs
window_DF.loc[:,"FFs"] = window_DF.loc[:,"Direction"].apply(FFs_finder)

latitude = raw_input("Enter latitude : ")
def SLF_finder(Direction):
    name_file_SLF="SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0) 
    value_SLF = SLF_DF.loc[Direction,latitude]
    return value_SLF
window_DF.loc[:,"SLF"] = window_DF.loc[:,"Direction"].apply(SLF_finder)

def Ed_finder(Direction):
    name_file_Ed="DiffuseIrradiance.csv"
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
    Ed_DF = pd.read_csv(path_file_Ed, sep=";", index_col = 0, header=0) 
    value_Ed = Ed_DF.loc[Direction,latitude]
    return value_Ed
window_DF.loc[:,"Ed"] = window_DF.loc[:,"Direction"].apply(Ed_finder)

def ED_finder(Direction):
    name_file_ED="BeamIrradiance.csv"
    path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED) 
    ED_DF = pd.read_csv(path_file_ED, sep=";", index_col = 0, header=0) 
    value_ED = ED_DF.loc[Direction,latitude]
    return value_ED
window_DF.loc[:,"ED"] = window_DF.loc[:,"Direction"].apply(ED_finder)

window_DF.loc[:,"Fshd"] = np.minimum(1,np.maximum(0,window_DF["SLF"]*(window_DF["Doh"]-window_DF["Xoh"]/window_DF["Height"])))
print(window_DF.loc[:,"Fshd"])
print(window_DF)

window_DF.loc[:,"PXI"]=window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+(1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"Ed"])
print(window_DF.loc[:,"PXI"])


location_deltaT_cooling=16
location_DR_cooling=24
C_Value = location_deltaT_cooling - 0.46*location_DR_cooling
window_DF["C_value"]= C_Value
window_DF.loc[:,"U"]=0.17
window_DF.loc[:,"SHGC"]=0.8

window_DF.loc[:,"CF"]=(window_DF.loc[:,"U"]*window_DF.loc[:,"C_value"])+window_DF.loc[:,"PXI"]*window_DF.loc[:,"SHGC"]*window_DF.loc[:,"IAC"]*window_DF.loc[:,"FFs"]

window_DF.loc[:,"Qcooling"]=window_DF.loc[:,"Area"]*window_DF.loc[:,"CF"]

path_file_excel1 = os.path.join(Folder_whereThoseTablesAre,"windows1.xlsx")
window_DF.to_excel(path_file_excel1)

print(window_DF)
