# -*- coding: utf-8 -*-
#Wall Functions by Arian Maghsoudnia
#Coded in Canopy Phython 2
 
 #Inserting Material Properties
woodBevelDict = {"length":0.013,"RValUnit":0.14}
woodStudDict = {"length":0.09,"RValUnit":0.63}
fireboardDict={"length":0.013,"RValUnit":0.23}
glassFiberDict={"length":0.025,"RValUnit":0.7}
GypsumDict = {"length":0.013,"RValUnit":0.079}
insideDict = {"RValUnit":0.12}
outsideDict = {"RValUnit":0.03}
 
 #Building the Library of Materials
libraryOfMaterials = { "woodBevel":woodBevelDict,"woodStud" : woodStudDict,"gypsum": GypsumDict,"fireboard":fireboardDict,"glassFiber":glassFiberDict, 
"inside":insideDict, "outside" :outsideDict}
 
#Function that recieves the resistance list and returns associated value of real resistance               
def local_R_calc(R):
    if R["type"]=="Cond":
        #RValUnitThisReistance = libraryOfMaterials[thisResistance["material"]] 
        LengthOFThisResistance = R["length"]
        materialOFThisResistance = R["material"]
        equivalentDictOFThisMaterialInTheLibrary = libraryOfMaterials[materialOFThisResistance]
        StandardLengthOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["length"]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["RValUnit"]
        RealUnitResistanceOFThisMaterial = StandardUnitResistanceOfThisMaterialInTheLibrary*LengthOFThisResistance/StandardLengthOfThisMaterialInTheLibrary
        R["RValueUnit"] = RealUnitResistanceOFThisMaterial
    if R["type"]=="Conv":
        materialOFThisResistance = R["material"]
        equivalentDictOFThisMaterialInTheLibrary = libraryOfMaterials[materialOFThisResistance]
        StandardUnitResistanceOfThisMaterialInTheLibrary = equivalentDictOFThisMaterialInTheLibrary["RValUnit"]
        R["RValueUnit"] = StandardUnitResistanceOfThisMaterialInTheLibrary
    return( R["RValueUnit"])

#

#This function recieves two valuse of resistances and returns heat transfer and total resistance value in an array
def HT(RA,RB):
    U_wood=1/RA
    U_ins=1/RB
    U_tot=U_wood*0.25+U_ins*0.75
    Rtot=1/U_tot
    Atot=100
    dt=24
    Qtot=U_tot*Atot*dt
    return([Rtot,Qtot])


     
