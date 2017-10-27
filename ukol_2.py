from turtle import right, left, forward, exitonclick
from math import sqrt
def domecek (velikost, pocet_domecku):
	"""Nakreslí domecek o zvolené straně, plus zvolený počet domecků"""
	for vice_domecku in range (pocet_domecku):
		left (90)
		for podsada_domku in range(3):
			forward (velikost)
			right (90)
	
		right (45)
		forward (velikost*sqrt(2))
		right (90)
	
		for dalsi_cast in range(2):
			forward (velikost*sqrt(2)/2)
			right (90)
	
		forward (velikost*sqrt(2))
		left (135)
		forward (velikost*1.2)

domecek(20,6)

exitonclick()