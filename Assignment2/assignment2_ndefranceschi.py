# -*- coding: utf-8 -*-
#Assignment 2
#Data
dict1 = {"Res_withwood":0.03,"Res_withinsulation":0.03}
dict2 = {"Res_withwood":0.14,"Res_withinsulation":0.14,"th":13}
dict3 = {"Res_withwood":0.23,"Res_withinsulation":0.23,"th":13}
dict4 = {"Res_withwood":0,"Res_withinsulation":0.7,"th":25}
dict5 = {"Res_withwood":0.63,"Res_withinsulation":0,"th":90}
dict6 = {"Res_withwood":0.079,"Res_withinsulation":0.079,"th":13}
dict7 = {"Res_withwood":0.12,"Res_withinsulation":0.12}
LibraryofMaterials = {"Outside_air":dict1,"Wood_bevel_lapped":dict2,"Fiberboard":dict3,"Glass_fib_insulation":dict4,"Wood_studs":dict5,"Gypsum":dict6,"Inside_air":dict7}
#print(LibraryofMaterials)

R1 = {"name":"R_out","type":"Conv","material":"Outside_air"}
R2 = {"name":"R_wood_b","type":"Cond","material":"Wood_bevel_lapped","thick":13}
R3 = {"name":"R_fiber","type":"Cond","material":"Fiberboard","thick":13}
R4 = {"name":"R_glass_fib","type":"Cond","material":"Glass_fib_insulation","thick":90}
R5 = {"name":"R_wood_s","type":"Cond","material":"Wood_studs","thick":90}
R6 = {"name":"R_gypsum","type":"Cond","material":"Gypsum","thick":13}
R7 = {"name":"R_in","type":"Conv","material":"Inside_air"}

ResistanceList = [R1,R2,R3,R4,R5,R6,R7]
R_tot_wood = 0
#print(ResistanceList)


for anyR in ResistanceList:
    if (anyR["type"] == "Conv"):
        materialofanyR=LibraryofMaterials[anyR["material"]]
        Rval=materialofanyR["Res_withwood"]
        print(Rval)
    elif (anyR["type"] == "Cond"):
        thicknessofanyR=anyR["thick"]
        materialofanyR=LibraryofMaterials[anyR["material"]]
        standardthicknessofanyR=materialofanyR["th"]
        standardresistanceofanyR=materialofanyR["Res_withwood"]
        Rval=standardresistanceofanyR*thicknessofanyR/standardthicknessofanyR
        print(Rval)
    R_tot_wood = R_tot_wood + Rval
print("The value of R_tot_with_wood is " + str(R_tot_wood) + " °Cm^2/W")
     
R_tot_ins = 0
for anyR in ResistanceList:
    if (anyR["type"] == "Conv"):
        materialofanyR=LibraryofMaterials[anyR["material"]]
        Rval=materialofanyR["Res_withinsulation"]
        print(Rval)
    elif (anyR["type"] == "Cond"):
        thicknessofanyR=anyR["thick"]
        materialofanyR=LibraryofMaterials[anyR["material"]]
        standardthicknessofanyR=materialofanyR["th"]
        standardresistanceofanyR=materialofanyR["Res_withinsulation"]
        Rval=standardresistanceofanyR*thicknessofanyR/standardthicknessofanyR
        print(Rval)
    R_tot_ins = R_tot_ins + Rval
print("The value of R_tot_with_insulation is " + str(R_tot_ins) + " °Cm^2/W")

p = 50 #m
h = 2.5 #m

#20 % of the area is occupied by the glazing
A = p*h*0.8
U_wood = float(1)/R_tot_wood
U_ins = float(1)/R_tot_ins

#The insulated cavity is 75% of the heat transfer area and the wood constitutes 25% of the heat transfer area
U_tot = 0.75*U_ins + 0.25*U_wood
print("U = " + str(U_tot) + " W/°Cm^2")

T_in = 22 #°C
T_out = -2 #°C

#Evaluation of the total heat transfer
Q = U_tot*(T_in-T_out)*A
print("Q = " + str(Q) + " W")



               
        
         
        
        
