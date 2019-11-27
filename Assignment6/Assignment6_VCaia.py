# -*- coding: utf-8 -*-

#Assignment6: Valentina Caia

import pandas as pd

#resistances
R_name = ["R1","R2","R3","R4","R5","R6","R7"]
R_material = ["OutsideAir","WoodBevelLapped","Fiberboard","GlassFiber","WoodStud","Gypsum","InsideAir"]
R_type = ["Conv.","Cond.","Cond.","Cond.","Cond.","Cond.","Conv."]
R_thickness = [None,0.013,0.013,0.09,0.09,0.013,None]
R_valWood = [0.03,0.14,0.23,0.,0.63,0.079,0.12]
R_insulation = [0.03,0.14,0.23,2.52,0.,0.079,0.12]

R_listofLists = [R_material,R_type,R_thickness,R_valWood,R_insulation]
resistances_DF = pd.DataFrame(R_listofLists, index = ["Material","Type","Thickness","Wood","Insulation"], columns = R_name)
resistances_DF

resistances_DF2 = resistances_DF.transpose()
print(resistances_DF2)

R_valWood = resistances_DF2["Wood"]
R_totWood = R_valWood.sum()
print(R_totWood)

R_valInsulation = resistances_DF2["Insulation"]
R_totIns = R_valInsulation.sum()
print(R_totIns)



#now using library of materials

import pandas as pd

dict1 = {"R_wood": 0.03, "R_insulation": 0.03, "thickness": 0}
dict2 = {"R_wood": 0.14, "R_insulation": 0.14, "thickness": 13}
dict3 = {"R_wood": 0.23, "R_insulation": 0.23, "thickness": 13}
dict4 = {"R_wood": 0, "R_insulation": 0.70, "thickness": 25}
dict5 = {"R_wood": 0.63, "R_insulation": 0, "thickness": 90}
dict6 = {"R_wood": 0.079, "R_insulation": 0.079, "thickness": 13}
dict7 = {"R_wood": 0.12, "R_insulation": 0.12, "thickness": 0}

LibraryOfMaterials = {"outsideAir": dict1, "woodBevelLapped": dict2, "fiberboard": dict3, "glassFiber": dict4, "woodStud": dict5, "gypsum": dict6, "insideAir": dict7}
print(LibraryOfMaterials)

R1 = {"name": "R_out", "type": "Conv.", "material": "outsideAir", "composition": "air", "thickness": None}
R2 = {"name": "R_woodBL", "type": "Cond.", "material": "woodBevelLapped", "composition": "both", "thickness": 13}
R3 = {"name": "R_fiber", "type": "Cond.", "material": "fiberboard", "composition": "both", "thickness": 13}
R4 = {"name": "R_glass", "type": "Cond.", "material": "glassFiber", "composition": "insulation", "thickness": 90}
R5 = {"name": "R_woodS", "type": "Cond.", "material": "woodStud", "composition": "wood", "thickness": 90}
R6 = {"name": "R_gypsum", "type": "Cond.", "material": "gypsum", "composition": "both", "thickness": 13}
R7 = {"name": "R_in", "type": "Conv.", "material": "insideAir", "composition": "air", "thickness": None}
ResistancesList = [R1, R2, R3, R4, R5, R6, R7]

resistances_DF = pd.DataFrame (index = [], columns = ["Name", "Material", "Type", "Thickness", "Composition", "Standard Thickness", "R_Wood", "Standard R_Insulation"])

def LibraryReader(R,x):
    Resistance = pd.DataFrame (index = [("R"+str(x))], columns = [])
    Resistance["Name"] = R["name"]
    Resistance["Material"] = R["material"]
    Resistance["Type"] = R["type"]
    Resistance["Thickness"] = R["thickness"]
    Resistance["Composition"] = R["composition"]
    Resistance["Standard Thickness"] = LibraryOfMaterials[R["material"]]["thickness"]
    Resistance["R_Wood"] = LibraryOfMaterials[R["material"]]["R_wood"] 
    Resistance["Standard R_Insulation"] = LibraryOfMaterials[R["material"]]["R_insulation"]              
    return(Resistance)
x = 1
for R in ResistancesList:
    resistances_DF = resistances_DF.append(LibraryReader(R,x))
    x = x+1
    
resistances_DF["R_Insulation Real"] = 0

resistances_DF.loc[resistances_DF["Type"] == "Cond.", "R_Insulation Real"] = resistances_DF.loc[resistances_DF["Type"] == "Cond.", "Standard R_Insulation"]*resistances_DF.loc[resistances_DF["Type"] == "Cond.", "Thickness"]/resistances_DF.loc[resistances_DF["Type"] == "Cond.", "Standard Thickness"]
resistances_DF.loc[resistances_DF["Type"] == "Conv.", "R_Insulation Real"] = resistances_DF.loc[resistances_DF["Type"] == "Conv.", "Standard R_Insulation"]

print(resistances_DF)

resistances_DF2 = resistances_DF.transpose()
resistances_DF2["R_tot"] = resistances_DF.sum()
Rtot_wood = resistances_DF2.loc["R_Wood","R_tot"]
print("The overall unit thermal resistance with wood is " + str(Rtot_wood) + " °C m^2/W")
Rtot_ins = resistances_DF2.loc["R_Insulation Real","R_tot"]
print("The overall unit thermal resistance with insulation is " + str(Rtot_ins) + " °C m^2/W")


#data
P = 50 #m
H = 2.5 #m
deltaT = 24 #°C
A = P*H*0.8 #20% of the wall area is occupied by glazing
print("The area is " + str(A) + " m^2")

#U calculation
U_wood = 1/float(Rtot_wood)
U_ins = 1/float(Rtot_ins)
U_tot= (U_wood*0.25)+(U_ins*0.75)
print("The toal heat transfer coefficient is " + str(U_tot) + " W/°C m^2")

#Heat loss
print("The temperature difference between inside and outside is " + str(deltaT) +"°C (winter)")
Q = round(U_tot*A*deltaT,1)
print("The heat loss through the walls of the house is "+ str(Q) + " W")


#exporting the obtained results to an excel file
import os 
myFolder = r"C:\Users\User\Desktop\Canopy\Assignments"
os.chdir(myFolder)
print(os.getcwd())
FileName = "FinalResults_VCaia.xlsx"          
resistances_DF.to_excel("FinalResults_VCaia.xlsx")