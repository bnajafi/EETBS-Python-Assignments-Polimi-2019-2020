T_out=-2
T_in=22
delta_T=float(T_in-T_out)
A_tot=0.8*50*2.5
R_out={"R_outside":{"type":"conv","material":"outside air"}}
R_bevel={"R_wood_bevel":{"type":"cond","material":"wood bevel","length":200}}
R_sheating={"R_sheating":{"type":"cond","material":"fiberboard","length":13}}
R_studs={"R_wood_stud":{"type":"cond","material":"wood stud","length":90}}
R_gyps={"R_gypsum":{"type":"cond","material":"gypsum wallboard","length":13}}
R_in={"R_inside":{"type":"conv","material":"inside air"}}
R_glassfiber={"R_glass_fiber":{"type":"cond","material":"glass fiber","length":90}}
Reslist=[R_out,R_bevel,R_sheating,R_studs,R_gyps,R_glassfiber,R_in]
def ResCal(Ress):
    Results=[]
    R=0
    materials_dict={"outside air":{"R_val":0.03},"wood bevel":{"length":200,"R_val":0.14},"fiberboard":{"length":13,"R_val":0.23},
    "wood stud":{"length":90,"R_val":0.63},"glass fiber":{"length":90,"R_val":2.52},"gypsum wallboard":{"length":13,"R_val":0.079},"inside air":{"R_val":0.12}}
    for anyR in range(len(Ress)):
        for anyr in Ress[anyR]:
            if Ress[anyR][anyr]["type"]=="cond":
                if  Ress[anyR][anyr]["length"]==materials_dict[Ress[anyR][anyr]["material"]]["length"]:
                    R_val=materials_dict[Ress[anyR][anyr]["material"]]["R_val"]                  
                else:
                    R_val=float((materials_dict[Ress[anyR][anyr]["material"]]["R_val"]*Ress[anyR][anyr]["length"]))/materials_dict[Ress[anyR][anyr]["material"]]["length"]
            elif Ress[anyR][anyr]["type"]=="conv":
                    R_val=materials_dict[Ress[anyR][anyr]["material"]]["R_val"]
            R=R+R_val
    Results.append(R)
    return Results

#For R_wood Calculation
Reslist_wood=[R_out,R_bevel,R_sheating,R_studs,R_gyps,R_in]
R_wood=ResCal(Reslist_wood)
print("The value of R_wood is "+str(R_wood))

#For R_ins Calculation
Reslist_ins=[R_out,R_bevel,R_sheating,R_gyps,R_glassfiber,R_in]
R_ins=ResCal(Reslist_ins)
print("The value of R_ins is "+str(R_ins))

U_wood=1/float(R_wood[0])
print("The value of U_wood is "+str(U_wood))
U_ins=1/float(R_ins[0])
print("The value of U_ins is "+str(U_ins))
U_tot=U_wood*0.25+U_ins*0.75
print("The value of U_tot is "+str(U_tot))
R_tot=1/float(U_tot)
print("The value of R'_tot is "+str(R_tot))
Q_tot=U_tot*A_tot*delta_T
print("The value of Q_tot is "+str(Q_tot)+" w")