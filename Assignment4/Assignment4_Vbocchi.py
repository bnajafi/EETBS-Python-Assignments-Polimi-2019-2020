# -*- coding: utf-8 -*-
'''ASSIGNMENT 4

In this assignment you should solve the exact same problem as that of the assignment 3 
but this time you should first define a module calledwallFunction_yourSurname.py and then 
call the functions from that module and use them in your main script 
(you should both format of **import module** and **from module import aFunction**)'''

import os
TheFolderWhereIhaveTheFile =r"C:\Users\Valentina\Desktop\quarto anno energetica\Building systems and environmental technologies"
os.chdir(TheFolderWhereIhaveTheFile)
print(os.getcwd())     #for enter in
filesIhave=os.listdir(TheFolderWhereIhaveTheFile)
print(filesIhave)    # we can see the files inside

print(" ")
print('wallFunction_Bocchi.py' in filesIhave) # check if an Item is inside a list
print(" ")
import wallFunction_Bocchi  #check before if the file is in the directory,if we are in that directory and then import

# List of Resistances
R1 = {"name":"R_out", "type": "conv","material":"outside_air"}
R2 = {"name":"R_gypsum","type":"cond","material":"gypsum","thickness":13.0}
R3 = {"name":"R_bevel","type":"cond","material":"wood_bevel_lapped","thickness":13.0}
R4 = {"name":"R_fiberboards","type":"cond","material":"wood_fiberboards","thickness":13.0}
R5 = {"name":"R_insulator","type":"cond","material":"glass_fiber_insulation","thickness":90.0}
R6 = {"name":"R_stud","type":"cond","material":"wood_stud","thickness":90.0}
R7 = {"name":"R_int","type":"conv","material":"inside_air"}
ResistanceList = [R1,R2,R3,R4,R5,R6,R7]

OnlyWood = [R1,R2,R3,R4,R6,R7]
WithInsulator = [R1,R2,R3,R4,R5,R7]


print("          IMPORT MODULE")
print(" ")
R_OnlyWood_list =wallFunction_Bocchi.ResistanceCalculatorWithLibrary(OnlyWood)
print(R_OnlyWood_list)
R_OnlyWood_tot=R_OnlyWood_list[-1]
print("The resistance of the wall assumed with complitely wood is: "+str(R_OnlyWood_tot)+" m^2*°C/W")
print(" ")

R_WithInsulator_list=wallFunction_Bocchi.ResistanceCalculatorWithLibrary(WithInsulator)
print(R_WithInsulator_list)
R_WithInsulator_tot = R_WithInsulator_list[-1]
print("The resistance of the wall when we have insulation is: "+str(R_WithInsulator_tot)+" m^2*°C/W")
print(" ")

# Data
Atot = 0.8*50*2.5 #mm^2
Tin = 22 #°C
Tout = -2 #°C
deltaT=Tin-Tout

U_factor=wallFunction_Bocchi.HeatTransCoeff(R_OnlyWood_tot,R_WithInsulator_tot)
print("The overall heat transfer coefficient is: "+str(U_factor)+" W/(m^2*°C)")
print(" ")
R_factor=wallFunction_Bocchi.Rfactor(U_factor)
print("The overall thermal resistance is: "+str(R_factor)+" m^2*°C/W")

print(" ")
Q_tot=wallFunction_Bocchi.ThLoss(U_factor,Atot,deltaT)
print("The rate of heat loss through the wall is: "+str(Q_tot)+" W")
print(" ")
print(" ")


print("          FROM MODULE IMPORT A FUNCTION")
print(" ")
from wallFunction_Bocchi import ResistanceCalculatorWithLibrary
R_OnlyWood_list =ResistanceCalculatorWithLibrary(OnlyWood)
print(R_OnlyWood_list)
R_OnlyWood_tot=R_OnlyWood_list[-1]
print("The resistance of the wall assumed with complitely wood is: "+str(R_OnlyWood_tot)+" m^2*°C/W")
print(" ")
R_WithInsulator_list=ResistanceCalculatorWithLibrary(WithInsulator)
print(R_WithInsulator_list)
R_WithInsulator_tot = R_WithInsulator_list[-1]
print("The resistance of the wall when we have insulation is: "+str(R_WithInsulator_tot)+" m^2*°C/W")
print(" ")
from wallFunction_Bocchi import HeatTransCoeff
U_factor=HeatTransCoeff(R_OnlyWood_tot,R_WithInsulator_tot)
print("The overall heat transfer coefficient is: "+str(U_factor)+" W/(m^2*°C)")
print(" ")
from wallFunction_Bocchi import Rfactor
R_factor=Rfactor(U_factor)
print("The overall thermal resistance is: "+str(R_factor)+" m^2*°C/W")
from wallFunction_Bocchi import ThLoss
print(" ")
Q_tot=ThLoss(U_factor,Atot,deltaT)
print("The rate of heat loss through the wall is: "+str(Q_tot)+" W")
print(" ")