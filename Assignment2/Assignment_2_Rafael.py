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

#We can say that 25% of the resistance is wood elements and they are in parallel with the other 75% that constitute of insulation
#We have that U-factor (total) = 1/Rtot

#The library of libraries would be a library with all the factors in the same library:

Std_R1 = {"R_Unit":0.03}
Std_R2 = {"R_Unit":0.14,"StdL":0.013}
Std_R3 = {"R_Unit":0.23,"StdL":0.013}
Std_R4 = {"R_Unit":0.7,"StdL":0.025}
Std_R5 = {"R_Unit":0.63,"StdL":0.038}
Std_R6 = {"R_Unit":0.079,"StdL":0.013}
Std_R7 = {"R_Unit":0.12}

#We can say that 25% of the resistance is wood elements and they are in parallel with the other 75% that constitute of insulation
#We have that U-factor (total) = 1/Rtot

#The library of libraries would be a library with all the factors above in the same library:

Std_Materials_Library = {"outsideWinter":Std_R1,"woodbevel_13mm":Std_R2,"woodfiber_13mm":Std_R3,"glassfiber_25mm":Std_R4,"woodstud_38mmx90mm":Std_R5,"gypsum_13mm":Std_R6,"insideSurface":Std_R7}

# print Std_Materials_Library  --> if we want to check the values for each material.

#We can sum the total resistance for the elements in series with the stud
R1 = {"type":"conv","material":"outsideWinter","Area":Atot,"Temperature":-2}
R2 = {"type":"cond","material":"woodbevel_13mm","L":0.013,"Area":Atot}
R3 = {"type":"cond","material":"woodfiber_13mm","L":0.013,"Area":Atot}
R4 = {"type":"cond","material":"glassfiber_25mm","L":0.09,"Area":Ains}
R5 = {"type":"cond","material":"woodstud_38mmx90mm","L":0.038,"Area":Awood}
R6 = {"type":"cond","material":"gypsum_13mm","L":0.013,"Area":Atot}
R7 = {"type":"conv","material":"insideSurface","Area":Atot,"Temperature":22}

RList = [R1,R2,R3,R4,R5,R6,R7]

for anyR in RList:
    if anyR["type"] == "cond":
        Length = anyR["L"]                                  #calls L in R1, R2..
        Material = anyR["material"]                         #calls the name of the material in R1, R2..
        Value_in_Library = Std_Materials_Library[Material]  #calls the value you want for the correspondant [Material] in the library of libraries
        Std_length = Value_in_Library["StdL"]               #Gets the value of StdL in Std_Materials_Library for each material
        Std_Resistance = Value_in_Library["R_Unit"]         #Gets the value of R_Unit in Std_Materials_Library for each material
        R_Value = Std_Resistance*(Length/Std_length)        #finds the real value or R for each material.
        anyR["R_Value"] = R_Value                           #Assigns a new fixture called "R_Value" in RList for each R1, R2..
     
    if anyR["type"] == "conv":
        Conv_Side = anyR["material"]                          #Calls the name of material in R1, R2 and makes it a real value
        Value_conv_Library = Std_Materials_Library[Conv_Side] #finds the value above in library of libraries and let's us find any value we want from library of libraries
        R_Value = Value_conv_Library["R_Unit"]                #creates a float with the value we want named R_Value from Lib of lib.
        anyR["R_Value"] = R_Value                             #Creates a new segment in R1, R2, R3.. called R_Value with the value R_Value
        
# print RList   #Used to print RList and check the values if they are right

R_value_wood = 0
R_value_ins = 0

#Notice that RList is already updated after the 'for' above, so the next for will count the real values of R.

for anyR in RList:
    if anyR["Area"]==Awood or anyR["Area"] == Atot:    #meaning that if the value of "Area" is Awood or Atot we count
        Rwood = anyR["R_Value"]
        R_value_wood = R_value_wood + Rwood

    if anyR["Area"]==Ains or anyR["Area"] == Atot:      #Can not be elif otherwise it will return only the R_unit correspondant to Area=Ains
        Rins = anyR["R_Value"]
        R_value_ins = R_value_ins + Rins
        
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

print ("The total Resistance is: "+str(Rtot)+" m2C/W")

#To find the Q we can do a for to use the values in the library of libraries

Q = U_factor*Atot*(R7["Temperature"]-R1["Temperature"])
      
print ("Finally, the heat transfer Q is equal to: "+str(Q)+" W")

