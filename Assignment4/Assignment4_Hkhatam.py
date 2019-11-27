#1 import module

import os
print(os.getcwd())
wall_function=r'C:\Users\Hamed\Dropbox\EETBS-Python-Assignments-Polimi-2019-2020\Assignment4'
os.chdir(wall_function)
print(os.getcwd())
print(os.listdir(wall_function))
import wallfunction_khatam
R1={"name":"R_out","type":"Conv","material":"outsideAir"}
R2={"name":"R_Woodbevel","type":"Cond","material": "Woodbevel","length": 0.013}
R3={"name":"R_fiberboard","type":"Cond","material": "fiberboard","length": 0.013}
R4={"name":"R_GlassFiberinsulation","type":"Cond","material": "GlassFiberinsulation","length": 0.09}
R5={"name":"R_Woodstuds","type":"Cond","material": "Woodstuds","length": 0.09}
R6={"name":"R_Gypsum","type":"Cond","material": "Gypsum","length": 0.013}
R7={"name":"R_InsideAir","type":"Conv","material": "InsideAir"}
#consider two lists resistanceList1 with Woodstuds, resistanceList2 with GlassFiberinsulation
resistanceList1=[R1,R2,R3,R5,R6,R7]
resistanceList2=[R1,R2,R3,R4,R6,R7]
Rtot_withwoodstud = 0
Rtot2_withGlassFiber = 0
for thisResistance in resistanceList1:
    Rtot_withwoodstud=Rtot_withwoodstud+wallfunction_khatam.R_calculator(thisResistance)
for thisResistance in resistanceList2:
    Rtot2_withGlassFiber=Rtot2_withGlassFiber+wallfunction_khatam.R_calculator(thisResistance)
print('The total resistance of wood part',str(Rtot_withwoodstud), 'C/W')
print('The total resistance with Insulation',str(Rtot2_withGlassFiber), 'C/W')
U_wood=1/Rtot_withwoodstud
U_insulation=1/Rtot2_withGlassFiber
U_tot=U_wood*0.25+U_insulation*0.75
Rtot=1/U_tot
print('The total resistance is ',str(Rtot),'C/W')
Atot=100
dt=24
Q_dot_tot=U_tot*Atot*dt
print('The rate of heat dissipated to the outside is ',str(Q_dot_tot), 'W')




#2 from module import a Function

import os
print(os.getcwd())
wall_function=r'C:\Users\Hamed\Dropbox\EETBS-Python-Assignments-Polimi-2019-2020\Assignment4'
os.chdir(wall_function)
print(os.getcwd())
print(os.listdir(wall_function))
from wallfunction_khatam import R_calculator
R1={"name":"R_out","type":"Conv","material":"outsideAir"}
R2={"name":"R_Woodbevel","type":"Cond","material": "Woodbevel","length": 0.013}
R3={"name":"R_fiberboard","type":"Cond","material": "fiberboard","length": 0.013}
R4={"name":"R_GlassFiberinsulation","type":"Cond","material": "GlassFiberinsulation","length": 0.09}
R5={"name":"R_Woodstuds","type":"Cond","material": "Woodstuds","length": 0.09}
R6={"name":"R_Gypsum","type":"Cond","material": "Gypsum","length": 0.013}
R7={"name":"R_InsideAir","type":"Conv","material": "InsideAir"}
#consider two lists resistanceList1 with Woodstuds, resistanceList2 with GlassFiberinsulation
resistanceList1=[R1,R2,R3,R5,R6,R7]
resistanceList2=[R1,R2,R3,R4,R6,R7]
Rtot_withwoodstud = 0
Rtot2_withGlassFiber = 0
for thisResistance in resistanceList1:
    Rtot_withwoodstud=Rtot_withwoodstud+R_calculator(thisResistance)
for thisResistance in resistanceList2:
    Rtot2_withGlassFiber=Rtot2_withGlassFiber+R_calculator(thisResistance)
print('The total resistance of wood part',str(Rtot_withwoodstud), 'C/W')
print('The total resistance with Insulation',str(Rtot2_withGlassFiber), 'C/W')
U_wood=1/Rtot_withwoodstud
U_insulation=1/Rtot2_withGlassFiber
U_tot=U_wood*0.25+U_insulation*0.75
Rtot=1/U_tot
print('The total resistance is ',str(Rtot),'C/W')
Atot=100
dt=24
Q_dot_tot=U_tot*Atot*dt
print('The rate of heat dissipated to the outside is ',str(Q_dot_tot), 'W')
