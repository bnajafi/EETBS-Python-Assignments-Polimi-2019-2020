# Importing numpy

import numpy as np

Restot1 = np.zeros(7)
Restot2 = np.zeros(7)

Res1 = 0
Res2 = 0

res_names = np.array(["WoodStud", "GlassFiber", "Gypsum", "WoodFiber", "WoodBevel", "Inside", "Outside"])

madeOf = np.array(["case1", "case2", "case12", "case12","case12", "case12", "case12"])

list_type = ["cond", "cond", "cond", "cond", "cond", "conv", "conv"]
res_type = np.array(list_type)
res_tstd = np.array([1, 0.025, 0.013, 0.013, 1, 1, 1])
res_R = np.array([0.63, 0.7, 0.079, 0.23, 0.14, 0.12, 0.03])
res_t = np.array([1, 0.9, 0.13, 0.13, 1, 1, 1])

Restot1[(res_type == "conv")] = res_R[(res_type == "conv")]

#print(Restot1)

Restot1[(madeOf == "case1") | (madeOf == "case12") & (res_type == "cond")] 

Restot1[(madeOf == "case1") | (madeOf == "case12") & (res_type == "cond")] 

res_R[(madeOf == "case1") | (madeOf == "case12") & (res_type == "cond")]*res_t[(madeOf == "case1") | 
    (madeOf == "case12") & (res_type == "cond")]/res_tstd[(madeOf == "case1") | 
        (madeOf == "case12") & (res_type == "cond")]
 
Restot2[(res_type == "conv")] = res_R[(res_type == "conv")]

Restot2[(madeOf == "case2") | (madeOf == "case12") & (res_type == "cond")] = res_R[((madeOf == "case2") | (
            madeOf == "case12")) & (res_type == "cond")] * res_t[(madeOf == "case2") | (madeOf == "case12") & (
                res_type == "cond")] / res_tstd[((madeOf == "case2") | (madeOf == "case12")) & (res_type == "cond")]

Utot1=round(1.0/Restot1.sum(),2)
Utot2=round(1.0/Restot2.sum(),2)

Utot = 1/Utot1*.25+1/Utot2*.75

Atot = .8*50*2.5

Tin = 22

Tout = -2

Qtot = Utot*Atot*(Tin - Tout)

print Qtot
