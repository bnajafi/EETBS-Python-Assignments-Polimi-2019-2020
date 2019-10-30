
#Dictionaries of every Resistance
R_i={"name":"inside surface", "type":"conv", "material":"InsideSurface"}
R_2={"name":"Wood bevel lapped Siding", "type":"cond", "material":"WoodLappedSiding", "length":0.013}
R_3={"name":"Wood fiberboard", "type":"cond", "material":"WoodFiberBoard", "length":0.013}
R_4={"name":"Glass fiber insulation", "type":"cond", "material":"GlassFiberInsulation", "length":0.09}
R_5={"name":"Wood studs", "type":"cond", "material":"WoodStud_90mm", "length":0.09}          
R_6={"name":"Gypsum Wallboard","type":"cond", "material":"Gypsum", "length":0.013}
R_o={"name":"Outside surface", "type":"conv", "material":"OutsideSurface"}

#There are in parallel: one passes through the wood stud 25% and the the other through the glass fiber 75%

import wallFunction_Panadero as David

#R_total_wood
#In serie this resistances R_i: I=i,2,3,4.a,5,o.

ResistanceList_withWood=[R_i,R_2,R_3,R_5,R_6,R_o]
RTotalwithWood=David.RValueUnitandTotal (ResistanceList_withWood) 

#R_total_glass
#In serie this resistances R_i: I=i,2,3,4.b,5,o. 

ResistanceList_withInsulation=[R_i,R_2,R_3,R_4,R_6,R_o]
RTotalwithInsulation=David.RValueUnitandTotal (ResistanceList_withInsulation)


#Utotal and Rtotal

U_wood=1/RTotalwithWood
U_insulation=1/RTotalwithInsulation
Utotal=0.25*U_wood+0.75*U_insulation

print("The total heat transfer coefficient is Utotal= "+str(Utotal))

Rtotal=1/Utotal
print("The total thermal resistance is Rtotal= "+str(Rtotal))

#Rate of heat loss through the walls

Area=50*2.5*0.8
T_1=22
T_2=-2
Q=Utotal*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q))
