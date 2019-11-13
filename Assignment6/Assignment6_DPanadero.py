# -*- coding: utf-8 -*-
#ASSIGNMENT 6:

#Matrix in Excel (PANDA)

import pandas as pd

#Library of Resistance values of each material
                
ThermalResDict_R = [0.12,0.14,0.23,0.7,0.63,0.079,0.03]
ThermalResDict_L = [None, 0.013, 0.013, 0.025, 0.09, 0.013, None]

#Lists of names of materials, types, length

R = ["R_i","R_1","R_2","R_3","R_4","R_5","R_o"]
resistance_names = ["inside surface","Wood bevel lapped Siding","Wood fiberboard","Glass fiber insulation","Wood studs","Gypsum Wallboard","Outside surface"]
resistance_types = ["conv","cond","cond","cond","cond","cond","conv"]
resistance_Length = [ None,0.013,0.013,0.09,0.09,0.013,None]

#Solutions of R, U, DT, HF, Q (Initialization)

R_Value= [0,0,0,0,0,0,0]
U_Value=[0,0,0,0,0,0,0]
U_Total=[0]
DT_heating =[0]
H_F = [0]
Q_Total=[0]

#List of lists
Resistances_list = [resistance_names,resistance_types,ThermalResDict_L,ThermalResDict_R,resistance_Length, R_Value, U_Value, U_Total,DT_heating,H_F,Q_Total]

#Data Frame with names, types, lengths, R, U, DT, HF, Q values
Resistance_Dataframe=pd.DataFrame (Resistances_list, index=["Layer's Names","Types","Length directory (m)","R directory (m2k/W)","Length (m)", "R Value (m2k/W)", "U Value (W/m2k)", "U total (W/m2k)", "Delta heating (ºC)", "Heating Factor W/m2","Q total (W)"], columns = R)
Resistance_Dataframe_2 = Resistance_Dataframe.transpose()

#Function for calculating the R unit Values

def RValueUnit(DataFrame):

    DataFrame.loc[DataFrame["Types"]=="conv","R Value (m2k/W)"] = DataFrame.loc[DataFrame["Types"]=="conv","R directory (m2k/W)"]
    DataFrame.loc[DataFrame["Types"]=="cond","R Value (m2k/W)"] =((DataFrame.loc[DataFrame["Types"]=="cond","Length (m)"])/(DataFrame.loc[DataFrame["Types"]=="cond","Length directory (m)"]))*DataFrame.loc[DataFrame["Types"]=="cond","R directory (m2k/W)"]
    DataFrame.loc[DataFrame["Types"]=="conv","U Value (W/m2k)"] = 1.0/DataFrame.loc[DataFrame["Types"]=="conv","R Value (m2k/W)"]
    DataFrame.loc[DataFrame["Types"]=="cond","U Value (W/m2k)"] =1.0/DataFrame.loc[DataFrame["Types"]=="cond","R Value (m2k/W)"]
    
    return(DataFrame)

ResistancesResults= RValueUnit(Resistance_Dataframe_2)

#There are in parallel: one passes through the wood stud 25% and the the other through the glass fiber 75%
  
#R_total_wood
#In serie this resistances R_i: I=i,2,3,4.a,5,o. Simply sum them. 

Rtotal_Wood= ResistancesResults.loc[ResistancesResults["Layer's Names"]!="Glass fiber insulation","R Value (m2k/W)"].sum()
print (" The R total with wood is "+str(Rtotal_Wood) +" m2k/W")

#R_total_glass
#In serie this resistances R_i: I=i,2,3,4.b,5,o. Simply sum them.

Rtotal_glass= ResistancesResults.loc[ResistancesResults["Layer's Names"]!="Wood studs","R Value (m2k/W)"].sum()
print (" The R total with glass fiber is "+str(Rtotal_glass) +" m2k/W")

#U total 
U_wood=1/Rtotal_Wood
U_insulation=1/Rtotal_glass
Utotal=0.25*U_wood+0.75*U_insulation

ResistancesResults.loc[ResistancesResults["Layer's Names"]=="inside surface","U total (W/m2k)"] = Utotal
print("The total heat transfer coefficient is Utotal= "+str(Utotal) +" W/m2k")

#Rate of heat loss through the walls Q

Area=50*2.5*0.8
T_1=22
T_2=-2

DeltaT_heating = T_1 - T_2
ResistancesResults.loc[ResistancesResults["Layer's Names"]=="inside surface","Delta heating (ºC)"] = DeltaT_heating
HF = Utotal*DeltaT_heating
ResistancesResults.loc[ResistancesResults["Layer's Names"]=="inside surface","Heating Factor W/m2"] = HF
Q=HF*Area
ResistancesResults.loc[ResistancesResults["Layer's Names"]=="inside surface","Q total (W)"] = Q
print("The rate of heat loss through the walls is Q= "+str(Q) +" W")

SOLUTION=ResistancesResults
print(SOLUTION)

#Export the solution to an excel file
import os
os.chdir(r"C:\Users\david\Desktop\ERASMUS\2_POLIMI\1_SEMESTER\Building Systems\3_My assignments")
SOLUTION.to_excel("Assignment6_DavidPanadero_Matrix.xlsx")




