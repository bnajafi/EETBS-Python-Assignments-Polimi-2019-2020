#Assignment #6 By Benjamin Traskunov

import pandas as pd
#First we create a matrix with all the information given to us .

#If material doesn't have a standard dimension, type 1 for Thick std and Thick

R1 = [.63,1,"cond",1,0]
R2 = [.7,0.025,"cond", .09,0]
R3 = [.079,0.013,"cond",.013,0]
R4 = [.23,0.013,"cond", .013,0]
R5 = [.14,1, "cond",1,0]
R6 = [.12,1, "conv",1,0]
R7 = [.03,1,"conv", 1,0]

#Materials =["WoodStud","GlassFiber","Gypsum","WoodFiber","Wood Bevel", "Inside", "Outside"]
#Info = ["resistance","Thick std","Type","Thick"]
MaterialData = [R1,R2,R3,R4,R5,R6,R7]

resistance_DF = pd.DataFrame(MaterialData,
index=["WoodStud","GlassFiber","Gypsum","WoodFiber","Wood Bevel", "Inside", "Outside"],
columns =["Resistance","Thick std","Type","Thick","R value"])

#print(resistance_DF) #Check if table is correct

resistance_DF.loc[resistance_DF.loc[:,"Type"] == "cond","R value"] = resistance_DF.loc[:,"Resistance"]*(resistance_DF.loc[:,"Thick"]/resistance_DF.loc[:,"Thick std"])
resistance_DF.loc[resistance_DF.loc[:,"Type"] == "conv","R value"] = resistance_DF.loc[:,"Resistance"]
print(resistance_DF)

import os
os.chdir(r"C:\Users\Class2018\OneDrive - Politecnico di Milano\Master Class Materials\Semester 3\Building Systems")
os.getcwd()

resistance_DF.to_excel("Resistance_Data.xlsx")

Rtot1 = resistance_DF["R value"].sum () - resistance_DF.loc["GlassFiber","R value"]
Rtot2 = resistance_DF["R value"].sum () - resistance_DF.loc["WoodStud","R value"]
print(Rtot1,Rtot2) #Check if Values is exist

Uins = 1/Rtot2
Uwood = 1/Rtot1

print(Uwood,Uins) # Check if values are the same

Utot = .25*Uwood +.75*Uins

print(Utot) #Final check of values

Rwall = 1/Utot

Atot = .8*50*2.5

Tin = 22

Tout = -2

Qtot = Utot*Atot*(Tin-Tout)

print("Here is the total heat flux", Qtot, ".")
