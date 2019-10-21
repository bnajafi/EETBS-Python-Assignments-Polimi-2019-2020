#MODULE OS 
import os
whereIam=os.getcwd()
whereIwantToGo=r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems\assignments" 
os.chdir(whereIwantToGo)
print (os.getcwd())

from wallFunction_Papadopoulos import listofmaterials #the format "FROM ...IMPORT...." has been used
print listofmaterials

import wallFunction_Papadopoulos     #the format "IMPORT...." has been used  
results=wallFunction_Papadopoulos.Rcalculator(listofmaterials)             
print results
#since the whole file has been imported the script remains the same as the assignment 3!                                                           
print ("the total heat tranfser, in W, is: " +str(wallFunction_Papadopoulos.Qtotal))
print ("the Rprime total, in (degC/W)*m^2, is : " +str(wallFunction_Papadopoulos.R_prime_tot))
print ("the U total, in W/(degC*m^2), is : " +str(wallFunction_Papadopoulos.Utot)) #prints the already calculated results of the file "wallFuction_Papadopoulos"

