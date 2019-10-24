import numpy as np
T_out=-2
T_in=22
delta_T=float(T_in-T_out)
A_tot=0.8*50*2.5
Resistances_names_wood=np.array(["outside","wood bevel","sheating","wood stud","gypsum","inside"])
Resistances_type_wood=np.array(["conv","cond","cond","cond","cond","conv"])
Resistances_L_wood=np.array([None,200,13,90,13,None])
materials_wood_L=np.array([None,200,13,90,13,None])
Resistances_RValu_wood=np.array([0.03,0.14,0.23,0.63,0.079,0.12])
Resistances_names_ins=np.array(["outside","wood bevel","sheating","glass fiber","gypsum","inside"])
Resistances_type_ins=np.array(["conv","cond","cond","cond","cond","conv"])
Resistances_L_ins=np.array([None,200,13,90,13,None])
materials_ins_L=np.array([None,200,13,90,13,None])
Resistances_RValu_ins=np.array([0.03,0.14,0.23,2.52,0.079,0.12])
RValu_wood=np.zeros(6)
RValu_wood[Resistances_type_wood=="cond"]=Resistances_L_wood[Resistances_type_wood=="cond"]*Resistances_RValu_wood[Resistances_type_wood=="cond"]/materials_wood_L[
    Resistances_type_wood=="cond"]
RValu_wood[Resistances_type_wood=="conv"]=Resistances_RValu_wood[Resistances_type_wood=="conv"]
print(RValu_wood)
RValu_ins=np.zeros(6)
RValu_ins[Resistances_type_ins=="cond"]=Resistances_L_ins[Resistances_type_ins=="cond"]*Resistances_RValu_ins[Resistances_type_ins=="cond"]/materials_ins_L[
    Resistances_type_ins=="cond"]
RValu_ins[Resistances_type_ins=="conv"]=Resistances_RValu_ins[Resistances_type_ins=="conv"]
print(RValu_ins)
U_wood=1/RValu_wood.sum()
print("The value of U_wood = "+str(U_wood))
U_ins=1/RValu_ins.sum()
print("The value of U_ins = "+str(U_ins))
U_tot=U_wood*0.25+U_ins*0.75
print("The value of U_tot = "+str(U_tot))
R_tot=1/U_tot
print("The value of R'_tot = "+str(R_tot))
Q_tot=U_tot*A_tot*delta_T
print("The value of Q_tot = "+str(Q_tot)+" w")