import pandas as pd
import os

def pathmk(directory,name):
    return(os.path.join(directory,name))
    
def file_to_df(path):
    df=pd.read_csv(path, sep=";", index_col = 0, header=0) 
    return(df)
    
def file_saver(path,df):
    df.to_csv(path,sep=";")
    print('Your file was saved in ',path)

def file_saver_html(path,df):
    df.to_html(path)
    print('Your file was saved in ',path)

def IAC_cl_finder(row):
    windowID= row["Window_ID"]
    IntShadingType=row["IntShading_ID"]
    IAC_DF=pd.read_csv(path_IAC, sep=";", index_col=1,header=0)
    value_IAC=IAC_DF.loc[windowID,IntShadingType]
    return(value_IAC)
def SLF_finder(row):
    index=row["Direction"]
    lat=row["Latitude"]
    value_SLF=SLF_DF_r.loc[index,str(lat)]
    return(value_SLF)   

def Ed_finder(row):
    index=row["Direction"]
    lat=row["Latitude"]
    value_Ed=Ed_DF_r.loc[index,str(lat)]
    return(value_Ed)   
    
def ED_finder(row):
    index=row["Direction"]
    lat=row["Latitude"]
    value_ED=ED_DF_r.loc[index,str(lat)]
    return(value_ED)
    
def FFs_finder(row):
    index=row["Direction"]
    col=familyType
    value_FFs=FFS_DF_r.loc[index,col]
    return(value_FFs)      
         
def isInWindowsDF(df):
    return(df[(df.index=="S")|(df.index=="E")|(df.index=="W")])

def F_shd(row):
    parameter=(row["SLF"]*row["Doh"]-row["Xoh"])/row["Height"]
    if parameter<0:
        fshd=0
    elif parameter>1:
        fshd=1
    else:
        fshd=parameter
    return(fshd)

def PXI(row):
    value_pxi=row["Tx"]*(row["Ed"]+(1-row["Fshd"])*row["ED"])
    return(value_pxi)
    
def CF(row):
    CF=(row["U"]*row["C_value"])+(row["PXI"]*row["SHGC"]*row["IAC"]*row["FFs"])
    return(CF)

def Q_c(row):
    return(row["Area"]*row["CF"])
    
    #main body
dir_def=os.getcwd()
dir_read='/home/arian/Dropbox/EETBS 2019-2020 Polimi Piacenza/1 Theory and Presentation/Charts and Tables/RLF Tables'
dir_save='/home/arian/Dropbox/Behzad/Codes/files_directory'
    #Windows DataFrame
window_DF = file_to_df(pathmk(dir_read,'windows.csv'))
window_DF.loc[:,"Area"]=window_DF.loc[:,"Height"]*window_DF.loc[:,"width"]
name_mod="mod_DF.csv"
name_html="windows.html"
file_saver(pathmk(dir_save,name_mod),window_DF)
    #IAC_Cl
nameIAC="IAC_cl.csv"
path_IAC=pathmk(dir_read,nameIAC)
IAC_cl=window_DF.apply(IAC_cl_finder,axis=1)
window_DF.loc[:,"IAC_cl"]=window_DF.apply(IAC_cl_finder,axis=1)
window_DF.loc[:,"IAC"]=1+window_DF.loc[:,"IntShading_closeness"]*(window_DF.loc[:,"IAC_cl"]-1)
    #Specifications
lat=45
familyType='SingleFamilyDetached'
window_DF.loc[:,"Latitude"]=lat
location_deltaT_cooling=15
location_DR_cooling=23
window_DF.loc[:,"U"]=0.17
window_DF.loc[:,"SHGC"]=0.8
window_DF.loc[:,"C_value"]=location_deltaT_cooling - 0.46*location_DR_cooling
    #SLF 
SLF_DF_file=file_to_df(pathmk(dir_read,"SLF.csv"))
SLF_DF_r=isInWindowsDF(SLF_DF_file)
window_DF.loc[:,"SLF"]=window_DF.apply(SLF_finder,axis=1)
    #Ed
Ed_DF_file=file_to_df(pathmk(dir_read,"DiffuseIrradiance.csv"))
Ed_DF_r=isInWindowsDF(Ed_DF_file)
window_DF.loc[:,"Ed"]=window_DF.apply(Ed_finder,axis=1)
    #ED
ED_DF_file=file_to_df(pathmk(dir_read,"BeamIrradiance.csv"))
ED_DF_r=isInWindowsDF(ED_DF_file)
window_DF.loc[:,"ED"]=window_DF.apply(ED_finder,axis=1)
    #FFS
FFS_DF_file=file_to_df(pathmk(dir_read,"FFs.csv"))
FFS_DF_r=isInWindowsDF(FFS_DF_file)
window_DF.loc[:,"FFs"]=window_DF.apply(FFs_finder,axis=1)
    #Fshd
window_DF.loc[:,"Fshd"]=window_DF.apply(F_shd,axis=1)
    #PXI
window_DF.loc[:,"PXI"]=window_DF.apply(PXI,axis=1)
    #CF
window_DF.loc[:,"CF"]=window_DF.apply(CF,axis=1)  
    #Qcooling
window_DF.loc[:,"Qcooling"]=window_DF.apply(Q_c,axis=1)  

file_saver_html(pathmk(dir_save,name_html),window_DF)