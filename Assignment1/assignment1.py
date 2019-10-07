#### example B 
# R1 = [type,conv,A,h,Result]
# R = [type,cond,A,L,k,Result]
R1=["R_inner","conv",1.2,10]
R2=["R_outer","conv",1.2,40]
R3=["R_glass","cond",1.2,0.004,0.78]
R4=["R_glass","cond",1.2,0.004,0.78]
R5=["R_gap","cond",1.2,0.01,0.026]
ResistanceList=[R1,R2,R3,R4,R5]
R_tot=0
for anyresistance in ResistanceList:
    print(anyresistance)
    if anyresistance[1] == "cond":
        R_value = float(anyresistance[3])/(anyresistance[2]*anyresistance[4])
        anyresistance.insert(6,R_value)
        R_tot = R_tot + R_value
    else:
   
        R_value = 1/(anyresistance[2]*anyresistance[3])
        anyresistance.insert(5,R_value)
        R_tot = R_tot + R_value
print(ResistanceList)
print("the total value of resistance"+ str(R_tot)+"   degree C/w")

T_inff1=20
T_inff2=-10
##R =[R_inner,R_glass1,R_gap,R_glass2,R_external]
R = [R1[-1],R3[-1],R5[-1],R3[-1],R2[-1]]
print(R)
Q_tot = float(T_inff1-T_inff2 )/(R_tot)
T1 = T_inff1 - Q_tot*R[0]
T2 = T1 - Q_tot*R[1]
T3 = T2 - Q_tot*R[2]
T4 = T3 - Q_tot*R[3]

T = [T1,T2,T3,T4]
print(T)
