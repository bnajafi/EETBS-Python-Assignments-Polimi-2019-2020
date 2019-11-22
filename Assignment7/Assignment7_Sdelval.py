# -*- coding: cp1252 -*-
#Assignment N°7

#Initial settings
import os
import pandas as pd
Exceltablesloc=r"C:\Users\Santi\Desktop\MoS Politecnico di Milano\3 Semestre\Building Systems\Panda excel files"
File1="BeamIrradiance.csv"
File2="DiffuseIrradiance.csv"
File3="FFs.csv"
File4="IAC_cl.csv"
File5="SLF.csv"
File6="SomeIntShading.csv"
File7="windows.csv"
os.chdir(Exceltablesloc)

#Checking we are in the excel file location folder
print(os.getcwd())

#Preparing several paths to files
#IAC_cl path
pathIAC_cl=os.path.join(Exceltablesloc,File4) 
IAC_clDF=pd.read_csv(pathIAC_cl,sep=";",index_col=1,header=0)
#Beam Irradiance path
pathBeamI=os.path.join(Exceltablesloc,File1) 
BeamI=pd.read_csv(pathBeamI,sep=";",index_col=0,header=0)
#Diffuse Irradiance path
pathDiffuseI=os.path.join(Exceltablesloc,File2) 
DiffuseI=pd.read_csv(pathDiffuseI,sep=";",index_col=0,header=0)
#FFS path
pathFFS=os.path.join(Exceltablesloc,File3) 
FFS=pd.read_csv(pathFFS,index_col=0,header=0)
#SLF path
pathSLF=os.path.join(Exceltablesloc,File5) 
SLF=pd.read_csv(pathSLF,sep=";",index_col=0,header=0)


#Analysing the initial situation
pathwindows=os.path.join(Exceltablesloc,File7)
windowsDF=pd.read_csv(pathwindows, sep=";",index_col=0,header=0) 
print(windowsDF)
#All the fields are empty and our goal is to complete them through the use of functions importing the data from other tables

#IAC_cl and IAC values
def IAC_cl_finder(row):
    windowID=row["Window_ID"]
    IntShadingType=row["IntShading_ID"] 
    valueIAC_cl=IAC_clDF.loc[windowID,IntShadingType]
    return valueIAC_cl
    
windowsDF.loc[:,"IAC_cl"]=windowsDF.apply(IAC_cl_finder,axis=1)
windowsDF.loc[:,"IAC"]=1.0+(windowsDF.loc[:,"IAC_cl"] -1 )*windowsDF.loc[:,"IntShading_closeness"] 

print(windowsDF)

#FFS values
Housetype=raw_input("Insert house characteristic:")
def FFSfinder(row):
    Exposure=row["Direction"]
    valueFFS=FFS.loc[Exposure,Housetype] 
    return valueFFS
    
windowsDF.loc[:,"FFs"]=windowsDF.apply(FFSfinder,axis=1)

print(windowsDF)

#SLF values
Lat=raw_input("Insert Latitude of the location(multiples of 5 only in between the range 20-60):")
def SLFfinder(row): 
    Direction=row["Direction"]
    valueSLF=SLF.loc[Direction,Lat]
    return valueSLF

windowsDF.loc[:,"SLF"]=windowsDF.apply(SLFfinder,axis=1)

print(windowsDF.loc[:,"SLF"])

#FSHD values
windowsDF.loc[:,"Fshd"]=(windowsDF.loc[:,"SLF"]*windowsDF.loc[:,"Doh"]-windowsDF.loc[:,"Xoh"])/windowsDF.loc[:,"Height"]
windowsDF.loc[windowsDF.loc[:,"Fshd"]>1,"Fshd"]=1
windowsDF.loc[windowsDF.loc[:,"Fshd"]<0,"Fshd"]=0

print(windowsDF.loc[:,"Fshd"])

#BeamIrradiance values
def Beamfinder(row):
    Direction=row["Direction"]
    valueBeam=BeamI.loc[Direction,Lat]
    return valueBeam

windowsDF.loc[:,"ED"]=windowsDF.apply(Beamfinder,axis=1)

print(windowsDF.loc[:,"ED"])

#DiffuseIrradiance values 
def Diffusefinder(row):
    Direction=row["Direction"]
    valueDiffuse=DiffuseI.loc[Direction,Lat]
    return valueDiffuse

windowsDF.loc[:,"Ed"]=windowsDF.apply(Diffusefinder,axis=1)

print(windowsDF.loc[:,"Ed"])

#PXI values
windowsDF.loc[:,"PXI"]=windowsDF.loc[:,"Tx"]*(windowsDF.loc[:,"Ed"]+(1-windowsDF.loc[:,"Fshd"])*windowsDF.loc[:,"ED"])

print(windowsDF.loc[:,"PXI"])
