# -*- coding: utf-8 -*-
#Assignment3: Valentina Caia
R1 = {"name": "R_out", "type": "Conv.", "material": "OutsideAir"}
R2 = {"name": "R_woodBL", "type": "Cond.", "material": "WoodBevelLapped", "thick": 13}
R3 = {"name": "R_fiber", "type": "Cond.", "material": "Fiberboard", "thick": 13}
R4 = {"name": "R_glass", "type": "Cond.", "material": "GlassFiber", "thick": 90}
R5 = {"name": "R_woodS", "type": "Cond.", "material": "WoodStud", "thick": 90}
R6 = {"name": "R_gypsum", "type": "Cond.", "material": "Gypsum", "thick": 13}
R7 = {"name": "R_in", "type": "Conv.", "material": "InsideAir"}

ResistancesList = [R1, R2, R3, R4, R5, R6, R7]

#R_wood
def WoodResistancesWithLibrary(ListOfWoodResistances):
    LibraryOfMaterials = {"OutsideAir": {"R":0.03}
    , "WoodBevelLapped": {"R":0.14, "Length":13}
    , "Fiberboard": {"R":0.23, "Length":13}
    , "GlassFiber": {"R":0, "Length":25}
    , "WoodStud": {"R":0.63, "Length":90}
    , "Gypsum": {"R":0.079, "Length":13}
    , "InsideAir": {"R":0.12}
    }
    
    Rtot_wood = 0
    Rvalue = []
    
    
    for anyR in ListOfWoodResistances:
        
        if anyR["type"] == "Conv.":
            materialOFanyR = LibraryOfMaterials[anyR["material"]]
            Rval = materialOFanyR["R"]
            Rvalue.append(Rval)
        elif anyR["type"] == "Cond.":
            thicknessOFanyR = anyR["thick"]
            materialOFanyR = LibraryOfMaterials[anyR["material"]]
            standardThickOFanyRinTheLibrary = materialOFanyR["Length"]
            standardResOFanyRinTheLibrary = materialOFanyR["R"]
            Rval = float(standardResOFanyRinTheLibrary)*(thicknessOFanyR/standardThickOFanyRinTheLibrary)
            Rvalue.append(Rval)
        Rtot_wood=Rtot_wood+Rval
    Rvalue.append(Rtot_wood)
    
    return Rvalue
    
Rwood_val=WoodResistancesWithLibrary(ResistancesList)
print(Rwood_val)
        
#R_insulation
def InsResistancesWithLibrary(ListOfInsResistances):
    LibraryOfMaterials = {"OutsideAir": {"R":0.03}
    , "WoodBevelLapped": {"R":0.14, "Length":13}
    , "Fiberboard": {"R":0.23, "Length":13}
    , "GlassFiber": {"R":0.70, "Length":25}
    , "WoodStud": {"R":0, "Length":90}
    , "Gypsum": {"R":0.079, "Length":13}
    , "InsideAir": {"R":0.12}
    }
    
    Rtot_ins = 0
    Rvalue = []
    
    
    for anyR in ListOfInsResistances:
        
        if anyR["type"] == "Conv.":
            materialOFanyR = LibraryOfMaterials[anyR["material"]]
            Rval = materialOFanyR["R"]
            Rvalue.append(Rval)
        elif anyR["type"] == "Cond.":
            thicknessOFanyR = anyR["thick"]
            materialOFanyR = LibraryOfMaterials[anyR["material"]]
            standardThickOFanyRinTheLibrary = materialOFanyR["Length"]
            standardResOFanyRinTheLibrary = materialOFanyR["R"]
            Rval = float(standardResOFanyRinTheLibrary)*thicknessOFanyR/standardThickOFanyRinTheLibrary
            Rvalue.append(Rval)
        Rtot_ins=Rtot_ins+Rval
    Rvalue.append(Rtot_ins)
    
    return Rvalue
    
Rins_val=InsResistancesWithLibrary(ResistancesList)
print(Rins_val)


print("The unit thermal resistances with wood are " + str(Rwood_val) + " °C m^2/W")
print("The unit thermal resistances with insulation are " + str(Rins_val) + " °C m^2/W")


#data
deltaT = 24 #°C
P = 50 #m
H = 2.5 #m

#20% of the wall area is occupied by glazing
A = P*H*0.8
print("The area is " + str(A) + " m^2")

U_wood = 1/float(R1_tot)
U_ins = 1/float(R2_tot)
U_tot= (U_wood*0.25)+(U_ins*0.75)
print("The toal heat transfer coefficient is " + str(U_tot) + " W/°C m^2")

Q = U_tot*A*deltaT
print("The heat loss through the walls of the house is "+ str(Q) + " W")