outsideAirDict={'Rvalue':0.03}
WoodbevelDict={'length':0.013,'Rvalue':0.14}
fiberboardDict={'length':0.013,'Rvalue':0.23}
GlassFiberinsulationDict={'length':0.025,'Rvalue':0.7}
WoodstudsDict={'length':0.09,'Rvalue':0.63}
GypsumDict={'length':0.013,'Rvalue':0.079}
InsideAirDict={'Rvalue':0.12}
Libraryofmaterials={'outsideAir':outsideAirDict,'Woodbevel':WoodbevelDict,'fiberboard':fiberboardDict,
'GlassFiberinsulation':GlassFiberinsulationDict,'Woodstuds':WoodstudsDict,'Gypsum':GypsumDict,'InsideAir':InsideAirDict}

R1={"name":"R_out","type":"Conv","material":"outsideAir"}
R2={"name":"R_Woodbevel","type":"Cond","material": "Woodbevel","length": 0.013}
R3={"name":"R_fiberboard","type":"Cond","material": "fiberboard","length": 0.013}
R4={"name":"R_GlassFiberinsulation","type":"Cond","material": "GlassFiberinsulation","length": 0.09}
R5={"name":"R_Woodstuds","type":"Cond","material": "Woodstuds","length": 0.09}
R6={"name":"R_Gypsum","type":"Cond","material": "Gypsum","length": 0.013}
R7={"name":"R_InsideAir","type":"Conv","material": "InsideAir"}
resistanceList1=[R1,R2,R3,R5,R6,R7]
resistanceList2=[R1,R2,R3,R4,R6,R7]
Rtot_withwoodstud = 0
Rtot2_withGlassFiber = 0
for thisResistance in resistanceList1:
    if thisResistance["type"]=="Cond":
        LengthOFThisResistance = thisResistance["length"]
        materialOFThisResistance = thisResistance["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardLengthOfThisMaterialInTheLibrary =  equivalentDictOFThisMaterialInTheLibrary["length"]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        RealUnitResistanceOFThisMaterial = StandardUnitResistanceOfThisMaterialInTheLibrary*LengthOFThisResistance/StandardLengthOfThisMaterialInTheLibrary
        thisResistance["Rvalue"] = RealUnitResistanceOFThisMaterial
        Rtot_withwoodstud=Rtot_withwoodstud+RealUnitResistanceOFThisMaterial
    if thisResistance["type"]=="Conv":
        materialOFThisResistance = thisResistance["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        thisResistance["Rvalue"] = StandardUnitResistanceOfThisMaterialInTheLibrary
        Rtot_withwoodstud=Rtot_withwoodstud+StandardUnitResistanceOfThisMaterialInTheLibrary
for thisResistance in resistanceList2:
    if thisResistance["type"]=="Cond":
        #RValUnitThisReistance = libraryOfMaterials[thisResistance["material"]] 
        LengthOFThisResistance = thisResistance["length"]
        materialOFThisResistance = thisResistance["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardLengthOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["length"]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        RealUnitResistanceOFThisMaterial = StandardUnitResistanceOfThisMaterialInTheLibrary*LengthOFThisResistance/StandardLengthOfThisMaterialInTheLibrary
        thisResistance["Rvalue"] = RealUnitResistanceOFThisMaterial
        Rtot2_withGlassFiber=Rtot2_withGlassFiber+RealUnitResistanceOFThisMaterial
    if thisResistance["type"]=="Conv":
        materialOFThisResistance = thisResistance["material"]
        equivalentDictOFThisMaterialInTheLibrary = Libraryofmaterials[materialOFThisResistance]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["Rvalue"]
        thisResistance["Rvalue"] = StandardUnitResistanceOfThisMaterialInTheLibrary
        Rtot2_withGlassFiber=Rtot2_withGlassFiber+StandardUnitResistanceOfThisMaterialInTheLibrary
print('The total resistance of wood part',str(Rtot_withwoodstud), 'C/W')
print('The total resistance with Insulation',str(Rtot2_withGlassFiber), 'C/W')
U_wood=1/Rtot_withwoodstud
U_insulation=1/Rtot2_withGlassFiber
U_tot=U_wood*0.25+U_insulation*0.75
Rtot=1/U_tot
print('The total resistance is ',str(Rtot),'C/W')
Atot=100
dt=24
Q_dot_tot=U_tot*Atot*dt
print('The rate of heat dissipated to the outside is ',str(Q_dot_tot), 'W')
