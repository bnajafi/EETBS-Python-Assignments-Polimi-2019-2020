# -*- coding: utf-8 -*-
#Assignment N°2
#R is expressed in m2*C/W
#Length is expressed in m

#Defining my dictionary of materials 
ListMat={
"Rin":{"Res":0.12},
"Rout":{"Res":0.030},
"Rwoodbps":{"Res":0.14,"length":0.013},
"Rwoodfs":{"Res":0.23,"length":0.013},
"Rglassf":{"Res":0.70,"length":0.025},
"Rwoodst":{"Res":0.63,"length":0.09},
"Rgypsum":{"Res":0.079,"length":0.013}
}

#Checking if my dictionary is well set
for x in ListMat:
    print(x)
    print(ListMat[x])

#Stablishing dictionaries for my resistances characteristics
ListRes1={
"Rwoodbps":{"length":0.013,"type":"cond"},
"Rwoodfs":{"length":0.013,"type":"cond"},
"Rglassf":{"length":0.09,"type":"cond"},
"Rwoodst":{"length":0.00,"type":"cond"},
"Rgypsum":{"length":0.013,"type":"cond"},
"Rin":{"type":"conv"},
"Rout":{"type":"conv"}
}
ListRes2={
"Rwoodbps":{"length":0.013,"type":"cond"},
"Rwoodfs":{"length":0.013,"type":"cond"},
"Rglassf":{"length":0.00,"type":"cond"},
"Rwoodst":{"length":0.09,"type":"cond"},
"Rgypsum":{"length":0.013,"type":"cond"},
"Rin":{"type":"conv"},
"Rout":{"type":"conv"}
}

#Checking again...
for y in ListRes1:
    print(y)
    
#Setting paramaters
Rtot1=0
Rtot2=0
Rval1=0
Rval2=0

#Calculating Roverall across glass fiber
for Rover1 in ListRes1:
    if ListRes1[Rover1]["type"]=="cond":
        MAT1=Rover1
        LENGTH1=ListMat[MAT1]["length"]
        RV=ListMat[MAT1]["Res"]
        Rval1=float(RV*ListRes1[Rover1]["length"])/LENGTH1
        Rtot1=Rtot1+Rval1
    elif ListRes1[Rover1]["type"]=="conv":
        Rtot1=Rtot1+float(RV)
print("The total resistance (across glass fiber) is R1 = "+str(Rtot1)+" m2*C/W")

#Calculating Roverall across wood stud (this time simplifying much more)
for Rover1 in ListRes2:
    if ListRes2[Rover1]["type"]=="cond":
        Rval2=float(ListMat[Rover1]["Res"]*ListRes1[Rover1]["length"])/ListMat[Rover1]["length"]
        Rtot2=Rtot2+Rval2
    elif ListRes1[Rover1]["type"]=="conv":
        Rtot2=Rtot2+float(ListMat[Rover1]["Res"])
print("The total resistance (across wood stub) is R2 = "+str(Rtot2)+" m2*C/W")

#CalculatiRng general overall resistance and heat transfer coefficient
Rgen=1.0/(0.75/Rtot1+0.25/Rtot2)
print("The overall general resistance is Rgen = "+str(Rgen)+" m2*C/W")
Ufac=1.0/Rgen
print("The heat transfer coefficient is Ufac = "+str(Ufac)+" W/m2*C")

#Heat loss calculations
Area=50*2.5 #m2
T1=-2 #°C
T2=22 #°C
Rglazing=0.433226495726*1.2 #As for this resistance I assumed its value from the resistance calculated in the previous assignment; a double pane window (0.433...C/W and 1.2 m2)
Uglazing=1.0/Rglazing
#Just checking...
print(Uglazing)
Q=(0.20*Uglazing+0.80*Ufac)*Area*(T2-T1)
print("The rate of heat loss is Q = "+str(Q)+" W")

clear


