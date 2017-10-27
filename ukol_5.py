def ano_nebo_ne (otazka):
	while True:
		odpoved = (input(otazka)).lower()
		if odpoved == "ano" or odpoved == "a" :
			return True
		elif odpoved == "ne" or odpoved == "n":
			return False
		else:
			print ("špatně zadaná vstupní data, zkus to znovu")


if ano_nebo_ne ("půjdeš zítra ven?"):
	print ("skvělé už se těším")
else:
	print ("škoda, tak příště")