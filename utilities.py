import shutil

def rewrite_README(molecule_list):
    r = open("README.md", "r")
    w = open("new-README.md", "w")
    write_molecule = False
    write_line = True
    for line in r:
        if write_line:
            w.write(line)
        if "Full molecule list" in line:
            write_molecule = True
            write_line = False
        if write_molecule:
            w.write("\n")
            for molecule in molecule_list:
                w.write("- [" + molecule[0] + "](" + molecule[0] + "_" + molecule[1] + ")" +"\n")
            w.write("\n")
            write_molecule = False
    r.close()
    w.close()

    shutil.move("new-README.md", "README.md")



