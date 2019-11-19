#Assignment7
import os 
import pandas as pd

Folder_WhereIwas= os.getcwd()
FolderWhereTheTablesAre = r"C:\Users\Nicoletta\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\A 2019-2020\Nuova cartella"
FileNameWindows = "windows.csv"
pathFileWindows = os.path.join(FolderWhereTheTablesAre,FileNameWindows)
window_DF = pd.read_csv(pathFileWindows,sep=";")
print(window_DF)

window_DF['width']
window_DF['Area']=window_DF['width']*window_DF['Height']
window_DF.to_csv(pathFileWindows,sep=";")



name_file_IAC_Cl="IAC_cl.csv"
path_file_IAC_Cl = os.path.join(FolderWhereTheTablesAre,name_file_IAC_Cl) 
IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0)
 
def IAC_CL_finder_DrapesDarkClosed(windowType):
    intShadinType = "DrapesDarkClosed"  
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(FolderWhereTheTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0)  
    IAC_cl_value = IAC_cl_DF.loc[windowType,intShadinType]
    return IAC_cl_value
    
print(IAC_CL_finder_DrapesDarkClosed("1c"))
print(IAC_CL_finder_DrapesDarkClosed("5c"))

W = window_DF.loc[:,"Window_ID"].apply(IAC_CL_finder_DrapesDarkClosed)
print(W)

window_DF.loc[:,"IntShading_ID"]

#window_DF.loc["west","Window_ID"]="1c"
window_DF.loc[:,"Window_ID"]
print(window_DF.loc[:,"Window_ID"])

def IAC_cl_finder(row):
    windowID = row["Window_ID"]
    intShadinType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(FolderWhereTheTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0)  
    IAC_cl_value = IAC_cl_DF.loc[windowID,intShadinType]
    return IAC_cl_value
window_DF.apply(IAC_cl_finder,axis=1)
window_DF.loc[:,"IAC_cl"]=window_DF.apply(IAC_cl_finder,axis=1)
print(window_DF.loc[:,"IAC_cl"])

window_DF.loc[:,"IAC"] = 1.0 + (window_DF.loc[:,"IAC_cl"] - 1)*window_DF.loc[:,"IntShading_closeness"] 
print(window_DF.loc[:,"IAC"]) 

nameFile_BeamIrradiance = "BeamIrradiance.csv"
pathFile_BeamIrradiance = os.path.join(FolderWhereTheTablesAre,nameFile_BeamIrradiance)
BeamIrradiance_DF = pd.read_csv(pathFile_BeamIrradiance, sep=";", index_col = 1, header=0)


window_DF.loc[:,"Latitude"] = "45"
window_DF.loc[:,"Direction"]

def BeamIrrReader1(beamirr):
    Direction = beamirr["Direction"]
    Latitude = beamirr["Latitude"]
    nameFile_BeamIrradiance="BeamIrradiance.csv"
    pathFile_BeamIrradiance= os.path.join(FolderWhereTheTablesAre,nameFile_BeamIrradiance)
    BeamIrradiance_DF = pd.read_csv(pathFile_BeamIrradiance, sep=";", index_col=0, header=0)
    BeamIrradianceValue = BeamIrradiance_DF.loc[Direction,Latitude]
    return BeamIrradianceValue
window_DF.apply(BeamIrrReader1,axis=1)
window_DF.loc[:,"ED"]=window_DF.apply(BeamIrrReader1,axis=1)
print window_DF.loc[:,"ED"]


def DiffuseIrrReader(dIrr):
    Direction = dIrr["Direction"]
    Latitude = dIrr["Latitude"]
    nameFile_DiffuseIrradiance="DiffuseIrradiance.csv"
    pathFile_DiffuseIrradiance= os.path.join(FolderWhereTheTablesAre,nameFile_DiffuseIrradiance)
    DiffuseIrradiance_DF = pd.read_csv(pathFile_DiffuseIrradiance, sep=";", index_col=0, header=0)
    DiffuseIrradianceValue = DiffuseIrradiance_DF.loc[Direction,Latitude]
    return DiffuseIrradianceValue
window_DF.apply(DiffuseIrrReader,axis=1)
window_DF.loc[:,"Ed"]=window_DF.apply(DiffuseIrrReader,axis=1)
print window_DF.loc[:,"Ed"]

window_DF.loc[:,"BuildingType"]="SingleFamilyDetached"
print window_DF
window_DF.loc[:,"Direction"]
def FFsReader1(FFs):
    Direction=FFs["Direction"]
    BuildingType=FFs["BuildingType"]
    nameFile_FFs = "FFs.csv"
    pathfile_FFs = os.path.join(FolderWhereTheTablesAre,nameFile_FFs)
    FFs_DF = pd.read_csv(pathfile_FFs, sep=";", index_col=0, header=0)
    FFs_value = FFs_DF.loc[Direction,BuildingType]
    return FFs_value
window_DF.apply(FFsReader1,axis=1)
window_DF.loc[:,"FFs"]=window_DF.apply(FFsReader1,axis=1)
print window_DF.loc[:,"FFs"]

window_DF.loc[:,"Latitude"] = "45"
print(window_DF)

def SLFReader1(slf):
    Direction = slf["Direction"]
    Latitude = slf["Latitude"]
    name_file_SLF="SLF.csv"
    path_file_SLF = os.path.join(FolderWhereTheTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0)  
    SLF_value = SLF_DF.loc[Direction,Latitude]
    return SLF_value

window_DF.apply(SLFReader1,axis=1)
window_DF.loc[:,"SLF"]=window_DF.apply(SLFReader1,axis=1)
print (window_DF.loc[:,"SLF"])
window_DF.loc[:,"Fshd"] = (window_DF.loc[:,"SLF"]*window_DF.loc[:,"Doh"]-window_DF.loc[:,"Xoh"])/(window_DF.loc[:,"Height"]) 
print(window_DF.loc[:,"Fshd"])

#Computation of PXI
#PXI = Tx[Ed+(1-Fshd)ED]
window_DF.loc[:,"PXI"]=window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+(1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"])
window_DF.loc[:,"PXI"]

#Computation of CValue
#CValue=deltaT-0.46DR
location_deltaT_cooling=7.8
location_DR_cooling=10.9

window_DF.loc[:,"C_value"]= location_deltaT_cooling - 0.46*location_DR_cooling
print window_DF.loc[:,"C_value"]

FileNameWindowsModified = "Assignment7_NDefranceschi.csv"
PathFileWindowsModified  = os.path.join(FolderWhereTheTablesAre,FileNameWindowsModified)
window_DF.to_csv(PathFileWindowsModified,sep=";")