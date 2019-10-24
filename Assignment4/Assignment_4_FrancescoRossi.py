# ASSIGNMENT 4 FRANCESCO ROSSI
""" import os
WhereIWas = os.getcwd()
print(WhereIWas)

WhereIWantToGo = r"/Users/francescorossi/Desktop/ASSIGNMENT"
os.chdir(WhereIWantToGo)
print(os.getcwd())

filesInside = os.listdir(WhereIWantToGo)
print(filesInside)

print('wallFunction_FRossi.py' in filesInside) """

import wallFunction_FRossi 

from wallFunction_FRossi import CalculationResistance

R1 = {"name":"R_Outside" , "type": "conv" , "material" : "Outside"}
R2 = {"name":"R_Inside" , "type": "conv" , "material" : "Inside"}
R3 = {"name":"R_WoodBevel" , "type": "cond" , "material" : "WoodBevel" , "length" : 0.013}
R4 = {"name":"R_WoodStud" , "type": "cond" , "material" : "WoodStud" , "length" : 0.09}
R5 = {"name":"R_Gypsum" , "type": "cond" , "material" : "Gypsum" , "length" : 0.013}
R6 = {"name":"R_WoodFiber" , "type": "cond" , "material" : "WoodFiber" , "length" : 0.013}
R7 = {"name":"R_GlassFiberIns" , "type": "cond" , "material" : "GlassFiberIns" , "length" : 0.09}

R_with_Insulation_List = [R1,R2,R3,R5,R6,R7]
R_with_woodStud_List = [R1,R2,R3,R4,R5,R6] 
     
CalculationResistance(R_with_Insulation_List , R_with_woodStud_List)


