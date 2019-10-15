#library of fiber_glass' resistance value

outside_AirWinterDictionary = {"RValUnit":0.03}
wood_bevel_lapped_sidingDictionary = {"length": 0.013, "RValUnit":0.14}   # from "13x200" i take only 13 (mm) for length, because i suppose that 13 represents the thickness
wood_fiberboardDictionary = {"length": 0.013, "RValUnit":0.23}           
fiberGlassDictionary = {"length": 0.09, "RValUnit":2.52}                 # "90 mm wide cavity", so length of 90 mm, values already converted
woodStudDictionary = {"length":0.09, "RValUnit":0.63}                    # "90 mm wide cavity", so length of 90 mm
gypsumDictionary = {"length":0.013, "RValUnit":0.079}
inside_AirDictionary = {"RValUnit":0.12}



libraryOfMaterials= {"outside_AirWinter": outside_AirWinterDictionary,"wood_bevel_lapped_siding" : wood_bevel_lapped_sidingDictionary, 
                     "fiberGlass":fiberGlassDictionary, "wood_fiberboard": wood_fiberboardDictionary,"woodStud": woodStudDictionary, 
                     "gypsum" : gypsumDictionary, "inside_Air":inside_AirDictionary}

R1= ["R_outside_Air","conv",libraryOfMaterials["outside_AirWinter"]["RValUnit"]] 
R2= ["R_wood_bevel_lapped_siding","cond",libraryOfMaterials["wood_bevel_lapped_siding"]["RValUnit"]]
R3= ["R_wood_fiberboard","cond",libraryOfMaterials["wood_fiberboard"]["RValUnit"]]
R4= ["R_fiberGlass","cond", libraryOfMaterials["fiberGlass"]["RValUnit"]]
R5= ["R_woodStud","cond",libraryOfMaterials["woodStud"]["RValUnit"]]
R6= ["R_gypsum","cond",libraryOfMaterials["gypsum"]["RValUnit"]]
R7= ["R_inside_Air","conv",libraryOfMaterials["inside_Air"]["RValUnit"]]

R_woodstud = [R1[-1],R2[-1],R3[-1],R5[-1],R6[-1],R7[-1]]
R_fiberglass = [R1[-1],R2[-1],R3[-1],R4[-1],R6[-1],R7[-1]]

# calculations

print(R_woodstud)
print(R_fiberglass)

R_tot_woodstud = 0
R_tot_fiberglass = 0

for res in R_woodstud:
    R_tot_woodstud = R_tot_woodstud + res
U_woodstud = 1.0/float(R_tot_woodstud)
print(R_tot_woodstud)
print(U_woodstud)

for res in R_fiberglass:
    R_tot_fiberglass = R_tot_fiberglass + res
U_fiberglass = 1.0/float(R_tot_fiberglass)
print(R_tot_fiberglass)
print(U_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75
print(U_value)
R_value = 1.0/float(U_value)
print(R_value)

A_tot = 0.8*50*2.5
print(A_tot)

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)

