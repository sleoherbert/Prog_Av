import scipy 
import random 
import numpy as np
import time
import csv
import monotonic
mtime = monotonic.time.time

#TP FONCTION DE TRI 

#Procedure de generation de tableau a vide

def gentab(tab,col):
	tab = np.random.randint(10000,size=col)
	print ("tableau initial")
	print (tab)
	return tab


#TRI SELECTION

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab



#TRI BULLE

def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]



#TRI RAPIDE
#Je cherche ce qui sont plus grand que la valeur auxilière
#contrairement à ce que j'ai fait en C

def partition(tab, start, end):
    aux = tab[start]
    deb = start + 1
    der = end

    while True:
        while deb <= der and tab[der] >= aux:
            der = der - 1

        while deb <= der and tab[deb] <= aux:
            deb = deb + 1

        if deb <= der:
            tab[deb], tab[der] = tab[der], tab[deb]
            # continue la boucle
        else:
            # sort de la boucle
            break

    tab[start], tab[der] = tab[der], tab[start]

    return der


def tri_rapide(tab, start, end):
    if start >= end:
        return

    p = partition(tab, start, end)
    tri_rapide(tab, start, p-1)
    tri_rapide(tab, p+1, end)




#TRI FUSION


#separer le tableau en 2 sous tableau, gtab et dtab
def merge(gtab, dtab):
    tab_trie = []
    #i index de gtab   j index de dtab
    i = j = 0

    gtab_len, dtab_len = len(gtab), len(dtab)

    for _ in range(gtab_len + dtab_len):
        #Verifie la plus petite valeur au debut de chaque tableau
        #Ajout ensuite la valeur dans tab_trié
        if i < gtab_len and j < dtab_len:
            if gtab[i] <= dtab[j]:
                tab_trie.append(gtab[i])
                i += 1
            else:
                tab_trie.append(dtab[j])
                j += 1
        #Si ajoute les valeurs de dtab on atteind la fin de gtab
        #Et inversement si on atteind la fin de dtab
        elif i == gtab_len:
            tab_trie.append(dtab[j])
            j += 1
        elif j == dtab_len:
            tab_trie.append(gtab[i])
            i += 1

    return tab_trie


def merge_sort(tab):
    # Dans le cas où le tableau n'a qu'un seul élement
    if len(tab) <= 1:
        return tab

    mid = len(tab) // 2
    gtab = merge_sort(tab[:mid])
    dtab = merge_sort(tab[mid:])

    return merge(gtab, dtab)




#Application

def main():
    print("Programme de Tri\n Le programme lancera les fonctions dans l'ordre suivante\nTri Selection\nTri Bulle\nTri Rapide\nTri Fusion")
    tab=[]
    print("veillez entrer la taille du tableau")
    taille=input()
    #Verifieque la valeur entrer est un entrier
    while True:
        try:
            taille=int(taille)
            print("La valeur entree est un entier = ", taille)
            break
        except ValueError:
            print("La valeur entrer est incorrect!")
            return -1

    tab=gentab(tab,taille)
    tab1=tab.copy()
    t0 = mtime()
    tri_selection(tab1)
    elapsed1 = mtime()-t0
    print ("Tri selection\nLe tableau trié est:")
    print (tab1)
    print ("temps d'execution: ",elapsed1)

    time.sleep(2)
    print("\n\n")
    tab2=tab.copy()
    t0 = mtime()
    tri_bulle(tab2)
    elapsed2 = mtime()-t0
    print ("\nTri bulle\nLe tableau trié est:")
    print (tab2)
    print ("temps d'execution: ",elapsed2)


    time.sleep(2)
    print("\n\n")
    tab3=tab.copy()
    t0 = mtime()
    tri_rapide(tab, 0, len(tab) - 1)
    elapsed3 = mtime()-t0
    print ("\nTri_rapide\nLe tableau trié est:")
    print (tab3)
    print ("temps d'execution: ",elapsed3)

    time.sleep(2)
    print("\n\n")
    tab4=tab.copy()
    t0 = mtime()
    merge_sort(tab4)
    elapsed4 = mtime()-t0
    print ("\nTri Fusion\nLe tableau trié est:")
    print (tab4)
    print ("temps d'execution: ",elapsed4)

    time.sleep(1)

    #Enregistrement des résultat dans un fichier csv
    fname="tempexecpy.csv"
    file = open(fname,"a")
    try:
        writer = csv.writer(file,delimiter=";")
        writer.writerow((taille,elapsed1,elapsed2,elapsed3,elapsed4))
        file.close()
        print("Résultat enregistrer")
    except:
            print("Probleme de lecture du ficher",nomFichier)



main()




"""
# TEST 
tab = [100,88, 22, 52, 35, 15, 32, 2, 74, 63, 70]

print ("tableau initial",tab)
 
tri_selection(tab)
 
print ("Tri selection\nLe tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])


tab = [100,88, 22, 52, 35, 15, 32, 2, 74, 63, 70]
 
tri_bulle(tab)
 
print ("\nTri bulle\nLe tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])


tab = [100,88, 22, 52, 35, 15, 32, 2, 74, 63, 70]

print ("\nTri_rapide\nLe tableau trié est:")
tri_rapide(tab, 0, len(tab) - 1)
for i in range(len(tab)):
    print ("%d" %tab[i])


tab = [100,88, 22, 52, 35, 15, 32, 2, 74, 63, 70]

print ("\nTri_Fusion\nLe tableau trié est:")
tab = merge_sort(tab)
for i in range(len(tab)):
    print ("%d" %tab[i])


"""





