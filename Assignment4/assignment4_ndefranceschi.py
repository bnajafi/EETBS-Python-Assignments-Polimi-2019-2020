# -*- coding: utf-8 -*-
#Assignment 4

import os 
WhereIwas = os.getcwd()
WhereIwanttogo = r"C:\Users\Nicoletta\Dropbox\Python4ScientificComputing_Fundamentals\A 2019-2020"
os.chdir(WhereIwanttogo)
print(os.getcwd())
print(os.listdir(WhereIwanttogo))
filesIhave = os.listdir(WhereIwanttogo)
print(filesIhave)
print("wallFunction_defranceschi.py" in filesIhave)

import wallFunction_defranceschi
print(wallFunction_defranceschi.ResistanceList)


from wallFunction_defranceschi import ResistanceList
Rval_new_wood = WoodResistanceCalculatorwithLibrary(ResistanceList)
print(Rval_new_wood)
print(Rwood)

from wallFunction_defranceschi import ResistanceList
Rval_new_ins = InsulationResistanceCalculatorwithLibrary(ResistanceList)
print(Rval_new_ins)
print(Rins)
print("U = " + str(U_tot) + " W/°Cm^2")
print("Q = " + str(Q) + " W")



