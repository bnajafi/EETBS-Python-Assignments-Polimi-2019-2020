#Wall Functions: Valentina Caia

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
Rwood_tot = Rwood_val[-1]
print(Rwood_tot)
        
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
    
