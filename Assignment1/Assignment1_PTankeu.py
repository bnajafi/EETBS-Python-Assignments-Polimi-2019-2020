#Assignment One: Double Pane Window

Tinf1=raw_input("insert indoor temperature in deg C")
Tinf2=raw_input("insert outdoor temperature in deg C")
height=raw_input("insert window's height in m")
width=raw_input("insert window's width in m")
print(Tinf1)
print(Tinf2)
print(height)
print(width)
A=float(height)*float(width)
print(A)
R_ext = ["R_external", "conv", 10, 1.2]
R1=["R_glass1","cond",0.004,0.78,1.2]
R2=["R_air","cond",0.01,0.026,1.2]
R3=["Rglass2","cond",0.004,0.78,1.2]
R_int=["R_internal","conv",40,1.2]
R_list=[R_ext,R1,R2,R3,R_int]
#Computing Q
R_tot=0
for anyR in R_list:
    if anyR[1]=="cond":
        R_val=float(anyR[2])/(anyR[3]*anyR[4])
        R_tot = R_tot+R_val
        anyR.append(R_val)
    elif anyR[1]=="conv":
        R_val=1/(float(anyR[2])*anyR[3])
        R_tot= R_tot+R_val
        anyR.append(R_val)
print("The total thermal resistance is "+ str(R_tot)+" deg C/W")

Q = (float(Tinf1)-float(Tinf2))/R_tot
print("The steady rate of heat transfer is "+ str(Q)+ " W")

#Computing tumperatures of Inner surface.

T_list =[]
for anyT in range((len(R_list))-1):
    if anyT==0:
        T_list.append(float(Tinf1)-(Q*R_list[anyT][-1]))
    else:
         T_list.append(float(T_list[-1])-(Q*R_list[anyT][-1]))

print("[T1,T2,T3,T4] = "+ str(T_list)+ " in deg C")

    