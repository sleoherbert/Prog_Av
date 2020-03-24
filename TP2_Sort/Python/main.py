from scipy import *
from random import *

#TP FONCTION DE TRI 

tab = np.empty()

#Procedure de generation de tableau a vide

def gentab(tab,col):
	tab = numpy.zeros((1,col),dtype='i')
	print ("tableau initial")
	print(tab)
