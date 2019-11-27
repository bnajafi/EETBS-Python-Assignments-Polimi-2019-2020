import os
import pandas as pd
Folder_WhereIwas = os.getcwd()

folder_of_tables = r"C:\Users\lorenzo\Desktop\somewhere"
os.chdir(folder_of_tables)
final_table = pd.read_csv("windows.csv" , sep= ";" , index_col=0 , header = 0)

# computation of Areas

final_table ["Area"] = final_table ["width"] * final_table ["Height"]

# computation of C_value 

deltaT_heating = 24.8
deltaT_cooling = 7.9
DR_cooling = 11.9
C_value = deltaT_cooling - 0.46 * DR_cooling
final_table["C_value"] = C_value

# computation of Heating Factor

final_table["U"] = 2.84
final_table["SHGC"] = 0.54
final_table.loc ["south-Operable", "U"] = 2.87
final_table.loc ["south-Operable", "SHGC"] = 0.46

final_table["HF"] = final_table["U"] * deltaT_heating


def IAC_cl_finder(row):
    
    name_of_file ="IAC_cl.csv"
    path_file = os.path.join(folder_of_tables, name_of_file)
    IAC_panda = pd.read_csv(path_file, sep=";", index_col = 1, header=0)
    
    windows_IDs_vector_fromFinalTable = row["Window_ID"]
    internal_shading_types_vector_fromData = row["IntShading_ID"]   # we don't need "pd.read" for data coming from "final_table" 
                                                                    # because we are going to apply the function exactly to "final_table"!
    
    #extracting a vector of values from RLF's table for "IAC" (IAC_panda)
    final_value = IAC_panda.loc[windows_IDs_vector_fromFinalTable, internal_shading_types_vector_fromData]  
    
    # normally we enter a table with one couple of values: the value of the row and the value of the column ---> one value in output
    #
    # In this case we enter the table with two vectors, which means we are entering with multiple couples of values --> multiple values in 
    #                                                                                                                 output (vector),each  
    #                                                                                                                 one corresponding  
    #                                                                                                                to each input couple! 
    
    return final_value    # since the final value is not simply a vector, but a column of the TABLE "IAC_panda" (RLF method's table), 
                           # each value will also have his index.. same indexes of IAC_panda: east, west, south-fixed, south-operable.
    
final_table.loc[:,"IAC_cl"] = final_table.apply(IAC_cl_finder,axis=1)  
                                                                   # we put our vector of IAC values (one for east, one for south etc)
                                                                   # into our final table called "final_table" 
                                                                   # into his corresponding column called "IAC_cl"

def IAC_calculator(row):
    IAC_cl = row["IAC_cl"]
    IS_cl = row["IntShading_closeness"]
    final_result = 1.0 + (IAC_cl -1)*IS_cl
    return final_result
    
final_table.loc[:,"IAC"] = final_table.apply(IAC_calculator,axis=1)
    

# THE SAME FOR ALL THE OTHER COLUMNS OF FINAL TABLE!

def FFs_finder(row) :
    name_of_file = "FFs.csv"
    path_file_FFs = os.path.join(folder_of_tables,name_of_file)
    FFs_panda = pd.read_csv(path_file_FFs, sep=";", index_col = 0, header=0) 
    
    direction_fromFinalTable = row["Direction"]
    
    final_value =  FFs_panda.loc[direction_fromFinalTable , "SingleFamilyDetached"]
    return final_value
    
final_table.loc[:, "FFs"] = final_table.apply(FFs_finder , axis=1)
#print(final_table.loc[:, "FFs"])


def BeamIrradiance_finder(row) :
    name_of_file = "BeamIrradiance.csv"
    path_file = os.path.join(folder_of_tables,name_of_file)
    BeamIrradiance_panda = pd.read_csv(path_file , sep=";", index_col = 0, header=0) 
    
    direction_fromFinalTable = row["Direction"]
    
    final_value =  BeamIrradiance_panda.loc[direction_fromFinalTable , "45"]
    return final_value
    
final_table.loc[:, "ED"] = final_table.apply(BeamIrradiance_finder , axis=1)
#print(final_table.loc[:, "ED"])


def DiffuseIrradiance_finder(row) :
    name_of_file = "DiffuseIrradiance.csv"
    path_file = os.path.join(folder_of_tables,name_of_file)
    DiffuseIrradiance_panda = pd.read_csv(path_file , sep=";", index_col = 0, header=0) 
    
    direction_fromFinalTable = row["Direction"]
    
    final_value =  DiffuseIrradiance_panda.loc[direction_fromFinalTable , "45"]
    return final_value
    
final_table.loc[:, "Ed"] = final_table.apply(DiffuseIrradiance_finder , axis=1)
#print(final_table.loc[:, "Ed"])


def ShadeLineFactor_finder(row) :
    name_of_file = "SLF.csv"
    path_file = os.path.join(folder_of_tables,name_of_file)
    ShadeLineFactor_panda = pd.read_csv(path_file , sep=";", index_col = 0, header=0) 
    
    direction_fromFinalTable = row["Direction"]
    
    final_value =  ShadeLineFactor_panda.loc[direction_fromFinalTable , "45"]
    return final_value
    
final_table.loc[:, "SLF"] = final_table.apply(ShadeLineFactor_finder , axis=1)
#print(final_table.loc[:, "SLF"])


def Fshd_calculator(row):
    SLF = row["SLF"]
    Doh = row["Doh"]
    Xoh = row["Xoh"]
    H = row["Height"]
    first_paranthesis = (SLF*Doh-Xoh)/H
    F_shd_Max = max(0,first_paranthesis)
    final_value = min(1,F_shd_Max)
    return final_value

final_table["Fshd"]=final_table.apply(Fshd_calculator,axis=1)
#print(final_table["Fshd"])

def PXI_calculator(row):
    Tx = row["Tx"]
    Ed = row["Ed"]
    Fshd = row["Fshd"]
    ED = row["ED"]
    final_value = Tx*(Ed+(1-Fshd)*ED)
    return final_value
    
final_table["PXI"]=final_table.apply(PXI_calculator,axis=1)
#print(final_table["PXI"])


def CF_calculator(row):
    U = row["U"]
    C_value = row["C_value"]
    PXI = row["PXI"]
    SHGC = row["SHGC"]
    FFs = row["FFs"]
    IAC = row["IAC"]
    final_value = U*C_value + PXI* SHGC* FFs* IAC
    return final_value
    
final_table["CF"]=final_table.apply(CF_calculator,axis=1)
#print(final_table["CF"])

final_table["Qcooling"] = final_table["CF"]* final_table["Area"]

print(final_table)

# EXPORTING

name_newfile ="window_lorenzo.csv"
path_newfile = os.path.join(folder_of_tables,name_newfile) 
path_newfile_windows_excel = os.path.join(folder_of_tables,"window_lorenzo.xlsx") 

final_table.to_csv(path_newfile,sep=";") 
final_table.to_excel(path_newfile_windows_excel)
