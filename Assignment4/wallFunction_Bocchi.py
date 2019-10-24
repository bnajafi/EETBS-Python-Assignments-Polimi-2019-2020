# -*- coding: utf-8 -*-


# Resistance Calculator
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

# Determine the overall heat transfer coefficient (the U-factor)
def HeatTransCoeff(R1,R2):
    Uwood = 1.0/R1
    Uwithins = 1.0/R2
    Utot=0
    Utot = Uwood*0.25 + Uwithins*0.75
    return(Utot)

# Compute the overall  thermal resistance 
def Rfactor(U):
    R_tot =1.0/U
    return(R_tot)

#Calculate thermal losses through the wall
def ThLoss(U,A,T):
    Q=U*A*T
    return(Q)
 
