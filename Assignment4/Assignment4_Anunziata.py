# -*- coding: utf-8 -*-
import os
filelist=os.listdir(r"C:\Users\Angela\Desktop\Building Systems EEE\ASSIGNMENTS") #here insert directory
print('calledwallFunction_Anunziata.py' in filelist)

import calledwallFunction_Anunziata       
"""I could use also --> from calledwallFunction_Anunziata import RCFL <-- 
and later (see line 33,34)* I won't need to repeat calledwallFunction_Anunziata.RCFL but only RCFL"""

Routside= {"name":"Routside","type":"conv",
"material":"outside"}   
RWood_bevel_lapped = {"name":"Rwoodbevel","type":"cond", 
"material":"Wood_bevel_lapped","length":13}  
R13mm_fiberboard={"name":"Rfiberboard","type":"cond", 
"material":"13mm_fiberboard","length":13} 
RWood_studs={"name":"Rwoodstuds","type":"cond", 
"material":"Wood_studs","length":90} 
R13mm_Gypsum={"name":"Rgypsum","type":"cond", 
"material":"13mm_Gypsum","length":13} 
RGlass_Fiber_insulation={"name":"Rglassfiber","type":"cond", 
"material":"Glass_Fiber_insulation","length":90} 
Rinside={"name":"Rinside","type":"conv", 
"material":"Inside_Air","length":0.5} 

ResistanceListA = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RWood_studs, R13mm_Gypsum, Rinside] 
ResistanceListB = [Routside, RWood_bevel_lapped, R13mm_fiberboard, 
RGlass_Fiber_insulation, R13mm_Gypsum, Rinside]  

solA= calledwallFunction_Anunziata.RCFL(ResistanceListA)          
solB= calledwallFunction_Anunziata.RCFL(ResistanceListB)                           

"""*here I would have-->solA=RCFL(ResistanceListA)
                     -->solB=RCFL(ResistanceListB)"""
                                                                      
print ("Individual resistances for wood are "+str(solB[0:-1])+ " °C/W * m^2")        
print ("Individual resistances for insulation are "+str(solA[0:-1])+ " °C/W * m^2")        
print ("Rtot for wood is "+str(solA[-1])+ " °C/W * m^2")
print ("Rtot for insulation is "+str(solB[-1])+ " °C/W * m^2")

House={"Tin":22,"Tout":-2, 
"%WOOD":0.25,"%INSULATION":0.75,
"perimeter":50, "wall_height": 2.5,"%glazing":0.2} 

Utot=round((1/solA[-1]*House["%WOOD"]+1/solB[-1]*House["%INSULATION"]),4)
print ("Utot is "+str(Utot)+ " W")

Area_tot=House["perimeter"]*House["wall_height"]*(1-House["%glazing"])
Qtot=Utot*Area_tot*(House["Tin"]-House["Tout"])
print ("--> Qtot is "+str(Qtot)+ " W")