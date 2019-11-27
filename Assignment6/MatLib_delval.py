# -*- coding: utf-8 -*-
#Assignment N°6 Material library
import pandas as pd

#Creating the library of materials
resistance_names=["Rout","Rwoodbps","Rwoodfs","Rglassf","Rgypsum","Rwoodst","Rin"]
resistances_types=["conv","cond","cond","cond","cond","cond","conv"]
resistances_r=[0.030,0.14,0.23,0.70,0.079,0.63,0.12]
resistances_Lstandar=[1,0.013,0.013,0.025,0.013,0.09,1]
resistances_RValues1=[0,0,0,0,0,0,0]
resistances_RValues2=[0,0,0,0,0,0,0]
resistance_listofLists=[resistances_types,resistances_r,resistances_Lstandar,resistances_RValues1,resistances_RValues2]
resistances_DF=pd.DataFrame(resistance_listofLists, index=["type","r","Lstandar","RValue1","RValue2"],columns =resistance_names)
resistances_DF=resistances_DF.T
print(resistances_DF)

clear