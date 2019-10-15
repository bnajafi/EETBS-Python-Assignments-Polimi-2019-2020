# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:54:07 2019
Assingment NO. 3
@author: sajid ali 
"""

R1 = {"name":"R_inside","type":"conv","material": "insideSurface","length":1.0}   # length": 0.05
R2 = {"name":"R_outside","type":"Conv","material":"outsideSurfaceWinter","length":1.0}
R3 = {"name":"R_woodbevel","type":"Cond","material":"Wood bevel lapped siding","length":0.013}
R4 = {"name":"R_woodfiber","type":"cond","material": "Wood fiberboard","length":0.013}# length": 0.05
R5 = {"name":"R_glassfiber","type":"Cond","material":"Glass fiber insulation","length":0.090}
R6 = {"name":"R_woodstud","type":"Cond","material":"Wood stud","length":0.09}
R7 = {"name":"gypsum","type":"Cond","material":"Gypsum wallboard","length":0.013}

######## i def a fucuction to take a list of resistance(actual Resistance length) 
##and give back the R-Values coresponding to that resistance's length
#########and then add R values(Runitvalues) in existing List and return the whole list)

def ResitanceCalculatorWithLibrary(Rlist):
    materialLibrary={"Wood bevel lapped siding":{"Rvalue":0.14,"length":0.013},
    "Wood fiberboard":{"Rvalue":0.23,"length":0.013},
    "Glass fiber insulation":{"Rvalue":0.7,"length":0.025},
    "Wood stud":{"Rvalue":0.63,"length":0.090},
    "Gypsum wallboard":{"Rvalue":0.079,"length":0.013},
    "insideSurface":{"Rvalue":0.12,"length":1.0},"outsideSurfaceWinter":{"Rvalue":0.030,"length":1.0}}
    Rvalues = []
    for Res in Rlist:
        lengthofresistance = Res["length"] ### take required length value from R1.....R7
        #print(lengthofresistance)
        materialofthisresistance = Res["material"]### material
        fromlibrary = materialLibrary[materialofthisresistance]### take value of material form dictionary
        standardRtvalue = fromlibrary["Rvalue"]#### Rvalue for that material
        standardlength = fromlibrary["length"]### standard length from dictionary
        #print(standardRtvalue)
       # print(standardlength)
        requierdResistancematerial = (standardRtvalue)*(lengthofresistance)/standardlength
       ## print(requierdResistancematerial)
        Res["Runitvalue"] = requierdResistancematerial
        Rvalues.append(Res)
    R_withwood = [R1,R2,R3,R4,R6,R7]#### resistance list for woodstud
    R_withins = [R1,R2,R3,R4,R5,R7]###### resistance list for insulator
    Rwithwoodtotal = 0
    for Rwood in R_withwood:
        Rvaluewithwood = Rwood["Runitvalue"]
        Rwithwoodtotal =  Rwithwoodtotal + Rvaluewithwood
    print("Resistance with woodstud   "+str(Rwithwoodtotal)+"  C.m2/W")
    
############ to calculate total resistance with insulator
    Rwithinsulatortotal = 0
    for Rins in R_withins:
        Rvaluewithins = Rins["Runitvalue"]
        Rwithinsulatortotal = Rwithinsulatortotal + Rvaluewithins
    print("resistance with insulatore   "+str(Rwithinsulatortotal)+"  m2.C/W")
    
    R_total = [Rwithwoodtotal,Rwithinsulatortotal]
    return R_total
################################################################################
Rlist = [R1,R2,R3,R4,R5,R6,R7] ###### my list of resistance(can see on the top)
myeffectiveresults = ResitanceCalculatorWithLibrary(Rlist)######################
print(myeffectiveresults)#######################################################
#################################################################################


u_wood = 1/R_total[0] ### heat transfer coeeficient with wood stud
U_ins = 1/R_total[1]  ## heat transfer coeeficient with insulator
U_tot = u_wood*0.25+U_ins*0.75 
print("overall heat transfer coffient    "+str(U_tot)+ "   W/m^2/C")
R_tot = 1/U_tot
print("overall unit thermal resistance   "+str(R_tot)+"  m2.C/W")
Area_tot = 100 ###m2
DT = 24 
Q_tot = U_tot*Area_tot*DT
print("the rate of heat loss through the walls of a house   "+str(Q_tot )+"  W")
