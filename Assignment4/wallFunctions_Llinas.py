def EquivalentResistance(X):
    Rtot=0  
    for anyR in X:
        anyRmaterial=anyR["material"]
        if anyR["type"]=="cond":
            if anyR["length"]==libraryOfMaterials[anyRmaterial]["length"]:
                Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]
                anyR.update( {'Rvalue' : Rvalue} ) #here we are adding the value of the resisntance into the resistance's dictionary
            else:
                Rvalue=float(libraryOfMaterials[anyRmaterial]["RValUnit"])*anyR["length"]/libraryOfMaterials[anyRmaterial]["length"]
                anyR.update( {'Rvalue' : Rvalue} ) #here we are adding the value of the resisntance into the resistance's dictionary
        elif anyR["type"]=="conv":
            Rvalue=libraryOfMaterials[anyRmaterial]["RValUnit"]
            anyR.update( {'Rvalue' : Rvalue} ) #here we are adding the value of the resisntance into the resistance's dictionary
        Rtot=Rtot+Rvalue
    return Rtot
    
gypsumDict = {"length":0.013,"RValUnit":0.079}
woodfiberDict = {"length":0.013,"RValUnit":0.23}
woodbevelDict = {"length":0.013,"RValUnit":0.14}
woodstudDict = {"length":0.09, "RValUnit":0.63}
glassfiberDict = {"length":0.025,"RValUnit":0.7}
insideDict = {"RValUnit":0.12}
outsideDict = {"RValUnit":0.03}

libraryOfMaterials = { "gypsum":gypsumDict,"woodStud" : woodfiberDict,"woodfiber": woodfiberDict,"woodbevel":woodbevelDict , 
"woodstud":woodstudDict,"glassfiber":glassfiberDict,"inside":insideDict, "outside" :outsideDict} 