#Example 1 Unit 1.2

# # Numpy, apart from all other features, provides us with the possibility of running our procedures using vectorized operations

#Calculate the overall unit thermal resistance (Rtotal) and overall heat transfer coefficient (Utotal)


#First, import numpy
import numpy as np

#DATA
#Library of Resistance values of each material
ThermalResDict={"GlassFiberInsulation":{"R":0.7,"length":0.025},
                "WoodStud_90mm":{"R":0.63,"length":0.09},
                "WoodFiberBoard":{"R":0.23,"length":0.013},
                "WoodLappedSiding":{"R":0.14,"length":0.013},
                "Gypsum":{"R":0.079,"length":0.013},
                "InsideSurface":{"R":0.12},
                "OutsideSurface":{"R":0.03},#WINTER
                }

#Dictionaries of every Resistance
R_i={"name":"inside surface", "type":"conv", "material":"InsideSurface"}
R_2={"name":"Wood bevel lapped Siding", "type":"cond", "material":"WoodLappedSiding", "length":0.013}
R_3={"name":"Wood fiberboard", "type":"cond", "material":"WoodFiberBoard", "length":0.013}
R_4={"name":"Glass fiber insulation", "type":"cond", "material":"GlassFiberInsulation", "length":0.09}
R_5={"name":"Wood studs", "type":"cond", "material":"WoodStud_90mm", "length":0.09}          
R_6={"name":"Gypsum Wallboard","type":"cond", "material":"Gypsum", "length":0.013}
R_o={"name":"Outside surface", "type":"conv", "material":"OutsideSurface"}

#VECTORS

#Library
                
ThermalResDict_R = np.array([0.12,0.14,0.23,0.7,0.63,0.079,0.03])
ThermalResDict_L = np.array([None, 0.013, 0.013, 0.025, 0.09, 0.013, None])

#Lists of names of materials, types, and length

resistance_names = np.array(["inside surface","Wood bevel lapped Siding","Wood fiberboard","Glass fiber insulation","Wood studs","Gypsum Wallboard","Outside surface"])
resistance_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
resistance_Length = np.array([ None,0.013,0.013,0.09,0.09,0.013,None])

#Parallel: Through the wood stud 25% and through the glass fiber 75%

#R_total_wood
#In serie this resistances R_i: I=i,2,3,4.a,5,o. Simply sum them.
list_withWood=np.array(["Yes","Yes","Yes","No","Yes","Yes","Yes"])

#Lists of Conv and Cond Resistances
ResistanceList_withWood=np.zeros(7) 

ResistanceList_withWood [(list_withWood=="Yes") & (resistance_types=="cond")]= (ThermalResDict_R[(list_withWood=="Yes") & (resistance_types=="cond")] * resistance_Length[(list_withWood=="Yes") & (resistance_types=="cond")])/ThermalResDict_L[(list_withWood=="Yes") & (resistance_types=="cond")]
ResistanceList_withWood [(list_withWood=="Yes") & (resistance_types=="conv")]= ThermalResDict_R[(list_withWood=="Yes") & (resistance_types=="conv")]
print ("ResistanceList_withWood =" +str(ResistanceList_withWood))

Rtotal_Wood = ResistanceList_withWood.sum() 
print (" The R total with wood is "+str(Rtotal_Wood) +" m2k/W")

#R_total_glass
#In serie this resistances R_i: I=i,2,3,4.b,5,o. Simply sum them.
list_withInsulation=np.array(["Yes","Yes","Yes","Yes","No","Yes","Yes"])

#Lists of Conv and Cond Resistances

ResistanceList_withInsulation=np.zeros(7)

ResistanceList_withInsulation [(list_withInsulation=="Yes") & (resistance_types=="cond")] = (ThermalResDict_R[(list_withInsulation=="Yes") & (resistance_types=="cond")] * resistance_Length[(list_withInsulation=="Yes") & (resistance_types=="cond")])/ThermalResDict_L[(list_withInsulation=="Yes") & (resistance_types=="cond")]
ResistanceList_withInsulation [(list_withInsulation=="Yes") & (resistance_types=="conv")]= ThermalResDict_R[(list_withInsulation=="Yes") & (resistance_types=="conv")]
print ("ResistanceList_withInsulation =" +str(ResistanceList_withInsulation))

Rtotal_glass = ResistanceList_withInsulation.sum() 
print (" The R total with glass fiber is "+str(Rtotal_glass) +" m2k/W")

#U total and R total
U_wood=1/Rtotal_Wood
U_insulation=1/Rtotal_glass
Utotal=np.round(0.25*U_wood+0.75*U_insulation,3)
print("The total heat transfer coefficient is Utotal= "+str(Utotal) +" W/m2k")
Rtotal=np.round(1/Utotal,3)
print("The total thermal resistance is Rtotal= "+str(Rtotal) +" m2k/W")

#Rate of heat loss through the walls Q

Area=50*2.5*0.8
T_1=22
T_2=-2

DeltaT_heating = T_1 - T_2
HF = Utotal*DeltaT_heating
Q=np.round(HF*Area,3)
print("The rate of heat loss through the walls is Q= "+str(Q) +" W")


