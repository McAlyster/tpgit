# bibliotheque d'affichage

def ecrireXFois(x, chaine):
    for i in range(x):
	ecrire(chaine, i+1)


def ecrire(chaine, index):
    print str(index) + " -> " + chaine

