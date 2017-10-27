from random import randrange 


pokracovani_hry = "hra"

while pokracovani_hry == "hra":

	hod_kostkou = randrange (0,3)

	if hod_kostkou == 0:
		tah_pocitace = "kamen"
	elif hod_kostkou == 1:
		tah_pocitace = "nuzky"
	elif hod_kostkou == 2:
		tah_pocitace = "papir"

	tah_hrace = input ("zvol kamen, nuzky nebo papir ")
	print ("tah pocitace je:", tah_pocitace)

	if tah_hrace == tah_pocitace:
		print ("plichta")
	elif tah_hrace == "kamen":
		if tah_pocitace == "nuzky":
			print ("vyhrál jsi")
		elif tah_pocitace == "papir":
			print ("prohrál jsi")
	elif tah_hrace == "nuzky":
		if tah_pocitace == "papir":
			print ("vyhrál jsi")
		elif tah_pocitace == "kamen":
			print ("prohrál jsi")
	elif tah_hrace == "papir":
		if tah_pocitace == "nuzky":
			print ("prohrál jis")
		elif tah_pocitace == "kamen":
			print ("vyhrál jsi")
	else:
		print("špatně zadaný tah hráče ")

	pokracovani_hry = input ( "Pokud chcete hrát dál napište - hra, pokud nechcte dál hrát napište - konec ")
	
print ("Tak si zahrajeme zase příště")
	


