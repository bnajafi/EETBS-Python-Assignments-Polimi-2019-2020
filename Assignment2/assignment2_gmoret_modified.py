# -*- coding: utf-8 -*-
# Assignment 2

# Data
L_cavity = 90.0 #mm
L_gypsum = 13.0 #mm
L_fiberboard = 13.0 #mm
L_bevel = 13.0 #mm x 200mm
A_tot = 0.8*50*2.5 #m^2
T_in = 22 #°C
T_out = -2 #°C

# Library of materials
Materials = {"Outside_Winter":0.03,
                "Inside":0.12,
                "Wood_Bevel_Lapped_Siding":{"std_th":13.0,"R_value":0.14},
                "Wood_Fiberboard":{"std_th":13.0,"R_value":0.23},
                "Wood_Stud":{"std_th":90.0,"R_value":0.63},
                "Gypsum":{"std_th":13.0,"R_value":0.079},
                "Glass_Fiber_Insulator":{"std_th":25.0,"R_value":0.70}}
               
R1 = {"name":"R_in","type":"conv","material":"Inside"}
R2 = {"name":"R_out","type":"conv","material":"Outside_Winter"}
R3 = {"name":"R_gypsum","type":"cond","material":"Gypsum","thickness":L_gypsum}
R4 = {"name":"R_bavel","type":"cond","material":"Wood_Bevel_Lapped_Siding","thickness":L_bevel}
R5 = {"name":"R_fiberboard","type":"cond","material":"Wood_Fiberboard","thickness":L_fiberboard}
R6 = {"name":"R_insulator","type":"cond","material":"Glass_Fiber_Insulator","thickness":L_cavity}
R7 = {"name":"R_stud","type":"cond","material":"Wood_Stud","thickness":L_cavity}

# Create a list for each case examinated: wall made up of only wood and wall made up of only insulator
OnlyInsulator = [R1,R2,R3,R4,R5,R6]
print(OnlyInsulator)
OnlyWood = [R1,R2,R3,R4,R5,R7]
print(OnlyWood)

# Step 1: wall made up of only wood
R_onlywood = 0
for Ri in OnlyWood:
    if Ri["type"] == "conv":
        material_of_Ri = Ri["material"]
        R_value_of_Ri = Materials[material_of_Ri]
        print(material_of_Ri)
        print(R_value_of_Ri)
        Ri["R_value"] = R_value_of_Ri
        print(Ri)  
        
    elif Ri["type"] == "cond":
        thickness_of_Ri = Ri["thickness"]
        material_of_Ri = Ri["material"]
        print(material_of_Ri)
        print(thickness_of_Ri)
        sub_dictionary = Materials[material_of_Ri]
        print(sub_dictionary)
        std_thickness_of_this_material = sub_dictionary["std_th"]
        print(std_thickness_of_this_material)
        R_value_of_this_material = sub_dictionary["R_value"]
        print(R_value_of_this_material)
        R_value_of_Ri = float(R_value_of_this_material) * (thickness_of_Ri / std_thickness_of_this_material)
        print(R_value_of_Ri)
        Ri["R_value"] = R_value_of_Ri
        print(Ri)
    
    R_onlywood = R_onlywood + R_value_of_Ri
    print("R_onlywood: "+str(R_onlywood))

    
# Step 2: wall made up of only glass fiber insulator
R_onlyinsulator = 0
for Ri in OnlyInsulator:
    if Ri["type"] == "conv":
        material_of_Ri = Ri["material"]
        R_value_of_Ri = Materials[material_of_Ri]
        print(material_of_Ri)
        print(R_value_of_Ri)
        Ri["R_value"] = R_value_of_Ri
        print(Ri)
        
    elif Ri["type"] == "cond":
        thickness_of_Ri = Ri["thickness"]
        material_of_Ri = Ri["material"]
        print(material_of_Ri)
        print(thickness_of_Ri)
        sub_dictionary = Materials[material_of_Ri]
        print(sub_dictionary)
        std_thickness_of_this_material = sub_dictionary["std_th"]
        print(std_thickness_of_this_material)
        R_value_of_this_material = sub_dictionary["R_value"]
        print(R_value_of_this_material)
        R_value_of_Ri = float(R_value_of_this_material) * (thickness_of_Ri / std_thickness_of_this_material)
        print(R_value_of_Ri)
        Ri["R_value"] = R_value_of_Ri
        print(Ri)
    R_onlyinsulator = R_onlyinsulator + R_value_of_Ri
    print("R_onlyinsulator: "+str(R_onlyinsulator))

# Overall heat transfer coefficient

U_wood = 1.0 / R_onlywood
U_ins = 1.0 / R_onlyinsulator
U_tot = float(U_wood) * 0.25 + float(U_ins) * 0.75

# Overall unit thermal resistance
R_tot = 1.0 / U_tot

# Rate of heat loss through the walls
Q = U_tot * A_tot * (T_in - T_out)

# Print the results
print("The resistance of the wall considering only wood is: "+str(R_onlywood)+" m^2*(°C/W)")
print("The resistance of the wall considering only insulator is: "+str(R_onlyinsulator)+" m^2*(°C/W)")
print("The overall unit thermal resistance is: "+str(R_tot)+" m^2*(°C/W)")
print("The overall heat transfer coefficient is: "+str(U_tot)+" W/(m^2*°C)")
print("The rate of heat loss through the wall is: "+str(Q)+" W")


