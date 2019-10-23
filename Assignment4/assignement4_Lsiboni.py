import os
import wallFunction_siboni

TheFolderWhereIhaveFunctions = r"C:\Users\lorenzo\Desktop\assignements Behzad"
os.chdir(TheFolderWhereIhaveFunctions)

R_woodstud = [wallFunction_siboni.R1, 
              wallFunction_siboni.R2, 
              wallFunction_siboni.R3, 
              wallFunction_siboni.R5, 
              wallFunction_siboni.R6, 
              wallFunction_siboni.R7]

R_fiberglass = [wallFunction_siboni.R1, 
                wallFunction_siboni.R2, 
                wallFunction_siboni.R3, 
                wallFunction_siboni.R4, 
                wallFunction_siboni.R6, 
                wallFunction_siboni.R7]
# i don't need to import the standard library of materials, the function uses it automatically

R_tot_woodstud = wallFunction_siboni.MyFunction(R_woodstud)
print(R_tot_woodstud)

R_tot_fiberglass = wallFunction_siboni.MyFunction(R_fiberglass)
print(R_tot_fiberglass)

U_woodstud = 1.0/float(R_tot_woodstud)
U_fiberglass = 1.0/float(R_tot_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75

R_value = 1.0/float(U_value)

A_tot = 0.8*50*2.5

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)

########################################### second version

import os
TheFolderWhereIhaveFunctions = r"C:\Users\lorenzo\Desktop\assignements Behzad"
os.chdir(TheFolderWhereIhaveFunctions)

from wallFunction_siboni import R1,R2,R3,R4,R5,R6,R7,MyFunction

R_woodstud = [R1, R2, R3, R5, R6, R7]
R_fiberglass = [R1, R2, R3, R4, R6, R7]

R_tot_woodstud = MyFunction(R_woodstud)
print(R_tot_woodstud)

R_tot_fiberglass = MyFunction(R_fiberglass)
print(R_tot_fiberglass)

U_woodstud = 1.0/float(R_tot_woodstud)
U_fiberglass = 1.0/float(R_tot_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75

R_value = 1.0/float(U_value)

A_tot = 0.8*50*2.5

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)
