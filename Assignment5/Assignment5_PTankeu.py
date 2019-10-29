# -*- coding: utf-8 -*-
##Assignment 5 by Tankeu Philippe

import numpy as np 
T_inside= 22
T_outside = -2

##A:Computing R_tot_wall

resistance_names = np.array(["R_outside","R_woodB","R_fiberboard","R_glass","R_Woodstud","R_gypsum","R_inside"])
resistance_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
Rval_standard = np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
Standard_length = np.array([None,0.013,0.013,0.025,0.09,0.013, None])
Resistance_length = np.array ([None,0.013,0.013,0.09,0.09,0.013, None])
R_values = np.zeros(7)
R_wood = np.array([1,1,1,0,1,1,1])
R_glass= np.array([1,1,1,1,0,1,1])
R_values[resistance_types == "conv"] = Rval_standard[resistance_types == "conv"]
R_values[resistance_types == "cond"] = Rval_standard[resistance_types == "cond"]*Resistance_length[resistance_types == "cond"]/Standard_length[resistance_types == "cond"]

R_with_wood = np.zeros(7)
R_with_wood[R_wood == 1] = R_values[R_wood ==1]
print(R_with_wood)
R_with_glass =np.zeros(7)
R_with_glass[R_glass ==1] = R_values[R_glass == 1]
print(R_with_glass)
R_tot_wood = np.sum(R_with_wood)
R_tot_glass =np.sum(R_with_glass)
U_wood = 1.0/R_tot_wood
U_glass = 1.0/R_tot_glass
U_total = U_wood*0.25+U_glass*0.75
R_tot_wall = 1.0/U_total
R_total_wall = round(R_tot_wall,3)
print("The Overall Unit thermal Resistance is " + str(R_total_wall) + " °C/W")

##B: Computing Q in W

wall_perimeter = 50
wall_heigth = 2.5
glazing_fraction = float(20)/100
A_tot = wall_perimeter * wall_heigth
A_actual = A_tot*(1-glazing_fraction)
Q = U_total * A_actual * (T_inside - T_outside)
Q = round(Q,3)
print("The rate of heat loss through the wall is "+ str(Q)+ " W")

