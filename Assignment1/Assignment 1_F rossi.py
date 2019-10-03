# -*- coding: utf-8 -*-
# Assignment 1

R1 = ["R_glass","cond",0.004,0.78,1.2]
R2 = ["R_air","cond",0.01,0.026,1.2]
R3 = ["R_glass","cond",0.004,0.78,1.2]
R_internal = ["R_internal","conv",10,1.2]
R_external = ["R_external","conv",40,1.2]
ResistancesList = [R1,R2,R3,R_internal,R_external]
R_total=0
T_int=20
T_ext=-10

# with a for loop now I "create" my total thermal resistance

for anyResistance in ResistancesList:
    if anyResistance[1] == "cond":
        R_Value = float(anyResistance[2])/(anyResistance[3]*anyResistance[4])
        anyResistance.append(R_Value) # add the value
        R_total=R_total+R_Value
    elif anyResistance[1] == "conv":
        R_Value = 1/(anyResistance[2]*anyResistance[3])
        anyResistance.append(R_Value)
        R_total=R_total+R_Value
print("The total resistance is: " +str(R_total) + " °C/W")

# let's compute the heat transfer rate
 
Q=(T_int-T_ext)/float(R_total)
print("The heat transfer rate is: " +str(Q) +" Watt")

# let's compute the temperature of the internal surface

Ts1=T_int-float(Q)*R_internal[4]
print("The temperature of the internal surfaces is: " +str(Ts1) +" °C")


