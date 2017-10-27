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
			novy_retezec = retezec[:pozice] + "x" + retezec[pozice+1:]
			print (novy_retezec)
			break

tah_hrace("------xx---ooooooooo",1)
