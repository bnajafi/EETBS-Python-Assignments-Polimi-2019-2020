# -*- coding: utf-8 -*-

'''
                   ASSIGNMENT 3
                   
                                         '''

# Function

def ResistanceCalculatorWithLibrary(ListOfResistances):
    libraryOfMaterials = {"outside_air":0.03,
                      "wood_bevel_lapped":{"std_thick":13.0,"R_value":0.14},
                      "wood_fiberboards":{"std_thick":13.0,"R_value":0.23},
                      "glass_fiber_insulation":{"std_thick":25.0,"R_value":0.70},
                      "wood_stud":{"std_thick":90.0,"R_value":0.63},
                      "gypsum":{"std_thick":13.0,"R_value":0.079},
                      "inside_air":0.12}
    Rtot=0
    Rvalue_List=[]
    for anyR in ListOfResistances:
        if anyR["type"]=="conv":
            material_anyR = anyR["material"]
            Rvalue_anyR=libraryOfMaterials[material_anyR]
            Rvalue_List.append(Rvalue_anyR)
            
        elif anyR["type"]=="cond":  
            material_anyR = anyR["material"]
            thick_anyR=anyR["thickness"] 
            extr_libr=libraryOfMaterials[material_anyR]
            standardThickOfthisMaterialInTheLibrary=extr_libr["std_thick"]
            standardRvalOfthisMaterialInTheLibrary=extr_libr["R_value"]
            Rvalue_anyR=standardRvalOfthisMaterialInTheLibrary*thick_anyR/standardThickOfthisMaterialInTheLibrary
            Rvalue_List.append(Rvalue_anyR)
        
        Rtot=Rtot+Rvalue_anyR
    Rvalue_List.append(Rtot)
    return(Rvalue_List)

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


R_OnlyWood_list = ResistanceCalculatorWithLibrary(OnlyWood)
print(R_OnlyWood_list)
R_OnlyWood_tot=R_OnlyWood_list[-1]
print("The resistance of the wall assumed with complitely wood is: "+str(R_OnlyWood_tot)+" m^2*°C/W")

R_WithInsulator_list=ResistanceCalculatorWithLibrary(WithInsulator)
print(R_WithInsulator_list)
R_WithInsulator_tot = R_WithInsulator_list[-1]
print("The resistance of the wall when we have insulation is: "+str(R_WithInsulator_tot)+" m^2*°C/W")

# Data

Atot = 0.8*50*2.5 #mm^2
Tin = 22 #°C
Tout = -2 #°C
deltaT=Tin-Tout

# Determine the overall heat transfer coefficient (the U-factor)

Uwood = 1.0/R_OnlyWood_tot
Uwithins = 1.0/R_WithInsulator_tot
Utot = Uwood*0.25 + Uwithins*0.75
print("The overall heat transfer coefficient is: "+str(Utot)+" W/(m^2*°C)")

# Compute the overall  thermal resistance and the heat transfered

R_tot =1.0/Utot
Q=Utot*Atot*deltaT
print("The overall thermal resistance is: "+str(R_tot)+" m^2*°C/W")
print("The rate of heat loss through the wall is: "+str(Q)+" W")


