# -*- coding: utf-8 -*-
import pandas as pd
import os
def resistance_reader (input_element):
    """This function reads the input materials and extract the standard resistance value"""
    where_table_is = "/Users/giuliamoret/Documents/Documenti università/EETBS/ASSIGNMENT"
    filename_LibraryMaterials = "LibraryMaterials.csv"
    path_LibraryMaterials = os.path.join(where_table_is, filename_LibraryMaterials)
    LibraryMaterials = pd.read_csv(path_LibraryMaterials, sep=";" , index_col=0 , header=0)
    Material_Rstd_Read = LibraryMaterials.loc[input_element,"Std_R_value"]
    return Material_Rstd_Read
    
def std_thickness_reader(input_element):
    """This function reads the input materials and extract the standard thickness value"""
    where_table_is = "/Users/giuliamoret/Documents/Documenti università/EETBS/ASSIGNMENT"
    filename_LibraryMaterials = "LibraryMaterials.csv"
    path_LibraryMaterials = os.path.join(where_table_is, filename_LibraryMaterials)
    LibraryMaterials = pd.read_csv(path_LibraryMaterials, sep=";" , index_col=0 , header=0)
    Material_Std_Thickness = LibraryMaterials.loc[input_element,"Std_Thickness"]    
                
where_table_is = "/Users/giuliamoret/Documents/Documenti università/EETBS/ASSIGNMENT"
filename_resistance = "resistance.csv"
path_resistance = os.path.join(where_table_is, filename_resistance)
resistance = pd.read_csv(path_resistance, sep=";" , index_col=0 , header=0)

resistance["Std_R_value"] = resistance.loc[:,"Materials"].apply(resistance_reader)
resistance["Std_Thickness"] = resistance.loc[:,"Materials"].apply(std_thickness_reader)

resistance.loc[resistance["Type"]=="cond","R_value"] = (resistance.loc[resistance["Type"]=="cond","Std_R_value"]).astype(float) * ((resistance.loc[resistance["Type"]=="cond","Thickness"]).astype(float))/(resistance.loc[resistance["Type"]=="cond","Std_Thickness"]).astype(float)
 
resistance.to_excel("resistancetable_gmoret.xlsx") 
results_folder = "/Users/giuliamoret/Documents/Documenti università/EETBS/ASSIGNMENT"
path_file = os.path.join(results_folder,"resistancetable_gmoret.xlsx")
