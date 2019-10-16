

#Assignment 2 WITH FUNCTION!

def RValueUnitandTotal (ResistanceList): 

    """This function receives a list of resistances and find the resistance total value considering that the heat transmission 
    is in serie and the directory of the unit thermal resistances of common components in buildings"""

#Library of Resistance values of each material
    ThermalResDict={"GlassFiberInsulation":{"R":0.7,"length":0.025},
                "WoodStud_90mm":{"R":0.63,"length":0.09},
                "WoodFiberBoard":{"R":0.23,"length":0.013},
                "WoodLappedSiding":{"R":0.14,"length":0.013},
                "Gypsum":{"R":0.079,"length":0.013},
                "InsideSurface":{"R":0.12},
                "OutsideSurface":{"R":0.03},#WINTER
                }

#Value of resistence total by calculating firstly the thermal resistance units. 
    Rtot=0
    for AnyResistance in ResistanceList:
        if AnyResistance["type"]=="cond":
            material_AnyResistance=AnyResistance["material"]
            length_AnyResistance=AnyResistance["length"]
            lengthOnLibrary=ThermalResDict[material_AnyResistance]["length"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]*length_AnyResistance/lengthOnLibrary
            AnyResistance["RValue"]=RValue_AnyResistance
            Rtot=Rtot+RValue_AnyResistance #In serie
        elif AnyResistance["type"]=="conv":
            material_AnyResistance=AnyResistance["material"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]
            AnyResistance["RValue"]=RValue_AnyResistance
            Rtot=Rtot+RValue_AnyResistance #In serie
    result=Rtot
    return result

#CASE: #Determine the overall unit thermal resistance (the Rvalue) and the overall heat transfer coefficient (the U-factor) of a wood frame wall that is built around 38-mm 90-mm
#wood studs with a center-to-center distance of 400 mm. The 90-mm-wide cavity between the studs is filled with
#glass fiber insulation. The inside is finished with 13-mm gypsum wallboard and the outside with 13-mm wood
#fiberboard and 13-mm 200-mm wood bevel lapped siding. The insulated cavity constitutes 75 percent of the heat
#transmission area while the studs, plates, and sills constitute 21 percent. The headers constitute 4 percent of the area, and
# they can be treated as studs. Also, determine the rate of heat loss through the walls of a
#house whose perimeter is 50 m and wall height is 2.5 m in Las Vegas, Nevada, whose winter design temperature is -2 C. Take the indoor design temperature to be 22 C and
#assume 20 percent of the wall area is occupied by glazing.


#Dictionaries of every Resistance
R_i={"name":"inside surface", "type":"conv", "material":"InsideSurface"}
R_2={"name":"Wood bevel lapped Siding", "type":"cond", "material":"WoodLappedSiding", "length":0.013}
R_3={"name":"Wood fiberboard", "type":"cond", "material":"WoodFiberBoard", "length":0.013}
R_4={"name":"Glass fiber insulation", "type":"cond", "material":"GlassFiberInsulation", "length":0.09}
R_5={"name":"Wood studs", "type":"cond", "material":"WoodStud_90mm", "length":0.09}          
R_6={"name":"Gypsum Wallboard","type":"cond", "material":"Gypsum", "length":0.013}
R_o={"name":"Outside surface", "type":"conv", "material":"OutsideSurface"}

#There are in parallel: one passes through the wood stud 25% and the the other through the glass fiber 75%

#R_total_wood
#In serie this resistances R_i: I=i,2,3,4.a,5,o. Simply sum them. 

ResistanceList_withWood=[R_i,R_2,R_3,R_5,R_6,R_o]
RTotalwithWood=RValueUnitandTotal (ResistanceList_withWood) 

#R_total_glass
#In serie this resistances R_i: I=i,2,3,4.b,5,o. Simply sum them.

ResistanceList_withInsulation=[R_i,R_2,R_3,R_4,R_6,R_o]
RTotalwithInsulation=RValueUnitandTotal (ResistanceList_withInsulation)


#Utotal and Rtotal

U_wood=1/RTotalwithWood
U_insulation=1/RTotalwithInsulation
Utotal=0.25*U_wood+0.75*U_insulation
print("The total heat transfer coefficient is Utotal= "+str(Utotal))

Rtotal=1/Utotal
print("The total thermal resistance is Rtotal= "+str(Rtotal))

#Rate of heat loss through the walls

Area=50*2.5*0.8
T_1=22
T_2=-2
Q=Utotal*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q))



