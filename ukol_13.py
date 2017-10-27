from random import randrange

def tah_pocitace (retezec, pozice):
	while True:
		pozice = randrange (0,19)
		print("počítač si vybírá pozici", pozice)
		if retezec[pozice] == "x" or retezec[pozice] == "o":
			print ("Toto místo už je obsazené, zkus jiné")
		else:
			retezec = retezec[:pozice] + "o" + retezec[pozice+1:]
			print (retezec)
			break

def tah_hrace (retezec, pozice):
	while True:
		pozice= int(input("Na kterou pozici, chcete hrát?"))
		if pozice < 0:
			print("špatně zvolená pozice, musí se jedna o kladné číslo")
		elif pozice >20:
			print("příliš velké číslo, zvol pozici od 0-19")
		elif retezec[pozice] == "x" or retezec[pozice] == "o":
			print ("Toto místo už je obsazené, zkus jiné")
		else:
			retezec = retezec[:pozice] + "x" + retezec[pozice+1:]
			print (retezec)
			break


def piskvorky1d (retezec):
	while True:
		tah_hrace (retezec, 1)
		tah_pocitace (retezec, 1)
		if ("xxx" in retezec) == True:
			print ("vyhrál hráč s \"x\"")
			break
		elif ("ooo" in retezec) == True:
			print("vyhrál hráč s \"o\"")
			break
		elif ( "-" not in retezec) == True:
			print("remíza")
			break
		else:
			print("další kolo")		

piskvorky1d ("-"*20)