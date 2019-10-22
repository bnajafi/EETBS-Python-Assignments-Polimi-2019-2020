# -*- coding: utf-8 -*-
#Assignment 4: Importing modules and functions###

import os
WhereIam = os.getcwd()
WhereIHaveFile = r"C:\Users\philt\OneDrive - Politecnico di Milano\LECTURES\Building Systems\Codes"
os.chdir(WhereIHaveFile)
filesIhave = os.listdir(WhereIHaveFile)
print(filesIhave)

#Import Module#

import wallFunction_Tankeu as WFT

print('Heat tranfer coef for wood is '+str(WFT.U_wood)+' W/m^2.°C' )

print('Heat tranfer coef for glass is '+str(WFT.U_glass)+' W/m^2.°C' )

print('The total Heat tranfer coef ' + ': '+ str(WFT.Utot)+ ' W/m^2.°C' )

print('Total Unit Resistance for wall' + ': ' + str(WFT.R_tot_wall)+ ' °C/W.m^2')
print("The rate of heat loss through the wall is "+ str(WFT.Q)+ " W")


#From Module Import#

from wallFunction_Tankeu import R1,R2,R3,R4,R5,R6,R7,StandardValues,Rprime_wood,Rprime_glass,Resistance,R_tot_wall,Utot,Q

Uwood = Resistance(Rprime_wood)
print('Heat tranfer coef for wood is '+str(Uwood)+' W/m^2.°C' )
Uglass = Resistance(Rprime_glass)
print('Heat tranfer coef for glass is '+str(Uglass)+' W/m^2.°C' )
print('The total Heat tranfer coef ' + ': '+ str(Utot)+ ' W/m^2.°C' )
print('Total Unit Resistance for wall' + ': ' + str(R_tot_wall)+ ' °C/W.m^2')
print("The rate of heat loss through the wall is "+ str(Q)+ " W")
