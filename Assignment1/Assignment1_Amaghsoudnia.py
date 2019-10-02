A = float
A=0.8*1.5
# Resistances cond : material,cond,L,K
R1 = ["R_glass","cond",0.004, 0.78]
R2 = ["R_air","cond",0.01,0.026]
# Resistances conv : material,conv,h
R_internal = ["R_internal","conv",10]
R_external = ["R_external","conv",40]
R_total = 0
# temperatures T inf hot,T1 surf hot ,T2 air hot ,T3 air cold ,T4 surf cold, T inf cold 
Temperatures = [20.0,0.0,0.0,0.0,0.0,-10.0]
ResistancesList = [R_internal,R1,R2,R1,R_external] 

for anyResistance in ResistancesList:
    if anyResistance[1]=="cond":
        R_Value = float(anyResistance[2])/(anyResistance[3]*A)
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
    elif anyResistance[1]=="conv":
        R_Value  = 1/(anyResistance[2]*A)
        R_total = R_total+R_Value
        anyResistance.append(R_Value)
        
print(ResistancesList)    

print("the total resistance is "+str(R_total)+ "degC/w")

Q_tot = float
Q_tot= (Temperatures[0]-Temperatures[5])/R_total
print("the total heat transfered is "+str(Q_tot)+ " Watts")

#To build the local resistances starting from left side to the needed point
R_local=[]
R=0
for anyResistance in ResistancesList:
    if anyResistance[1]=="cond":
        R=R+float(anyResistance[4])
        R_local.append(R)
    elif anyResistance[1]=="conv":
         R=R+float(anyResistance[3])
         R_local.append(R)


#print(R_local)         
count=0
# from left to right we have Q=(T_in_inf - T_i)/R-i so we have T_i = T_in_inf - Q*R_local
for anyResistance in ResistancesList:   
    if count < len(ResistancesList)-1:
        Temperatures[count+1] = float(Temperatures[0])-float(Q_tot)*float(R_local[count])
        count +=1
 
    
print(Temperatures)    

