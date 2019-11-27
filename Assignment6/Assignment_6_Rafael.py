"""
Assignment 6 - In this assignment you should solve assignment 3 using Pandas employing the same methodology 
we went through this week, (creating a function that reads from library of materials) and exporting the final 
results to an excel file.
""" 
import pandas as pd
import numpy as np

Atot = 50*2.5*0.8  #The walls constitute of 80% of the house with 50x2.5 of area.
Awood = Atot*.25    #25% of the house is wood
Ains = Atot*.75     #75% of the house is insulation

INDEX = [1,2,3,4,5,6,7,8,9,10]
materials = np.array(["outsideWinter","woodbevel_13mm","woodfiber_13mm","glassfiber_25mm","woodstud_38mmx90mm","gypsum_13mm","inside","insulation","wood","total"])
Rtypes = np.array(["conv","cond","cond","cond","cond","cond","conv","cond","cond",None])
std_R = np.array([ 0.03,0.14,0.23,0.7,0.63,0.079,0.12,None,None,None])   #Standard Resistances
std_L = np.array([ None,0.013,0.013,0.025,0.038,0.013,None,None,None,None])        #Needed to fix the Real R value later on
Area = np.array([ Atot,Atot,Atot,Ains,Awood,Atot,Atot,Ains,Awood,Atot])  
Temperature = np.array([-2,None,None,None,None,None,22,None,None,None])

#we introduce new arrays for the table we are creating with values of zero
#notice that the arrays need to have the same length in order for us to make calculations with them
Length = np.array([None,0.013,0.013,0.090,0.038,0.013,None,None,None,None])
R_value = np.zeros(10)
U_value = np.zeros(10)
Rtot = np.zeros(10)
Utot = np.zeros(10)
Q = np.zeros(10)

#we make a list of lists that will give the names for each column:

ListofLists = [materials, Area, std_R, std_L, Length, Rtypes, R_value, U_value, Temperature, Rtot, Utot, Q]

def Table_of_Results (ListofLists):
    import os
    os.chdir (r"C:\Users\Rafael Ferrato\Documents\CLASSES_Politecnico_Milano\Building_Systems\Python_Assignments")
    whereIwantToGo = os.getcwd()
    
    
    ListofLists = [materials, Area, std_R, std_L, Length, Rtypes, R_value, U_value, Temperature, Rtot, Utot, Q]
    INDEX_DF = pd.DataFrame(ListofLists, index = ["materials","Area", "std_R", "std_L", "Length", "Rtypes", "R_value", "U_value", "Temperature", "Rtot", "Utot", "Q"], columns = INDEX )
    INDEX_DF2 = INDEX_DF.transpose()
    #we make the transpose of INDEX_DF so we can make the calculations between the values
    
    INDEX_DF2["R_value"][INDEX_DF2["Rtypes"]=="cond"] = INDEX_DF2["std_R"][INDEX_DF2["Rtypes"] == "cond"]*INDEX_DF2["Length"][INDEX_DF2["Rtypes"] == "cond"]/INDEX_DF2["std_L"][INDEX_DF2["Rtypes"] == "cond"]
    
    INDEX_DF2["R_value"][INDEX_DF2["Rtypes"]=="conv"] = INDEX_DF2["std_R"][INDEX_DF2["Rtypes"] == "conv"]
    
    Rwood_value = (INDEX_DF2["Area"] == Atot) | (INDEX_DF2["Area"] == Awood)      #Rwood grabs each resistance that is assigned as Atot OR Awood
    Rwood = np.sum(INDEX_DF2["R_value"][Rwood_value])
        
    INDEX_DF2["R_value"][INDEX_DF2["materials"] == "wood"] = Rwood
    
    
    Rins_value = (INDEX_DF2["Area"] == Atot) | (INDEX_DF2["Area"] == Ains)    #Rins grabs each resistance that is assigned as Atot OR Ains
    Rins = np.sum(INDEX_DF2["R_value"][Rins_value])
        
    INDEX_DF2["R_value"][INDEX_DF2["materials"] == "insulation"] = Rins
    
    INDEX_DF2["R_value"][INDEX_DF2["materials"] == "total"] = sum(INDEX_DF2.loc[1:9,"R_value"])    

    
    INDEX_DF2["U_value"][INDEX_DF2["Rtypes"] == "cond"] = 1.0/INDEX_DF2["R_value"][INDEX_DF2["Rtypes"] == "cond"]
    INDEX_DF2["U_value"][INDEX_DF2["Rtypes"] == "conv"] = 1.0/INDEX_DF2["R_value"][INDEX_DF2["Rtypes"] == "conv"]
    INDEX_DF2["U_value"][INDEX_DF2["materials"] == "wood"] = 1.0/INDEX_DF2["R_value"][INDEX_DF2["materials"] == "wood"]
    INDEX_DF2["U_value"][INDEX_DF2["materials"] == "insulation"] = 1.0/INDEX_DF2["R_value"][INDEX_DF2["materials"] == "insulation"]
    
    INDEX_DF2["U_value"][INDEX_DF2["materials"] == "total"] = sum(INDEX_DF2.loc[1:9,"U_value"])    
    
    
    INDEX_DF2["Utot"][INDEX_DF2["materials"] == "insulation"] = (Ains/Atot)*(INDEX_DF2["U_value"][INDEX_DF2["materials"] == "insulation"])
    INDEX_DF2["Utot"][INDEX_DF2["materials"] == "wood"] = (Awood/Atot)*INDEX_DF2["U_value"][INDEX_DF2["materials"] == "wood"]

    INDEX_DF2["Utot"][INDEX_DF2["materials"] == "total"] = sum(INDEX_DF2.loc[8:9,"Utot"])
    
    INDEX_DF2["Rtot"][INDEX_DF2["materials"] == "insulation"] = 1.0/INDEX_DF2["Utot"][INDEX_DF2["materials"] == "insulation"]
    INDEX_DF2["Rtot"][INDEX_DF2["materials"] == "wood"] = 1.0/INDEX_DF2["Utot"][INDEX_DF2["materials"] == "wood"]
    
    INDEX_DF2["Q"][INDEX_DF2["materials"] == "total"]= INDEX_DF2["Utot"][INDEX_DF2["materials"] == "total"]*Atot*(float(INDEX_DF2["Temperature"][INDEX_DF2["materials"] == "inside"]) - float(INDEX_DF2["Temperature"][INDEX_DF2["materials"] == "outsideWinter"]))

    
    results="results_assignment_6.xlsx" #name the new file you want to save

    path_file_results = os.path.join(whereIwantToGo,results)
    
    INDEX_DF2.to_excel(path_file_results)
    
    return results
    
print Table_of_Results(ListofLists)
    