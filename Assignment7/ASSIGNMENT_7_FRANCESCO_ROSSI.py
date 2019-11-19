######## ASSIGNMENT 7 FRANCESCO ROSSI ########

import os
import pandas as pd
Folder_WhereIwas = os.getcwd()
print (Folder_WhereIwas)
Folder_whereThoseTablesAre = r"/Users/francescorossi/Desktop/WhereTablesAre/RLF Tables"
os.chdir(Folder_whereThoseTablesAre)
window_DF = pd.read_csv("windows.csv" , sep= ";" , index_col=0 , header = 0)
latitude = 45

# SO I HAVE TO FILL THIS TABLE

# let's start from the area

window_DF ["Area"] = window_DF ["width"] * window_DF ["Height"]

# let'a compute the C_value as usual
location_deltaT_heating = 24.8
location_deltaT_cooling = 7.9
location_DR_cooling = 11.9
C_Value = location_deltaT_cooling - 0.46*location_DR_cooling
window_DF["C_value"] = C_Value

# now about the U and SHGC value i don't have any table given so i will use "usual" value filling it by hand.

window_DF["U"] = 2.84
window_DF["SHGC"] = 0.54
window_DF.loc ["south-Operable", "U"] = 2.87
window_DF.loc ["south-Operable", "SHGC"] = 0.46

# Heating Factor

window_DF["HF"] = window_DF["U"] * location_deltaT_heating

def FFs_finder(row) :
    direction = row["Direction"]
    name_file_FFs = "FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre,name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0)
    FFs_value =  FFs_DF.loc[direction , "SingleFamilyDetached"]
    return FFs_value
window_DF.loc[:, "FFs"] = window_DF.apply(FFs_finder , axis=1)

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

def BeamIrradiance(row) :
    direction = row["Direction"]
    name_file_ED = "BeamIrradiance.csv"
    path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED) 
    ED_DF = pd.read_csv(path_file_ED, sep=";", index_col = 0, header=0)
    ED_value =  ED_DF.loc[direction , "45"]
    return ED_value
window_DF.loc[:, "ED"] = window_DF.apply(BeamIrradiance , axis=1)

def DiffuseIrradiance(row) :
    direction = row["Direction"]
    name_file_Ed = "DiffuseIrradiance.csv"
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
    Ed_DF = pd.read_csv(path_file_Ed, sep=";", index_col = 0, header=0)
    Ed_value =  Ed_DF.loc[direction , "45"]
    return Ed_value
window_DF.loc[:, "Ed"] = window_DF.apply(DiffuseIrradiance , axis=1)

def ShadeLineFactor(row) :
    direction = row["Direction"]
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0)
    SLF_value =  SLF_DF.loc[direction , "45"]
    return SLF_value
window_DF.apply(ShadeLineFactor , axis=1)

def Fshd(row):
    SLF=row["SLF"]
    Doh=row["Doh"]
    Xoh=row["Xoh"]
    H=row["Height"]
    a=(SLF*Doh-Xoh)/H
    FshdMax=max(0,a)
    FshdMin=min(1,FshdMax)
    return FshdMin

window_DF["Fshd"]=window_DF.apply(Fshd,axis=1)

window_DF["PXI"]=window_DF["Tx"]*(window_DF["Ed"]+(1-window_DF["Fshd"])*window_DF["ED"])

# let's now compute the cooling factor

window_DF["CF"] = window_DF["U"] *window_DF["C_value"] + window_DF["PXI"] * window_DF["SHGC"] * window_DF["FFs"] * window_DF["IAC"]

# and finally the cooling load

window_DF["Qcooling"] = window_DF["CF"]*window_DF["Area"]

print (window_DF)


