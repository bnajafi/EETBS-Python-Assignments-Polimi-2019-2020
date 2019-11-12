import pandas as pd
resistance_names=["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"]
names=["air_out","wood_bevel","wood_fiber_board","glass_fiber_insulation","wood_studs","gypsum","air_in","total","wood","ins"]
Type=["conv","cond","cond","cond","cond","cond","conv","total","wood","ins"]
R_val=[0.03,0.14,0.23,0.7,0.63,0.079,0.12,0,0,0]
L=[None,0.013,0.013,0.025,0.09,0.013,None,None]
Rvalues=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
Uvalues=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
A=[None,None,None,None,None,None,None,100.0,25.0,75.0]
Temp_in_C=[-2.0,None,None,None,None,None,22.0,None,None,None]
Rprime=[None,None,None,None,None,None,None,0.0,None,None]
Utotal=[None,None,None,None,None,None,None,0.0,None,None]
Q_inW=[None,None,None,None,None,None,None,0.0,0.0,0.0,]

ListsofLists=[names,Type,R_val,L,Rvalues,Uvalues,A,Temp_in_C,Rprime,Utotal,Q_inW]
#Assignment goal: solve assignment 3 by creating a function that reads from library of materials and exporting the final results to an excel file
def exercise3(ListsofLists): 
    import os 
    os.chdir (r"C:\Users\upatr\Desktop\polimi\1st semester\building_systems")
    os.getcwd()
    resistances_DF=pd.DataFrame(ListsofLists,index=["name","Type","R_val","L","Rvalues","Uvalues","A","Temp_in_C","Rprime","Utotal","Q_inW"],columns=resistance_names)
    resistances_DF2=resistances_DF.transpose()
    resistances_DF2["Rvalues"][resistances_DF2["Type"]=="conv"]=resistances_DF2["R_val"][resistances_DF2["Type"]=="conv"]
    resistances_DF2["Rvalues"][resistances_DF2["Type"]=="cond"]=resistances_DF2["R_val"][resistances_DF2["Type"]=="cond"]
    resistances_DF2["Rvalues"][resistances_DF2["name"]=="glass_fiber_insulation"]=((resistances_DF2["R_val"][resistances_DF2["name"]=="glass_fiber_insulation"])*0.09)/resistances_DF2["L"][resistances_DF2["name"]=="glass_fiber_insulation"]
    g=resistances_DF2.iloc[:,4]
    resistances_DF2["Rvalues"][resistances_DF2["name"]=="total"]=float(g.sum())
    resistances_DF2["Rvalues"][resistances_DF2["Type"]=="wood"]=float((resistances_DF2["Rvalues"][resistances_DF2["name"]=="total"]))-float((resistances_DF2["Rvalues"][resistances_DF2["name"]=="glass_fiber_insulation"]))
    resistances_DF2["Rvalues"][resistances_DF2["Type"]=="ins"]=float((resistances_DF2["Rvalues"][resistances_DF2["name"]=="total"]))-float((resistances_DF2["Rvalues"][resistances_DF2["name"]=="wood_studs"]))
    resistances_DF2["Uvalues"]=1.0/resistances_DF2["Rvalues"]
    resistances_DF2["Utotal"][resistances_DF2["Type"]=="total"]=(float(resistances_DF2["Uvalues"][resistances_DF2["Type"]=="wood"])*float(resistances_DF2["A"][resistances_DF2["Type"]=="wood"])+float(resistances_DF2["Uvalues"][resistances_DF2["Type"]=="ins"])*float(resistances_DF2["A"][resistances_DF2["Type"]=="ins"]))/float(resistances_DF2["A"][resistances_DF2["Type"]=="total"])
    resistances_DF2["Rprime"]=1.0/resistances_DF2["Utotal"]
    resistances_DF2["Q_inW"][resistances_DF2["name"]=="total"]=float(resistances_DF2["Utotal"][resistances_DF2["name"]=="total"])*float(resistances_DF2["A"][resistances_DF2["name"]=="total"])*abs(float(resistances_DF2["Temp_in_C"][resistances_DF2["name"]=="air_out"])-float(resistances_DF2["Temp_in_C"][resistances_DF2["name"]=="air_in"]))
    
    result=resistances_DF2.to_excel("exercise3.xlsx")
    return result

print exercise3(ListsofLists) #it will give "none", but it will make the xlsx file at the path given. It is only a step to make the function show it's results.