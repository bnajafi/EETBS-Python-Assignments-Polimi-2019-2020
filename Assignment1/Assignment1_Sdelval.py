# -*- coding: utf-8 -*-
#Example B solved
#A=1.2 m2
R1=["Rinternal","conv",10,1.2]
#hin=10 W/(m2*C)
R2=["Rexternal","conv",40,1.2]
#hex=40 W/(m2*C)
R3=["Rglass","cond",0.004,0.78,1.2]
R5=["Rglass","cond",0.004,0.78,1.2]
R6=["Rmiddle","cond",0.010,0.026,1.2]
#L=0.004/0.010 m , K=0.78/0.026 W/(m*C)
Rlist=[R1,R2,R3,R5,R6]
Rtot=0
Rval=0
print(Rlist)

for anyresistance in Rlist:
    if anyresistance[1]=="conv":
        Rval=1.0/(anyresistance[2]*anyresistance[3])
        Rtot=Rtot+Rval
    elif anyresistance[1]=="cond":
        Rval=float(anyresistance[2])/(anyresistance[3]*anyresistance[4])
        Rtot=Rtot+Rval
print("The Total resistance is R = "+str(Rtot)+" C/W")

#Rate of heat transfer  
T1=20 #°C
T2=-10 #°C 
Q=(T1-T2)/Rtot

print("The rate of heat transfer is Q = "+str(Q)+" W" )

#Temperature of the inner surface
R4=1.0/(R1[2]*R1[3])
R1.append(R4)
print(R1)

Tinsurf=T1-(Q*R1[4])
print("The inner surface temperature is T= "+str(Tinsurf)+ "°C")
