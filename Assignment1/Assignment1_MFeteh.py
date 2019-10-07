height=0.8
w=1.5
A=height*w
K_glass=0.78
K_air=0.026
h1=10
h2=40
L_glass=0.004
L_air=0.010
T1=20
T2=-10
R1=["R1","conv",h1,A]
R2=["R_glass","cond",L_glass,K_glass,A]
R3=["R_air","cond",L_air,K_air,A]
R4=["R_glass","cond",L_glass,K_glass,A]
R5=["R5","conv",h2,A]
Ressistancelist=[R1,R2,R3,R4,R5]
for anyresistance in Ressistancelist:
    if anyresistance[1]=="conv":
        R_value=1/float((anyresistance[2]*anyresistance[3]))
    elif anyresistance[1]=="cond":
        R_value=float(anyresistance[2])/(anyresistance[3]*anyresistance[4])
    anyresistance.append(R_value)
    print(anyresistance)
Q=(T1-T2)/(R1[4]+R2[5]+R3[5]+R4[5]+R5[4])
print(Q)
T_inner=T1-(Q/(h1*A))
print(T_inner)