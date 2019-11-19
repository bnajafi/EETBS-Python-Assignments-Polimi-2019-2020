# -*- coding: utf-8 -*-
import os 
import pandas as pd  

def Material_Rstd_reader(MaterialName):
     Folder_wherethetablesare=r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS"
     filename_MaterialsLibrary="MaterialsLibrary.csv"
     path_MaterialsLibrary=os.path.join(Folder_wherethetablesare,filename_MaterialsLibrary)
     MaterialsLibrary = pd.read_csv(path_MaterialsLibrary, sep=";" , index_col=0 , header=0)
     Material_RstdRead=MaterialsLibrary.loc[MaterialName,"Rstd"]
     return Material_RstdRead
     
def Material_STDlength_reader(MaterialName):
     Folder_wherethetablesare=r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS"
     filename_MaterialsLibrary="MaterialsLibrary.csv"
     path_MaterialsLibrary=os.path.join(Folder_wherethetablesare,filename_MaterialsLibrary)
     MaterialsLibrary = pd.read_csv(path_MaterialsLibrary, sep=";" , index_col=0 , header=0)
     Material_STDlengthRead=MaterialsLibrary.loc[MaterialName,"length_std"]
     return Material_STDlengthRead    

Folder_wherethetablesare=r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS"
filename_Resistances="Resistances.csv"
path_Resistances=os.path.join(Folder_wherethetablesare,filename_Resistances)
Resistances = pd.read_csv(path_Resistances, sep=";" , index_col=0 , header=0)

Resistances["Rstd"]=Resistances.loc[:,"Material"].apply(Material_Rstd_reader)
Resistances["length_std"]=Resistances.loc[:,"Material"].apply(Material_STDlength_reader)


Resistances.loc[Resistances["type"]=="cond","Rvalue"] =Resistances.loc[Resistances["type"]=="cond","Rstd"] * ((Resistances.loc[Resistances["type"]=="cond","length"]).astype(float))/Resistances.loc[Resistances["type"]=="cond","length_std"]
Resistances.loc[Resistances["type"]=="conv","Rvalue"]=Resistances.loc[Resistances["type"]=="conv","Rstd"]
#astype(float) serve perchè leggeva colonna length non come float (ma come object=stringa) e non moltiplica stringhe*float (invece funziona con interi)

'''save file with results:'''
Resistances.to_excel("ResistancesData_AngelaNunziata.xlsx")
ResultsFolder=r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS"
path_file=os.path.join(ResultsFolder,"ResistanceData_AngelaNunziata.xlsx")