# -*- coding: utf-8 -*-
#Assignment Two

T_inside= 22
T_outside = -2
StandardValues = {"Outside Air":{"RValUnit":0.03},"Wood Bevel":{"Standard_L":0.013, "RValUnit": 0.14}, "fiberboard":{"Standard_L":0.013,"RValUnit":0.23},"Glass Fiber":{"Standard_L":0.025,"RValUnit":0.7},"Wood Studs":{"Standard_L":0.09, "RValUnit":0.63},"Gypsum":{"Standard_L":0.013,"RValUnit":0.079},"Inside Air":{"RValUnit":0.12}}

R1 = {"name":"R_outside","type":"conv","material":"Outside Air"}
R2 = {"name":"R_woodB","type":"cond","material":"Wood Bevel","length":0.013}
R3 = {"name":"R_fiberboard","type":"cond","material":"fiberboard","length":0.013}
R4 = {"name":"R_glass","type":"cond","material":"Glass Fiber","length":0.09}
R5 = {"name":"R_Woodstud","type":"cond","material":"Wood Studs","length":0.09}
R6 = {"name":"R_gypsum","type":"cond","material":"Gypsum","length":0.013}
R7 = {"name":"R_inside","type":"conv","material":"Inside Air"}

#A. Determining R_tot_wall in °C/W

Rprime_wood =[R1,R2,R3,R5,R6,R7]
Rprime_glass=[R1,R2,R3,R4,R6,R7]
#Computing Rtot_wood in m^2*°C/W
Rtot_wood = 0
for anyR in Rprime_wood:
    if anyR["type"] == "conv":
        MatOfAnyR = anyR["material"]
        RValOfAnyR = StandardValues[MatOfAnyR]
        R_val_anyR =  RValOfAnyR["RValUnit"]
        print(R_val_anyR)
        Rtot_wood = Rtot_wood + R_val_anyR
        
    elif anyR["type"] == "cond":
        lengthOfanyR = anyR["length"]
        MatOfAnyR= anyR["material"]
        dict1 = StandardValues[MatOfAnyR]
        standardLof_material = dict1["Standard_L"]
        standardR_ofMaterial = dict1["RValUnit"]
        R_val_anyR = (standardR_ofMaterial * lengthOfanyR)/standardLof_material
        Rtot_wood = Rtot_wood + R_val_anyR
print(Rtot_wood)

#Computing Rtot_glass in m^2*°C/W
Rtot_glass = 0
for anyR in Rprime_glass:
    if anyR["type"] == "conv":
        MatOfAnyR = anyR["material"]
        RValOfAnyR = StandardValues[MatOfAnyR]
        R_val_anyR =  RValOfAnyR["RValUnit"]
        Rtot_glass = Rtot_glass + R_val_anyR
    elif anyR["type"] == "cond":
        lengthOfanyR = anyR["length"]
        MatOfAnyR= anyR["material"]
        dict2 = StandardValues[MatOfAnyR]
        standardLof_material = dict2["Standard_L"]
        standardR_ofMaterial = dict2["RValUnit"]
        R_val_anyR = (standardR_ofMaterial * lengthOfanyR)/standardLof_material
        Rtot_glass = Rtot_glass + R_val_anyR
print(Rtot_glass)
        
#Computing U_tot (Overall Heat Transfer Coefficient)

U_wood = 1/Rtot_wood
U_glass = 1/Rtot_glass
U_total = float(U_wood)*0.25 + float(U_glass)*0.75 #from specifications given in the text

R_tot_wall = 1/U_total
R_total_wall = round(R_tot_wall,3)
print("The Overall Unit thermal Resistance is " + str(R_total_wall) + " °C/W")

#B. Determining Q (rate of heat loss through wall)

wall_perimeter = 50
wall_heigth = 2.5
glazing_fraction = float(20)/100
A_tot = wall_perimeter * wall_heigth
A_actual = A_tot*(1-glazing_fraction)

Q = U_total * A_actual * (T_inside - T_outside)
Q = round(Q,3)

print("The rate of heat loss through the wall is "+ str(Q)+ " W")
        