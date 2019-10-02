'''Assignmet 1 by Benjamin Traskunov'''

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

