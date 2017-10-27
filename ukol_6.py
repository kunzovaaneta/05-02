prijmeni = input ("Zadej svoje příjmení a já zkusím uhádnout zda jsi muž nebo žena - ")

if prijmeni[-3:] == "ová":
	print ("Jsi žena")
else:
	print ("Jsi muž")