# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:40:50 2019

@author: sajid ali
"""
import pandas as pd
## with standard Runit values and standard length
'''materialLibrary={"Wood bevel lapped siding":{"Rvalue":0.14,"length":0.013},
    "Wood fiberboard":{"Rvalue":0.23,"length":0.013},
    "Glass fiber insulation":{"Rvalue":0.7,"length":0.025},
    "Wood stud":{"Rvalue":0.63,"length":0.090},
    "Gypsum wallboard":{"Rvalue":0.079,"length":0.013},
    "insideSurface":{"Rvalue":0.12,"length":1.0},"outsideSurfaceWinter":{"Rvalue":0.030,"length":1.0}}'''
R_in_list=["conv",None,None,0.12,0]
##R_in_list
R_out_list=["conv",None,None,0.030,0]
R_bevel_list=["cond",0.013,0.013,0.14,0]
R_fiber_list=["cond",0.013,0.013,0.23,0]
R_glass_list=["cond",0.090,0.025,0.7,0]
R_stud_list=["cond",0.09,0.09,0.63,0]
R_gypsum_list=["cond",0.013,0.013,0.079,0]
resistances_names=["R_in_list","R_out_list","R_bevel_list","R_fiber_list","R_glass_list","R_stud_list","R_gypsum_list"]
columns_names=["Resistance_type","given_L","stand_L","RValue_std","Rvalue"]
Resistances_DF=pd.DataFrame([R_in_list,R_out_list,R_bevel_list,R_fiber_list,R_glass_list,R_stud_list,R_gypsum_list],index=resistances_names, columns=columns_names)
Resistances_DF
### now converting standarad resistance to required one according to length
Resistances_DF.loc[Resistances_DF["Resistance_type"]=="conv","Rvalue"]= Resistances_DF["RValue_std"]
##Resistances_DF
Resistances_DF.loc[Resistances_DF["Resistance_type"]=="cond","Rvalue"]=(Resistances_DF["RValue_std"]*Resistances_DF["given_L"])/Resistances_DF["stand_L"]
Resistances_DF
R_total1 = Resistances_DF.loc[:,"Rvalue"]##### find resistance with wood stud
Res1 = R_total1.sum()
##print(Res1)
##Resistances_DF.loc["R_glass_list" ,"Rvalue"]
R_withstud=Res1 - Resistances_DF.loc["R_glass_list" ,"Rvalue"]
#print(R_withstud)

#### now find Resistance with fiber glass######################

R_total2 = Resistances_DF.loc[:,"Rvalue"]
Res2 = R_total2.sum()
##print(Res2)
##Resistances_DF.loc["R_stud_list" ,"Rvalue"]
R_withglassfiber=Res2- Resistances_DF.loc["R_stud_list" ,"Rvalue"]
##print(R_withglassfiber)

#### overall heat transfer coefficent ####
U_stud = 1/R_withstud
U_glassfiber = 1/R_withglassfiber

U_total = U_stud*0.25 + U_glassfiber*0.75
Area_tot = 100 ###m2
DT = 24 
Q_tot = U_total*Area_tot*DT
print(Q_tot)
rownames = ["U_stud","U_glassfiber","U_total","Area_tot","DT","Q_tot"]
final = pd.DataFrame([U_stud,U_glassfiber,U_total,Area_tot,DT,Q_tot],index=rownames)
final


import os
os.chdir(r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone")
os.getcwd()
Tablefolder = r"D:\energy engnering polimi stuff\smester 3\Energy building system\pythone"
FileName_resistance = "Assingment6_2.csv"
path_file_resistance = os.path.join(Tablefolder,FileName_resistance)
print(path_file_resistance)
Resistances_DF.to_csv(path_file_resistance)
final.to_csv(path_file_resistance)



    

