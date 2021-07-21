

soubor = open("D:/skola UNOB/Python/adventofcode/mapa.txt", "r")

mapa = [[pole for pole in radek.strip()] for radek in soubor]


rad=0 #(1-NELZE pretece o jeden radek v cyklu(byla by treba podminka))
prv=0
Pocet=0

for prvek in mapa:
	if (mapa[rad][prv]=='#'):
			Pocet=Pocet+1		
	if prv==28:
		prv=-3
	if prv==29:
		prv=-2
	if prv==30:
		prv=-1
	prv=prv+3
	rad=rad+1

print(f"Pocet stromu je : {Pocet}")
"""print("Kontrola: \n")
#print(mapa)
print(mapa[1])
print(mapa[5])
print(mapa[-1])"""