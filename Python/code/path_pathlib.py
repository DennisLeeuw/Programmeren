import pathlib

pad = Path("C:/Users/Public/Documents/bestand.txt")

if pathlib.path.exists():
    print("Pad bestaat")
    if pathlib.path.is_file():
        print("Het is een bestand")
    elif pathlib.path.is_dir():
        print("Het is een map")
else:
    print("Pad bestaat niet")

