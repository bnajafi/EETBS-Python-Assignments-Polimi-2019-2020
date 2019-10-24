# -*- coding: utf-8 -*-
#Assingment N°4

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

#Importing part...
import os
os.getcwd()
Loc2=r"C:\Users\Santi\Desktop\MoS Politecnico di Milano\3 Semestre\Building Systems"
os.chdir(Loc2)
os.getcwd()
Files=os.listdir(os.getcwd())
print("wallFunctions_delval.py" in Files)

#Solving the exercise
#Case1
import wallFunctions_delval as wall
Rcase1=wall.Calculatingresoverall(ListRes1)
print(Rcase1)
#Case2
from wallFunctions_delval import Calculatingresoverall
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

clear