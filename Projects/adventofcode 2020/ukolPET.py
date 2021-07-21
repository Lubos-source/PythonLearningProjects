
soubor = open("D:/skola UNOB/Python/adventofcode/sedadla.txt", "r")

#ZACATEK :	128 rows	0-127
sedadla=[]
for radek in soubor.read().split("\n"):
	sedadla.append(radek)					#rozdeleni po radkach

for sedadlo in sedadla:
	start=0		#nastavim start rows
	end=127		#nastavime end rows
	for pismeno in sedadlo:
		if (pismeno=="F"):
			end=(end+1)/2
			start=start
		elif(pismeno=="B"):
			start=(end+1)/2
			end=end

	print("Row je: start: "+str(start)+" end: "+str(end))

print(sedadla)