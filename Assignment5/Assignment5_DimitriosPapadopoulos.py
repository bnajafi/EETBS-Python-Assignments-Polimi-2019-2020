#Assignment_5

names=np.array(["Routside","Rwood_bevel","Rwood_fiber_board","Rglass_fiber","Rwood_studs","Rgypsum","Rinside"]) #all layers
types=np.array(["conv","cond","cond","cond","cond","cond","conv"])
Rcond=np.array([None,0.14,0.23,0.7,0.63,0.079,None])
L=np.array([None,0.013,0.013,0.025,0.09,0.013,None])
Rconv=np.array([0.03,None,None,None,None,None,0.12])
x=raw_input("give me the lenght of the glass fiber insulation:" ) #the user will give 0.09, in different case the value might change

RealRvalues=np.zeros(7)
AllRnotconv=np.zeros(5)

RealRvalues[(names=="Rglass_fiber")]=((float(x))*Rcond[(names=="Rglass_fiber")])/L[(names=="Rglass_fiber")]
RealRvalues[(names!="Rglass_fiber")]=Rcond[(names!="Rglass_fiber")]
AllRnotconv=RealRvalues[types=="cond"]
allRconvention=AllRnotconv.sum() 
AllRnotCond=Rconv[types=="conv"]
allRconduction=AllRnotCond.sum()
TotalR=allRconvention+allRconduction
Rwood=TotalR-RealRvalues[(names=="Rglass_fiber")][0]
Rins=TotalR-RealRvalues[(names=="Rwood_studs")][0]

Atot = 50*2.5*0.8  
Awood = Atot*0.25    
Ains = Atot*0.75 
Uwood=1/Rwood
Uins=1/Rins
T1=22
T2=-2
Utot=(Uwood*Awood+Uins*Ains)/Atot
R_prime_tot=1/Utot
DeltaT=(T2-T1)
Qtot=Utot*Atot*DeltaT
Qtotal=(abs(Qtot))
print("the R conduction values for each layer are:"+ str(RealRvalues))
print("the R convection values for the inside and outside are"+ str(AllRnotCond))
Utot=(Uwood*Awood+Uins*Ains)/Atot
R_prime_tot=1/Utot
print ("the Utotal is"+ str(Utot))
print ("the R_prime_total is"+ str(R_prime_tot))
print ("the total heat transfer is:" +str(Qtotal)+ "Watt")