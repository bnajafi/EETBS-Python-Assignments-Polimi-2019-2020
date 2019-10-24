#import wallFunctions_Llinas
#libraryOfMaterials=wallFunctions_Llinas.libraryOfMaterials

from wallFunctions_Llinas import libraryOfMaterials
from wallFunctions_Llinas import EquivalentResistance


R1={"name":"R_out","type":"conv","material":"outside"}
R2={"name":"R_woodbevel","type":"cond","material":"woodbevel","length":0.013}
R3={"name":"R_woodfiber","type":"cond","material":"woodfiber","length":0.013}
R4={"name":"R_glassfiber","type":"cond","material":"glassfiber","length":0.09}
R5={"name":"R_woodstud","type":"cond","material":"woodstud","length":0.09}
R6={"name":"R_gypsum","type":"cond","material":"gypsum","length":0.013}
R7={"name":"R_in","type":"conv","material":"inside"}

Rwithwood=[R1,R2,R3,R5,R6,R7]
Rwithinsulation=[R1,R2,R3,R4,R6,R7]

fractionwood=0.25
fractioninsulation=1-fractionwood
perimeter=50
wallheight=2.5
glazingfraction=0.2

Rwithwood=[R1,R2,R3,R5,R6,R7]
Rwithinsulation=[R1,R2,R3,R4,R6,R7]
Tin=22
Tout=-2


#Rtot1=wallFunctions_Llinas.EquivalentResistance(Rwithwood)
#Rtot2=wallFunctions_Llinas.EquivalentResistance(Rwithinsulation)

Rtot1=EquivalentResistance(Rwithwood)
Rtot2=EquivalentResistance(Rwithinsulation)


print("The value of " +str(R1["name"]) +" is: " +str(R1["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R2["name"]) +" is: " +str(R2["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R3["name"]) +" is: " +str(R3["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R4["name"]) +" is: " +str(R4["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R5["name"]) +" is: " +str(R5["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R6["name"]) +" is: " +str(R6["Rvalue"]) +" degC*m2/W")
print("The value of " +str(R7["name"]) +" is: " +str(R7["Rvalue"]) +" degC*m2/W")

print("The value of the total resistance with Wood studs is: " +str(Rtot1) +" degC/Wm2")
print("The value of the total resistance with Insulation is: " +str(Rtot2) +" degC*m2/W")


Uwood=1/float(Rtot1)
Uinsulation=1/float(Rtot2)
Utotal=Uwood*fractionwood+Uinsulation*fractioninsulation
print("The value of the total overall heat transfer coeficient is: " +str(Utotal) +" W/degC*m2")


Rprimetot=1/float(Utotal)
Atot=(1-glazingfraction)*wallheight*perimeter
Qtot=Atot*Utotal*(Tin-Tout)
print("The value of the heat transfer rate loss is: " +str(Qtot) +" W")