from scipy import *
from random import *

#TP FONCTION DE TRI 

tab= array[]

#Procédure d'affichage de tableau

def afficher(tab)
	for i in range(len(tab)):
		print(tab[i])



#Procédure de génération de tableau

def gentab(tab):
	for i in range(len(tab)):
		tab[i] = randrange(30000)
	print ("tableau initial")
	afficher(tab)

