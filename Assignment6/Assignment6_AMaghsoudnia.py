# -*- coding: utf-8 -*-

#Assignment 6 by Arian Maghsoudnia
import pandas as pd
import os 

default_dir=os.getcwd()
 
woodBevelDict = {"length":0.013,"RValUnit":0.14}
woodStudDict = {"length":0.09,"RValUnit":0.63}
fireboardDict= {"length":0.013,"RValUnit":0.23}
glassFiberDict= {"length":0.025,"RValUnit":0.7}
GypsumDict = {"length":0.013,"RValUnit":0.079}
insideDict =  {"length":None,"RValUnit":0.12}
outsideDict = {"length":None,"RValUnit":0.03}
 
 
libraryOfMaterials = { "woodBevel":woodBevelDict,"woodStud" : woodStudDict,"gypsum": GypsumDict,"fireboard":fireboardDict,"glassFiber":glassFiberDict, 
"inside":insideDict, "outside" :outsideDict}
 
#categories: A: with wood B: With Insulation

R1 = {"name":"R_wb","type":"Cond","material": "woodBevel","length": 0.013,"category":"A,B"}
R2 = {"name":"R_ws","type":"Cond","material": "woodStud","length": 0.09,"category":"A"}
R3 = {"name":"R_fb","type":"Cond","material": "fireboard","length": 0.013,"category":"A,B"}
R4 = {"name":"R_gf","type":"Cond","material": "glassFiber","length": 0.09,"category":"B"}
R5 = {"name":"R_gy","type":"Cond","material": "gypsum","length": 0.013,"category":"A,B"}
R6 = {"name":"R_int","type":"Conv","material":"inside","length": None,"category":"NaN"}
R7 = {"name":"R_out","type":"Conv","material":"outside","length": None,"category":"NaN"}

res_list= [R1,R2,R3,R4,R5,R6,R7]
resDF= pd.DataFrame (index=[],columns=["Names","Type","Material","Length","Category","Standard Length","Standard Res"])


def lib_to_DF(R,i):
    df_thisRes=pd.DataFrame (index=[("R"+str(i))],columns=[])
    df_thisRes["Names"]=R["name"]
    df_thisRes["Type"]=R["type"]
    df_thisRes["Material"]=R["material"]
    df_thisRes["Length"]=R["length"]
    df_thisRes["Category"]=R["category"]
    df_thisRes["Standard Length"]=libraryOfMaterials[R["material"]]["length"]
    df_thisRes["Standard Res"]=libraryOfMaterials[R["material"]]["RValUnit"]               
    return(df_thisRes)
i=1
for R in res_list:
    resDF = resDF.append(lib_to_DF(R,i))
    i=i+1
resDF["Real Res"]=0
resDF["Res A"]=0
resDF["Res B"]=0

resDF.loc[resDF["Type"]=="Cond","Real Res"] = resDF.loc[resDF["Type"]=="Cond","Standard Res"]*resDF.loc[resDF["Type"]=="Cond","Length"]/resDF.loc[resDF["Type"]=="Cond","Standard Length"]
resDF.loc[resDF["Type"]=="Conv","Real Res"] = resDF.loc[resDF["Type"]=="Conv","Standard Res"]
logic_A=(resDF["Category"]=="A,B")|(resDF["Category"]=="A")|(resDF["Category"]=="NaN") 
logic_B=(resDF["Category"]=="A,B")|(resDF["Category"]=="B")|(resDF["Category"]=="NaN") 
resDF.loc[logic_A,"Res A"] = resDF.loc[logic_A,"Real Res"]
resDF.loc[logic_B,"Res B"] = resDF.loc[logic_B,"Real Res"]
resDFtrnsps= resDF.transpose()
resDFtrnsps["Sum"]=resDF.sum()
RtotA=resDFtrnsps.loc["Res A","Sum"]
RtotB=resDFtrnsps.loc["Res B","Sum"]
 
U_wood=1/RtotA
U_ins=1/RtotB
U_tot=U_wood*0.25+U_ins*0.75
Rtot=1/U_tot
Atot=100
dt=24
Qtot=U_tot*Atot*dt
 
print("The total resistance is ",str(Rtot)," °C/W")
print("The rate of heat dissipation is ",str(Qtot), " W")

current_dir = '/home/arian/Dropbox'
os.chdir(current_dir)
fileName = "output.xlsx"          
resDF.to_excel("output.xlsx")    


os.chdir(default_dir)