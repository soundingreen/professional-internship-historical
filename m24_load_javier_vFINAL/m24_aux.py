def get_badElectrodes(path="C:/Users/sound/Downloads/m24_load_javier/"):
    fname = "bad_electrodes.csv"
    with open(path+fname,"r") as f:
        lines = f.readlines()
    bad = []
    for l in lines[1:]:
        x = l.strip()
        if x[0] == "#":
            continue
        bad.append(x)
    return bad
