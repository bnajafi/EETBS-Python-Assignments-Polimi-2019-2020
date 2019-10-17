# -*- coding: utf-8 -*-
# ASSIGNMENT 2 FRANCESCO ROSSI #

# Let's first report the tabulated values of the materials

Outside_tab = {"R_value": 0.03}
Inside_tab = {"R_value" : 0.12}
WoodBevelLapped_tab = {"R_value": 0.14 , "length": 0.013}
WoodStud_tab = {"R_value": 0.63 , "length": 0.090}
Gypsum_tab = {"R_value": 0.079 , "length": 0.013}
WoodFiberboard_tab = {"R_value": 0.23 , "length": 0.013}
GlassFiberIns_tab = {"R_value": 0.70 , "length": 0.025}

# Now Let's create the LibraryOfMaterials

LibraryOfMaterials = {"Outside" : Outside_tab , "Inside" : Inside_tab , "WoodBevel" : WoodBevelLapped_tab , "WoodStud" : WoodStud_tab ,
                "Gypsum" : Gypsum_tab , "WoodFiber" : WoodFiberboard_tab , "GlassFiberIns" : GlassFiberIns_tab }
                
# Now let's define the Resistances 

R1 = {"name":"R_Outside" , "type": "conv" , "material" : "Outside"}
R2 = {"name":"R_Inside" , "type": "conv" , "material" : "Inside"}
R3 = {"name":"R_WoodBevel" , "type": "cond" , "material" : "WoodBevel" , "length" : 0.013}
R4 = {"name":"R_WoodStud" , "type": "cond" , "material" : "WoodStud" , "length" : 0.09}
R5 = {"name":"R_Gypsum" , "type": "cond" , "material" : "Gypsum" , "length" : 0.013}
R6 = {"name":"R_WoodFiber" , "type": "cond" , "material" : "WoodFiber" , "length" : 0.013}
R7 = {"name":"R_GlassFiberIns" , "type": "cond" , "material" : "GlassFiberIns" , "length" : 0.09}

R_with_Insulation_List = [R1,R2,R3,R5,R6,R7]
R_with_woodStud_List = [R1,R2,R3,R4,R5,R6]
R_tot_ins=0;
R_tot_wood=0;

# Let's now compute the series of the resistances in the Insulation case

for anyResistance in R_with_Insulation_List :
    R_Material = anyResistance["material"]
    if anyResistance["type"] == "cond" :
        if anyResistance["length"]== LibraryOfMaterials[R_Material]["length"] :
            Rvalue=LibraryOfMaterials[R_Material]["R_value"] 
        else :
            Rvalue=LibraryOfMaterials[R_Material]["R_value"]*anyResistance["length"]/LibraryOfMaterials[R_Material]["length"]
    elif anyResistance["type"] == "conv" :
        Rvalue=LibraryOfMaterials[R_Material]["R_value"]
    R_tot_ins = R_tot_ins + Rvalue
print("The value of the total resistance with Insulation is: " +str(R_tot_ins) +" °C*m2/W")  

# Let's now compute the series of the resistances in the Wood Stud case

for anyResistance in R_with_woodStud_List :
    R_Material = anyResistance["material"]
    if anyResistance["type"] == "cond" :
        if anyResistance["length"]== LibraryOfMaterials[R_Material]["length"] :
            Rvalue=LibraryOfMaterials[R_Material]["R_value"] 
        else :
            Rvalue=LibraryOfMaterials[R_Material]["R_value"]*anyResistance["length"]/LibraryOfMaterials[R_Material]["length"]
    elif anyResistance["type"] == "conv" :
        Rvalue=LibraryOfMaterials[R_Material]["R_value"]
    R_tot_wood = R_tot_wood + Rvalue
print("The value of the total resistance with Wood Stud is: " +str(R_tot_wood) +" °C*m2/W") 

U_insulation=1/float(R_tot_ins)
U_wood=1/float(R_tot_wood)
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