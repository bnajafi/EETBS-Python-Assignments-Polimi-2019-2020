# -*- coding: utf-8 -*-
## Assignment 2

libraryOfMaterials = {"outside_air":{"R_value":0.03},
                      "wood_bevel_lapped":{"std_thick":13.0,"R_value":0.14},
                      "wood_fiberboards":{"std_thick":13.0,"R_value":0.23},
                      "glass_fiber_insulation":{"std_thick":25.0,"R_value":0.70},
                      "wood_stud":{"std_thick":90.0,"R_value":0.63},
                      "gypsum":{"std_thick":13.0,"R_value":0.079},
                      "inside_air":{"R_value":0.12}}
print(libraryOfMaterials)


                        ## Compute the overall unit thermal resistance (R_Value)

R1 = {"name":"R_out", "type": "conv","material":"outside_air","case":"AB"}
R2 = {"name":"R_gypsum","type":"cond","material":"gypsum","thickness":13.0,"case":"AB"}
R3 = {"name":"R_bevel","type":"cond","material":"wood_bevel_lapped","thickness":13.0,"case":"AB"}
R4 = {"name":"R_fiberboards","type":"cond","material":"wood_fiberboards","thickness":13.0,"case":"AB"}
R5 = {"name":"R_insulator","type":"cond","material":"glass_fiber_insulation","thickness":90.0,"case":"B"}
R6 = {"name":"R_stud","type":"cond","material":"wood_stud","thickness":90.0,"case":"A"}
R7 = {"name":"R_int","type":"conv","material":"inside_air","case":"AB"}
ResistanceList = [R1,R2,R3,R4,R5,R6,R7]
print(ResistanceList)



R_with_ins_real=0
R_A=0
R_AB=0
for anyR in ResistanceList:
    if anyR["case"]=="AB":    ##only wood and with insulation 
        material_anyR = anyR["material"]
        blabla=libraryOfMaterials[material_anyR]
        Rvalue_anyR = blabla["R_value"]
        anyR["R_val"]=Rvalue_anyR
        R_AB=R_AB+Rvalue_anyR
    elif anyR["case"]=="B":  ##only insulation
        material_anyR = anyR["material"]
        thick_anyR=anyR["thickness"] 
        blabla=libraryOfMaterials[material_anyR]
        standardThickOfthisMaterialInTheLibrary=blabla["std_thick"]
        standardRvalOfthisMaterialInTheLibrary=blabla["R_value"]
        RealRval=standardRvalOfthisMaterialInTheLibrary*thick_anyR/standardThickOfthisMaterialInTheLibrary
        print(RealRval)
        anyR["R_val"] = RealRval
        R_with_ins_real=R_with_ins_real+RealRval
    else:         ##only wood
        material_anyR = anyR["material"]
        blabla=libraryOfMaterials[material_anyR]
        Rvalue_A = blabla["R_value"]
        anyR["R_val"]=Rvalue_A
        R_A=R_A+Rvalue_A
      
        
R_with_wood= R_AB+R_A          
R_with_ins=R_with_wood + R_with_ins_real-R_A
        
print(ResistanceList)
print("The resistance of the wall assumed with complitely wood is: "+str(R_with_wood)+" m^2*(°C/W)")
print("The resistance of the wall when we have insulation is: "+str(R_with_ins)+" m^2*(°C/W)")  
print("The real insulation resistance with respect to the standard thickness is: "+str(R_with_ins_real)+" m^2*(°C/W)")            


"""1/R_tot =1/R_wood +1/R_ins            R′=R×A→R=R′/A
   A_tot/(R_tot′)=A_wood/R'_wood +A_ins/R′_ins →U=1/R′ → U_tot×A_tot=U_wood×A_wood+U_ins×A_ins
   → U_tot=U_wood×A_wood/A_tot +U_ins×A_ins/A_tot  """
        
               ## Determine the overall heat transfer coefficient (the U-factor)

  #  DATA
Atot = 0.8*50*2.5 #mm^2
Tin = 22 #°C
Tout = -2 #°C
deltaT=Tin-Tout

Uwood = 1.0/R_with_wood
Uinsulation =1.0/R_with_ins
Utot = Uwood*0.25 + Uinsulation*0.75
print("The overall heat transfer coefficient is: "+str(Utot)+" W/(m^2*°C)")

Rtot = 1.0/Utot
print("The overall resistance is: "+str(Rtot)+" W/(m^2*°C)")
Qtot=Utot*Atot*deltaT
print("The rate of heat loss through the wall is: "+str(Qtot)+" W")
