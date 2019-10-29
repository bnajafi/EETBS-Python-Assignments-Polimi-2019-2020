# -*- coding: utf-8 -*-
#In this assignment you should solve the same examplle as that of assignment 2 and this time you should do that using numpy !
#You are not allowed to use for and if

import numpy as np

# Define vectors
resistance_names=np.array(["R_in","R_gypsum","R_bavel","R_fiberboard","R_insulator","R_woodstud","R_out"])
resistance_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
resistance_Lwoodstud = np.array([None,13.0,13.0,13.0,0.0,90.0,None])
resistance_Lglassfiber=np.array([ None,13.0,13.0,13.0,90,0.0,None])
materials_names=np.array(["Inside","Gypsum","Wood_Bevel_Lapped_Siding","Wood_Fiberboard","Glass_Fiber_Insulator","Wood_Stud","Outside_Winter"])
materials_st_thick = np.array([None,13,13,13,25,90,None])
materials_R_value= np.array([0.12,0.079,0.14,0.23,0.70,0.63,0.03])

# Initialization
Resistance_RValuesWood=np.zeros(7)
Resistance_RValuesIns=np.zeros(7)

RtotIns=0
RtotWood=0

#Wood stud
Resistance_RValuesWood[resistance_types=="conv"]=materials_R_value[resistance_types=="conv"]
Resistance_RValuesWood[resistance_types=="cond"]=materials_R_value[resistance_types=="cond"]*resistance_Lwoodstud[resistance_types=="cond"]/materials_st_thick[resistance_types=="cond"]
print(Resistance_RValuesWood)
print(" ")
RtotWood=Resistance_RValuesWood.sum()
print("The resistance of the wall assumed with complitely wood is: "+str(RtotWood)+" m^2*°C/W")
print(" ")

#Glass fiber insulator
Resistance_RValuesIns[resistance_types=="conv"]=materials_R_value[resistance_types=="conv"]
Resistance_RValuesIns[resistance_types=="cond"]=materials_R_value[resistance_types=="cond"]*resistance_Lglassfiber[resistance_types=="cond"]/materials_st_thick[resistance_types=="cond"]
print(Resistance_RValuesIns)
print(" ")
RtotIns=Resistance_RValuesIns.sum()
print("The resistance of the wall when we have insulation is: "+str(RtotIns)+" m^2*°C/W")
print(" ")

#Determine the overall heat transfer coefficient,the overall  thermal resistance and the heat loss transfered
Uwood = 1.0/RtotWood
Uwithins = 1.0/RtotIns
Utot = Uwood*0.25 + Uwithins*0.75
print("The overall heat transfer coefficient is: "+str(Utot)+" W/(m^2*°C)")
print(" ")

# Data
Atot = 0.8*50*2.5 #mm^2
Tin = 22 #°C
Tout = -2 #°C
deltaT=Tin-Tout

R_tot =1.0/Utot
Q=Utot*Atot*deltaT
print("The overall thermal resistance is: "+str(R_tot)+" m^2*°C/W")
print(" ")
print("The rate of heat loss through the wall is: "+str(Q)+" W")
print(" ")