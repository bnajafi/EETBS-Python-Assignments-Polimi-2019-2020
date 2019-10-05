'''Assignmet 1 by Benjamin Traskunov'''
'''
h = (10,40)

a = float(1.2)

kg = float(.78)

kgap = float(0.026)

Lgap = float(0.01)

Lg = float(.004)

tinf1 = 20

tinf2 = -10

R1 = round(float (1/(h[0]*a)),2)

R2 = round(float (1/(h[1]*a)),2)

Rg = round((Lg/(kgap*a)),2)

Rgap = round((Lgap/(kgap*a)),2)

Rtot = round(float(Rgap+Rg*2+Rg+R1+R2),2)

print 'Here are the resulting resistances', R1,'R1,', R2, 'R2,', Rg, 'Rg,', Rgap, 'Rgap,', Rtot, 'Rtot, all in [C/W].'

print 'Now lets find the Q or heat flux through the window.'

Q = round(float ((tinf1-tinf2)/Rtot),2)

print 'Q is', Q , '[W].'

print ' Last thing to find is the T of the inside surface.'

Ts1 = round(float (tinf1-(Q*R1)),2)

print ' The value is ', Ts1, 'Degrees C.'
'''
''' 2nd attempt at assingment '''

R1 = ["Rint", "conv", 10, 1.2]

R2 = ["Rglass", "cond", .004, 0.78, 1.2]

R3 = ["Rgap", "cond", 0.01, 0.026, 1.2]

R4 = ["Rext", "conv", 40, 1.2]

'''We have two glass walls so R2 will be repeated 2 times'''

Rlist = [R1, R2, R2, R3, R4]

Rtot = 0

for item in Rlist:
    if item[1] == "cond":
        Rval = float(item[2]/(item[3]*item[4]))
        Rtot = Rtot + Rval
        item.append(Rval)
    elif item[1] == "conv":
        Rval = float(1.0 /(item[2]*item[3]))
        Rtot = Rtot + Rval
        item.append(Rval)
    
print "The total resistance is", Rtot, " degrees C per W."

Tinf1 = 20

Tinf2 = -10

Q = float((Tinf1 -Tinf2)/ Rtot)

print "The heat transfer rate is ", Q, " Watts."

Ts1 = float(Tinf1 - Q*R1[4]) 

print " The internal temperature of the glass is " , Ts1, "Deg C."

