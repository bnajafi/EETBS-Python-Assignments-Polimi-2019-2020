# -*- coding: utf-8 -*-
#FUNCTION
def resistanceCalculatorFromLibrary (listOfResistances):
    '''This function receives a list of resistances and finds a vector with:
    -the corresponding list of resistance values considering the case in which
    the resistance has not standard length 
    -the total resistance (last term of the vector)  
    It also adds the new term "RValueUnit" in the dictionary of each resistance.'''
    Rtot=0
    listResults=[]
    for i in listOfResistances:
     if i ["type"]=="cond":
        StdThickness = libraryOfMaterials[ i ["material"]]["thickness"]
        StdResistance = libraryOfMaterials[ i ["material"]]["Rvalue"]
        RealUnitRes_i = StdResistance*i["length"]/StdThickness
        i ["RValueUnit"] = RealUnitRes_i
        listResults.append(RealUnitRes_i)
        Rtot=Rtot+RealUnitRes_i
     elif i ["type"]=="conv":
        StdResistance = libraryOfMaterials [ i ["material"]]["Rvalue"]
        i ["RValueUnit"] = StdResistance
        listResults.append(StdResistance)
        Rtot=Rtot+StdResistance
    listResults.append(Rtot)
    return (listResults)

#PROBLEM SOLUTION
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

ResistanceListA = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RWood_studs, R13mm_Gypsum, Rinside] 
ResistanceListB = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RGlass_Fiber_insulation, R13mm_Gypsum, Rinside]  

solA= resistanceCalculatorFromLibrary(ResistanceListA)
solB= resistanceCalculatorFromLibrary(ResistanceListB)

help(resistanceCalculatorFromLibrary)

print ("Individual resistances for wood are "+str(solB[0:-1])+ " °C/W * m^2")        
print ("Individual resistances for insulation are "+str(solA[0:-1])+ " °C/W * m^2")        
print ("Rtot for wood is "+str(solA[-1])+ " °C/W * m^2")
print ("Rtot for insulation is "+str(solB[-1])+ " °C/W * m^2")

House={"Tin":22,"Tout":-2, 
"%WOOD":0.25,"%INSULATION":0.75,
"perimeter":50, "wall_height": 2.5,"%glazing":0.2} 

Utot=1/solA[-1]*House["%WOOD"]+1/solB[-1]*House["%INSULATION"]
print ("Utot is "+str(Utot)+ " W")

Area_tot=House["perimeter"]*House["wall_height"]*(1-House["%glazing"])
Qtot=Utot*Area_tot*(House["Tin"]-House["Tout"])
print ("--> Qtot is "+str(Qtot)+ " W")