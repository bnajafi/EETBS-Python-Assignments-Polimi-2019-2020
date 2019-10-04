# -*- coding: utf-8 -*-
H = 0.8 #m
W = 1.5 #m
A = H*W #m^2

Tin = 20 #deg C
Tout = -10 #deg C

k_glass=0.78 #W/mC
L_glass=0.004 #m
k_gap=0.026 #W/mC
L_gap=0.01 #m
hin = 10 #W/m^2
hout = 40 #W/m^2

print("The value of the area is " + str(A) + " m^2")

R1 = ["R_in", "Conv", 10, 1.2]
R2 = ["R_glass1", "Cond", 0.004, 0.78, 1.2]
R3 = ["R_air", "Cond", 0.01, 0.026, 1.2]
R4 = ["R_glass2", "Cond", 0.004, 0.78, 1.2]
R5 = ["R_out", "Conv", 40, 1.2]

ResistancesList = [R1, R2, R3, R4, R5]
print(ResistancesList)

R_total = 0
for anyResistance in ResistancesList:
    if anyResistance[1] == "Conv":
        Rval = 1/float((anyResistance[2]*anyResistance[3]))
        anyResistance.append(Rval)
        print(anyResistance)
    elif anyResistance[1] == "Cond":
        Rval = float(anyResistance[2]/(anyResistance[3]*anyResistance[4]))
        anyResistance.append(Rval)
        print(anyResistance)
    R_total = R_total + Rval
print("The total value of the resistance is " + str(R_total) + " °C/W") 

Q = (Tin-Tout)/R_total
print("Q = " + str(Q) + " W")
Ts1 = Tin-(Q*R1[4])
print("Ts1= " + str(Ts1) + " °C")