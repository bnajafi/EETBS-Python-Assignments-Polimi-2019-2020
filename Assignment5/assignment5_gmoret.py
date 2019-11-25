# -*- coding: utf-8 -*-
# ASSIGNMENT 5 

# Data
L_cavity = 90.0 #mm
L_gypsum = 13.0 #mm
L_fiberboard = 13.0 #mm
L_bevel = 13.0 #mm x 200mm
A_tot = 0.8*50*2.5 #m^2
T_in = 22 #°C
T_out = -2 #°C

import numpy as np

resistance_name = np.array(["R_in","R_out","R_gypsum","R_bavel","R_fiberboard","R_insulator","R_stud"])
resistance_type = np.array(["conv","conv","cond","cond","cond","cond_insulator","cond_wood"])
resistance_L_std = np.array([ None,None,13.0,13.0,13.0,25.0,90.0 ])
resistance_L = np.array([ None,None,L_gypsum, L_bevel,L_fiberboard,L_cavity,L_cavity ])
resistance_R_std = np.array([ 0.12,0.03,0.079,0.14,0.23,0.7,0.63 ])

R_only_wood = np.zeros(7)

conv_index = resistance_type == "conv"
R_only_wood[conv_index] = resistance_R_std[conv_index]
cond_index = resistance_type == "cond"
R_only_wood[cond_index] = resistance_R_std[cond_index]*(resistance_L[cond_index]/resistance_L_std [cond_index])
wood_index = resistance_type == "cond_wood"
R_only_wood[wood_index] = resistance_R_std[wood_index]*(resistance_L[wood_index]/resistance_L_std [wood_index])
print("Resistance value considering only wood is: "+str(R_only_wood.sum())+" m^2*°C/W")

R_only_insulator = np.zeros(7)

R_only_insulator[conv_index] = resistance_R_std[conv_index]
R_only_insulator[cond_index] = resistance_R_std[cond_index]*(resistance_L[cond_index]/resistance_L_std [cond_index])
insulator_index = resistance_type == "cond_insulator"
R_only_insulator[insulator_index] = resistance_R_std[insulator_index]*(resistance_L[insulator_index]/resistance_L_std [insulator_index])
print("Resistance value considering only insulator is: "+str(R_only_insulator.sum())+" m^2*°C/W")

U_wood = 1.0 / R_only_wood.sum()
U_ins = 1.0 / R_only_insulator.sum()
U_tot = float(U_wood) * 0.25 + float(U_ins) * 0.75
R_tot = 1.0 / U_tot
Q = U_tot * A_tot * (T_in - T_out)

print("The overall unit thermal resistance is: "+str(R_tot)+" m^2*(°C/W)")
print("The overall heat transfer coefficient is: "+str(U_tot)+" W/(m^2*°C)")
print("The rate of heat loss through the wall is: "+str(Q)+" W")