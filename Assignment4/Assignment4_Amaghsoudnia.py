# -*- coding: utf-8 -*-
#categories: A: with wood B: With Insulation
R1 = {"name":"R_wb","type":"Cond","material": "woodBevel","length": 0.013,"category":"A,B"}
R2 = {"name":"R_ws","type":"Cond","material": "woodStud","length": 0.09,"category":"A"}
R3 = {"name":"R_fb","type":"Cond","material": "fireboard","length": 0.013,"category":"A,B"}
R4 = {"name":"R_gf","type":"Cond","material": "glassFiber","length": 0.09,"category":"B"}
R5 = {"name":"R_gy","type":"Cond","material": "gypsum","length": 0.013,"category":"A,B"}
R6 = {"name":"R_int","type":"Conv","material":"inside"}
R7 = {"name":"R_out","type":"Conv","material":"outside"}
 
ResistanceList = [R1,R2,R3,R4,R5,R6,R7]

#This part calls the function in the format "import module"

import os 
print(os.getcwd())
codesdir='/home/arian/Dropbox/Behzad/Codes'
os.chdir(codesdir)
filesIhave  = os.listdir(codesdir)
print (filesIhave)
print('calledwallFunction_Amaghsoudnia.py' in filesIhave)
import calledwallFunction_Amaghsoudnia

RtotA=0
RtotB=0
for thisResistance in ResistanceList:
    if thisResistance["type"]=="Cond":
        if thisResistance["category"]=="A,B" :
            RtotA=RtotA+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
            RtotB=RtotB+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
        elif thisResistance["category"]=="A" :
            RtotA=RtotA+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
        else :
            RtotB=RtotB+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
    if thisResistance["type"]=="Conv":
        RtotA=RtotA+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
        RtotB=RtotB+calledwallFunction_Amaghsoudnia.local_R_calc(thisResistance)
print ("The valuse of total Resistance in °C/W and heat transfer in W are respectively as follows: ")
calledwallFunction_Amaghsoudnia.HT(RtotA,RtotB)        
 
#This part calls the function in the format "from module import aFunction"
 
import os 
print(os.getcwd())
codesdir='/home/arian/Dropbox/Behzad/Codes'
os.chdir(codesdir)
filesIhave  = os.listdir(codesdir)
print (filesIhave)
print('calledwallFunction_Amaghsoudnia.py' in filesIhave) 

from calledwallFunction_Amaghsoudnia import local_R_calc
RtotA=0
RtotB=0
for thisResistance in ResistanceList:
    if thisResistance["type"]=="Cond":
        if thisResistance["category"]=="A,B" :
            RtotA=RtotA+local_R_calc(thisResistance)
            RtotB=RtotB+local_R_calc(thisResistance)
        elif thisResistance["category"]=="A" :
            RtotA=RtotA+local_R_calc(thisResistance)
        else :
            RtotB=RtotB+local_R_calc(thisResistance)
    if thisResistance["type"]=="Conv":
        RtotA=RtotA+local_R_calc(thisResistance)
        RtotB=RtotB+local_R_calc(thisResistance)

from calledwallFunction_Amaghsoudnia import HT
print ("The valuse of total Resistance in °C/W and heat transfer in W are respectively as follows: ")
HT(RtotA,RtotB)   