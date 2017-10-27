from random import randrange

def tah_pocitace (retezec,pozice):
	while True:
		pozice = randrange (0,19)
		print("počítač si vybírá pozici", pozice)
		if retezec[pozice] == "x" or retezec[pozice] == "o":
			print ("Toto místo už je obsazené, zkus jiné")
		else:
			novy_retezec = retezec[:pozice] + "o" + retezec[pozice+1:]
			print (novy_retezec)
			break

tah_pocitace ("x----xoooooo--------",1)