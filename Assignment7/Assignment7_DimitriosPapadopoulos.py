import os
import pandas as pd
Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables"
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0) 

window_DF.loc[:,"Area"]=(window_DF.loc[:,"Height"])*(window_DF.loc[:,"width"])
#the goal is to make functions to easily apply the values from different files to our data frame

#find the IAC
def IAC_cl_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID,IntShadingType]
    return value_IAC_cl
window_DF.apply(IAC_cl_finder,axis=1)
window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_cl_finder,axis=1)
window_DF.loc[:,"IAC_cl"] 

window_DF.loc[:, "IAC"] = 1.0 + (window_DF.loc[:,"IAC_cl"] -1 )* window_DF.loc[:,"IntShading_closeness"] 
#find the U values
def Uvalues_ope(omega):
    windowID = omega["Window_ID"]
    Frame_material = omega["Frame_material"]
    name_file="Uvalues_ope.csv"
    path_file= os.path.join(Folder_whereThoseTablesAre,name_file) 
    result_DF = pd.read_csv(path_file, sep=";", index_col = 1, header=0) 
    value = result_DF.loc[windowID,Frame_material]
    return value

window_DF["U"][window_DF["Frame_type"]=="Operable"]=window_DF.apply(Uvalues_ope,axis=1)

def Uvalues_fixed(omega):
    windowID = omega["Window_ID"]
    Frame_material = omega["Frame_material"]
    name_file="Uvalues_fixed.csv"
    path_file= os.path.join(Folder_whereThoseTablesAre,name_file) 
    result_DF = pd.read_csv(path_file, sep=";", index_col = 1, header=0) 
    value = result_DF.loc[windowID,Frame_material]
    return value

window_DF["U"][window_DF["Frame_type"]=="Fixed"]=window_DF.apply(Uvalues_fixed,axis=1)
#Find the SHGC 
def SHGC_ope(omega):
    windowID = omega["Window_ID"]
    Frame_material = omega["Frame_material"]
    name_file="SHGC_ope.csv"
    path_file= os.path.join(Folder_whereThoseTablesAre,name_file) 
    result_DF = pd.read_csv(path_file, sep=";", index_col = 0, header=0) 
    value = result_DF.loc[windowID,Frame_material]
    return value


window_DF["SHGC"][window_DF["Frame_type"]=="Operable"]=window_DF.apply(SHGC_ope,axis=1)

def SHGC_fixed(omega):
    windowID = omega["Window_ID"]
    Frame_material = omega["Frame_material"]
    name_file="SHGC_fixed.csv"
    path_file= os.path.join(Folder_whereThoseTablesAre,name_file) 
    result_DF = pd.read_csv(path_file, sep=";", index_col = 0, header=0) 
    value = result_DF.loc[windowID,Frame_material]
    return value
window_DF["SHGC"][window_DF["Frame_type"]=="Fixed"]=window_DF.apply(SHGC_fixed,axis=1)

DeltaTheating=25.0 #From the exercise we did on class 
DeltaTcooling=7.8 #The values can change accordingly 

window_DF["HF"]=window_DF["U"]*DeltaTheating
window_DF["Q heating"]=window_DF["HF"]*window_DF["Area"]

#import the SLF
Direction=window_DF.loc[:,"Direction"]
Degrees="45d" #for the 45 degrees
def SLF(Direction,Degrees):
    Folder_wherethetablesare=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables" 
    filename="SLF.csv"
    path_IAC_cl= os.path.join(Folder_wherethetablesare,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[Direction,Degrees]
    return IAC_cl_ValueForThisInput
DF=SLF(Direction,Degrees)
Y=DF.transpose()
W= pd.DataFrame(DF, index=window_DF.loc[:,"Direction"], columns=DF) #because we use the directions of window_DF we will take the results with the right order
window_DF.loc[:,"SLF"]=W.columns

#calculate the Fsh
h=1.0 #I just set a value for the height of the window, which is less than the wall's height
window_DF.loc[:,"Fshd"]=((window_DF.loc[:,"SLF"]*window_DF.loc[:,"Doh"])-window_DF.loc[:,"Xoh"])/h
window_DF.loc[:,"Fshd"][window_DF.loc[:,"Fshd"]>1]=1.0 #the Fshd can not be above 1.0

#import the Et
Direction=window_DF.loc[:,"Direction"]
Degrees="45d" #for the 45 degrees
def Et(Direction,Degrees):
    Folder_wherethetablesare=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables" 
    filename="Et.csv"
    path_IAC_cl= os.path.join(Folder_wherethetablesare,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[Direction,Degrees]
    return IAC_cl_ValueForThisInput
DF_Et=Et(Direction,Degrees)
S=DF_Et.transpose()
Et_df= pd.DataFrame(DF_Et, index=window_DF.loc[:,"Direction"], columns=DF_Et) #because we use the directions of window_DF we will take the results with the right order
window_DF.loc[:,"Et"]=Et_df.columns

#import the Edd
Direction=window_DF.loc[:,"Direction"]
Degrees="45d" #for the 45 degrees
def Edd(Direction,Degrees):
    Folder_wherethetablesare=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables" 
    filename="Edd.csv"
    path_IAC_cl= os.path.join(Folder_wherethetablesare,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[Direction,Degrees]
    return IAC_cl_ValueForThisInput
DF_Edd=Edd(Direction,Degrees)
L=DF_Edd.transpose()
Edd_df= pd.DataFrame(DF_Edd, index=window_DF.loc[:,"Direction"], columns=DF_Edd) #because we use the directions of window_DF we will take the results with the right order
window_DF.loc[:,"Edd"]=Edd_df.columns
window_DF.loc[:,"Edd"]

#import the ED
Direction=window_DF.loc[:,"Direction"]
Degrees="45d" #for the 45 degrees
def ED(Direction,Degrees):
    Folder_wherethetablesare=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables" 
    filename="ED.csv"
    path_IAC_cl= os.path.join(Folder_wherethetablesare,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[Direction,Degrees]
    return IAC_cl_ValueForThisInput
DF_ED=ED(Direction,Degrees)
L=DF_ED.transpose()
ED_df= pd.DataFrame(DF_ED, index=window_DF.loc[:,"Direction"], columns=DF_ED) #because we use the directions of window_DF we will take the results with the right order
window_DF.loc[:,"ED"]=ED_df.columns

#PXI
window_DF.loc[:,"PXI"]=(window_DF.loc[:,"Tx"])*(window_DF.loc[:,"Edd"]+(1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"])

#FFs
DirectionFF=window_DF.loc[:,"Direction"]
TypeofhousingFF="SingleFamilyDetached" #for one family
def FF(DirectionFF,TypeofhousingFF):
    Folder_wherethetablesare=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\python4ScientificComputing_Numpy_Pandas_MATPLotLIB-master\ExternalFiles\Tables" 
    filename="FFs.csv"
    path_IAC_cl= os.path.join(Folder_wherethetablesare,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[DirectionFF,TypeofhousingFF]
    return IAC_cl_ValueForThisInput

DF_FF=FF(DirectionFF,TypeofhousingFF)
P=DF_FF.transpose()
FF_df= pd.DataFrame(DF_FF, index=window_DF.loc[:,"Direction"], columns=DF_FF) 
window_DF.loc[:,"FFs"]=FF_df.columns
window_DF.loc[:,"FFs"]

#C_value
DailyRange=10.9 #I just took it from the exercise we did on the class
window_DF.loc[:,"C_value"]=(window_DF.loc[:,"U"])*(DeltaTcooling-(0.46)*(DailyRange))

#CF
window_DF.loc[:,"CF"]=window_DF.loc[:,"C_value"]+window_DF.loc[:,"PXI"]*window_DF.loc[:,"SHGC"]*window_DF.loc[:,"IAC"]*window_DF.loc[:,"FFs"]


#Qcooling
window_DF.loc[:,"Qcooling"]=window_DF.loc[:,"CF"]*window_DF.loc[:,"Area"]

#export the excel 
windowtoexcel=os.path.join(Folder_whereThoseTablesAre,"window_modified.xlsx")
window_DF.to_excel(windowtoexcel)
