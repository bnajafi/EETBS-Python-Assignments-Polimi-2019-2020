# we notice that we cannot do the same operations of assignem

import numpy as np

outside_AirWinterDictionary = {"standard_length": 0, "RVal_standard":0.03}
wood_bevel_lapped_sidingDictionary = {"standard_length": 0.013, "RVal_standard":0.14}  
wood_fiberboardDictionary = {"standard_length": 0.013, "RVal_standard":0.23}           
fiberGlassDictionary = {"standard_length": 0.025, "RVal_standard":0.70}                
woodStudDictionary = {"standard_length":0.09, "RVal_standard":0.63}                    
gypsumDictionary = {"standard_length":0.013, "RVal_standard":0.079}
inside_AirDictionary = {"standard_length": 0, "RVal_standard":0.12}

Materials_standard = {"outside_air_winter": outside_AirWinterDictionary,
                        "wood_bevel_lapped_siding" : wood_bevel_lapped_sidingDictionary, 
                        "fiber_glass":fiberGlassDictionary, 
                        "wood_fiberboard": wood_fiberboardDictionary,
                        "wood_stud": woodStudDictionary, 
                        "gypsum" : gypsumDictionary, 
                        "inside_air_still":inside_AirDictionary}


RVal_standard = np.array([ Materials_standard["outside_air_winter"]["RVal_standard"], 
                           Materials_standard["wood_bevel_lapped_siding"]["RVal_standard"], 
                           Materials_standard["wood_fiberboard"]["RVal_standard"],
                           Materials_standard["fiber_glass"]["RVal_standard"], 
                           Materials_standard["wood_stud"]["RVal_standard"], 
                           Materials_standard["gypsum"]["RVal_standard"],
                           Materials_standard["inside_air_still"]["RVal_standard"]])
                           
length_standard = np.array([ Materials_standard["outside_air_winter"]["standard_length"], 
                           Materials_standard["wood_bevel_lapped_siding"]["standard_length"], 
                           Materials_standard["wood_fiberboard"]["standard_length"],
                           Materials_standard["fiber_glass"]["standard_length"], 
                           Materials_standard["wood_stud"]["standard_length"], 
                           Materials_standard["gypsum"]["standard_length"],
                           Materials_standard["inside_air_still"]["standard_length"]])
                           
R1 = {"name":"R_outside_Air","type":"conv", "material": "outside_air_winter", "length":0}
R2 = {"name":"R_wood_bevel_lapped_siding","type":"cond","material":"wood_bevel_lapped_siding","length":0.013}
R3 = {"name":"R_wood_fiberboard","type":"cond","material":"wood_fiberboard","length":0.013}
R4 = {"name":"R_fiber_glass","type":"cond","material":"fiber_glass","length":0.09}
R5 = {"name":"R_wood_stud","type":"cond","material":"wood_stud","length":0.09}  # different from 0.025
R6 = {"name":"R_gypsum","type":"cond","material":"gypsum","length":0.013}
R7 = {"name":"R_inside_Air","type":"conv", "material": "inside_air_still", "length":0}

R_names = np.array([R1["name"], R2["name"], R3["name"], R4["name"], R5["name"], R6["name"], R7["name"]])

R_type = np.array([R1["type"], R2["type"], R3["type"], R4["type"], R5["type"], R6["type"], R7["type"]])

R_length = np.array([R1["length"], R2["length"], R3["length"], R4["length"], R5["length"], R6["length"], R7["length"]])




R_real = np.zeros(7)

Rvalues_cond = RVal_standard[R_type == "cond"]*(R_length[R_type == "cond"]/length_standard[R_type == "cond"])

Rvalues_conv = RVal_standard[R_type == "conv"]

R_real[R_type == "cond"] = Rvalues_cond
R_real[R_type == "conv"] = Rvalues_conv


R_woodstud = np.array([R_real[0], R_real[1], R_real[2], R_real[4], R_real[5], R_real[6]])
print(R_woodstud)
R_fiberglass = np.array([R_real[0], R_real[1], R_real[2], R_real[3], R_real[5], R_real[6]])
print(R_fiberglass)

R_tot_woodstud = R_woodstud.sum()
print(R_tot_woodstud)
R_tot_fiberglass = R_fiberglass.sum()
print(R_tot_fiberglass)

# problem solving

U_woodstud = 1.0/float(R_tot_woodstud)
U_fiberglass = 1.0/float(R_tot_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75

R_value = 1.0/float(U_value)

A_tot = 0.8*50*2.5

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)






resistance_standard_names = np.array(["outside_air_winter",
                                      "wood_bevel_lapped_siding",
                                      "fiber_glass",])



A = [R1, R2, R3, R5, R6, R7]
B = [R1, R2, R3, R4, R6, R7]

R_woodstud = np.array(A)
R_fiberglass = np.array(B)

material_of_res4 = R4["material"]
print(material_of_res4)
C = Materials_standard["fiber_glass"]
print(C)

# X = Materials_aaaaaaaaaa["fiber_glass"]                   # this works: it will print the fiberGlassDictionary
# print(X)
                        
# Materials_standard = np.array(Materials_aaaaaaaaaa)       # but these DON'T work! Once we converted the library into a
# Y = Materials_standard["fiber_glass"]                     # numpy array we cannot do any more the same operations
# Z = Materials_standard[2]                                 # that we used to do with libraries!
# print(Y), print(Z)


# numpy_library = np.array(list(Materials_standard.items()))
# print(numpy_library)
# print(numpy_library[1][0])
# print(numpy_library[1][1]["RVal_standard"])


#matching = [s for s in numpy_library if "wood_bevel_lapped_siding" in s]
#print(matching[0][1]["RVal_standard"])



# new order; 0: inside_air, 1: gypsum, 2: fiber_glass, 3: wood_fiberboard, 4: wood_bevel, 5: wood_stud, 6: outside_air