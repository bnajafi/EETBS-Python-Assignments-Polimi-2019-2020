"""
In this assignment you should solve the same examplle as that of assignment 2 and this time you should do that using numpy !
You are not allowed to use for and if 
"""
"""
Determine the overall thermal Resistance (Rvalue) and the overall heat transfer coefficient (U-factor) of a wood frame 
wall that is built around a 38mm 90mmm wood studs with a center-to-center distance of 400mm. 
The 90mm-wide cavity between the studs is filled with glass fiber insulation. 
The inside is finished with a 13-mm wood fiberboard and 13mm 200mm wood bevel lapped siding.
The insulated cavity constitutes 75 percent of the heat transmission area while the studs, plates, and sills constitute 21 percent. 
The headers constitute 4 percent of the area, and they can be treated as studs. 
Also, determine the rate of heat loss through the walls of a house whose perimeter is 50m and 
wall height is 2.5m in Las Vegas, Nevada, whose winter design temperature is -2C. 
Take the indoor design temperature to be 22 C and assume 20 percent of the wall area is occupied by glazin
"""

import numpy as np

Atot = 50*2.5*0.8  #The walls constitute of 80% of the house with 50x2.5 of area.
Awood = Atot*.25    #25% of the house is wood
Ains = Atot*.75     #75% of the house is insulation

materials = np.array(["outsideWinter","woodbevel_13mm","woodfiber_13mm","glassfiber_25mm","woodstud_38mmx90mm","gypsum_13mm","insideSurface"])
resistances_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
std_resistances = np.array([ 0.03,0.14,0.23,0.7,0.63,0.079,0.12])   #Standard Resistances
std_L = np.array([ None,0.013,0.013,0.025,0.038,0.013,None])        #Needed to fix the Real R value later on
area_type = np.array([ Atot,Atot,Atot,Ains,Awood,Atot,Atot])        #The R values change according to the Area.

Tin = 22
Tout = -2
DeltaT = Tin-Tout

real_lenghts = np.array([None,0.013,0.013,0.090,0.038,0.013,None])  #The real Length used to find the real R

real_resistances = np.zeros(7)      #in order to compute the resistances in the same order of arrays used in the std_resistances
#print real_resistances

real_resistances[resistances_types=="cond"] = std_resistances[resistances_types == "cond"]*real_lenghts[resistances_types == "cond"]/std_L[resistances_types == "cond"]
#the result is placed on the same place as "cond" is for each array; grabs the values correspondants to the place where "cond" is in each array

real_resistances[resistances_types=="conv"] = std_resistances[resistances_types == "conv"]
#we don't need to change r for out and in, so we just place its std values in the same place as "conv" is in the arrays.


print ("The real resistances are: " +str(real_resistances))

Rwood = (area_type == Atot) | (area_type == Awood)      #Rwood grabs each resistance that is assigned as Atot OR Awood
Rwood_value = np.sum(real_resistances[Rwood])           #sums up each value in the array created in Rwood
# print Rwood_value

Uwood_value = 1/Rwood_value                             #the portion of U_factor correspondant to the area covered by Wood

Rins = (area_type == Atot) | (area_type == Ains)        #Rins grabs each resistance that is assigned as Atot OR Ains
Rins_value = np.sum(real_resistances[Rins])             #sums up each value in the array created in Rins
# print Rins_value

Uins_value = 1/Rins_value                               #the portion of U_factor correspondant to the area covered by insulation

U_factor = (Ains/Atot)*Uins_value + (Awood/Atot)*Uwood_value  #U_factor is the sum of each U times its covered area
print ("The Ufactor is: "+str(U_factor))

Rtot = 1/U_factor   
print ("The total Resistance is: "+str(Rtot))

Q = U_factor*Atot*DeltaT

print ("The total heat transfer Q is: "+str(Q))