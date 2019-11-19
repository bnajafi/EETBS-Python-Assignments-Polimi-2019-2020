import pandas as pd
import os

Folder_wherethetablesare=r"C:\Users\Angela\Desktop\Building Systems EEE\Charts and Tables\RLF Tables"
filename_windows="windows.csv"
path_windows=os.path.join(Folder_wherethetablesare,filename_windows)
windows_DF = pd.read_csv(path_windows, sep=";" , index_col=0 , header=0)

'''IAC'''
def IAC_finder(row):
     windowID = row["Window_ID"] 
     shadingType = row["IntShading_ID"]
     filename="IAC_cl.csv"
     path_IAC_cl=os.path.join(Folder_wherethetablesare,filename)
     IAC_cl_DF = pd.read_csv(path_IAC_cl, sep=";" , index_col=1 , header=0)
     IAC_cl_valueforthisinput=IAC_cl_DF.loc[windowID,shadingType]
     return IAC_cl_valueforthisinput
     
windows_DF.loc[:,"IAC_cl"]=windows_DF.apply(IAC_finder, axis=1)

windows_DF.loc[:,"IAC"]=1.0 + (windows_DF.loc[:,"IAC_cl"] - 1) *windows_DF.loc[:,"IntShading_closeness"]

'''SLF for Fshd'''
def SLF_finder(row):
     latitude = "45"
     direction = row["Direction"]
     filename="SLF.csv"
     path_SLF=os.path.join(Folder_wherethetablesare,filename)
     SLF_DF = pd.read_csv(path_SLF, sep=";" , index_col=0 , header=0)
     SLF_valueforthisinput=SLF_DF.loc[direction,latitude]
     return SLF_valueforthisinput
     
windows_DF.loc[:,"SLF"]=windows_DF.apply(SLF_finder, axis=1)

'''Fshd using a new matrix with max and min terms'''
listDF = {'ones': [1, 1,1,1], 'zeros': [0,0,0,0], 'max_term': [0,0,0,0], 'result_max_and_zero': [0,0,0,0]}
newDF = pd.DataFrame(listDF,
                              index=["east","west","south-Fixed","south-Operable"], 
                              columns = ["ones","zeros","max_term","result_max_and_zero"])
newDF.loc[:,"max_term"]=(windows_DF.loc[:,"SLF"]*windows_DF.loc[:,"Doh"]-windows_DF.loc[:,"Xoh"])/windows_DF.loc[:,"Height"]
newDF.loc[:,"result_max_and_zero"]=newDF[["max_term", "zeros"]].max(axis=1)
windows_DF.loc[:,"Fshd"]= newDF[["result_max_and_zero", "ones"]].min(axis=1)

'''Ed'''
def Ed_finder(row):
     latitude = "45"
     direction = row["Direction"]
     filename="DiffuseIrradiance.csv"
     path_Ed=os.path.join(Folder_wherethetablesare,filename)
     Ed_DF = pd.read_csv(path_Ed, sep=";" , index_col=0 , header=0)
     Ed_valueforthisinput=Ed_DF.loc[direction,latitude]
     return Ed_valueforthisinput

windows_DF.loc[:,"Ed"]=windows_DF.apply(Ed_finder, axis=1)

'''ED'''          
def ED_finder(row):
     latitude = "45"
     direction = row["Direction"]
     filename="BeamIrradiance.csv"
     path_ED=os.path.join(Folder_wherethetablesare,filename)
     ED_DF = pd.read_csv(path_ED, sep=";" , index_col=0 , header=0)
     ED_valueforthisinput=ED_DF.loc[direction,latitude]
     return ED_valueforthisinput

windows_DF.loc[:,"ED"]=windows_DF.apply(ED_finder, axis=1)

'''PXI=Tx[Ed+(1-Fshd)ED]'''
windows_DF.loc[:,"PXI"]=windows_DF.loc[:,"Tx"]*(windows_DF.loc[:,"Ed"]+(1-windows_DF.loc[:,"Fshd"])*windows_DF.loc[:,"ED"])

'''FFs'''
def FFs_finder(row):
     Type = "SingleFamilyDetached"
     direction = row["Direction"]
     filename="FFs.csv"
     path_FFs=os.path.join(Folder_wherethetablesare,filename)
     FFs_DF = pd.read_csv(path_FFs, sep=";" , index_col=0 , header=0)
     FFs_valueforthisinput=FFs_DF.loc[direction,Type]
     return FFs_valueforthisinput
    
windows_DF.loc[:,"FFs"]=windows_DF.apply(FFs_finder, axis=1)

'''filling the missing columns'''
windows_DF.loc[:,"U"]=[2.84,2.84,2.84,2.87]
windows_DF.loc[:,"SHGC"]=[0.54,0.54,0.54,0.46]
deltaT_cooling=7.9
deltaT_heating=24.8
DR=11.9
windows_DF.loc[:,"HF"]=deltaT_heating*windows_DF.loc[:,"U"]
windows_DF.loc[:,"Area"]=windows_DF.loc[:,"width"]*windows_DF.loc[:,"Height"]
windows_DF.loc[:,"Q heating"]=windows_DF.loc[:,"HF"]*windows_DF.loc[:,"Area"]
windows_DF.loc[:,"C_value"]=deltaT_cooling-0.46*DR
windows_DF.loc[:,"CF"]=windows_DF.loc[:,"U"]*windows_DF.loc[:,"C_value"]+windows_DF.loc[:,"PXI"]*windows_DF.loc[:,"SHGC"]*windows_DF.loc[:,"IAC"]*windows_DF.loc[:,"FFs"]
windows_DF.loc[:,"Qcooling"]=windows_DF.loc[:,"CF"]*windows_DF.loc[:,"Area"]

#save file
Folder_assignments=r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS"
path_modified_window_excel=os.path.join(Folder_assignments,"Assignment7_windows_Anunziata.xlsx")
windows_DF.to_excel(path_modified_window_excel)