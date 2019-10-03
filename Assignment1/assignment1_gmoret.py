# -*- coding: utf-8 -*-
# ASSIGNMENT 1 

# Data
L_glass = 4*10**(-3) #m
L_air = 10*10**(-3) #m
A = 0.8*1.5 #m^2
k_glass = 0.78 #W/m/°C
k_air = 0.026 #W/m/°C
h_in = 10 #W/m^2/°C
h_out = 40 #W/m^2/°C
T_in = 20 #°C
T_out = -10 #°C

# Resistances
R1 = ["int convection","conv",h_in,A]
R2 = ["ext convection","conv",h_out,A]
R3 = ["glass conduction",L_glass,k_glass,A]
R4 = ["air conduction",L_air,k_air,A]
R5 = ["glass conduction",L_glass,k_glass,A]
ResistanceList = [R1,R2,R3,R4,R5]
R_total = 0
for anyresistance in ResistanceList:
    print(anyresistance)
    if anyresistance[1]=="conv":
        R_value = float(1)/(anyresistance[2]*anyresistance[3])
        R_total = R_total + R_value
        anyresistance.append(R_value)
    else:
        R_value = float(anyresistance[1])/(anyresistance[2]*anyresistance[3])
        R_total = R_total + R_value
        anyresistance.append(R_value)
print("The total resistance is "+str(R_total)+" °C/W")

# Steady rate of heat transfert
Q = float(T_in-T_out)/R_total #W
print("Steady rate of heat flux: "+str(Q)+" W")

# Temperature of the inner face
T_inglass = T_in - float(Q*R1[-1])
print("Temperature of the inner glass: "+str(T_inglass)+" °C")




        