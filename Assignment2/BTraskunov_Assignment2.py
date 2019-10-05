# Assignment 2 by Benjamin Traskunov

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
Rtota = 0
Rtotb = 0

R1 = {"Name": "WoodStud", "type": "cond", "thick": 0}
R2 = {"Name": "GlassFiber", "type": "cond", "thick": .09}
R3 = {"Name": "Gypsum", "type": "cond", "thick": .013}
R4 = {"Name": "WoodFiber", "type": "cond", "thick": .013}
R5 = {"Name": "WoodBevel", "type": "cond", "thick": 0}
R6 = {"Name": "Inside", "type": "conv", "thick": 0}
R7 = {"Name": "Outside", "type": "conv", "thick": 0}

ResList1 = [R1, R3, R4, R5, R6, R7]
ResList2 = [R2, R3, R4, R5, R6, R7]

# Calculating each material's resistance

for item in ResList1:
    matsearch = item["Name"]
    insidelib = LibraryOfMaterials[matsearch]
    if item["type"] == "cond":
        if insidelib["thick_st"] == "N/A":
            Rval = insidelib["resistance"]
            item["calc"] = Rval
            print Rval
        else:
            Rval = (insidelib["resistance"]*(item["thick"]/insidelib["thick_st"]))
            item["calc"] = Rval
            print Rval
        Rtota = Rtota + Rval

    elif item["type"] == "conv":
        Rval = insidelib["resistance"]
        item["calc"] = Rval
        print Rval
        Rtota = Rtota + Rval

for item in ResList2:
    matsearch = item["Name"]
    insidelib = LibraryOfMaterials[matsearch]
    if item["type"] == "cond":
        if insidelib["thick_st"] == "N/A":
            Rval = insidelib["resistance"]
            item["calc"] = Rval
            print Rval
        else:
            Rval = (insidelib["resistance"]*(item["thick"]/insidelib["thick_st"]))
            item["calc"] = Rval
            print Rval
        Rtotb = Rtotb + Rval

    elif item["type"] == "conv":
        Rval = insidelib["resistance"]
        item["calc"] = Rval
        print Rval
        Rtotb = Rtotb + Rval

print Rtota, Rtotb

Rtot = 1/((1/Rtota) + (1/Rtotb))

Uins = 1/Rtotb

print Uins

Uwood = 1/Rtota

print Uwood

Utot = Uwood*.25 + Uins*.75

print Utot

Rnewtot = 1/Utot

print Rnewtot

Atot = .8*50*2.5

print Atot

Tin = 22

Tout = -2

Qtot = Utot*Atot*(Tin - Tout)

print Qtot
