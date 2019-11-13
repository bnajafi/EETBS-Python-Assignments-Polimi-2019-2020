# -*- coding: utf-8 -*-
#       ASSIGNMENT 6   #

import pandas as pd
import os 

# Functions

def Material_RSTDreader(MaterialName):
     Folder_wherethetablesare=r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies"
     filename_MaterialsLibrary="MaterialsLibrary.csv"
     path_MaterialsLibrary=os.path.join(Folder_wherethetablesare,filename_MaterialsLibrary)
     MaterialsLibrary = pd.read_csv(path_MaterialsLibrary, sep=";" , index_col=0 , header=0)
     Material_RstdRead=MaterialsLibrary.loc[MaterialName,"Rstd"]
     return Material_RstdRead

def Material_STDlengthreader(MaterialName):
     Folder_wherethetablesare=r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies"
     filename_MaterialsLibrary="MaterialsLibrary.csv"
     path_MaterialsLibrary=os.path.join(Folder_wherethetablesare,filename_MaterialsLibrary)
     MaterialsLibrary = pd.read_csv(path_MaterialsLibrary, sep=";" , index_col=0 , header=0)
     Material_STDlengthRead=MaterialsLibrary.loc[MaterialName,"lenght_std"]
     return Material_STDlengthRead    
    
Folder_wherethetablesare=r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies"
filename_Resistances="Resistances.csv"
path_Resistances=os.path.join(Folder_wherethetablesare,filename_Resistances)
Resistances =pd.read_csv(path_Resistances, sep=";" , index_col=0 , header=0)

Resistances["Rstd"]=Resistances.loc[:,"Material"].apply(Material_RSTDreader)
Resistances["lenght_std"]=Resistances.loc[:,"Material"].apply(Material_STDlengthreader)

Resistances.loc[Resistances["type"]=="cond","Rvalue"]=(Resistances.loc[Resistances["type"]=="cond","Rstd"]).astype(float) * ((Resistances.loc[Resistances["type"]=="cond","lenght"]).astype(float))/((Resistances.loc[Resistances["type"]=="cond","lenght_std"]).astype(float))
Resistances.loc[Resistances["type"]=="conv","Rvalue"]=Resistances.loc[Resistances["type"]=="conv","Rstd"].astype(float)

Resistances.to_excel("ResistancesResults_VBocchi.xlsx")
ResultsFolder=r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies"
path_file=os.path.join(ResultsFolder,"ResistancesResults_VBocchi.xlsx")

