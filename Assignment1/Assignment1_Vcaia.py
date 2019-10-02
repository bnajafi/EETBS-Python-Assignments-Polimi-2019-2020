# -*- coding: utf-8 -*-

#Assignment 1
#Heat loss through a double pane window

#We define the variables related to the area of the window
H = 0.8 #m
W = 1.5 #m
A = H*W
print("The area of the window is " +str(A) + " m^2")

#We define the outside and inside temperatures
Tin = 20 #deg C
Tout = -10 #deg C

layer1 = "glass 4 mm"
if layer1 == "glass 4 mm":
    k=0.78 #W/mC
    L=0.004 #m
    R1=L/(k*A) #°C/W
    print("The resistance value of the glass is " + str(R1) + " °C/W")
else:
    print("I don't have these material properties")
    
layer2 = "stagnant air 10 mm"
if layer2 == "stagnant air 10 mm":
    k=0.026 #W/mC
    L=0.01 #m
    R2=L/(k*A) #°C/W
    print("The resistance value of the gap is " + str(R2) + " °C/W")
else:
    print ("I don't have these material properties")
    
#We define the heat transfer coefficients of the inner and outer surfaces of the window
hin = 10 #W/m^2
hout = 40 #W/m^2
Rin = float(1)/(hin*A)
Rout = float(1)/(hout*A)
print("The resistance value of the inner surface is " + str(Rin) + "°C/W")
print("The resistance value of the outer surface is " + str(Rout) + "°C/W")

Rtot = 2*R1+R2+Rin+Rout
print("The total resistance value is " + str(Rtot) + " °C/W")

#We compute the steady rate of the heat transfer and the temperature of the inner surface
Q = (Tin-Tout)/Rtot
print("Q = " + str(Q) + " W")
Ts1 = Tin-(Q*Rin)
print("Ts1= " + str(Ts1) + " °C")




    

      
    
    