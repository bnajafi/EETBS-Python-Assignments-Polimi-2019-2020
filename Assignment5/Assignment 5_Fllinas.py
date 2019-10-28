import numpy as np

R_standard_length = np.array([0,0.013,0.013,0.025,0.09,0.013,0])
R_standard_value =  np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
R_length = np.array([0,0.013,0.013,0.09,0.09,0.013,0])
R_type = np.array(["conv","cond","cond","cond","cond","cond","conv"])
R_in_wood=np.array([1,1,1,0,1,1,1])
R_in_insulation=np.array([1,1,1,1,0,1,1])

R_value=np.zeros(7)
R_value[R_type=="conv"]=R_standard_value[R_type=="conv"]
R_value[R_type=="cond"]=R_standard_value[R_type=="cond"]*R_length[R_type=="cond"]/R_standard_length[R_type=="cond"]

Rwithwood=np.zeros(7)
Rwithinsulation=np.zeros(7)

Rwithwood[R_in_wood==1]=R_value[R_in_wood==1]
Rwithinsulation[R_in_insulation==1]=R_value[R_in_insulation==1]

R_total_wood = np.sum(Rwithwood)
R_total_insulation = np.sum(Rwithinsulation)

print("The value of the total resistance with Wood studs is: " +str(R_total_wood) +" degC*m2/W")
print("The value of the total resistance with Insulation is: " +str(R_total_insulation) +" degC*m2/W")

fractionwood=0.25
fractioninsulation=1-fractionwood
perimeter=50
wallheight=2.5
glazingfraction=0.2

Tin=22
Tout=-2

Uwood=1/float(R_total_wood)
Uinsulation=1/float(R_total_insulation)

Utotal=Uwood*fractionwood+Uinsulation*fractioninsulation
print("The value of the total overall heat transfer coeficient is: " +str(Utotal) +" W/degC*m2")

Rprimetot=1/float(Utotal)
Atot=(1-glazingfraction)*wallheight*perimeter

Qtot=Atot*Utotal*(Tin-Tout)
print("The value of the heat transfer rate loss is: " +str(Qtot) +" W")
