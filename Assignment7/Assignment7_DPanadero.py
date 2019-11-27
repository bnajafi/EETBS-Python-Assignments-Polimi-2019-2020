import os
import pandas as pd

#Transparent Fenestration Surfaces

#Q_heating_fen= A*HF
    #A=Width*Height
    #HF= delta_T*U
        # U. Table 2 Typical Fenestration Characteristics
        #delta_T and DR. Table Location


#Q_cooling_fen= A*CF_fen
    #A    
    #CF_fen= U*(C)+PXI*SHGC*IAC*FFs    
        #C=(delta_T-0.46*DR)        
        #PXI
            #PXI (unshaded fenestration)=T_x*E_t            
            #PXI (shaded fenestration)=T_x*(E_d+(1-F_shd)*E_D)            
                #T_x: Table 11. Exterior Attachment transmission
                #E_d,E_D,E_t. Table 10 Peak Irradiance                
                #F_shd= min(1,max(0,(SLF*D_oh-X_oh)/h))                
                    #SLFs. Table 12 Shade Line Factors 
                    #D_oh. Depth of overhang
                    #X_oh. Vertical distance from top of fenestration to overhang
                    #h. Height of fenestration
        #SHGC. Table 2 Typical Fenestration Characteristics      
        #IAC (Interior shading)= 1+F_cl*(IAC_cl-1)      
            #F_cl Shade fraction closed (0 to 1)
            #IAC_cl. Table 14 interior attenuation coefficient of fully closed configuration.       
        #FFs. Table 13 Fenestration solar load factors
    
#Read Windows_DF csv
Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\david\Desktop\ERASMUS\2_POLIMI\1_SEMESTER\Building Systems\3_My assignments\RLF Tables"
os.chdir(Folder_whereThoseTablesAre)
name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows) 
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0)   

#Q_heating_fen   
#A
window_DF['Area']=window_DF['width']*window_DF['Height']

#HF 
T_1=22 #For example, temperatures of assignment 6 problem
T_2=-2
location_deltaT_heating = T_1-T_2
location_deltaT_cooling= 7.9
location_DR_cooling=11.9

#U
def U_finder(row):
    Window_ID = row["Window_ID"]
    Frame_material = row["Frame_material"]
    Frame_type = row["Frame_type"]     
    name_file_U="U.csv"
    path_file_U = os.path.join(Folder_whereThoseTablesAre,name_file_U) 
    U_DF = pd.read_csv(path_file_U, sep=";", index_col = 0, header=0) 
    value_U = U_DF.loc[Window_ID,Frame_material,Frame_type]
    return value_U
window_DF.loc[:,"U"] = window_DF.apply(U_finder,axis=1)
window_DF.loc[:,"U"] = 10
#HF = U*location_deltaT_heating
window_DF['HF']=window_DF['U']*location_deltaT_heating
#Q_heating_fen= A*HF
window_DF['Q heating']=window_DF['Area']*window_DF['HF']


#Q_cooling_fen= A*CF_fen

#A
window_DF['Area']=window_DF['width']*window_DF['Height']

#CF_fen= U*(C)+PXI*SHGC*IAC*FFs 



#C=(delta_T-0.46*DR) 
window_DF["C_value"]= location_deltaT_cooling - 0.46*location_DR_cooling

#PXI

#E_d,E_D,E_t. Table 10 Peak Irradiancedef FFs_finder_SingleFamilyDetached(row):
def ED_finder(row):
    Direction = row["Direction"]
    name_file_ED="BeamIrradiance.csv"
    path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED) 
    ED_DF = pd.read_csv(path_file_ED, sep=";", index_col = 0, header=0)
    value_ED = ED_DF.loc[Direction,"45"]
    return value_ED


window_DF.loc[:,"ED"] = window_DF.apply(ED_finder,axis=1)

def Ed_finder(row):
    Direction = row["Direction"]
    name_file_Ed="DiffuseIrradiance.csv"
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
    Ed_DF = pd.read_csv(path_file_Ed, sep=";", index_col = 0, header=0) 
    value_Ed = Ed_DF.loc[Direction,"45"]
    return value_Ed

window_DF.loc[:,"Ed"] = window_DF.apply(Ed_finder,axis=1)

def Et_finder(row):
    Direction = row["Direction"]
    name_file_Ed="TotalIrradiance.csv"
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
    Et_DF = pd.read_csv(path_file_Ed, sep=";", index_col = 0, header=0) 
    value_Et = Et_DF.loc[Direction]
    return value_Et

window_DF.loc[:,"Et"] = window_DF.apply(Et_finder,axis=1)

#F_shd= min(1,max(0,(SLF*D_oh-X_oh)/h)) 
#SLF
def SLF_finder(row):
    Direction = row["Direction"]
    name_file_SLF="SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0) 
    value_SLF = SLF_DF.loc[Direction,"45"]
    return value_SLF

window_DF.loc[:,"SLF"] = window_DF.apply(SLF_finder,axis=1)

def Fshd_finder(row):
    #D_oh. Depth of overhang
    D_oh=row["SLF"]
    #X_oh. Vertical distance from top of fenestration to overhang
    X_oh=row["SLF"]
    #h. Height of fenestration
    h=row["Height"]
    SLF= row["SLF"]   
    #F_shd
    Fsh= min(1,max(0,(SLF*D_oh-X_oh)/h))
    return Fsh


window_DF.loc[:,"Fshd"] = window_DF.apply(Fshd_finder,axis=1)

#PXI (unshaded fenestration)
window_DF['PXI']=window_DF['Tx']*window_DF['Et']

#PXI (shaded fenestration)=T_x*(E_d+(1-F_shd)*E_D)  
def PXI_finder(row):
    Tx=row["Tx"] 
    Ed=row["Ed"]
    ED = row["ED"]
    Fshd = row["Fshd"]
    PXI = Tx*(Ed+ED*(1-Fshd))
    return PXI
   
window_DF.loc[:,"PXI"]= window_DF.apply(PXI_finder,axis=1)

#SHGC. Table 2 Typical Fenestration Characteristics 
def SHGC_finder(row):
    Window_ID = row["Window_ID"]
    Frame_material = row["Frame_material"]
    Frame_type = row["Frame_type"]     
    name_file_SHGC="SHGC.csv"
    path_file_SHGC = os.path.join(Folder_whereThoseTablesAre,name_file_SHGC) 
    SHGC_DF = pd.read_csv(path_file_SHGC, sep=";", index_col = 0, header=0) 
    value_SHGC = SHGC_DF.loc[Window_ID,Frame_material,Frame_type]
    return value_SHGC

window_DF.loc[:,"SHGC"] = window_DF.apply(SHGC_finder,axis=1)

#IAC (Interior shading)

def IAC_cl_finder(row):
    windowID = row["Window_ID"]
    IntShadingType = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    value_IAC_cl = IAC_cl_DF.loc[windowID,IntShadingType]
    return value_IAC_cl

window_DF.loc[:,"IAC_cl"] = window_DF.apply(IAC_cl_finder,axis=1)

#IAC = 1 + (IAC_Cl - 1 )* closeNess
window_DF['IAC'] = 1.0 + (window_DF['IAC_cl'] -1 )* window_DF['IntShading_closeness'] 

#FFs. Table 13 Fenestration solar load factors

def FFs_finder_SingleFamilyDetached(row):
    Direction = row["Direction"]
    Family = "SingleFamilyDetached"
    name_file_FFs="FFs.csv"
    path_file_FFs = os.path.join(Folder_whereThoseTablesAre,name_file_FFs) 
    FFs_DF = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0) 
    value_FFs = FFs_DF.loc[Direction,Family]
    return value_FFs

window_DF.loc[:,"FFs"] = window_DF.apply(FFs_finder_SingleFamilyDetached,axis=1)

#CF_fen= U*(C)+PXI*SHGC*IAC*FFs

window_DF['CF']= window_DF['U']*window_DF['C_value']+window_DF['PXI']*window_DF['SHGC']*window_DF['IAC']*window_DF['FFs']

#Q_cooling_fen
window_DF['Qcooling']= window_DF['Area']*window_DF['CF']


#SAVE THE SOLUTION
name_file_modifiedWindows="window_modified.csv"

path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
path_file_modifiedwindows_excel = os.path.join(Folder_whereThoseTablesAre,"window_modified.xlsx") 
path_file_modifiedwindows_webpage = os.path.join(Folder_whereThoseTablesAre,"window_modified.html")
  
window_DF.to_csv(path_file_modifiedwindows,sep=";") # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !
window_DF.to_excel(path_file_modifiedwindows_excel) # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !
window_DF.to_html(path_file_modifiedwindows_webpage) # I am adding this sep=";" just because if not I will have to rearrange it in excel and I am lazy !