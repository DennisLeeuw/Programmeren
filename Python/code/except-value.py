x = input("Geef een getal: ")

try:
    waarde = int(x)
except ValueError:
    print("Dit is geen integer")
