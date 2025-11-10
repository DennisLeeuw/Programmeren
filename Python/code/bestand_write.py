try:
    fh = open("testbestand.txt", "wt")
except fh.FileNotFoundError:
    print("Bestand niet gevonden")

fh.write("Dit is de eerste regel van ons nieuwe bestand.")
fh.write("Dan is dit dus de tweede regel van ons nieuwe bestand.")
fh.write("En tot slotte de derde en laatste van ons nieuwe bestand.")
fh.close()

