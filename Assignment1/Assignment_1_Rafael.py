#Assignment 1.

#Consider a 0.8m high and 1.5m wide double-pane window consisting of two 4mm
#thick layers of glass (kg=0.78 W/mC) separated by a 10mm-wide stagnat air space.
#(ka=0.026 W/mC). Determine the steady rate of heat transfer through this double 
#pane window and the temperature of its inner surface.

#Consider heat transfer coefficients on the inner and outer surfaces of the window
#to be h1=10 W/m2C and h2=40 W/m2C T(inside) = T0=20C and T(outside) = T1=-10C.

#We know that the heat transfer (Q) is equal to the difference of temperature 
#inside and outsite devided by the total Resistance (Rtot) -> Q = (T1-T2)/Rtot.

#We also know that Rtot is equal to the sum of all the resistances in the system,
#which are in series for this situation. Rconv = 1/(hA) and Rcond = L/(kA)
#Rtot = R inside + R(glass) + R(air gap) + Rglass + Routside;

L =[0.004, 0.01, 0.004] #List of length of glass and air gap

print ("The lengths of the layers are: "+str(L[0:])+"m")

A = 0.8*1.5 #Area

print ("The area A is equal to: "+str(A)+" m2")

k = [0.78, 0.026, 0.78] #list of heat transfer conductive coefficient
h = [10,40] #list of heat transfer convective coefficient

print ("The coeficients are: "+str(k[0:])+"(W/mC)"+" and "+str(h[0:])+"(W/m2C)")

Rcond = [L[0]/(A*k[0]), L[1]/(A*k[1]), L[2]/(A*k[2])] #list of Conductive Resistance

Rcond = [round(Rcond[0],5), round(Rcond[1],5), round(Rcond[2],5)]   #ROUND VALUES

print("The Conductive Resistance for glass and air are respectively: "+str(Rcond))

Rconv = [1/(h[0]*A),1/(h[1]*A)] #list of convective resistance

Rconv = [round(Rconv[0],5), round(Rconv[1],5)]

print("The Convective Resistance for heat transfer inside and outside are respectively: "+str(Rconv))

R = Rcond+Rconv #list of convective and conductive resistances

print ("The total resistance is the sum of Rcond and Rconv given in the following list: "+str(R))

R = R
Rtot = 0
for Sum in R:
    Rtot += Sum     #Soma de todos os valores em R

print("The Total Resistance is: Rtot = "+str(Rtot))

T = [20,-10] #Temperature inside T0 and outside T1
Q = (T[0] - T[1])/Rtot      #Heat Transfer coefficient
Q = round(Q,2)

print ("Thus, the steady rate of heat transfer (Q) through this double pane window is: Q = "+str(Q)+" W")

#Temperature of its inner surfaces T1, T2, T3 and T4.

R = [R[3],R[0],R[1],R[2],R[4]] #rearenge the values of R so it follows the heat transfer for the loop below

Tlist = [20,0,0,0,0,-10]  #list of Temperatures

Tlist[1] = Tlist[0]-Q*R[0]  #The equation for T[1] is different than the rest so comes out of the loop

#i=1
#for i in range(1,len(Tlist)):
    
 #   i=i
  #  Tlist[i+1] = -(Q*R[i])+Tlist[i]

   # if len(Tlist)>5:
    #    break

#print Tlist

n=0
for Temp in Tlist:      #Loop to put each value of T in the Tlist
    n = n+1
    Tlist[n+1] = -(Q*R[n])+Tlist[n]
    Tlist[n+2] = -(Q*R[n+1])+Tlist[n+1]
    Tlist[n+3] = -(Q*R[n+2])+Tlist[n+2]
    
    if len(Tlist)>5:
        break

Tlist = [round(Tlist[0],3),round(Tlist[1],3),round(Tlist[2],3),round(Tlist[3],3),round(Tlist[4],3),round(Tlist[5],3)]
print ("The Temperatures in each suface are respectively: "+str(Tlist)+" C")
    