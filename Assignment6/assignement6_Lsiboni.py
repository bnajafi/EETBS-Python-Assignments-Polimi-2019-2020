import pandas as pd

standard_types = ["conv","cond","cond","cond","cond","cond","conv"]
standard_length = [None, 0.013, 0.013, 0.025, 0.09, 0.013, None]
R_std = [0.12,0.14,0.23,0.7,0.63,0.079,0.03]
length_real = [ None,0.013,0.013,0.09,0.09,0.013,None]
R_real = [None,None,None,None,None,None,None]

list_of_lists = [standard_types, standard_length, R_std, length_real, R_real]

Dataframe_temporary = pd.DataFrame(list_of_lists)
Dataframe_temporary2 = Dataframe_temporary.transpose()

Dataframe_temporary2.index =  ["inside_air", "wood_bevel", "wood_fiber", "glass_fiber", "wood_stud", "gypsum","outside_air"]
Dataframe_temporary2.columns = ["type", "length_std", "R_std","length_real", "R_real"]
#print(Dataframe_temporary2)

#print(Dataframe_temporary2.loc[Dataframe_temporary2["type"]=="conv","R_std"])

def RValue(DataFrame):

    DataFrame.loc[DataFrame["type"]=="conv","R_real"] = DataFrame.loc[DataFrame["type"]=="conv","R_std"]
    DataFrame.loc[DataFrame["type"]=="cond","R_real"] =((DataFrame.loc[DataFrame["type"]=="cond","length_real"])/(DataFrame.loc[DataFrame["type"]=="cond","length_std"]))*DataFrame.loc[DataFrame["type"]=="cond","R_std"]
    #DataFrame.loc[DataFrame["type"]=="conv","U Value (W/m2k)"] = 1.0/DataFrame.loc[DataFrame["type"]=="conv","R_std"]
    #DataFrame.loc[DataFrame["type"]=="cond","U Value (W/m2k)"] =1.0/DataFrame.loc[DataFrame["type"]=="cond","R Value_std"]

    return(DataFrame)

Final_Dataframe= RValue(Dataframe_temporary2)
#print(Final_Dataframe)

# problem solving

R_tot_woodstud= Final_Dataframe.loc[Final_Dataframe.index!="glass_fiber","R_real"].sum()
print(R_tot_woodstud)
R_tot_fiberglass= Final_Dataframe.loc[Final_Dataframe.index!="wood_stud","R_real"].sum()
print(R_tot_fiberglass)

U_woodstud = 1.0/float(R_tot_woodstud)
U_fiberglass = 1.0/float(R_tot_fiberglass)

U_value = U_woodstud*0.25 + U_fiberglass*0.75

R_value = 1.0/float(U_value)

A_tot = 0.8*50*2.5

Q_tot = U_value*A_tot*(22-(-2))
print(Q_tot)

Final_Dataframe.loc[:,"U_real"]= None
Final_Dataframe.loc["OVERALL",:] = None

Final_Dataframe.loc["OVERALL","U_real"]= U_value
print(Final_Dataframe)

# exporting into excel

import os
os.chdir(r"C:\Users\lorenzo\Desktop\assignements Behzad")
Final_Dataframe.to_excel("Assignment6_SiboniLorenzo_Matrix.xlsx")
