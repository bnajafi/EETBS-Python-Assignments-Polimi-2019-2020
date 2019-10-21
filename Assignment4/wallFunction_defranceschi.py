# -*- coding: utf-8 -*-
#Wall Function
R1 = {"name":"R_out","type":"Conv","material":"Outside_air"}
R2 = {"name":"R_wood_b","type":"Cond","material":"Wood_bevel_lapped","thick":13}
R3 = {"name":"R_fiber","type":"Cond","material":"Fiberboard","thick":13}
R4 = {"name":"R_glass_fib","type":"Cond","material":"Glass_fib_insulation","thick":90}
R5 = {"name":"R_wood_s","type":"Cond","material":"Wood_studs","thick":90}
R6 = {"name":"R_gypsum","type":"Cond","material":"Gypsum","thick":13}
R7 = {"name":"R_in","type":"Conv","material":"Inside_air"}

ResistanceList = [R1,R2,R3,R4,R5,R6,R7]

def WoodResistanceCalculatorwithLibrary(ListofResistance):
    LibraryofMaterials = {"Outside_air":{"R":0.03}
    ,"Wood_bevel_lapped":{"R":0.14,"th":13}
    ,"Fiberboard":{"R":0.23,"th":13}
    ,"Glass_fib_insulation":{"R":0,"th":25}
    ,"Wood_studs":{"R":0.63,"th":90}
    ,"Gypsum":{"R":0.079,"th":13}
    ,"Inside_air":{"R":0.12}
    }
    
    R_tot_wood = 0
    R_value = []
    for anyR in ListofResistance:
        if (anyR["type"] == "Conv"):
            materialofanyR=LibraryofMaterials[anyR["material"]]
            Rval=materialofanyR["R"]
            R_value.append(Rval)
        elif (anyR["type"] == "Cond"):
            thicknessofanyR=anyR["thick"]
            materialofanyR=LibraryofMaterials[anyR["material"]]
            standardthicknessofanyR=materialofanyR["th"]
            standardresistanceofanyR=materialofanyR["R"]
            Rval=standardresistanceofanyR*thicknessofanyR/standardthicknessofanyR
            R_value.append(Rval)
        R_tot_wood = R_tot_wood+Rval
    R_value.append(R_tot_wood)
             
    return R_value
    
Rval_new_wood=WoodResistanceCalculatorwithLibrary(ResistanceList)
Rwood = Rval_new_wood[-1] 
print("The resistance values with wood are " + str(Rval_new_wood))
print("The total resistance value with wood is " + str(Rwood) + " °C/W")

def InsulationResistanceCalculatorwithLibrary(ListofInResistance):
    LibraryofMaterials = {"Outside_air":{"R":0.03}
    ,"Wood_bevel_lapped":{"R":0.14,"th":13}
    ,"Fiberboard":{"R":0.23,"th":13}
    ,"Glass_fib_insulation":{"R":0.7,"th":25}
    ,"Wood_studs":{"R":0,"th":90}
    ,"Gypsum":{"R":0.079,"th":13}
    ,"Inside_air":{"R":0.12}
    }
    
    R_tot_ins = 0
    R_value = []
    
    for anyR in ListofInResistance:
        if (anyR["type"] == "Conv"):
            materialofanyR=LibraryofMaterials[anyR["material"]]
            Rval=materialofanyR["R"]
            R_value.append(Rval)
        elif (anyR["type"] == "Cond"):
            thicknessofanyR=anyR["thick"]
            materialofanyR=LibraryofMaterials[anyR["material"]]
            standardthicknessofanyR=materialofanyR["th"]
            standardresistanceofanyR=materialofanyR["R"]
            Rval=standardresistanceofanyR*thicknessofanyR/standardthicknessofanyR
            R_value.append(Rval)
        R_tot_ins = R_tot_ins+Rval
    R_value.append(R_tot_ins)
    
    return R_value

Rval_new_ins=InsulationResistanceCalculatorwithLibrary(ResistanceList)
Rins=Rval_new_ins[-1]
print("The resistance values with insulation are " + str(Rval_new_ins))
print("The total resistance value with insulation is " + str(Rins) + " °C/W")

p = 50 #m
h = 2.5 #m

#20 % of the area is occupied by the glazing
A = p*h*0.8
U_wood = float(1)/Rwood
U_ins = float(1)/Rins

#The insulated cavity is 75% of the heat transfer area and the wood constitutes 25% of the heat transfer area
U_tot = 0.75*U_ins + 0.25*U_wood
print("U = " + str(U_tot) + " W/°Cm^2")

T_in = 22 #°C
T_out = -2 #°C

#Evaluation of the total heat transfer
Q = U_tot*(T_in-T_out)*A
print("Q = " + str(Q) + " W")


    
            


    