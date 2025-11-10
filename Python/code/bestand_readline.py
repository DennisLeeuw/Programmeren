file='testbestand.txt'

with open(file, 'rt', encoding="utf-8") as fh:
	print(fh.readline())
	print(fh.readline())
	print(fh.readline())
	print(fh.readline())
	print(fh.readline())

