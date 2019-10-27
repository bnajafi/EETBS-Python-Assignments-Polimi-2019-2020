# -*- coding: utf-8 -*-
import numpy as np
resistance_names = np.array(["Routside","RWood_bevel_lapped","R13mm_fiberboard","RWood_studs","R13mm_Gypsum","RGlass_Fiber_insulation","Rinside"])
resistance_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
resistance_L = np.array([ 0, 13 ,13 ,90,13 ,90 ,0])
resistance_L_std = np.array([ 0, 13, 13, 90, 13, 25,0])
resistance_R_std = np.array([ 0.03, 0.14, 0.23, 0.63, 0.079, 0.7, 0.12])
resistance_list = np.array([ "both_conv","both","both","wood","both","insulation","both_conv"])

resistance_RValues_wood=np.zeros(7)
resistance_RValues_ins=np.zeros(7)

resistance_RValues_wood[((resistance_list=="both")|(resistance_list=="wood"))&(resistance_types=="cond")] = resistance_R_std[((resistance_list=="both")|(resistance_list=="wood"))&(resistance_types=="cond")] * resistance_L[(resistance_list=="both")|(resistance_list=="wood")&(resistance_types=="cond")] / resistance_L_std[((resistance_list=="both")|(resistance_list=="wood"))&(resistance_types=="cond")]      
resistance_RValues_wood[(resistance_types=="conv")] = resistance_R_std[(resistance_types=="conv")]

resistance_RValues_ins[((resistance_list=="both")|(resistance_list=="insulation"))&(resistance_types=="cond")] = resistance_R_std[((resistance_list=="both")|(resistance_list=="insulation"))&(resistance_types=="cond")] * resistance_L[(resistance_list=="both")|(resistance_list=="insulation")&(resistance_types=="cond")] / resistance_L_std[((resistance_list=="both")|(resistance_list=="insulation"))&(resistance_types=="cond")]      
resistance_RValues_ins[(resistance_types=="conv")] = resistance_R_std[(resistance_types=="conv")]

print ("Rwood: "+str(resistance_RValues_wood[(resistance_list!="insulation")]))
print ("Rinsulation: "+str(resistance_RValues_ins[(resistance_list!="wood")]))       
print ("Rtot for wood is "+str(resistance_RValues_wood.sum())+ " °C/W * m^2")
print ("Rtot for insulation is "+str(resistance_RValues_ins.sum())+ " °C/W * m^2")
print ("Utot for wood is "+str(round(1.0/resistance_RValues_wood.sum(),2))+ " W/°C/m^2")
print ("Utot for insulation is "+str(round(1.0/resistance_RValues_ins.sum(),2))+ " W/°C/m^2")

HouseData={"Tin":22,"Tout":-2, 
"%WOOD":0.25,"%INSULATION":0.75,
"perimeter":50, "wall_height": 2.5,"%glazing":0.2} 

Utot=round((1.0/resistance_RValues_wood.sum())*HouseData["%WOOD"]+(1.0/resistance_RValues_ins.sum())*HouseData["%INSULATION"],4)
Area_tot=HouseData["perimeter"]*HouseData["wall_height"]*(1-HouseData["%glazing"])
Qtot=Utot*Area_tot*(HouseData["Tin"]-HouseData["Tout"])
print ("Utot is "+str(Utot)+ " W/°C/m^2")
print ("Qtot is "+str(Qtot)+ " W")