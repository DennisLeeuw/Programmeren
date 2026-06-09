import argparse

# We maken een object dat opties afhandeld
parser = argparse.ArgumentParser(
    description="Voorbeeld script met opties"
)

# We voegen opties toe
parser.add_argument("-n", required=True, type=int)
parser.add_argument("-s", required=True, type=str)
parser.add_argument("-o", required=False, type=int)

# Verwerk alle argumenten
args = parser.parse_args()

# Laat zien wat we hebben
print(args)
print(args.n)
print(args.s)
print(args.o)

