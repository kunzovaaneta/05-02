from random import randrange
hod_prvniho_hrace = 0
hod_druheho_hrace = 0
hod_tretiho_hrace = 0
hod_ctvrteho_hrace = 0
kolo1 = 0
kolo2 = 0
kolo3 = 0
kolo4 = 0

while hod_prvniho_hrace < 6 :
	hod_prvniho_hrace = randrange (1,7)
	kolo1 = kolo1 + 1
	if hod_prvniho_hrace < 6:
		print ("Hod prvního hráce v", kolo1, "kole je", hod_prvniho_hrace)
	else:
		print ("Hurá, hodil jsi ", hod_prvniho_hrace," v ", kolo1, "kole !! Hraje další hráč")
	
	


while hod_druheho_hrace < 6:
	hod_druheho_hrace = randrange (1,7)
	kolo2 = kolo2 + 1
	if hod_druheho_hrace < 6:
		print ("Hod druheho hráce v", kolo2, "kole je", hod_druheho_hrace)
	else:
		print ("Hurá hodil jsi ", hod_druheho_hrace," v ", kolo2, "kole !! Hraje další hráč")

	

while hod_tretiho_hrace < 6:
	hod_tretiho_hrace = randrange (1,7)
	kolo3 = kolo3 + 1
	if hod_tretiho_hrace < 6:
		print ("Hod tretiho hráce v", kolo3, "kole je", hod_tretiho_hrace)
	else:
		print ("Hurá, hodil jsi ", hod_tretiho_hrace," v ", kolo3, "kole !! Hraje další hráč")
	kolo3

while hod_ctvrteho_hrace < 6:
	hod_ctvrteho_hrace = randrange (1,7)
	kolo4 = kolo4 + 1
	if hod_ctvrteho_hrace < 6:
		print ("Hod ctvrteho hráce v", kolo4, "kole je", hod_ctvrteho_hrace)
	else:
		print ("Hurá hodil jsi ", hod_ctvrteho_hrace," v ", kolo4, "kole !!")
	kolo4

	
hody_hracu=[kolo1,kolo2, kolo3, kolo4]
if max(hody_hracu) == kolo1:
	print ("vyhrál první hráč")
elif max(hody_hracu) == kolo2:
	print ("vyhrál druhý hráč")
elif max(hody_hracu) == kolo3:
	print ("vyhrál třetí hráč")
elif max(hody_hracu) == kolo4:
	print ("vyhrá čtvrté hráč")


