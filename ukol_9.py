def vyhodnot (herni_radek):

	if ("xxx" in herni_radek) == True:
		print ("vyhrál hráč s \"x\"")
	elif ("ooo" in herni_radek) == True:
		print("vyhrál hráč s \"o\"")
	elif ( "-" not in herni_radek) == True:
		print("remíza")
	else:
		print("další kolo")




