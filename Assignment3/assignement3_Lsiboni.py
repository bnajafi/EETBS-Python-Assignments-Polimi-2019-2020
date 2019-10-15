outside_AirWinterDictionary = {"RVal_standard":0.03}
wood_bevel_lapped_sidingDictionary = {"standard_length": 0.013, "RVal_standard":0.14}  
wood_fiberboardDictionary = {"standard_length": 0.013, "RVal_standard":0.23}           
fiberGlassDictionary = {"standard_length": 0.025, "RVal_standard":0.70}                
woodStudDictionary = {"standard_length":0.09, "RVal_standard":0.63}                    
gypsumDictionary = {"standard_length":0.013, "RVal_standard":0.079}
inside_AirDictionary = {"RVal_standard":0.12}

Materials_standard = {"outside_air_winter": outside_AirWinterDictionary,
                        "wood_bevel_lapped_siding" : wood_bevel_lapped_sidingDictionary, 
                        "fiber_glass":fiberGlassDictionary, 
                        "wood_fiberboard": wood_fiberboardDictionary,
                        "wood_stud": woodStudDictionary, 
                        "gypsum" : gypsumDictionary, 
                        "inside_air_still":inside_AirDictionary}

# Let's take for example resistance R6. 
# We want to add, to this dictionary, the voice "R_val", and put inside the same standard value 0.079 that
# we can find in the library above: 
# Materials_standard { "gypsum" { "RVal_standard" } }
#
# So, when res = R6, we can create a new voice inside R6... we will have: R6 { "RVal" }
#
# We want to do:   R6 { "RVal" } = Materials_standard { "gypsum" { "RVal_standard" } }
#
# But the problem is that, on the the right side of the equation, we cannot write "gypsum" by hand, because
# the for cycle works AUTOMATICALLY, we cannot decide it.
# Therefore, since in this moment we have res = R6, what we can do is to write "gypsum" as an information taken
# exactly from res = R6.
# Therefore, R6 must already have the information "gypsum" inside himself... and that name taken from R6 must be
# exactly "gypsum", because it must match perfectly with the name we have in the library above.
#
# R6 { "RVal" } = Materials_standard { R6{"material"} { "RVal_standard" } }
#
# And the same of all other resistances "res": R3 must have inside itself the exact information "wood_fiberboard",
# and R4 must have inside itself the exact information "fiberGlass", etc etc.
#  
# All this only to say that: to make dictionaries communicate, names must be EXACTLY the same.

R1 = {"name":"R_outside_Air","type":"conv", "material": "outside_air_winter"}
R2 = {"name":"R_wood_bevel_lapped_siding","type":"cond","material":"wood_bevel_lapped_siding","ex1_length":0.013}
R3 = {"name":"R_wood_fiberboard","type":"cond","material":"wood_fiberboard","ex1_length":0.013}
R4 = {"name":"R_fiber_glass","type":"cond","material":"fiber_glass","ex1_length":0.09}
R5 = {"name":"R_wood_stud","type":"cond","material":"wood_stud","ex1_length":0.09}  # different from 0.025
R6 = {"name":"R_gypsum","type":"cond","material":"gypsum","ex1_length":0.013}
R7 = {"name":"R_inside_Air","type":"conv", "material": "inside_air_still"}

R_woodstud = [R1, R2, R3, R5, R6, R7]
R_fiberglass = [R1, R2, R3, R4, R6, R7]

################################################################################ # with a function

def MyFunction(x):

    R_tot = 0
    R_list = []

    # case of wood_stud

    for res in x:
        if res["type"] == "conv":
            material_of_res = res["material"]                                  # material_of_res = 1) outside_air_winter 2)inside_air_still
            res["R_value"] = Materials_standard[material_of_res]["RVal_standard"]
            #print(res["R_value"])
            R_list.append(res["R_value"])
            
        elif res["type"] == "cond":
            material_of_res = res["material"]                                  # material_of_res = 1) wood_bevel_lapped_siding 2)wood_fiberboard, etc etc
            res["R_value"] = float(Materials_standard[material_of_res]["RVal_standard"])*(res["ex1_length"] / Materials_standard[material_of_res]["standard_length"])
            #print(res["R_value"])
            R_list.append(res["R_value"])
        
        R_tot = R_tot + res["R_value"]
    
    return R_tot

R_tot_woodstud = MyFunction(R_woodstud)
print(R_tot_woodstud)
R_tot_fiberglass = MyFunction(R_fiberglass)
print(R_tot_fiberglass)

# problem solving

U_woodstud = 1.0/float(R_tot_woodstud)
U_fiberglass = 1.0/float(R_tot_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75

R_value = 1.0/float(U_value)

A_tot = 0.8*50*2.5

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)




############################################################################## without a function

R_tot_woodstudd = 0
R_tot_fiberglasss = 0

# case of wood_stud

for res in R_woodstud:
    if res["type"] == "conv":
        material_of_res = res["material"]                                  # material_of_res = 1) outside_air_winter 2)inside_air_still
        res["R_value"] = Materials_standard[material_of_res]["RVal_standard"]
        #print(res["R_value"])
        
    elif res["type"] == "cond":
        material_of_res = res["material"]                                  # material_of_res = 1) wood_bevel_lapped_siding 2)wood_fiberboard, etc etc
        res["R_value"] = float(Materials_standard[material_of_res]["RVal_standard"])*(res["ex1_length"] / Materials_standard[material_of_res]["standard_length"])
        #print(res["R_value"])
       
    R_tot_woodstudd = R_tot_woodstudd + res["R_value"]
print (R_tot_woodstudd)

# case of fiber_glass

for res in R_fiberglass:
    if res["type"] == "conv":
        material_of_res = res["material"]                                  # material_of_res = 1) outside_air_winter 2)inside_air_still
        res["R_value"] = Materials_standard[material_of_res]["RVal_standard"]
        #print(res["R_value"])
        
    elif res["type"] == "cond":
        material_of_res = res["material"]                                  # material_of_res = 1) wood_bevel_lapped_siding 2)wood_fiberboard, etc etc
        res["R_value"] = float(Materials_standard[material_of_res]["RVal_standard"])*(res["ex1_length"] / Materials_standard[material_of_res]["standard_length"])
        #print(res["R_value"])
       
    R_tot_fiberglasss = R_tot_fiberglasss + res["R_value"]
print (R_tot_fiberglasss)


# problem solving

U_woodstudd = 1.0/float(R_tot_woodstudd)
U_fiberglasss = 1.0/float(R_tot_fiberglasss)

U_valuee = U_woodstudd*0.25 + U_fiberglasss*0.75

R_valuee = 1.0/float(U_valuee)

A_tott = 0.8*50*2.5

Q_tott = U_valuee*A_tott*(22-(-2))
print(Q_tott)




