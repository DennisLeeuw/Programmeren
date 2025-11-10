file='testbestand.txt'

try:
	with open(file, 'rt', encoding="utf-8") as fh:
		read_data = fh.read()
except FileNotFoundError:
	print(f"Bestand {file} niet gevonden")
	exit()
except PermissionError:
	print(f"Geen rechten on {file} te lezen")
	exit()

print(type(read_data))
print(read_data, end='')
