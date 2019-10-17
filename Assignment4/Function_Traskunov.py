# Assignment 4 by Benjamin Traskunov

import os

print(os.getcwd())

"If your are in the correct, move on. If not, get to the folder which has the data for the assignment."

goto = r"C:\Users\Class2018\OneDrive - Politecnico di Milano\Master Class Materials\Semester 3\Building Systems\EETBS-Python-Assignments-Polimi-2019-2020\Assignment4"

os.chdir(goto)

# just in case we are not in the right place

print(os.chdir(goto))

print(os.getcwd())

print(os.listdir(goto))

# gives me a list of files in the folder

filesIhave = os.listdir(goto)

print('Function_Traskunov_Pt2.py' in filesIhave)

# if True we found the right file

from Function_Traskunov_Pt2 import *

Rult = 1/(1/RtotList[0] + 1/RtotList[1])

print(Rult)

Uins = 1/RtotList[1]

print(Uins)

Uwood = 1/RtotList[0]

print(Uwood)

Utot = Uwood*.25 + Uins*.75

print(Utot)

Rnewtot = 1/Utot

Atot = .8*50*2.5

Tin = 22

Tout = -2

Qtot = round(Utot*Atot*(Tin-Tout),2)

print("Here is the total heat flux", Qtot, ".")
