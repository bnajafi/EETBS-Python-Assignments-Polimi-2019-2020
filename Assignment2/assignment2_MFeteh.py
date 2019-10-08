T_out=-2
T_in=22
delta_T=float(T_in-T_out)
A_tot=0.8*50*2.5
Resistances_wood={"R_outside":{"type":"conv","material":"outside air"},"R_wood_bevel":{"type":"cond","material":"wood bevel","length":200},"R_sheating":{"type":"cond"
    ,"material":"fiberboard","length":13},"R_wood_stud":{"type":"cond","material":"wood stud","length":90},
    "R_gypsum":{"type":"cond","material":"gypsum wallboard","length":13},"R_inside":{"type":"conv","material":"inside air"}}

Resistances_ins={"R_outside":{"type":"conv","material":"outside air"},"R_wood_bevel":{"type":"cond","material":"wood bevel","length":200},"R_sheating":{"type":"cond",
"material":"fiberboard","length":13},"R_glass_fiber":{"type":"cond","material":"glass fiber","length":90},
"R_gypsum":{"type":"cond","material":"gypsum wallboard","length":13},"R_inside":{"type":"conv","material":"inside air"}}

materials_dict_wood={"outside air":{"R_val":0.03},"wood bevel":{"length":200,"R_val":0.14},"fiberboard":{"length":13,"R_val":0.23},
"wood stud":{"length":90,"R_val":0.63},"gypsum wallboard":{"length":13,"R_val":0.079},"inside air":{"R_val":0.12}}

materials_dict_ins={"outside air":{"R_val":0.03},"wood bevel":{"length":200,"R_val":0.14},"fiberboard":{"length":13,"R_val":0.23},"glass fiber":{"length":90,"R_val":2.52},
"gypsum wallboard":{"length":13,"R_val":0.079},"inside air":{"R_val":0.12}}

R_wood=0

for anyR in Resistances_wood:
    if Resistances_wood[anyR]["type"]=="cond":
        if  Resistances_wood[anyR]["length"]==materials_dict_wood[Resistances_wood[anyR]["material"]]["length"]:
            R_val=materials_dict_wood[Resistances_wood[anyR]["material"]]["R_val"]                  
        else:
            R_val=float((materials_dict_wood[Resistances_wood[anyR]["material"]]["R_val"]*Resistances_wood[anyR]["length"]))/materials_dict_wood[Resistances_wood[anyR]["material"]]["length"]
    elif Resistances_wood[anyR]["type"]=="conv":
        R_val=materials_dict_wood[Resistances_wood[anyR]["material"]]["R_val"]
    R_wood=R_wood+R_val       
print(R_wood)
U_wood=1/float(R_wood)
print(U_wood)
R_ins=0
for anyRes in Resistances_ins:
    if Resistances_ins[anyRes]["type"]=="cond":
        if  Resistances_ins[anyRes]["length"]==materials_dict_ins[Resistances_ins[anyRes]["material"]]["length"]:
            R_val=materials_dict_ins[Resistances_ins[anyRes]["material"]]["R_val"]                  
        else:
            R_val=float((materials_dict_ins[Resistances_ins[anyRes]["material"]]["R_val"]*Resistances_ins[anyRes]["length"]))/materials_dict_ins[Resistances_ins[anyRes]["material"]]["length"]
    elif Resistances_ins[anyRes]["type"]=="conv":
        R_val=materials_dict_ins[Resistances_ins[anyRes]["material"]]["R_val"]
    R_ins=R_ins+R_val       
print(R_ins)
U_ins=1/float(R_ins)
print(U_ins)
U_tot=U_wood*0.25+U_ins*0.75
print("The value of U_tot is "+str(U_tot))
R_tot=1/float(U_tot)
print("The value of R'_tot is "+str(R_tot))
Q_tot=U_tot*A_tot*delta_T
print("The value of Q_tot is "+str(Q_tot)+" w")