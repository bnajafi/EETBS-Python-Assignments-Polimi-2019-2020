# -*- coding: utf-8 -*-
#Assignment1 Ndefranceschi
#Data
L_glass = 0.004 #m
L_air = 0.01 #m
A = 0.8*1.5 #m^2
k_glass = 0.78 #W/mC
k_air = 0.026 #W/mC
h_in = 10 #W/m^2C
h_out = 40 #W/m^2C
T_in = 20 #C
T_out = -10 #C
print("The value of the area is " + str(A) + " m^2")
#Evaluation of Resistances
R1 = ["R_glass","Cond",0.78,0.004,A]
R2 = ["R_gap","Cond",0.026,0.01,A]
R3 = ["R_in","Conv",10,A]
R4 = ["R_out","Conv",40,A]
R5 = ["R_glass","Cond",0.78,0.004,A]
ResistanceList = [R1,R2,R3,R4,R5]
R_total = 0

for anyR in ResistanceList:
    if (anyR[1] == "Cond"):
        RVal = float(anyR[3])/(anyR[2]*anyR[4])
        anyR.append(RVal)
        print(anyR)
    elif (anyR[1] == "Conv"):
        RVal = float(1)/(anyR[2]*anyR[3])
        anyR.append(RVal)
        print(anyR)
    R_total = R_total + RVal
print("The total R value is " + str(R_total) + " °C/W")
    
#Evaluation of the heat transfer
Q = (T_in-T_out)/R_total
print("Q = " + str(Q) + " W")
#Evaluation of the temperature of the inner surface
Ts1 = T_in-Q*R3[4]
print("Ts1 = " + str(Ts1) + " °C")

