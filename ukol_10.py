def tah (herni_radek, znak, pozice):

	herni_radek = herni_radek[:pozice] + znak + herni_radek[pozice+1:]
	return herni_radek

prvnitah = tah("xxxxxx----","o",0)

print (prvnitah)