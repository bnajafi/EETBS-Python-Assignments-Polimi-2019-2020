"""
Determine the overall thermal Resistance (Rvalue) and the overall heat transfer 
coefficient (U-factor) of a wood frame wall that is built around a 38mm 90mmm
wood studs with a center-to-center distance of 400mm. 
The 90mm-wide cavity between the studs is filled with glass fiber insulation. 
The inside is finished with a 13-mm wood fiberboard and 13mm 200mm wood bevel lapped siding.
The insulated cavity constitutes 75 percent of the heat transmission area while 
the studs, plates, and sills constitute 21 percent. 
The headers constitute 4 percent of the area, and they can be treated as studs. 
Also, determine the rate of heat loss through the walls of a house whose perimeter is 50m and 
wall height is 2.5m in Las Vegas, Nevada, whose winter design temperature is -2C. 
Take the indoor design temperature to be 22 C and assume 20 percent of the wall area is occupied by glazin
"""
#We have 7 different kinds of resistances that we need to put into account:
#Each resistance will have its own dictionary in order to facilitate calculations further on
#The values of the R_Units are taken according to standard tests and are given in a Table.

Atot = 50*2.5*0.8  #The walls constitute of 80% of the house with 50x2.5 of area.
Awood = Atot*.25    #25% of the house is wood
Ains = Atot*.75     #75% of the house is insulation

R1 = {"name":"outsideWinter","R_Unit":0.03,"Area":Atot,"Temperature":-2}
R2 = {"name":"woodbevel_13mm","R_Unit":0.14,"Area":Atot}
R3 = {"name":"woodfiber_13mm","R_Unit":0.23,"Area":Atot}
R4 = {"name":"glassfiber_90mm","R_Unit":2.52,"Area":Ains}
R5 = {"name":"woodstud_38mmx90mm","R_Unit":0.63,"Area":Awood}
R6 = {"name":"gypsum_13mm","R_Unit":0.079,"Area":Atot}
R7 = {"name":"insideSurface","R_Unit":0.12,"Area":Atot,"Temperature":22}

#We can say that 25% of the resistance is wood elements and they are in parallel with the other 75% that constitute of insulation
#We have that U-factor (total) = 1/Rtot

#The library of libraries would be a library with all the factors above in the same library:

Materials_Library = {"outsideWinter":R1,"woodbevel_13mm":R2,"woodfiber_13mm":R3,"glassfiber_90mm":R4,"woodstud_38mmx90mm":R5,"gypsum_13mm":R6,"insideSurface":R7}

print Materials_Library

#We can sum the total resistance for the elements in series with the stud


RList = [R1,R2,R3,R4,R5,R6,R7]
R_value_wood = 0
R_value_ins = 0
for anyR in RList:
    if anyR["Area"]==Awood or anyR["Area"] == Atot:    #meaning that if the value of "Area" is Awood or Atot we count
        Rwood = anyR["R_Unit"]
        R_value_wood = R_value_wood+Rwood
    if anyR["Area"]==Ains or anyR["Area"] == Atot:      #Can not be elif otherwise it will return only the R_unit correspondant to Area=Ains
        Rins = anyR["R_Unit"]
        R_value_ins = R_value_ins+Rins
        
#print R_value_wood
#print R_value_ins

#this way we have:
#The U-factor is = 1/Rvalue 

U_wood = 1.0/R_value_wood #U-factor for all wood
U_ins = 1.0/R_value_ins #U-factor for all insulation

#print U_wood
#print U_ins
#U-factor needs to count the areas

U_factor = (Ains/Atot)*U_ins + (Awood/Atot)*U_wood

print ("The U_factor is: "+str(U_factor)+" W/m2C")

Rtot = 1.0/U_factor

print ("The total Rvalue is: "+str(Rtot)+" m2C/W")

#To find the Q we can do a for to use the values in the library of libraries

Q = U_factor*Atot*(R7["Temperature"]-R1["Temperature"])
      
print ("Finally, the heat transfer Q is equal to: "+str(Q)+" W")
