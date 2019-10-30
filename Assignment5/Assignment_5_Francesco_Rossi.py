# -*- coding: utf-8 -*-

# ASSIGNMENT 5 FRANCESCO ROSSI

 # let's first import numpy
 
import numpy as np

 # now we define the arrays containg all the data necessary for the calculation of the total resistance
 
R_tabulated_length = np.array([0,0.013,0.013,0.025,0.09,0.013,0])
R_tabulated_value =  np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
R_length = np.array([0,0.013,0.013,0.09,0.09,0.013,0])
R_type = np.array(["conv","cond","cond","cond","cond","cond","conv"])
R_wood=np.array([1,1,1,0,1,1,1])
R_insulation=np.array([1,1,1,1,0,1,1])

# let's initialize the vector that will be filled with the value of the resistance
 
R_value=np.zeros(7)

# let's fill it!

R_value[R_type=="conv"]=R_tabulated_value[R_type=="conv"]
R_value[R_type=="cond"]=R_tabulated_value[R_type=="cond"]*R_length[R_type=="cond"]/R_tabulated_length[R_type=="cond"]

R_with_woodStud = np.zeros(7)
R_insulated = np.zeros(7)

R_with_woodStud[R_wood==1]=R_value[R_wood==1]
R_insulated[R_insulation==1]=R_value[R_insulation==1]

R_total_wood = np.sum(R_with_woodStud)
R_total_insulation = np.sum(R_insulated)

U_insulation=1/float(R_total_insulation)
U_wood=1/float(R_total_wood)
Area_ratio_wood=0.25
Area_ratio_ins=0.75

# Now Let's compute the overall heat transfer coefficient

U_tot= U_insulation*Area_ratio_ins + U_wood*Area_ratio_wood
print("The Overall heat transfer coefficient is : " +str(U_tot)+  "W/m^2/°C")

# Total resistance

R_tot_prime = 1/ U_tot
print("The Total resistance is : " +str(R_tot_prime)+  "m^2*°C/W")


# Now Let's compute the rate of heat loss throught the walls

perimeter=50
wall_height=2.5
glazing_fraction=0.8
T_in = 22  # °C
T_out= -2

Q= U_tot*perimeter*wall_height*glazing_fraction*(T_in - T_out)
print("The rate of the heat loss is: " +str(Q) +" W")

