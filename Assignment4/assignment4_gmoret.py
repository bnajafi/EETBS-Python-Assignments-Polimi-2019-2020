# -*- coding: utf-8 -*-
    
# Data

L_cavity = 90.0 #mm
L_gypsum = 13.0 #mm
L_fiberboard = 13.0 #mm
L_bevel = 13.0 #mm x 200mm
A_tot = 0.8*50*2.5 #m^2
T_in = 22 #°C
T_out = -2 #°C

# Resistance

R1 = {"name":"R_in","type":"conv","material":"Inside"}
R2 = {"name":"R_out","type":"conv","material":"Outside_Winter"}
R3 = {"name":"R_gypsum","type":"cond","material":"Gypsum","thickness":L_gypsum}
R4 = {"name":"R_bavel","type":"cond","material":"Wood_Bevel_Lapped_Siding","thickness":L_bevel}
R5 = {"name":"R_fiberboard","type":"cond","material":"Wood_Fiberboard","thickness":L_fiberboard}
R6 = {"name":"R_insulator","type":"cond","material":"Glass_Fiber_Insulator","thickness":L_cavity}
R7 = {"name":"R_stud","type":"cond","material":"Wood_Stud","thickness":L_cavity}

# Create a list for each case examinated: wall made up of only wood and wall made up of only insulator

Only_Insulator = [R1,R2,R3,R4,R5,R6]
Only_Wood = [R1,R2,R3,R4,R5,R7]

# IMPORT MODULE

import os
where_I_want_to_go = "/Users/giuliamoret/Documents/Documenti università/EETBS/ASSIGNMENT"
os.chdir(where_I_want_to_go)
files_I_have = os.listdir(where_I_want_to_go)
print(files_I_have)
print('wallFunction_gmoret.py' in files_I_have)
import wallFunction_gmoret

# Step 1: wall made up of only wood

R_value_of_only_wood_list = wallFunction_gmoret.R_tot_calculator(Only_Wood)
print(R_value_of_only_wood_list)
R_tot_only_wood = R_value_of_only_wood_list[-1]

# Step 2: wall made up of only glass fiber insulator

R_value_of_only_insulator_list = wallFunction_gmoret.R_tot_calculator(Only_Insulator)
print(R_value_of_only_insulator_list)
R_tot_only_insulator = R_value_of_only_insulator_list[-1]

# Overall heat transfer coefficient

U_wood = 1.0 / R_tot_only_wood
U_ins = 1.0 / R_tot_only_insulator
U_tot = float(U_wood) * 0.25 + float(U_ins) * 0.75

# Overall unit thermal resistance

R_tot = 1.0 / U_tot

# Rate of heat loss through the walls

Q = U_tot * A_tot * (T_in - T_out)

# Print the results

print("****************************************************************")
print("Total resistance in case of only wood: "+str(R_tot_only_wood)+" m^2*(°C/W)")
print("****************************************************************")
print("Total resistance in case of only insulator: "+str(R_tot_only_insulator)+" m^2*(°C/W)")
print("****************************************************************")
print("The overall unit thermal resistance is: "+str(R_tot)+" m^2*(°C/W)")
print("****************************************************************")
print("The overall heat transfer coefficient is: "+str(U_tot)+" W/(m^2*°C)")
print("****************************************************************")
print("The rate of heat loss through the wall is: "+str(Q)+" W")

# FROM THE MODULE IMPORT THE FUNCTION

from wallFunction_gmoret import R_tot_calculator

# Step 1: wall made up of only wood

R_value_of_only_wood_list = R_tot_calculator(Only_Wood)
print(R_value_of_only_wood_list)
R_tot_only_wood = R_value_of_only_wood_list[-1]

# Step 2: wall made up of only glass fiber insulator

R_value_of_only_insulator_list = R_tot_calculator(Only_Insulator)
print(R_value_of_only_insulator_list)
R_tot_only_insulator = R_value_of_only_insulator_list[-1]

# Overall heat transfer coefficient

U_wood = 1.0 / R_tot_only_wood
U_ins = 1.0 / R_tot_only_insulator
U_tot = float(U_wood) * 0.25 + float(U_ins) * 0.75

# Overall unit thermal resistance

R_tot = 1.0 / U_tot

# Rate of heat loss through the walls

Q = U_tot * A_tot * (T_in - T_out)

# Print the results

print("****************************************************************")
print("Total resistance in case of only wood: "+str(R_tot_only_wood)+" m^2*(°C/W)")
print("****************************************************************")
print("Total resistance in case of only insulator: "+str(R_tot_only_insulator)+" m^2*(°C/W)")
print("****************************************************************")
print("The overall unit thermal resistance is: "+str(R_tot)+" m^2*(°C/W)")
print("****************************************************************")
print("The overall heat transfer coefficient is: "+str(U_tot)+" W/(m^2*°C)")
print("****************************************************************")
print("The rate of heat loss through the wall is: "+str(Q)+" W")