air_outside={"type":"conv","Rval":0.03,"lenght":1.0,"usage":1}
wood_bevel={"type":"cond","Rval":0.14,"lenght":0.09,"usage":1}
wood_fiber_board={"type":"cond","Rval":0.23,"lenght":1.2,"usage":1}
glass_fiber_insulation={"type":"cond","Rval":0.7,"lenght":0.025,"usage":"insulation"} #0.7*0.9/0.25
wood_studs={"type":"cond","Rval":0.63,"lenght":0.09,"usage":"support"}
gypsum={"type":"cond","Rval":0.079,"lenght":0.013,"usage":1}
air_inside={"type":"conv","Rval":0.12,"lenght":1.0,"usage":1}

libraryofmaterials= {"air_outside":air_outside, "wood_bevel":wood_bevel,"wood_fiber_board":wood_fiber_board, "wood_studs":wood_studs,"glass_fiber_insulation":glass_fiber_insulation, "gypsum":gypsum, "air_inside":air_inside,}

listofmaterials=[air_outside,wood_bevel,wood_fiber_board,glass_fiber_insulation,wood_studs,gypsum,air_inside]


x=raw_input("give me the lenght of the glass fiber insulation:" ) #the user will give 0.09, in different case the value might change

Rdif=0
Rins=0


for anyR in listofmaterials:

        if  anyR["type"]=="cond" and anyR["usage"]=="insulation": #replace the real value of the insulation with respect on the lenght
                leng= anyR["lenght"]
                Rval=anyR["Rval"]
                R1=Rval*(float(x)/leng)
                anyR["Rval"]=R1
        elif anyR["type"]=="cond" and anyR["usage"]=="support": #replace the real value of the support with respect on the lenght
                leng= anyR["lenght"]
                Rval=anyR["Rval"]
                R2=Rval*(float(x)/leng)
                anyR["Rval"]=R2
        else:
            Rdif=Rdif+anyR["Rval"]
Rwood=Rdif+R2
Rins=Rdif+R1

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

