gypsumDict = {"length":0.013,"RValUnit":0.079}
woodfiberDict = {"length":0.013,"RValUnit":0.23}
woodbevelDict = {"length":0.013,"RValUnit":0.14}
woodstudDict = {"length":0.09, "RValUnit":0.63}
glassfiberDict = {"length":0.025,"RValUnit":0.7}
insideDict = {"RValUnit":0.12}
outsideDict = {"RValUnit":0.03}

libraryOfMaterials = { "gypsum":gypsumDict,"woodStud" : woodfiberDict,"woodfiber": woodfiberDict,"woodbevel":woodbevelDict , 
"woodstud":woodstudDict,"glassfiber":glassfiberDict,"inside":insideDict, "outside" :outsideDict} 

R1={"name":"R_out","type":"conv","material":"outside"}
R2={"name":"R_woodbevel","type":"cond","material":"woodbevel","length":0.013}
R3={"name":"R_woodfiber","type":"cond","material":"woodfiber","length":0.013}
R4={"name":"R_glassfiber","type":"cond","material":"glassfiber","length":0.09}
R5={"name":"R_woodstud","type":"cond","material":"woodstud","length":0.09}
R6={"name":"R_gypsum","type":"cond","material":"gypsum","length":0.013}
R7={"name":"R_in","type":"conv","material":"inside"}

fractionwood=0.25
fractioninsulation=1-fractionwood
perimeter=50
wallheight=2.5
glazingfraction=0.2

Rwithwood=[R1,R2,R3,R5,R6,R7]
Rwithinsulation=[R1,R2,R3,R4,R6,R7]
Rtot1=0
Rtot2=0
Tin=22
Tout=-2

for anyR in Rwithwood:
    anyRmaterial=anyR["material"]
    if anyR["type"]=="cond":
        if anyR["length"]==libraryOfMaterials[anyRmaterial]["length"]:
            Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]  
        else:
            Rvalue=float(libraryOfMaterials[anyRmaterial]["RValUnit"])*anyR["length"]/libraryOfMaterials[anyRmaterial]["length"]
    elif anyR["type"]=="conv":
        Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]
    Rtot1=Rtot1+Rvalue
print("The value of the total resistance with Wood studs is: " +str(Rtot1) +" degC/Wm2")

for anyR in Rwithinsulation:
    anyRmaterial=anyR["material"]
    if anyR["type"]=="cond":
        if anyR["length"]==libraryOfMaterials[anyRmaterial]["length"]:
            Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]  
        else:
            Rvalue=float(libraryOfMaterials[anyRmaterial]["RValUnit"])*anyR["length"]/libraryOfMaterials[anyRmaterial]["length"]
    elif anyR["type"]=="conv":
        Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]
    Rtot2=Rtot2+Rvalue
print("The value of the total resistance with Insulation is: " +str(Rtot2) +" degC*m2/W")


Uwood=1/float(Rtot1)
Uinsulation=1/float(Rtot2)

Utotal=Uwood*fractionwood+Uinsulation*fractioninsulation
print("The value of the total overall heat transfer coeficient is: " +str(Utotal) +" W/degC*m2")

Rprimetot=1/float(Utotal)
Atot=(1-glazingfraction)*wallheight*perimeter

Qtot=Atot*Utotal*(Tin-Tout)
print("The value of the heat transfer rate loss is: " +str(Qtot) +" W")
