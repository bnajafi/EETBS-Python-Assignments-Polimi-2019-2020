#Importing pandas and operating system 
import pandas as pd
import os
#define resistances dictionary and list by their characteristics
R1={"name":"R_out","type":"Conv","material":"outsideAir","length": None}
R2={"name":"R_Woodbevel","type":"Cond","material": "Woodbevel","length": 0.013}
R3={"name":"R_fiberboard","type":"Cond","material": "fiberboard","length": 0.013}
R4={"name":"R_GlassFiberinsulation","type":"Cond","material": "GlassFiberinsulation","length": 0.09}
R5={"name":"R_Woodstuds","type":"Cond","material": "Woodstuds","length": 0.09}
R6={"name":"R_Gypsum","type":"Cond","material": "Gypsum","length": 0.013}
R7={"name":"R_InsideAir","type":"Conv","material": "InsideAir","length": None}

outsideAirDict={"length": None,'Rvalue':0.03}
WoodbevelDict={'length':0.013,'Rvalue':0.14}
fiberboardDict={'length':0.013,'Rvalue':0.23}
GlassFiberinsulationDict={'length':0.025,'Rvalue':0.7}
WoodstudsDict={'length':0.09,'Rvalue':0.63}
GypsumDict={'length':0.013,'Rvalue':0.079}
InsideAirDict={"length": None,'Rvalue':0.12}

Libraryofmaterials={'outsideAir':outsideAirDict,'Woodbevel':WoodbevelDict,'fiberboard':fiberboardDict,
'GlassFiberinsulation':GlassFiberinsulationDict,'Woodstuds':WoodstudsDict,'Gypsum':GypsumDict,'InsideAir':InsideAirDict}

resistanceList=[R1,R2,R3,R4,R5,R6,R7]
#Using Dataframe 
Resist_DF= pd.DataFrame (index=[],columns=["Names","Type","Material","Length","Std Length","Std Resist"])
#define function to  Enter the values of resistances in Dataframe 
i=1
def Resistances(resist,i):
    Resistances_DF=pd.DataFrame(index=[("R"+str(i))],columns=[])
    Resistances_DF["Names"]=resist["name"]
    Resistances_DF["Type"]=resist["type"]
    Resistances_DF["Material"]=resist["material"]
    Resistances_DF["Length"]=resist["length"]
    Resistances_DF["Std Length"]=Libraryofmaterials[resist["material"]]["length"]
    Resistances_DF["Std Resist"]=Libraryofmaterials[resist["material"]]["Rvalue"]
    return(Resistances_DF)
for resist in resistanceList:
    Resist_DF = Resist_DF.append(Resistances(resist,i))
    i=i+1 
#define two different resistances in row 
Resist_DF["Actual Resist"]=0
Resist_DF["Resistance with insulation"]=0
Resist_DF["Resistance with Woodstud"]=0

Resist_DF.loc[Resist_DF["Type"]=="Cond","Actual Resist"] = Resist_DF.loc[Resist_DF["Type"]=="Cond","Std Resist"]*Resist_DF.loc[Resist_DF["Type"]=="Cond","Length"]/Resist_DF.loc[Resist_DF["Type"]=="Cond","Std Length"]
Resist_DF.loc[Resist_DF["Type"]=="Conv","Actual Resist"] = Resist_DF.loc[Resist_DF["Type"]=="Conv","Std Resist"]
Resist_DF.loc[('R1','R2','R3','R4','R5','R6','R7'),"Resistance with insulation"] = Resist_DF.loc[('R1','R2','R3','R5','R6','R7'),"Actual Resist"]
Resist_DF.loc[('R1','R2','R3','R4','R5','R6','R7'),"Resistance with Woodstud"] = Resist_DF.loc[('R1','R2','R3','R4','R6','R7'),"Actual Resist"]

Rtot_withwoodstud=Resist_DF['Resistance with insulation'].sum()
Rtot_withGlassFiber=Resist_DF['Resistance with Woodstud'].sum()

print(Resist_DF)

U_wood=1/Rtot_withwoodstud
U_insulation=1/Rtot_withGlassFiber
U_tot=U_wood*0.25+U_insulation*0.75
Rtotal=1/U_tot
print('The total resistance is ',str(Rtotal),'C/W')
Atot=100
dt=24
Q_dot_tot=U_tot*Atot*dt
print('The rate of heat dissipated to the outside is ',str(Q_dot_tot), 'W')
a=os.getcwd()
print(a)
address=r'C:\Users\Hamed\Desktop\behzad assginment'
os.chdir(address)         
Resist_DF.to_excel("Excelfile.xlsx") 
