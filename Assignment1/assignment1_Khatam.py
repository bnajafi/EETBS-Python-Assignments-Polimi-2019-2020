area=0.8*1.5
# TEMPERATURES Temperatures[0]= external inf, Temperatures[1]= hot outer surface, Temperatures[2]=hot inner surface 
# TEMPERATURES Temperatures[3]=cold inner surface ,Temperatures[4]=cold outer surface, Temperatures[5]=internal inf 
Temperatures = [20.0,0.0,0.0,0.0,0.0,-10.0]
#Conduction Resistances [material, Type of Heat Transfer, lenght,Thermal conductivity, Area]
R1 = ["R_glass","cond",0.004, 0.78,area]
R2 = ["R_air","cond",0.01, 0.026,area]
#Convection Resistances [material, Type of Heat Transfer, convective heat transfer coefficient, Area]
R_internal = ["R_internal","conv",10,area]
R_external = ["R_external","conv",40,area]

Resist=[] #will contains all of resistances in a list

ResistancesList = [R_internal,R1,R2,R1,R_external]

R_total=0
# use for and if loop ti calculate resistances 
for anyResistance in ResistancesList:
    if anyResistance[1]=="cond":
        R_Value = float(anyResistance[2])/(anyResistance[3]*anyResistance[4])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
        Resist.append(R_Value)
    elif anyResistance[1]=="conv":
        R_Value  = 1/(anyResistance[2]*anyResistance[3])
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
        Resist.append(R_Value)
print(ResistancesList)
print("The resistance list inorder from outside to inside is "+str(Resist)+ "deg C/w")
print("The total resistance is "+str(R_total)+ "deg C/w")

#calculating rate of heat transfer Q_dot
Q_dot= float(Temperatures[0]-Temperatures[5])/R_total
print("The rate of heat transfered is "+str(Q_dot)+ "W")


#calculating Temperatures
i=0 # will be used as a counter 
for R in Resist:
    if i < len(Resist)-1:
        Temperatures[i+1]=Temperatures[i]-(Q_dot*Resist[i])#Q_dot=(1/R[i])*(T[i]-T[i+1]) so T[i+1]=T[i]-(Q_dot*R[i])
        i+=1
print("The final temperatures are: ",(Temperatures),"degC")
        

