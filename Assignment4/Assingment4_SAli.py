# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:27:31 2019

@author: sajid ali
"""
"""R1 = {"name":"R_inside","type":"conv","material": "insideSurface","length":1.0}   # length": 0.05
R2 = {"name":"R_outside","type":"Conv","material":"outsideSurfaceWinter","length":1.0}
R3 = {"name":"R_woodbevel","type":"Cond","material":"Wood bevel lapped siding","length":0.013}
R4 = {"name":"R_woodfiber","type":"cond","material": "Wood fiberboard","length":0.013}# length": 0.05
R5 = {"name":"R_glassfiber","type":"Cond","material":"Glass fiber insulation","length":0.090}
R6 = {"name":"R_woodstud","type":"Cond","material":"Wood stud","length":0.09}
R7 = {"name":"gypsum","type":"Cond","material":"Gypsum wallboard","length":0.013}
"""
from Assingment3_SAli import R1,R2,R3,R4,R5,R6,R7

import os
whereiamnow = os.getcwd()
print(whereiamnow)

whereiwanttogo =r"D:\cleanfolder\EETBS-Python-Assignments-Polimi-2019-2020\Assignment3"
os.chdir(whereiwanttogo)
##whereiamnow = os.getcwd()
##print(whereiamnow)
filesihave = os.listdir(whereiwanttogo)#### this function is list of files
print(filesihave)

from Assingment3_SAli import R1,R2,R3,R4,R5,R6,R7

importing the whole module and final answer is served
from Assingment3_SAli import *
Rlist = [R1,R2,R3,R4,R5,R6,R7]
print("the rate of heat loss through the walls of a house   "+str(Q_tot )+"  W") ###### my list of resistance(can see on the top)


##### importing module function in which include converting standard Rvalues to actual one ccoressponding to there actual length
# & caclulating the resistance with wood and resistance with insulatore
from Assingment3_SAli import ResitanceCalculatorWithLibrary
Rlist = [R1,R2,R3,R4,R5,R6,R7]
print(ResitanceCalculatorWithLibrary(Rlist))


