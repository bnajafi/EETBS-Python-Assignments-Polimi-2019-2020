air_outside={"Rval":0.03,"lenght":1.0,"usage":1}
wood_bevel={"Rval":0.14,"lenght":0.013,"usage":1}
wood_fiber_board={"Rval":0.23,"lenght":0.013,"usage":1}
glass_fiber_insulation={"Rval":0.7,"lenght":0.025,"usage":"insulation"} #0.7*0.9/0.25
wood_studs={"Rval":0.63,"lenght":0.09,"usage":"support"}
gypsum={"Rval":0.079,"lenght":0.013,"usage":1}
air_inside={"Rval":0.12,"lenght":1.0,"usage":1}#THE LENGHT OF THE air/out/inside IS 1.0 BECAUSE WHEN IT'S MULTIPLIED GIVES THE SAME VALUE 

listofmaterials=[air_outside,wood_bevel,wood_fiber_board,glass_fiber_insulation,wood_studs,gypsum,air_inside]
x=raw_input("give me the lenght of the glass fiber insulation:" ) #the user will give 0.09, in different case the value might change


def Rcalculator(listofmaterials):
    RealR = []
    for anyR in listofmaterials:
    
            if  anyR["usage"]=="insulation": #replace the real value of the insulation with respect on the lenght
                    leng= anyR["lenght"]
                    Rval=anyR["Rval"]
                    R1=Rval*(float(x)/leng)
                    RealR.append(R1)
            else: #replace the real value of the rest materials as it is
                    R=anyR["Rval"]
                    RealR.append(R)
    return RealR

NewRvalues=Rcalculator(listofmaterials)

print ("The new R values calculated by the function are:" +str(NewRvalues))
sumofRnew=0
for anynewR in NewRvalues:
    sumofRnew=sumofRnew+anynewR

Rins=sumofRnew-NewRvalues[4]
print ("the Rins is " +str(Rins))

Rwood=sumofRnew-NewRvalues[3]
print ("the Rwood is" +str(Rwood))


Uwood=1/Rwood
Uins=1/Rins

Atot = 50*2.5*0.8  
Awood = Atot*0.25   
Ains = Atot*0.75     
Utot=(Uwood*Awood+Uins*Ains)/Atot
R_prime_tot=1/Utot

T1=raw_input("give the inside temp:" ) #the inside is 22deg.Celsius
T2=raw_input("give the outside temp:" ) #the outside is -2 deg.Celsius

T1=float(T1)
T2=float(T2)
DeltaT=(T2-T1)
Qtot=Utot*Atot*DeltaT
Qtotal=(abs(Qtot))
print ("the total heat tranfser, in W, is: " +str(Qtotal))
print ("the Rprime total, in W, is : " +str(R_prime_tot))
print ("the U total, in W, is : " +str(Utot))




