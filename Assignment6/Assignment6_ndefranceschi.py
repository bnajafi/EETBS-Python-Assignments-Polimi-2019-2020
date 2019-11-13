#Assignmnent6
import os
import pandas as pd

def MaterialCalculator(Material):
    Folder_wherethetablesare = r"C:\Users\Nicoletta\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\A 2019-2020"
    filenameoftables = "LibraryofMaterials.csv"
    path_LibraryofMaterials = os.path.join(Folder_wherethetablesare,filenameoftables)
    LibraryofMaterials = pd.read_csv(path_LibraryofMaterials,sep=";",index_col=0,header=0)
    MaterialRst_Read = LibraryofMaterials.loc[Material,"StResistance"]
    return MaterialRst_Read

    
def MaterialThCalculator(Material):
    Folder_wherethetablesare = r"C:\Users\Nicoletta\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\A 2019-2020"
    filenameoftables = "LibraryofMaterials.csv"
    path_LibraryofMaterials = os.path.join(Folder_wherethetablesare,filenameoftables)
    LibraryofMaterials = pd.read_csv(path_LibraryofMaterials,sep=";",index_col=0,header=0)
    MaterialTh_Read = LibraryofMaterials.loc[Material,"StThickness"]
    return MaterialTh_Read
    
Folder_wherethetablesare = r"C:\Users\Nicoletta\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\A 2019-2020"
filenameofRestables = "ResistanceLibrary.csv"
path_Resistances = os.path.join(Folder_wherethetablesare,filenameofRestables)
ResistanceLibrary = pd.read_csv(path_Resistances, sep=";" , index_col=0 , header=0)

ResistanceLibrary["Rstandard"]= ResistanceLibrary.loc[:,"Material"].apply(MaterialCalculator)
ResistanceLibrary["Tstandard"] = ((ResistanceLibrary.loc[:,"Material"].apply(MaterialThCalculator)).astype(float))

print(ResistanceLibrary["Rstandard"])
print(ResistanceLibrary["Tstandard"])


ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Cond","Rnew"]=((ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Cond","Rstandard"]).astype(float))*((ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Cond","Thickness"]).astype(float))/ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Cond","Tstandard"]
ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Conv","Rnew"]=ResistanceLibrary.loc[ResistanceLibrary["Type"]=="Conv","Rstandard"]

ResistanceLibrary.to_excel("ResistanceData_NDefranceschi.xlsx")
FolderofResults = r"C:\Users\Nicoletta\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\A 2019-2020"
path_file = os.path.join(FolderofResults,"ResistanceData_NDefranceschi.xlsx")   