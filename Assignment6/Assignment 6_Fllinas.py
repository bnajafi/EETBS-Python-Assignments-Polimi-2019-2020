import pandas as pd
import os

def RValue_Finder(material,length=1):
    #IF LENGTH NOT SPECIFIED IT TAKES DEFAULT VALUE OF 1 (DONE FOR NONEXISTANT LENGTH OF CONVECTIVE RESISTANCES)
    #Folder_whereTheTablesAre = r"C:\Users\fabri\Dropbox\Polimi\3rd Semester\Building Systems\Assignments"
    Folder_whereTheTablesAre = os.getcwd()
    #Be sure to have csv file of library material on same folder as python file, current directory will be the one searched for the files (unless specified otherwise)
    fileName_library = "LibraryOfMaterials_Fllinas.csv"
    path_library = os.path.join(Folder_whereTheTablesAre,fileName_library)
    material_library = pd.read_csv(path_library,sep=";",index_col=0,header=0)
    typ=material_library.loc[material,"Type"]
    if typ=="cond":
        std_length = material_library.loc[material,"Length"]
        std_Rval = material_library.loc[material,"RvalUnit"]
        RValue=std_Rval*length/std_length
    elif typ=="conv":
        RValue=material_library.loc[material,"RvalUnit"]
    return RValue


resistance_names = ["R1","R2","R3","R4","R5","R6","R7"]
resistances_material = ["outside","gypsum","woodfiber","woodbevel","woodstud","glassfiber","inside"]
resistances_types = ["conv","cond","cond","cond","cond","cond","conv"]
resistances_lengths = [None,0.013,0.013,0.013,0.09,0.09,None]
resistances_RValues=[0,0,0,0,0,0,0]
resistance_listofLists = [resistances_material,resistances_types,resistances_lengths,resistances_RValues]

resistances_DF0 = pd.DataFrame(resistance_listofLists,
                              index=["Material","type","Length","RValue"], 
                              columns = resistance_names)

resistances_DF = resistances_DF0.transpose()

resistances_DF['RValue']=resistances_DF.apply(lambda x: RValue_Finder(x.Material,x.Length), axis=1)
print(resistances_DF)

total=resistances_DF['RValue'].sum()

Rtot1=total-resistances_DF[resistances_DF["Material"]=="glassfiber"]["RValue"]
Rtot2=total-resistances_DF[resistances_DF["Material"]=="woodstud"]["RValue"]
#Rtot1=total-resistances_DF.iloc[5,3]
#Rtot2=total-resistances_DF.iloc[4,3]

print("The value of the total resistance with Wood studs is: " +str(Rtot1) +" degC/Wm2")
print("The value of the total resistance with Insulation is: " +str(Rtot2) +" degC*m2/W")


fractionwood=0.25
fractioninsulation=1-fractionwood
perimeter=50
wallheight=2.5
glazingfraction=0.2
Tin=22
Tout=-2


Uwood=1/float(Rtot1)
Uinsulation=1/float(Rtot2)
Utotal=Uwood*fractionwood+Uinsulation*fractioninsulation
print("The value of the total overall heat transfer coeficient is: " +str(Utotal) +" W/degC*m2")


Rprimetot=1/float(Utotal)
Atot=(1-glazingfraction)*wallheight*perimeter
Qtot=Atot*Utotal*(Tin-Tout)
print("The value of the heat transfer rate loss is: " +str(Qtot) +" W")

#Results of the Resistances table will be published in current directory
currentdir=os.getcwd()
fileName_exp= "ResistanceData_Fllinas.xlsx"
path_exp = os.path.join(currentdir,fileName_exp)
resistances_DF.to_excel(path_exp)