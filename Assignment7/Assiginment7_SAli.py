# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:17:55 2019

@author: sajid ali
"""

import os
import pandas as pd
os.getcwd()
path_files = r"C:\Users\sajid ali\Dropbox\EETBS 2019-2020 Polimi Piacenza\1 Theory and Presentation\Charts and Tables\RLF Tables"
name_file = "windows.csv"
path_file_windows = os.path.join(path_files,name_file)
windows_DF = pd.read_csv(path_file_windows, sep=";",index_col = 0, header=0)
windows_DF

#find the area
windows_DF.loc[:,"Area"]=(windows_DF.loc[:,"Height"])*(windows_DF.loc[:,"width"])

def IAC_cl_finder(row):## If the function that we want to apply has to receive multiple inputs
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(path_files,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID,IntShadingType]
    return value_IAC_cl
windows_DF.apply(IAC_cl_finder,axis=1)
windows_DF.loc[:,"IAC_cl"] = windows_DF.apply(IAC_cl_finder,axis=1)
windows_DF.loc[:, "IAC"] = 1.0 + (windows_DF.loc[:,"IAC_cl"] -1 )* windows_DF.loc[:,"IntShading_closeness"]
#### there is no file to import data from so i input data for those parameters
windows_DF.loc[:,"U"]= pd.Series([6.42,6.42,6.42,7.24], index = ["east","west","south-Fixed","south-Operable"])
windows_DF
windows_DF.loc[:,"SHGC"]= pd.Series([0.66,0.66,0.66,0.64], index = ["east","west","south-Fixed","south-Operable"])

##### calculating Q_heating
DeltaTheating=25.0
DeltaTcooling=7.8
windows_DF["HF"]=windows_DF["U"]*DeltaTheating
windows_DF.loc[:,"Q_heating"]=0 ## creating new colum for Q_heating
windows_DF.loc[:,"Q heating"]=(windows_DF.loc[:,"HF"])*(windows_DF.loc[:,"Area"])

##### SLF calcultation 
direction = windows_DF.loc[:,"Direction"]
latitud_degree = "45"
def SLF(direction,latitud_degree ):
    path_folder=r"C:\Users\sajid ali\Dropbox\EETBS 2019-2020 Polimi Piacenza\1 Theory and Presentation\Charts and Tables\RLF Tables"
    name_file = "SLF.csv"
    path_SLF_file = os.path.join(path_folder,name_file)
    path_SLF_DF = pd.read_csv(path_SLF_file, sep=";",index_col=0, header=0)
    path_SLF_DF
    SLF_valuesforthisinput = path_SLF_DF.loc[direction,latitud_degree]
    return SLF_valuesforthisinput 
SLF_values = SLF(direction,latitud_degree)
windows_DF.loc[:,"SLF"]= pd.Series([SLF_values [0],SLF_values [1],SLF_values [2],SLF_values [3]],index = ["east","west","south-Fixed","south-Operable"])
##windows_DF.loc[:,"Fshd1"] = 0
D_oh = 0.8 ## m
X_oh = 0.4#m
h = 1.8#m
#SLF_values.loc[:,"Fsh"]=(SLF_values[:]*D_oh-X_oh)/h
F_shd = (SLF_values[:]*D_oh-X_oh)/h ##### calculate F_shading
windows_DF.loc[:,"Fshd"]= pd.Series([F_shd[0],F_shd[1],F_shd[2],F_shd[3]],index = ["east","west","south-Fixed","south-Operable"])
windows_DF.loc[:,"Fshd"][windows_DF.loc[:,"Fshd"]>1]=1.0 # condition if F_shading is greater than 1 .

# calculating ffs
TypeofhousingFF="SingleFamilyDetached"
def FFs(direction):
    Typeofhouse="SingleFamilyDetached"
    path_folder=r"C:\Users\sajid ali\Dropbox\EETBS 2019-2020 Polimi Piacenza\1 Theory and Presentation\Charts and Tables\RLF Tables"
    name_file1 = "FFs.csv"
    path_FFs_file = os.path.join(path_folder,name_file1)
    path_FFs_DF = pd.read_csv(path_FFs_file, sep=";",index_col=0, header=0)
    path_FFs_DF
    FFs_valuesforthisinput = path_FFs_DF.loc[direction,Typeofhouse]
    return FFs_valuesforthisinput 

DF_FF=FFs(direction)
# fill in values from above "DF_FF"
windows_DF.loc[:,"FFs"]= pd.Series([DF_FF[0],DF_FF[1],DF_FF[2],DF_FF[3]],index = ["east","west","south-Fixed","south-Operable"])

#For Et
#Direction=windows_DF.loc[:,"Direction"]
Degrees="45d" #for the 45 degrees
def Ed(direction,Degrees):
    Degrees="45d"
    path=r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone\asdsadsadasd 8888" 
    filename="Et.csv"
    path_IAC_cl= os.path.join(path,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[direction,Degrees]
    return IAC_cl_ValueForThisInput
values_Ed=Ed(direction,Degrees)
Tranpose_values_Ed=values_Ed.transpose()
Et_df= pd.DataFrame(values_Ed, index=windows_DF.loc[:,"Direction"], columns=values_Ed) #because we use the directions of window_DF we will take the results with the right order
windows_DF.loc[:,"Ed"]=Et_df.columns

##### for values for Edd
def EDD(direction,Degrees):
    Degrees="45d"
    path=r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone\asdsadsadasd 8888" 
    filename="Edd.csv"
    path_IAC_cl= os.path.join(path,filename)
    path_IAC_DF= pd.read_csv(path_IAC_cl, sep=";",index_col=1, header=0)
    IAC_cl_ValueForThisInput=path_IAC_DF.loc[direction,Degrees]
    return IAC_cl_ValueForThisInput
values_EDD=EDD(direction,Degrees)
Tranpose_values_EDD=values_EDD.transpose()
EDD_DF= pd.DataFrame(values_EDD, index=windows_DF.loc[:,"Direction"], columns=values_EDD) #because we use the directions of window_DF we will take the results with the right order
windows_DF.loc[:,"ED"]=EDD_DF.columns

#################calculate PXI
windows_DF.loc[:,"PXI"]=(windows_DF.loc[:,"Tx"])*(windows_DF.loc[:,"Ed"]+(1-windows_DF.loc[:,"Fshd"])*windows_DF.loc[:,"ED"])

### C values
D_Range=10.9 #degrees Celsius
windows_DF.loc[:,"C_value"]=(windows_DF.loc[:,"U"])*(DeltaTcooling-(0.46)*(D_Range))
#### calculate CF
windows_DF.loc[:,"CF"]=windows_DF.loc[:,"C_value"]+windows_DF.loc[:,"PXI"]*windows_DF.loc[:,"SHGC"]*windows_DF.loc[:,"IAC"]*windows_DF.loc[:,"FFs"]
###### 
windows_DF.loc[:,"Et"]="nan"
#Qcooling
windows_DF.loc[:,"Qcooling"]=windows_DF.loc[:,"CF"]*windows_DF.loc[:,"Area"]

name_file_tosave="window_modified_Assigenment_8.csv"
path = r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone"
path_file= os.path.join(path,name_file_tosave) 
windows_DF.to_csv(path_file,sep=",") #  this sep="" just because if not I will have to rearrange it in excel and I am lazy !