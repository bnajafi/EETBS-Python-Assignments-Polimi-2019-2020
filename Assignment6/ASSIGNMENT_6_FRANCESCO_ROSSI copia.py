# -*- coding: utf-8 -*-
######## ASSIGNMENT 6 FRANCESCO ROSSI #########

import pandas as pd
 
resistance_names = ["R_Outside","R_Inside","R_WoodBevel","R_WoodStud","R_Gypsum","R_WoodFiber","R_GlassFiberIns"]
resistances_material=["Outside","Inside","WoodBevel","WoodStud","Gypsum","WoodFiber","GlassFiberIns"]
resistances_types = ["conv","conv","cond","cond","cond","cond","cond"]
resistances_L= [None,None,0.013,0.09,0.013,0.013,0.09]
resistances_L_tab = [None,None,0,0,0,0,0]
resistances_RValues_Dict=[0,0,0,0,0,0,0]
resistances_RValues_real=[0,0,0,0,0,0,0]
resistance_ListOfLists = [resistances_material,resistances_types,resistances_L ,resistances_L_tab ,resistances_RValues_Dict , resistances_RValues_real]

 # Let's create the data frame for the problem!
 
resistances_DF_1 = pd.DataFrame(resistance_ListOfLists, index = ["material","type","L","L_tab","RValues_Dict","RValues_Real"] , columns = resistance_names)
resistances_DF = resistances_DF_1.transpose()
#print(resistances_DF)

def CalculationResistance( Input ) :
    
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
    
    OutputValue = LibraryOfMaterials[Input]["R_value"]
    
    return OutputValue
    
# now let's apply the function to the "material" data frame filling the column regarding the tabulated Resistances values
 
resistances_DF.loc[resistances_DF["type"]== "cond" , "RValues_Dict"] = resistances_DF["material"][resistances_DF["type"]=="cond"].apply(CalculationResistance)

# About convention resistance values,there is no difference between the tabulated and the real values,so we can fill the data frame with no regard to the length!!

resistances_DF.loc[resistances_DF["type"]== "conv" , "RValues_Dict" ] = resistances_DF["material"][resistances_DF["type"]=="conv"].apply(CalculationResistance)
resistances_DF.loc[resistances_DF["type"]== "conv" , "RValues_Real" ] = resistances_DF["material"][resistances_DF["type"]=="conv"].apply(CalculationResistance)

# Let's check if it has worked!

print(resistances_DF)

# Now let's deal with the length

def LengthResistance( Input ) :
    
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
                
    OutputValue = LibraryOfMaterials[Input]["length"]
    
    return OutputValue
    
resistances_DF.loc[resistances_DF["type"]== "cond" , "L_tab"] = resistances_DF["material"][resistances_DF["type"]=="cond"].apply(LengthResistance)

# Let's check if it has worked!

print(resistances_DF)

resistances_DF.loc[resistances_DF["type"]== "cond" , "RValues_Real"]=resistances_DF["RValues_Dict"][resistances_DF["type"]=="cond"]*resistances_DF["L"][resistances_DF["type"]=="cond"]/resistances_DF["L_tab"][resistances_DF["type"]=="cond"]

print(resistances_DF)

# Ok so now my data frame is completed! Now as usual let's compute the overall heat transfer coefficient and the Heating load

RtotWood=resistances_DF["RValues_Real"][resistances_DF["material"]!="GlassFiberIns"].sum()
RtotFiber=resistances_DF["RValues_Real"][resistances_DF["material"]!="WoodStud"].sum()
U1=1/float(RtotWood)
U2=1/float(RtotFiber)

U_overall=U1*0.25+U2*0.75
print("The Overall heat transfer coefficient is : " +str(U_overall)+  "W/m^2/°C")

perimeter=50
wall_height=2.5
glazing_fraction=0.8
T_in = 22  # °C
T_out= -2

Q= U_overall*perimeter*wall_height*glazing_fraction*(T_in - T_out)
print("The rate of the heat loss is: " +str(Q) +" W")
