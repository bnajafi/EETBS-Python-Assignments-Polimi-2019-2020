# -*- coding: utf-8 -*-
#Assignment 3 by Arian Maghsoudnia
#Coded in Canopy 2.1.9
 
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
 
#categories: A: with wood B: With Insulation
R1 = {"name":"R_wb","type":"Cond","material": "woodBevel","length": 0.013,"category":"A,B"}
R2 = {"name":"R_ws","type":"Cond","material": "woodStud","length": 0.09,"category":"A"}
R3 = {"name":"R_fb","type":"Cond","material": "fireboard","length": 0.013,"category":"A,B"}
R4 = {"name":"R_gf","type":"Cond","material": "glassFiber","length": 0.09,"category":"B"}
R5 = {"name":"R_gy","type":"Cond","material": "gypsum","length": 0.013,"category":"A,B"}
R6 = {"name":"R_int","type":"Conv","material":"inside"}
R7 = {"name":"R_out","type":"Conv","material":"outside"}
 
ResistanceList = [R1,R2,R3,R4,R5,R6,R7]
 
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

#This part calls the function in a loop

RtotA=0
RtotB=0
for thisResistance in ResistanceList:
    if thisResistance["type"]=="Cond":
        if thisResistance["category"]=="A,B" :
            RtotA=RtotA+local_R_calc(thisResistance)
            RtotB=RtotB+local_R_calc(thisResistance)
        elif thisResistance["category"]=="A" :
            RtotA=RtotA+local_R_calc(thisResistance)
        else :
            RtotB=RtotB+local_R_calc(thisResistance)
    if thisResistance["type"]=="Conv":
        RtotA=RtotA+local_R_calc(thisResistance)
        RtotB=RtotB+local_R_calc(thisResistance)

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

print ("The valuse of total Resistance in °C/W and heat transfer in W are respectively as follows: ")
HT(RtotA,RtotB)
     
