# -*- coding: utf-8 -*-

#Assignment 5 by Arian Maghsoudnia

import numpy as np 

woodBevelDict = np.array({"length":0.013,"RValUnit":0.14})
woodStudDict = np.array({"length":0.09,"RValUnit":0.63})
fireboardDict=np.array({"length":0.013,"RValUnit":0.23})
glassFiberDict=np.array({"length":0.025,"RValUnit":0.7})
GypsumDict = np.array({"length":0.013,"RValUnit":0.079})
insideDict = np.array({"RValUnit":0.12})
outsideDict = np.array({"RValUnit":0.03})


libraryOfMaterials = np.array({ "woodBevel":woodBevelDict,"woodStud" : woodStudDict,"gypsum": GypsumDict,"fireboard":fireboardDict,"glassFiber":glassFiberDict, 
"inside":insideDict, "outside" :outsideDict})

#categories: A: with wood B: With Insulation
res_names = np.array(["R_wb","R_ws","R_fb","R_gf","R_gy","R_int","R_out"])
res_types = np.array(["cond","cond","cond","cond","cond","conv","conv"])
res_materials = np.array(["woodBevel","woodStud","fireboard","glassFiber","gypsum","inside","outside"])
res_lengths= np.array([0.013,0.09, 0.013,0.09, 0.013,None,None])
res_category=np.array(["A,B","A","A,B","B","A,B",None,None])
res_std_length=np.array([0.013,0.09, 0.013,0.025, 0.013,None,None])
res_std_value=np.array([0.14,0.63,0.23,0.7,0.079,0.12,0.03])

res_real = np.zeros(7)
res_real[res_types=="cond"] = res_std_value[res_types=="cond"]*res_lengths[res_types=="cond"]/res_std_length[res_types=="cond"]
res_real[res_types=="conv"] = res_std_value[res_types=="conv"]

res_real_a= np.zeros(7)
res_real_b= np.zeros(7)

### res_real_a = (res_real[res_category=="A"]) | (res_real[res_category=="B"])  *** for future attention : this doesn't work ***
res_real_a = res_real[(res_category=="A") | (res_category=="A,B") | (res_category==None)]
res_real_b = res_real[(res_category=="B") | (res_category=="A,B") | (res_category==None)]

RtotA=res_real_a.sum()
RtotB=res_real_b.sum()

U_wood=1/RtotA
U_ins=1/RtotB
U_tot=U_wood*0.25+U_ins*0.75
Rtot=1/U_tot
Atot=100
dt=24
Qtot=U_tot*Atot*dt

print("The total resistance is ",str(Rtot)," °C/W")
print("The rate of heat dissipation is ",str(Qtot), " W")
