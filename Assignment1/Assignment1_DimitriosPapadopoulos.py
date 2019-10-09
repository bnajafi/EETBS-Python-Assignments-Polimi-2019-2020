#programm double pane window

Tout= float(raw_input("please insert the outside temperature in oC: "))
Tin= float(raw_input("please insert the inside temperature in oC: "))
A= float(raw_input("please insert the area in sq.meters: "))
hin=float(raw_input("please insert the inner heat transfer coefficient: "))
hout=float(raw_input("please insert the outer heat transfer coefficient: "))
xl=0.0
Rin=1/(hin*A)
Rout=1/(hout*A)
Rtotal=Rin+Rout

layers=[1,2,3]
for omega in layers:             #use the command "for"
    xl=float(raw_input("please insert 1 if it is glass or insert 2 if it air: "))
    x=int(xl)
    if x==1:                    #use the command "if" for the lists "Glass" and "Air"
        Lg= float(raw_input("please insert the glass lenght in meters: "))
        Glass=[0.78,Lg] #Glass[k,L]
        Rg=1
        Rg=Glass[1]/(Glass[0]*A)
        Rtotal=Rtotal+Rg
    elif x==2:
        Air=[0.026,1] #Air[k,L]
        La=float(raw_input("please insert the lenght of the air gap in meters: "))
        Air=[0.026,La]
        Ra=Air[1]/(Air[0]*A)
        Rtotal=Rtotal+Ra
    else:
        print("not valid value")
    
#end repetition

Rtotround=round(Rtotal,4)
print("the total resistance is" +str(Rtotround))
Q=(Tin-Tout)/Rtotal
Qround=round(Q,4)
print("the lost power in watt is " +str(Qround))
T1=-(Q*Rin)+Tin #condensation temperature
print("the indoor temperature of the first layer is" +str(T1))


T=[T1]
Rg=0.0043
Ra=0.3205
#No.temperatures(3+in+out)=No.layers+1(2+1+in+out)
layers=[1,2] #for the inbetween layers
for omega in layers: 
    xl=float(raw_input("please insert 1 if it is glass or insert 2 if it air: "))
    y=int(xl)
    if y==1:                    
        res=-Q*Rg+T[0]
        T.append(res)
        print("the next temp at the glass is"+ str(T)) 
    elif y==2:
        res=-Q*Ra+T[1]
        T.append(res)
        print("the next temp at the air gap is"+ str(T)) 
    else:
        print("not valid value")

T4=-Q*Rg+Tout #for the outside glass
T.append(T4)
print("the temperatures exept the in and out are as following" +str(T))






