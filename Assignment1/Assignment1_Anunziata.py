# -*- coding: utf-8 -*-
#EXAMPLE B Angela Nunziata 
Tinf1_internal=20.0
Tinf2_external=-10.0
Rglass1 = ["R_Glass1","cond", 0.004, 0.78, 1.2]
Rglass2 = ["R_Glass2","cond", 0.004, 0.78, 1.2]
Rgap = ["R_Gap","cond", 0.01, 0.026, 1.2]
R1_internal = ["R_internal","conv",10,1.2]
R2_external = ["R_external","conv",40,1.2]
R_total=0
ResistanceList = [Rglass1, Rglass2, Rgap, R1_internal,R2_external]

for santiago in ResistanceList: 
    if santiago[1]=="cond":
         R_value = santiago[2]/(santiago[3]*santiago[4])
         R_total = R_total+R_value
         santiago.append(R_value)
    elif santiago[1]=="conv":
        R_value= 1.0/(santiago[2]*santiago[3])
        R_total=R_total+R_value
        santiago.append(R_value)
        
print(ResistanceList)
print("--> The total resistance is "+str(R_total)+ " °C/W")

Q=(Tinf1_internal-Tinf2_external)/R_total
print("--> The heat transfer through this double pane window is "+str(Q)+ " W")

T1=Tinf1_internal-Q*R1_internal[4]
print("--> The temperature of the inner surface is "+str(T1)+ " °C")