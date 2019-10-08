# -*- coding: utf-8 -*-
libraryOfMaterials = {
"outside":{"Rvalue":0.03,"thickness":0},
"Wood_bevel_lapped":{"Rvalue":0.14,"thickness":13},
"13mm_fiberboard":{"Rvalue":0.23,"thickness":13},
"Wood_studs":{"Rvalue":0.63,"thickness":90},
"13mm_Gypsum":{"Rvalue":0.079,"thickness":13},
"Inside_Air":{"Rvalue":0.12,"thickness":0},
"Glass_Fiber_insulation":{"Rvalue":0.7,"thickness":25},
}

Routside= {"name":"Routside","type":"conv",
"material":"outside"}   
RWood_bevel_lapped = {"name":"Rwoodbevel","type":"cond", 
"material":"Wood_bevel_lapped","length":13}  
R13mm_fiberboard={"name":"Rfiberboard","type":"cond", 
"material":"13mm_fiberboard","length":13} 
RWood_studs={"name":"Rwoodstuds","type":"cond", 
"material":"Wood_studs","length":90} 
R13mm_Gypsum={"name":"Rgypsum","type":"cond", 
"material":"13mm_Gypsum","length":13} 
RGlass_Fiber_insulation={"name":"Rglassfiber","type":"cond", 
"material":"Glass_Fiber_insulation","length":90} 
Rinside={"name":"Rinside","type":"conv", 
"material":"Inside_Air","length":0.5} 

RtotA=0
RtotB=0
ResistanceListA = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RWood_studs, R13mm_Gypsum, Rinside] 
ResistanceListB = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RGlass_Fiber_insulation, R13mm_Gypsum, Rinside]      

for i in ResistanceListA:
    if i ["type"]=="cond":
        StdThickness = libraryOfMaterials[ i ["material"]]["thickness"]
        StdResistance = libraryOfMaterials[ i ["material"]]["Rvalue"]
        RealUnitRes_i = StdResistance*i["length"]/StdThickness
        i ["RValueUnit"] = RealUnitRes_i
        RtotA=RtotA+RealUnitRes_i
    elif i ["type"]=="conv":
        StdResistance = libraryOfMaterials [ i ["material"]]["Rvalue"]
        i ["RValueUnit"] = StdResistance
        RtotA=RtotA+StdResistance
        UtotA=1/RtotA

for i in ResistanceListB:
    if i ["type"]=="cond":
        StdThickness = libraryOfMaterials[ i ["material"]]["thickness"]
        StdResistance = libraryOfMaterials[ i ["material"]]["Rvalue"]
        RealUnitRes_i = StdResistance*i["length"]/StdThickness
        i ["RValueUnit"] = RealUnitRes_i
        RtotB=RtotB+RealUnitRes_i
    elif i ["type"]=="conv":
        StdResistance = libraryOfMaterials [ i ["material"]]["Rvalue"]
        i ["RValueUnit"] = StdResistance
        RtotB=RtotB+StdResistance
        UtotB=1/RtotB
        
print ("Rtot for wood is "+str(RtotA)+ " °C/W * m^2")
print ("Rtot for insulation is "+str(RtotB)+ " °C/W * m^2")
print ("Utot for wood is "+str(UtotA)+ " W/°C/m^2")
print ("Utot for insulation is "+str(UtotB)+ " W/°C/m^2")

House={"Tin":22,"Tout":-2, 
"%WOOD":0.25,"%INSULATION":0.75,
"perimeter":50, "wall_height": 2.5,"%glazing":0.2} 

Utot=UtotA*House["%WOOD"]+UtotB*House["%INSULATION"]
print ("Utot is "+str(Utot)+ " W")

Area_tot=House["perimeter"]*House["wall_height"]*(1-House["%glazing"])
Qtot=Utot*Area_tot*(House["Tin"]-House["Tout"])
print ("Qtot is "+str(Qtot)+ " W")