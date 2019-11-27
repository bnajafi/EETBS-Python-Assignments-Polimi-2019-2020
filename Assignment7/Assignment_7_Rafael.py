# -*- coding: utf-8 -*-
#ASSIGNMENT 7 - COMPLETE THE HEAT TRANSFER GAINS ON THE WINDOWS TABLE

#IMPORTANT CONSTANTS USED:
#there wasn't a table for the following values on excel so I just took them from the pictures we usually use for RLF.

DR = 10.9             #DB Range temperature for Italy
DeltaT_cool = 31.8 - 24
DeltaT_heat = 20 -(-5) #Difference of inside and outside
U_fixed = 2.84         #for window_ID 5c and Frame_material Wood
U_operable = 2.87      #for window_ID 5c and Frame_material Wood
SHGC_fixed = 0.54      #for window_ID 5c and Frame_material Wood
SHGC_operable = 0.46   #for window_ID 5c and Frame_material Wood

import os
import pandas as pd

os.getcwd()
Tables = r"C:\Users\Rafael Ferrato\Documents\CLASSES_Politecnico_Milano\Building_Systems\RLF_Tables"
os.chdir(Tables)

window_DF = pd.read_csv("windows.csv", sep=",", index_col = 0, header = 0) #my computer separates .csv files with ","
window_DF


window_DF.loc[:,"U"][window_DF.loc[:,"Frame_type"]=="Fixed"] = U_fixed
window_DF.loc[:,"U"][window_DF.loc[:,"Frame_type"]=="Operable"] = U_operable
window_DF.loc[:,"SHGC"][window_DF.loc[:,"Frame_type"]=="Fixed"] = SHGC_fixed
window_DF.loc[:,"SHGC"][window_DF.loc[:,"Frame_type"]=="Operable"] = SHGC_operable

window_DF.loc[:,"HF"] = window_DF.loc[:,"U"]*DeltaT_heat

window_DF.loc[:,"Q heating"] = window_DF.loc[:,"HF"]*window_DF.loc[:,"Area"]

window_DF.loc[:,"Q heating"]

def IAC_Cl_finder(row):
    window_ID = row["Window_ID"]
    intShadingType = row["IntShading_ID"]
    name_file_IAC_Cl = "IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Tables,name_file_IAC_Cl)
    
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=",", index_col=1, header = 0) #here we choose the index as ID not Window Type
    #the separation by "," is used because my excel is brasilian.
    IAC_Cl_value = IAC_cl_DF.loc[window_ID,intShadingType]
    return IAC_Cl_value

window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_Cl_finder, axis = 1) #this returns the actual value of the table for Drapes Light Open.

#print window_DF.loc[:,"IAC_cl"]


window_DF.loc[:,"IntShading_closeness"]
window_DF.loc[:,"IAC"] = 1 + window_DF.loc[:,"IntShading_closeness"]*(window_DF.loc[:,"IAC_cl"]-1)
#window_DF.loc[:,"IAC"]


def DiffuseIrradiance_Finder (Direction):
    name_file_DiffuseIrradiance = "DiffuseIrradiance.csv"
    path_file_DiffuseIrradiance = os.path.join(Tables,name_file_DiffuseIrradiance)

    DiffuseIrradiance_DF = pd.read_csv(path_file_DiffuseIrradiance, sep=",", index_col=0, header = 0) #here we choose the index as ID not Window Type
    #the separation by "," is used because my excel is brasilian.
    Ed_value = DiffuseIrradiance_DF.loc[Direction,"45"]
    return Ed_value

window_DF.loc[:,"Ed"] = window_DF.loc[:,"Direction"].apply(DiffuseIrradiance_Finder) 


def DirectIrradiance_Finder (Direction):
    name_file_DirectIrradiance = "BeamIrradiance.csv"
    path_file_DirectIrradiance = os.path.join(Tables,name_file_DirectIrradiance)

    DirectIrradiance_DF = pd.read_csv(path_file_DirectIrradiance, sep=",", index_col=0, header = 0) #here we choose the index as ID not Window Type
    #the separation by "," is used because my excel is brasilian.
    ED_value = DirectIrradiance_DF.loc[Direction,"45"]
    return ED_value

window_DF.loc[:,"ED"] = window_DF.loc[:,"Direction"].apply(DirectIrradiance_Finder) 

def SLF_Finder (Direction):
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(Tables,name_file_SLF)

    SLF_DF = pd.read_csv(path_file_SLF, sep=",", index_col=0, header = 0) #here we choose the index as ID not Window Type
    #the separation by "," is used because my excel is brasilian.
    SLF_value = SLF_DF.loc[Direction,"45"]
    return SLF_value

window_DF.loc[:,"SLF"] = window_DF.loc[:,"Direction"].apply(SLF_Finder) 

#window_DF.loc[:,"SLF"]


window_DF.loc[:,"Fshd"] = (window_DF.loc[:,"SLF"]*window_DF.loc[:,"Doh"] - window_DF.loc[:,"Xoh"])/(window_DF.loc[:,"Height"])

window_DF.loc[:,"Fshd"][window_DF.loc[:,"Fshd"]>1] = 1

# window_DF.loc[:,"Fshd"]


window_DF.loc[:,"PXI"] = window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+(1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"])

# window_DF.loc[:,"PXI"]


def FFs_Finder (Direction):
   
    name_file_FFs = "FFs.csv"
    path_file_FFs = os.path.join(Tables,name_file_FFs)

    FFs_DF = pd.read_csv(path_file_FFs, sep=",", index_col=0, header = 0) #here we choose the index as ID not Window Type
    #the separation by "," is used because my excel is brasilian.
    FFs_value = FFs_DF.loc[Direction,"SingleFamilyDetached"]
    return FFs_value

window_DF.loc[:,"FFs"] = window_DF.loc[:,"Direction"].apply(FFs_Finder) 

# window_DF.loc[:,"FFs"]

C = window_DF.loc[:,"U"]*(DeltaT_cool - 0.46*DR)
window_DF.loc[:,"C_value"] = C
window_DF.loc[:,"C_value"]


CF = window_DF.loc[:,"C_value"] + window_DF.loc[:,"PXI"]*window_DF.loc[:,"SHGC"]*window_DF.loc[:,"IAC"]*window_DF.loc[:,"FFs"]

# window_DF.loc[:,"CF"] = CF

Qcooling = window_DF.loc[:,"Area"]*window_DF.loc[:,"CF"]
window_DF.loc[:,"Qcooling"] = Qcooling

name_file_modifiedWindows="window_modified.csv" #name the new file you want to save

path_file_modifiedwindows = os.path.join(Tables,name_file_modifiedWindows)
    
window_DF.to_csv(path_file_modifiedwindows,sep=",")

