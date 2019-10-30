import numpy as np
resistance_names = np.array(["R_out","R_Woodbevel","R_fiberboard","R_GlassFiberinsulation","R_Woodstuds","R_Gypsum","R_InsideAir"])
resistance_types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
resistance_r = np.array([ 0.03,0.14,0.23,0.7,0.63,0.079,0.12]) #Resistance Standard value
resistance_L_ST = np.array([ None,0.013,0.013,0.025,0.09,0.013,None])#Resistance Standard Lenght
resistance_L = np.array([None,0.013,0.013,0.09,0.09,0.013,None])#Resistance lenght
resistance_RValues = np.zeros(7)
resistance_RValues[resistance_types=='cond']=resistance_r[resistance_types=='cond']*resistance_L[resistance_types=='cond']/resistance_L_ST[resistance_types=='cond']
resistance_RValues[resistance_types=='conv']=resistance_r[resistance_types=='conv']
print(resistance_RValues)
R_withwood=resistance_RValues.sum()-resistance_RValues[resistance_names=="R_GlassFiberinsulation"]
R_withinsulation=resistance_RValues.sum()-resistance_RValues[resistance_names=="R_Woodstuds"]
print('The resistance with woodstud is ',str(R_withwood),'C/W')
print('The resistance with R_GlassFiberinsulation is ',str(R_withinsulation),'C/W')
U_wood=1/R_withwood
U_insulation=1/R_withinsulation
U_tot=U_wood*0.25+U_insulation*0.75
Rtot=1/U_tot
print('The total resistance is ',str(Rtot),'C/W')
Atot=100
dt=24
Q_dot_tot=U_tot*Atot*dt
print('The rate of heat dissipated to the outside is ',str(Q_dot_tot), 'W')

