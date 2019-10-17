# Assignment 3 by Benjamin Traskunov

RtotList = []


def function(x):
    # Creating dictionary of material properties

    WoodStud = {"resistance": .63, "length_st": 50.8, "width_st": .09, "area_st": .004572, "thick_st": "N/A"}
    GlassFiber = {"resistance": .7, "length_st": "N/A", "width_st": "N/A", "area_st": "N/A", "thick_st": 0.025}
    Gypsum = {"resistance": .079, "length_st": "N/A", "width_st": "N/A", "area_st": "N/A", "thick_st": 0.013}
    WoodFiber = {"resistance": .23, "length_st": "N/A", "width_st": "N/A", "area_st": "N/A", "thick_st": 0.013}
    WoodBevel = {"resistance": .14, "length_st": .013, "width_st": .20, "area_st": 0.0026, "thick_st": "N/A"}
    Inside = {"resistance": .12, "length_st": "N/A", "width_st": "N/A", "area_st": "N/A", "thick_st": "N/A"}
    Outside = {"resistance": .03, "length_st": "N/A", "width_st": "N/A", "area_st": "N/A", "thick_st": "N/A"}

    # Creating A list of the materials

    LibraryOfMaterials = {
        "WoodStud": WoodStud, "GlassFiber": GlassFiber, "Gypsum": Gypsum,
        "WoodFiber": WoodFiber, "WoodBevel": WoodBevel, "Outside": Outside,
        "Inside": Inside
    }

    # Creating list of Resistances , thickness 0 if not needed
    Rtot = 0

    for item in x:
        matsearch = item["Name"]
        insidelib = LibraryOfMaterials[matsearch]
        if item["type"] == "cond":
            if insidelib["thick_st"] == "N/A":
                Rval = insidelib["resistance"]
                item["calc"] = Rval
                print("The resistance of ", item["Name"] , " is ", Rval, ".")
            else:
                Rval = (insidelib["resistance"] * (item["thick"] / insidelib["thick_st"]))
                item["calc"] = Rval
                print("The resistance of ", item["Name"], " is ", Rval, ".")
            Rtot = Rtot + Rval

        elif item["type"] == "conv":
            Rval = insidelib["resistance"]
            item["calc"] = Rval
            print Rval
            Rtot = Rtot + Rval

    print("The total resistance for this in series set is", Rtot, ".")

    return Rtot


R1 = {"Name": "WoodStud", "type": "cond", "thick": 0}
R2 = {"Name": "GlassFiber", "type": "cond", "thick": .09}
R3 = {"Name": "Gypsum", "type": "cond", "thick": .013}
R4 = {"Name": "WoodFiber", "type": "cond", "thick": .013}
R5 = {"Name": "WoodBevel", "type": "cond", "thick": 0}
R6 = {"Name": "Inside", "type": "conv", "thick": 0}
R7 = {"Name": "Outside", "type": "conv", "thick": 0}

ResList1 = [R1, R3, R4, R5, R6, R7]
ResList2 = [R2, R3, R4, R5, R6, R7]

stuff1 = function(ResList1)
stuff2 = function(ResList2)

RtotList.append(stuff1)
RtotList.append(stuff2)

print("Here is the resulting total resistance of both in-series sets", RtotList, ".")

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

Qtot = Utot*Atot*(Tin-Tout)

print("Here is the total heat flux", Qtot, ".")
