file='testbestand.txt'

with open(file, 'rt', encoding="utf-8") as fh:
	for line in fh:
    		print(f"{line}\n", end='')
