file='testbestand.txt'

with open(file, 'rt', encoding="utf-8") as fh:
	file = fh.readlines()

for line in file:
	print(line)

