"""
In this assignment you should write a function that receives a list of resistances,
(the same as previous assignment) and calculate the individual and total resistance values.

Use it to solve the same problem as that of last week.
"""
Atot = 50*2.5*0.8  #The walls constitute of 80% of the house with 50x2.5 of area.
Awood = Atot*.25    #25% of the house is wood
Ains = Atot*.75     #75% of the house is insulation

def ResistanceCalculatorLibrary (ResistanceList):
    
    Std_R1 = {"R_Unit":0.03}
    Std_R2 = {"R_Unit":0.14,"StdL":0.013}
    Std_R3 = {"R_Unit":0.23,"StdL":0.013}
    Std_R4 = {"R_Unit":0.7,"StdL":0.025}
    Std_R5 = {"R_Unit":0.63,"StdL":0.038}
    Std_R6 = {"R_Unit":0.079,"StdL":0.013}
    Std_R7 = {"R_Unit":0.12}

    Std_Materials_Library = {"outsideWinter":Std_R1,"woodbevel_13mm":Std_R2,"woodfiber_13mm":Std_R3,"glassfiber_25mm":Std_R4,"woodstud_38mmx90mm":Std_R5,"gypsum_13mm":Std_R6,"insideSurface":Std_R7}
    
    for anyR in ResistanceList:
        if anyR ["type"] == "cond":
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
            R_Value_conv = Value_conv_Library["R_Unit"]           #creates a float with the value we want named R_Value from Lib of lib.
            anyR["R_Value"] = R_Value_conv
        
        R_value_wood = 0
        R_value_ins = 0

        if anyR["Area"]==Awood or anyR["Area"] == Atot:    #meaning that if the value of "Area" is Awood or Atot we count
            Rwood = anyR["R_Value"]
            R_value_wood = R_value_wood + Rwood
            

        if anyR["Area"]==Ains or anyR["Area"] == Atot:      #Can not be elif otherwise it will return only the R_unit correspondant to Area=Ains
            Rins = anyR["R_Value"]
            R_value_ins = R_value_ins + Rins    
            
    U_wood = 1.0/R_value_wood #U-factor for all wood
    U_ins = 1.0/R_value_ins #U-factor for all insulation

    U_factor = (Ains/Atot)*U_ins + (Awood/Atot)*U_wood

    # print ("The U_factor is: "+str(U_factor)+" W/m2C")

    Rtot = 1.0/U_factor

    # print ("The total Resistance is: "+str(Rtot)+" m2C/W")
    return Rtot


#now we can give the list of materials used in the problem:

R1 = {"type":"conv","material":"outsideWinter","Area":Atot,"Temperature":-2}
R2 = {"type":"cond","material":"woodbevel_13mm","L":0.013,"Area":Atot}
R3 = {"type":"cond","material":"woodfiber_13mm","L":0.013,"Area":Atot}
R4 = {"type":"cond","material":"glassfiber_25mm","L":0.09,"Area":Ains}
R5 = {"type":"cond","material":"woodstud_38mmx90mm","L":0.038,"Area":Awood}
R6 = {"type":"cond","material":"gypsum_13mm","L":0.013,"Area":Atot}
R7 = {"type":"conv","material":"insideSurface","Area":Atot,"Temperature":22}

RList = [R1,R2,R3,R4,R5,R6,R7]  #this RList will be used in the FUNCTION in order to calculate the U_factor, the Rtot and each Resistance

Results = ResistanceCalculatorLibrary(RList)    #The function called ResistanceCalculatorLibrary will get the values in RList to give us the results

Real_R = []                     #If I want to print just the resistances from the new RList I need to assign an empty list
for R in RList:
    Resistance = R["R_Value"]   #gets each R_Value in RList
    Real_R.append(Resistance)   #appends each R_Value in Real_R list.

print ("Each resistance is for each material is respectively: "+str(Real_R))

print ("The U_factor is: "+str(U_factor)+" W/m2C")      #the U_factor is already inside the function and is calculated once we have a list of Materials

print ("The total Resistance is: "+str(Rtot)+" m2C/W")  #the same is valid for R total.

#To find the Q we can do a for to use the values in the library of libraries

Q = U_factor*Atot*(R7["Temperature"]-R1["Temperature"])
      
print ("Finally, the heat transfer Q is equal to: "+str(Q)+" W")
