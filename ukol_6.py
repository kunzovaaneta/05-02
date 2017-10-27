prijmeni = input ("Zadej svoje příjmení a já zkusím uhádnout zda jsi muž nebo žena - ")

pohlavi = "ová" in prijmeni

if pohlavi == True: # proč nemůžu napsat rovnou za if "ová" in prijmeni == True: ??
	print ("Jsi žena")
else:
	print ("jsi muž")