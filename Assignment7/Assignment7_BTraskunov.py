#Assignment 7 by Benjamin Traskunov

import os
import pandas as pd
import numpy as np

Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\Class2018\OneDrive - Politecnico di Milano\Master Class Materials\Semester 3\Building Systems\1 Theory and Presentation\Charts and Tables\RLF Tables"
os.chdir(Folder_whereThoseTablesAre)
window_DF = pd.read_csv("windows.csv", sep=";", index_col = 0, header=0) 
#os.chdir(Folder_WhereIwas)

window_DF.loc[:, 'Height'] = 1.9
latitude = 45
location_deltaT_cooling = 7.9
location_deltaT_heating = 24.9
location_DR_cooling = 11.9
Uopr = 2.87
Ufix = 2.84
SHGCopr = 0.46
SHGCfix = 0.54

#Values for U/SHGC found in RLF method table. House also assumed to be single.

def IAC_CL_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl = "IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl)
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl,sep = ";", index_col =1, header = 0)
    value_IAC_cl = IAC_cl_DF.loc[windowID,IntShadingType]
    return value_IAC_cl
  
def FFs_finder(row):
    #windowID = row["Direction"]
    FFs_var = "SingleFamilyDetached"
    name_file_FFs="FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre,name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0)
    value_FFs = FFs_DF.get_value(row,FFs_var)
    return value_FFs

def SLF_finder(row):
    SLF_var = str(latitude)
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF)
    SLF_DF = pd.read_csv(path_file_SLF, sep = ";", index_col = 0, header = 0)
    value_SLF = SLF_DF.loc[row,SLF_var]
    return value_SLF

def SomeIntshd(row):
    shade1 = "IntShading1"
    shade2 = "IntShading2"
    name_file_SomeIntShd = "SomeIntShading.csv"
    path_file_SomeIntShd = os.path.join(Folder_whereThoseTablesAre,name_file_SomeIntShd)
    SomeIntShd_DF = pd.read_csv(path_file_SomeIntShd, sep=";", index_col = 0, header=0)
    value_SLF1= SomeIntShd_DF.loc[row,shade1]
    value_SLF2 = SomeIntShd_DF.loc[row,shade2]
    return (value_SLF1,value_SLF2)
    
def IrradianceBeam(row):
    Lat = str(latitude)
    name_file_irradb = "BeamIrradiance.csv"
    path_file_irradb = os.path.join(Folder_whereThoseTablesAre,name_file_irradb)
    irrad_DF =pd.read_csv(path_file_irradb, sep = ";", index_col = 0, header =0)
    ED_val = irrad_DF.loc[row,Lat]
    return ED_val
    
def Irradiancediff(row):
    Lat = str(latitude)
    name_file_irradd = "DiffuseIrradiance.csv"
    path_file_irradd = os.path.join(Folder_whereThoseTablesAre,name_file_irradd)
    irrad_DF =pd.read_csv(path_file_irradd, sep = ";", index_col = 0, header =0)
    ED_val = irrad_DF.loc[row,Lat]
    return ED_val

window_DF['Area']=window_DF['width']*window_DF['Height']

window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_CL_finder,axis=1)

window_DF.loc[:,"IAC"] = 1.0 + (window_DF.loc[:,"IAC_cl"]-1)*window_DF.loc[:,"IntShading_closeness"]

window_DF.loc[:,"ED"] =window_DF.loc[:,"Direction"].apply(IrradianceBeam)

window_DF.loc[:,"Ed"] =window_DF.loc[:,"Direction"].apply(Irradiancediff)

window_DF.loc[:,"FFs"] =window_DF.loc[:,"Direction"].apply(FFs_finder)

window_DF.loc[:,"SLF"] =window_DF.loc[:,"Direction"].apply(SLF_finder)

C_Value = location_deltaT_cooling - 0.46*location_DR_cooling

window_DF["C_value"]= C_Value

check = ((window_DF.loc[:,"SLF"]*window_DF.loc[:,"Doh"]-window_DF.loc[:,"Xoh"])
/window_DF.loc[:,"Height"])

window_DF["Fshd"] = check

window_DF["Fshd"] = np.where(check > 1, 1, check).tolist()

window_DF["PXI"] = (window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+
(1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"]))

window_DF.loc[window_DF.loc[:,"Frame_type"]=="Operable","U"] = Uopr
window_DF.loc[window_DF.loc[:,"Frame_type"]=="Operable","SHGC"] = SHGCopr
window_DF.loc[window_DF.loc[:,"Frame_type"]=="Fixed","U"] = Ufix
window_DF.loc[window_DF.loc[:,"Frame_type"]=="Fixed","SHGC"] = SHGCfix

window_DF["HF"] = window_DF["U"]*location_deltaT_heating

window_DF["Q heating"] = window_DF["HF"]*window_DF["Area"]

window_DF["CF"] = (window_DF["U"]*(location_deltaT_cooling-0.46*
location_DR_cooling)+window_DF["PXI"]*window_DF["SHGC"]*window_DF["IAC"]
*window_DF["FFs"])

window_DF["Qcooling"] = window_DF["CF"]*window_DF["Area"]

print(window_DF) #check for updated values

name_modified_window ="window_modified.xlsx"
path_modified_window_fin = os.path.join(Folder_whereThoseTablesAre,name_modified_window)
window_DF.to_excel(path_modified_window_fin)
