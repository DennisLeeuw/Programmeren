import os

pad = "C:/Users/Public/Documents/bestand.txt"

if os.path.exists(pad):
    print("Pad bestaat")
    if os.path.isfile(pad):
        print("Het is een bestand")
    elif os.path.isdir(pad):
        print("Het is een map")
else:
    print("Pad bestaat niet")

