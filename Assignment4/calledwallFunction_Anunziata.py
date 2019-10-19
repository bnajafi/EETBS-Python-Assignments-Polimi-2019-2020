
#Material Library
ML = {"outside":{"Rvalue":0.03,"thickness":0},
"Wood_bevel_lapped":{"Rvalue":0.14,"thickness":13},
"13mm_fiberboard":{"Rvalue":0.23,"thickness":13},
"Wood_studs":{"Rvalue":0.63,"thickness":90},
"13mm_Gypsum":{"Rvalue":0.079,"thickness":13},
"Inside_Air":{"Rvalue":0.12,"thickness":0},
"Glass_Fiber_insulation":{"Rvalue":0.7,"thickness":25}


}

#Resistance Calculator From Library
def RCFL (listOfResistances):
    '''This function receives a list of resistances and finds a vector with:
    -the corresponding list of resistance values considering the case in which
    the resistance has not standard length 
    -the total resistance (last term of the vector)  
    It also adds the new term "RValueUnit" in the dictionary of each resistance.'''
    Rtot=0
    listResults=[]
    for i in listOfResistances:
     if i ["type"]=="cond":
        StdThickness = ML[ i ["material"]]["thickness"]
        StdResistance = ML[ i ["material"]]["Rvalue"]
        RealUnitRes_i = round((StdResistance*i["length"]/StdThickness),3)
        i ["RValueUnit"] = RealUnitRes_i
        listResults.append(RealUnitRes_i)
        Rtot=Rtot+RealUnitRes_i
     elif i ["type"]=="conv":
        StdResistance = ML[ i ["material"]]["Rvalue"]
        i ["RValueUnit"] = StdResistance
        listResults.append(StdResistance)
        Rtot=Rtot+StdResistance
    listResults.append(Rtot)
    return (listResults)