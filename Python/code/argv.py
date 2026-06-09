import sys

if len(sys.argv) < 2:
    print("ERROR: Er zijn geen argumenten opgegeven")
    exit(1)

# argv[0] is de naam van het script
# De argumenten beginnen vanaf index 1
for i in range(0,len(sys.argv)):
    print(sys.argv[i])

