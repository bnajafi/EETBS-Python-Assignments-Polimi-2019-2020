Where_I_need_to_be = r"C:\Users\Rafael Ferrato\Documents\CLASSES_Politecnico_Milano\Building_Systems\Python_Assignments"

import os

os.chdir(Where_I_need_to_be)

print os.getcwd()

import wallFunction_Rafael

Atot = 50*2.5*0.8  #The walls constitute of 80% of the house with 50x2.5 of area.
Awood = Atot*.25    #25% of the house is wood
Ains = Atot*.75     #75% of the house is insulation


#now we can give the list of materials used in the problem:

R1 = {"type":"conv","material":"outsideWinter","Area":"Atot","Temperature":-2}
R2 = {"type":"cond","material":"woodbevel_13mm","L":0.013,"Area":"Atot"}
R3 = {"type":"cond","material":"woodfiber_13mm","L":0.013,"Area":"Atot"}
R4 = {"type":"cond","material":"glassfiber_25mm","L":0.09,"Area":"Ains"}
R5 = {"type":"cond","material":"woodstud_38mmx90mm","L":0.038,"Area":"Awood"}
R6 = {"type":"cond","material":"gypsum_13mm","L":0.013,"Area":"Atot"}
R7 = {"type":"conv","material":"insideSurface","Area":"Atot","Temperature":22}


Resistance_List = [R1,R2,R3,R4,R5,R6,R7]  #this RList will be used in the FUNCTION in order to calculate the U_factor, the Rtot and each Resistance

Resistances = wallFunction_Rafael.ResistanceCalculatorLibrary(Resistance_List)    #The function called ResistanceCalculatorLibrary will get the values in RList to give us the results

RealR = []                     #If I want to print just the resistances from the new RList I need to assign an empty list
for R in Resistance_List:
    Resistance = R["R_Value"]   #gets each R_Value in RList
    RealR.append(Resistance)

print ("Each resistance is for each material is respectively: "+str(Resistances))

U_factor = wallFunction_Rafael.U(Resistance_List)

print ("The U_factor is: "+str(U_factor)+" W/m2C")      #the U_factor is already inside the function and is calculated once we have a list of Materials

Resistance_tot = 1/U_factor

print ("The total Resistance is: "+str(Resistance_tot)+" m2C/W")  #the same is valid for R total.

#To find the Q we can do a for to use the values in the library of libraries

Q = U_factor*Atot*(R7["Temperature"]-R1["Temperature"])
      
print ("Finally, the heat transfer Q is equal to: "+str(Q)+" W")


print ("\nAnother way of calling a function is using the 'from 'function' import 'attribute'.")

from wallFunction_Rafael import ResistanceCalculatorLibrary
Resistances_with_from = ResistanceCalculatorLibrary(Resistance_List)

Resistances_with_from = []                     #If I want to print just the resistances from the new RList I need to assign an empty list
for R in Resistance_List:
    Resistance = R["R_Value"]   #gets each R_Value in RList
    Resistances_with_from.append(Resistance)   #appends each R_Value in Real_R list.

print ("Each resistance is for each material is respectively: "+str(Resistances_with_from))


from wallFunction_Rafael import U
U_with_from = U(Resistance_List)

print ("The U_factor is: "+str(U_with_from)+" W/m2C")   

from wallFunction_Rafael import Rtot

Rtot_with_from = 1/U_with_from

print ("The totar resistance is: "+str(Rtot_with_from)+" W/m2C")   


Q = U_factor*Atot*(R7["Temperature"]-R1["Temperature"])
      
print ("Finally, the heat transfer Q is equal to: "+str(Q)+" W")

