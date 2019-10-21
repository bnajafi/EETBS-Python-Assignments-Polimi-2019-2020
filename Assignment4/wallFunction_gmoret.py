def R_tot_calculator (resistance_list):
    """This function receives a list of resistances
    and calculates the individual and total resistance values. The last element
    of the output list is the total resistance"""
    
    Materials = {"Outside_Winter":0.03,
                "Inside":0.12,
                "Wood_Bevel_Lapped_Siding":{"std_th":13.0,"R_value":0.14},
                "Wood_Fiberboard":{"std_th":13.0,"R_value":0.23},
                "Wood_Stud":{"std_th":90.0,"R_value":0.63},
                "Gypsum":{"std_th":13.0,"R_value":0.079},
                "Glass_Fiber_Insulator":{"std_th":25.0,"R_value":0.70}}
    
    R_value_list = []
    R_tot = 0
    
    for Ri in resistance_list:
        
        if Ri["type"] == "conv":
            material_of_Ri = Ri["material"]
            R_value_of_Ri = Materials[material_of_Ri]
            R_value_list.append(R_value_of_Ri)
            
        
        elif Ri["type"] == "cond":
            thickness_of_Ri = Ri["thickness"]
            material_of_Ri = Ri["material"]
            sub_dictionary = Materials[material_of_Ri]
            std_thickness_of_this_material = sub_dictionary["std_th"]
            R_value_of_this_material = sub_dictionary["R_value"]
            R_value_of_Ri = float(R_value_of_this_material) * (thickness_of_Ri / std_thickness_of_this_material)
            R_value_list.append(R_value_of_Ri)
        
        R_tot = R_tot + R_value_of_Ri
    R_value_list.append(R_tot)
    
    return R_value_list 