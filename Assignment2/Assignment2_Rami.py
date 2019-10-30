# -*- coding: utf-8 -*-
dict1 = {"R_wood": 0.03, "R_insulation": 0.03}
dict2 = {"R_wood": 0.14, "R_insulation": 0.14, "thickness": 13}
dict3 = {"R_wood": 0.23, "R_insulation": 0.23, "thickness": 13}
dict4 = {"R_wood": 0, "R_insulation": 0.70, "thickness": 25}
dict5 = {"R_wood": 0.63, "R_insulation": 0, "thickness": 90}
dict6 = {"R_wood": 0.079, "R_insulation": 0.079, "thickness": 13}
dict7 = {"R_wood": 0.12, "R_insulation": 0.12}

LibraryOfMaterials = {"outsideAir": dict1, "woodBevelLapped": dict2, "fiberboard": dict3, "glassFiber": dict4, "woodStud": dict5, "gypsum": dict6, "insideAir": dict7}
print(LibraryOfMaterials)

R1 = {"name": "R_out", "type": "Conv.", "material": "outsideAir"}
R2 = {"name": "R_woodBL", "type": "Cond.", "material": "woodBevelLapped", "thick": 13}
R3 = {"name": "R_fiber", "type": "Cond.", "material": "fiberboard", "thick": 13}
R4 = {"name": "R_glass", "type": "Cond.", "material": "glassFiber", "thick": 90}
R5 = {"name": "R_woodS", "type": "Cond.", "material": "woodStud", "thick": 90}
R6 = {"name": "R_gypsum", "type": "Cond.", "material": "gypsum", "thick": 13}
R7 = {"name": "R_in", "type": "Conv.", "material": "insideAir"}
ResistancesList = [R1, R2, R3, R4, R5, R6, R7]

R1_tot = 0
for anyR in ResistancesList:
    if anyR["type"] == "Conv.":
        materialOFanyR = LibraryOfMaterials[anyR["material"]]
        Rval = materialOFanyR["R_wood"]
        print(Rval)
    elif anyR["type"] == "Cond.":
        thicknessOFanyR = anyR["thick"]
        materialOFanyR = LibraryOfMaterials[anyR["material"]]
        standardThickOFanyRinTheLibrary = materialOFanyR["thickness"]
        standardResOFanyRinTheLibrary = materialOFanyR["R_wood"]
        Rval = standardResOFanyRinTheLibrary*thicknessOFanyR/standardThickOFanyRinTheLibrary
        print(Rval)
    R1_tot=R1_tot+Rval
print("The overall unit thermal resistance with wood is " + str(R1_tot) + " °C m^2/W")

R2_tot = 0      
for anyR in ResistancesList:
    if anyR["type"] == "Conv.":
        materialOFanyR = LibraryOfMaterials[anyR["material"]]
        Rval = materialOFanyR["R_insulation"]
        print(Rval)
    elif anyR["type"] == "Cond.":
        thicknessOFanyR = anyR["thick"]
        materialOFanyR = LibraryOfMaterials[anyR["material"]]
        standardThickOFanyRinTheLibrary = materialOFanyR["thickness"]
        standardResOFanyRinTheLibrary = materialOFanyR["R_insulation"]
        Rval = standardResOFanyRinTheLibrary*thicknessOFanyR/standardThickOFanyRinTheLibrary
        print(Rval)
    R2_tot=R2_tot+Rval
print("The overall unit thermal resistance with wood is " + str(R2_tot) + " °C m^2/W")

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
print("The heat loss through the walls of a house (whose winter design temperature is -2°C and the indoor design temperature is 22°C) is "+ str(Q) + " W")
