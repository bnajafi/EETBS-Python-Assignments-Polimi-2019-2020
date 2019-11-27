import pandas as pd
import os

#Insert where the tables are in your PC
Folder_whereThoseTablesAre = r"C:\Users\fabri\Dropbox\Polimi\3rd Semester\Building Systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles\Tables"
#Folder_whereThoseTablesAre = os.getcwd()
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows) 
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0) 


#Calculating Area
window_DF.loc[:,"Area"]=window_DF.loc[:,"width"]*window_DF.loc[:,"Height"]


#Calculating the IAC
def IAC_CL_finder(row):
    windowID=row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,IntShadingType]
    return IAC_cl_value

window_DF.apply(IAC_CL_finder, axis=1)
window_DF.loc[:,"IAC_cl"]=window_DF.apply(IAC_CL_finder, axis=1)
window_DF.loc[:,"IAC"]=1+(window_DF.loc[:,"IAC_cl"]-1)*window_DF.loc[:,"IntShading_closeness"]


#Calculating Fsh

latitude="45"

window_DF.columns
window_DF.loc[:,'SLF']

def SLF_finder(row):
    direction=row["Direction"]
    LAT = latitude
    name_file_IAC_Cl="SLF.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    SLF_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 0, header=0) 
    SLF_value = SLF_DF.loc[direction,LAT]
    return SLF_value

window_DF.loc[:,"SLF"]=window_DF.apply(SLF_finder, axis=1)

def Fshd_finder(row):
    SLF = row["SLF"]
    Doh=row["Doh"]
    Xoh = row["Xoh"]
    h = row["Height"]
    Fsh0 = (SLF*Doh-Xoh)/h
    Fsh = min(1,max(Fsh0,0))
    return Fsh

window_DF.loc[:,"Fshd"]=window_DF.apply(Fshd_finder, axis=1)


#Calculating PXI

def Ed_finder(row):
    direction=row["Direction"]
    LAT = latitude
    name_file_IAC_Cl="DiffuseIrradiance.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    Ed_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 0, header=0) 
    Ed_value = Ed_DF.loc[direction,LAT]
    return Ed_value

window_DF.loc[:,"Ed"]=window_DF.apply(Ed_finder, axis=1)

def ED_finder(row):
    direction=row["Direction"]
    LAT = latitude
    name_file_IAC_Cl="BeamIrradiance.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    ED_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 0, header=0) 
    ED_value = ED_DF.loc[direction,LAT]
    return ED_value

window_DF.loc[:,"ED"]=window_DF.apply(ED_finder, axis=1)

def PXI_finder(row):
    Tx = row["Tx"]
    Ed=row["Ed"]
    ED = row["ED"]
    Fshd = row["Fshd"]
    PXI = Tx*(Ed+ED*(1-Fshd))
    return PXI

window_DF.loc[:,"PXI"]=window_DF.apply(PXI_finder, axis=1)


#Calculating FFs

def FFs_finder(row):
    direction=row["Direction"]
    Type = "SingleFamilyDetached"
    name_file_IAC_Cl="FFs.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    FFs_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 0, header=0) 
    FFs_value = FFs_DF.loc[direction,Type]
    return FFs_value

window_DF.loc[:,"FFs"]=window_DF.apply(FFs_finder, axis=1)

print(window_DF)

#The SHGC table was not available on the folder and so the loads cant be calculated.

#Exporting Results
name_file_modifiedWindows="window_modified.csv"
path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows) 
path_file_modifiedwindows_excel = os.path.join(Folder_whereThoseTablesAre,"window_modified.xlsx") 
path_file_modifiedwindows_webpage = os.path.join(Folder_whereThoseTablesAre,"window_modified.html") 

window_DF.to_csv(path_file_modifiedwindows,sep=";") 
window_DF.to_excel(path_file_modifiedwindows_excel)
window_DF.to_html(path_file_modifiedwindows_webpage)