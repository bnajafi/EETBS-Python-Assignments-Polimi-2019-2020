# -*- coding: utf-8 -*-
## EXAMPLE B

R1 = ["R_Glass1","cond",0.004, 0.78,1.2]
R2 = ["R_Glass2","cond",0.004, 0.78,1.2]
R3 = ["R_Gap","cond",0.01,0.026,1.2]
#L_R1 = R1[2]
#k_R1 = R1[3]
#A_R1 = R1[4]

R_internal = ["R_internal","conv",10,1.2]
R_external = ["R_external","conv",40,1.2]

ResistancesList = [R_internal,R1,R2,R3,R_external] 

R_total=0

for anyResistance in ResistancesList:
    print(anyResistance)
    if anyResistance[1]=="cond":
        R_Value = float(anyResistance[2])/(anyResistance[3]*anyResistance[4])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
    elif anyResistance[1]=="conv":
        R_Value  = 1/(anyResistance[2]*anyResistance[3])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
        
print(ResistancesList)    

print("the total resistance is "+str(R_total)+ "degC/W")

T_inf1=20
T_inf2=-10

Q=(T_inf1-T_inf2)/R_total

print("the heat transfered through the double-pane window is "+str(Q)+ " W")

T_S1=T_inf1 - R_internal[4]*Q

print("the temperature of the inner surface is "+str(T_S1)+ "°C")