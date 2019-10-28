# -*- coding: utf-8 -*-
#Assignment 5: Valentina Caia

import numpy as np

#data
Tout = -2 #°C
Tin = 22 #°C
deltaT = Tin-Tout

P = 50 #m
H = 2.5 #m
A = P*H*0.8 #m^2    #20% of the wall area is occupied by glazing


#defining vectors
R_name = np.array(["R_out","R_woodBL","R_fiber","R_glass","R_woodS","R_gypsum","R_in"])
R_type = np.array(["Conv.","Cond.","Cond.","Cond.","Cond.","Cond.","Conv."])
R_thickness_standard = np.array([None,0.013,0.013,0.025,0.09,0.013,None])
R_thickness = np.array([None,0.013,0.013,0.09,0.09,0.013,None])
R_wood = np.array([0.03,0.14,0.23,0.,0.63,0.079,0.12])
R_insulation_std = np.array([0.03,0.14,0.23,0.70,0.,0.079,0.12])

RValues_wood = np.zeros(7)
RValues_ins = np.zeros(7)

Rwood_tot = 0
Rins_tot = 0

#wood
print("If we have only convection")
indexArray_resistance_type_Conv = R_type == "Conv."
print(indexArray_resistance_type_Conv)
RValues_wood[indexArray_resistance_type_Conv] = R_wood[indexArray_resistance_type_Conv]
print("the resistances are: " +str(RValues_wood))
print("When we have also conduction the resistances will be:")
RValues_wood[R_type == "Cond."] = R_wood[R_type == "Cond."]
print(RValues_wood)

Rwood_tot = RValues_wood.sum()
print("The overall unit thermal resistance with wood is " + str(Rwood_tot) + " °C m^2/W")

#insulation
print("If we have the insulation the resistances are:")
RValues_ins[R_type == "Conv."] = R_insulation_std[R_type == "Conv."]
RValues_ins[R_type == "Cond."] = R_insulation_std[R_type == "Cond."]*R_thickness[R_type == "Cond."]/R_thickness_standard[R_type == "Cond."]
print(RValues_ins)

Rins_tot = RValues_ins.sum()
print("The overall unit thermal resistance with insulation is " + str(Rins_tot) + " °C m^2/W")


#U calculation
U_wood = 1/float(Rwood_tot)
U_ins = 1/float(Rins_tot)
U_tot= (U_wood*0.25)+(U_ins*0.75)
print("The toal heat transfer coefficient is " + str(U_tot) + " W/°C m^2")

#Heat loss
print("The area is " + str(A) + " m^2")
print("The temperature difference, in winter, between inside and outside is " + str(deltaT) +"°C")
Q = round(U_tot*A*deltaT,1)
print("The heat loss through the walls of the house is "+ str(Q) + " W")