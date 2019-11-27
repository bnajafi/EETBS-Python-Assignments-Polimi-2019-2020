# -*- coding: utf-8 -*-
#Assignment N°6 Exercise
import pandas as pd

#Importing part
import os
os.getcwd()
Loc2=r"C:\Users\Santi\Desktop\MoS Politecnico di Milano\3 Semestre\Building Systems"
os.chdir(Loc2)
os.getcwd()
Files=os.listdir(os.getcwd())
print("MatLib_delval.py" in Files)
print(resistances_DF)


#Adding the lengths for this case
RealLength1=pd.Series([1,0.013,0.013,0.09,0.013,0,1],index=resistances_DF.index)
RealLength2=pd.Series([1,0.013,0.013,0,0.013,0.09,1],index=resistances_DF.index)
#Checking
print(RealLength1)

RList=[RealLength1,RealLength2]
resistances_real=pd.DataFrame(RList,index=["Length Glass","Length Wood"])
resistances_real=resistances_real.T
print(resistances_real)

#Defining the function for pandas
def CalculRES(row1,row2):
    A=float(raw_input("Insert value of AREA:"))
    T1=float(raw_input("Insert inside temperature:"))
    T2=float(raw_input("Insert outside temperature:"))
    Res=row1["r"]
    Lengthst=row1["Lstandar"]
    L1=row2["Length Glass"]
    L2=row2["Length Wood"]
    resistances_DF["RValue1"]=Res*L1/Lengthst
    resistances_DF["RValue2"]=Res*L2/Lengthst
    Rtot=1.0/(0.75/resistances_DF.loc[:,"RValue1"].sum()+0.25/resistances_DF.loc[:,"RValue2"].sum())
    Utot=1.0/Rtot
    Qtot=Utot*A*(T1-T2)
    AnsList=[Rtot,Utot,Qtot]
    Result=pd.Series(AnsList,index=["Resistance","Heat Transfer Coefficient","Heat Transfer Rate"])
    return Result

#Solving the exercise
Result=CalculRES(resistances_DF,resistances_real)
Result=pd.DataFrame(Result,columns=["Total"])
Result=Result.T
print(Result)

#Uploading results to excel file
currentdir=os.getcwd()
fileName_exp= "ResistanceData_Sdelval.xlsx"
path_exp = os.path.join(currentdir,fileName_exp)
Result.to_excel(path_exp)
    
        
    
clear