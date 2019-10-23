#resistance and lenght of different materials
outsideAirDict={'Rvalue':0.03}
WoodbevelDict={'length':0.013,'Rvalue':0.14}
fiberboardDict={'length':0.013,'Rvalue':0.23}
GlassFiberinsulationDict={'length':0.025,'Rvalue':0.7}
WoodstudsDict={'length':0.09,'Rvalue':0.63}
GypsumDict={'length':0.013,'Rvalue':0.079}
InsideAirDict={'Rvalue':0.12}
#library of all materials
Libraryofmaterials={'outsideAir':outsideAirDict,'Woodbevel':WoodbevelDict,'fiberboard':fiberboardDict,
'GlassFiberinsulation':GlassFiberinsulationDict,'Woodstuds':WoodstudsDict,'Gypsum':GypsumDict,'InsideAir':InsideAirDict}
#write function: R_calculator recieve resistant from list and calculate the exact resistant based on the material that we use   
def R_calculator(resist):
    if resist["type"]=="Cond":
        LengthOFThisResistance = resist["length"]
        materialOFThisResistance = resist["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardLengthOfThisMaterialInTheLibrary =  equivalentDictOFThisMaterialInTheLibrary["length"]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        RealUnitResistanceOFThisMaterial = StandardUnitResistanceOfThisMaterialInTheLibrary*LengthOFThisResistance/StandardLengthOfThisMaterialInTheLibrary
        resist["Rvalue"] = RealUnitResistanceOFThisMaterial
    if resist["type"]=="Conv":
        materialOFThisResistance = resist["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        resist["Rvalue"] = StandardUnitResistanceOfThisMaterialInTheLibrary
    return (resist["Rvalue"])
#for calculating total resistance for two different types (woodstud and glassfiber) we use for loop 