# -*- coding: utf-8 -*-
#Assignment N°5
#R is expressed in m2*C/W
#Length is expressed in m
#A in m2

#First we import the module we are going to need
import numpy as np

#We set the define data as a vector
resistance_names=np.array(["R_internal","R_woodbps","R_woodfs","R_glassf","R_woodst","R_gypsum","R_external"])
resistance_types=np.array(["conv","cond","cond","cond","cond","cond","conv"])
resistance_R= np.array([ 0.12,0.14,0.23,0.70,0.63,0.079,0.030])
resistance_Lstandar=np.array([None,0.013,0.013,0.025,0.09,0.013,None ])
resistance_Lglass=np.array([ None,0.013,0.013,0.09,0.00,0.013,None])
resistance_Lwoodst=np.array([ None,0.013,0.013,0.00,0.09,0.013,None])
A=125

#Stablishing the resistance vectors for each case
resistance_RVal1=np.zeros(7)
resistance_RVal2=np.zeros(7)
#Cheking
print(resistance_RVal1)

#Solving the problem with logical operators 
Rtot1=0
Rtot2=0
#First case:glass fiber
resistance_RVal1[resistance_types=="conv"]=resistance_R[resistance_types=="conv"]
resistance_RVal1[resistance_types=="cond"]=resistance_R[resistance_types=="cond"]*resistance_Lglass[resistance_types=="cond"]/resistance_Lstandar[resistance_types=="cond"]
print(resistance_RVal1)
Rtot1=resistance_RVal1.sum()
print(Rtot1)
#Second case:wood stub
resistance_RVal2[resistance_types=="conv"]=resistance_R[resistance_types=="conv"]
resistance_RVal2[resistance_types=="cond"]=resistance_R[resistance_types=="cond"]*resistance_Lwoodst[resistance_types=="cond"]/resistance_Lstandar[resistance_types=="cond"]
print(resistance_RVal2)
Rtot2=resistance_RVal2.sum()
print(Rtot2)

#Calculating general overall resistance and heat transfer coefficient
Rgen=1.0/(0.75/Rtot1+0.25/Rtot2)
print("The overall general resistance is Rgen = "+str(Rgen)+" m2*C/W")
Ufac=1.0/Rgen
print("The heat transfer coefficient is Ufac = "+str(Ufac)+" W/m2*C")

#Heat loss calculations
T1=-2 #°C
T2=22 #°C

#Just checking...
Q=(0.80*Ufac)*A*(T2-T1)
print("The rate of heat loss is Q = "+str(Q)+" W")

clear
