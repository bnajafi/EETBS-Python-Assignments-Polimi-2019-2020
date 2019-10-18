# -*- coding: utf-8 -*-
#Assignment 4: Valentina Caia

import os
Assignments = r"C:\Users\User\Desktop\Canopy\Assignments"
os.chdir(Assignments) 
print(os.getcwd())
lisOfFiles = os.listdir(Assignments)
print(lisOfFiles)

#is Assignment 4 in my folder? Let's check!
print('Assignment4_VCaia.py' in lisOfFiles)



#previous data

P = 50 #m
H = 2.5 #m
A = P*H*0.8 #20% of the wall area is occupied by glazing
print("The area is " + str(A) + " m^2")



from WallFunctions_VCaia import ResistancesList
print ("Here there is the Resistances' list: " +str(ResistancesList))

from WallFunctions_VCaia import WoodResistancesWithLibrary
print("The unit thermal resistances with wood are: " + str(Rwood_val))
print(LibraryOfMaterials)
print("The overall unit thermal resistance with wood is " + str(Rwood_tot) + " °C m^2/W")



import WallFunctions_VCaia
Rins_val=WallFunctions_VCaia.InsResistancesWithLibrary(ResistancesList)
Rins_tot = Rins_val[-1]
print("The overall unit thermal resistance with the insulation is " + str(Rins_tot) + " °C m^2/W")
print("All the unit thermal resistances with the insulation are: " + str(Rins_val))



from WallFunctions_VCaia import *
Tin = 22 #°C
Tout = -2 #°C
deltaT = Tin-Tout 
print("The temperature difference is " + str(deltaT) + "°C")
U_wood = 1/float(Rwood_tot)
U_ins = 1/float(Rins_tot)
U_tot= (U_wood*0.25)+(U_ins*0.75)
print("The overall heat transfer coefficient is " + str(U_tot) + " W/°C m^2")

Q = U_tot*A*deltaT
print("The heat loss through the walls of the house is "+ str(Q) + " W")