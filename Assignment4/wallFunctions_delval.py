# -*- coding: utf-8 -*-
ListRes1={
"Rwoodbps":{"length":0.013,"type":"cond"},
"Rwoodfs":{"length":0.013,"type":"cond"},
"Rglassf":{"length":0.09,"type":"cond"},
"Rgypsum":{"length":0.013,"type":"cond"},
"Rin":{"type":"conv"},
"Rout":{"type":"conv"}
}
ListRes2={
"Rwoodbps":{"length":0.013,"type":"cond"},
"Rwoodfs":{"length":0.013,"type":"cond"},
"Rwoodst":{"length":0.09,"type":"cond"},
"Rgypsum":{"length":0.013,"type":"cond"},
"Rin":{"type":"conv"},
"Rout":{"type":"conv"}
}



def Calculatingresoverall(Resistancelist):
    ListMat={
    "Rin":{"Res":0.12},
    "Rout":{"Res":0.030},
    "Rwoodbps":{"Res":0.14,"length":0.013},
    "Rwoodfs":{"Res":0.23,"length":0.013},
    "Rglassf":{"Res":0.70,"length":0.025},
    "Rwoodst":{"Res":0.63,"length":0.09},
    "Rgypsum":{"Res":0.079,"length":0.013}
    }
    ResList=[]
    Rtot=0
    Rval=0
    for resistance in Resistancelist:
        if Resistancelist[resistance]["type"]=="cond":
            Rval=float(ListMat[resistance]["Res"]*Resistancelist[resistance]["length"])/ListMat[resistance]["length"]
            Rtot=Rtot+Rval
            ResList.append(ListMat[resistance]["Res"])
        elif Resistancelist[resistance]["type"]=="conv":
            Rtot=Rtot+float(ListMat[resistance]["Res"])
            ResList.append(ListMat[resistance]["Res"])
    ResList.append(Rtot)
    return ResList


Rcase1=Calculatingresoverall(ListRes1)
print(Rcase1)
Rcase2=Calculatingresoverall(ListRes2)
print(Rcase2)

#CalculatiRng general overall resistance and heat transfer coefficient
Rgen=1.0/(0.75/Rcase1[6]+0.25/Rcase2[6])
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