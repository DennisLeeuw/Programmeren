try:
    fh = open("testbestand.txt", "wt")
except fh.FileNotFoundError:
    print("Bestand niet gevonden")
    exit()

fh.write("Dit is de eerste regel van ons nieuwe bestand.\r\n")
fh.write("Dan is dit dus de tweede regel van ons nieuwe bestand.\r\n")
fh.write("En tot slotte de derde en laatste van ons nieuwe bestand.\r\n")
fh.close()

