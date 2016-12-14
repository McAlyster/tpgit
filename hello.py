#
# Repete l'affichage d'un message
#

import sys
from lib import ecrireXFois


def main(argv):
    if len(argv) < 2 or not argv[0].isdigit():
        print "Erreur!"
        print "Usage: python hello.py nbfois message"
        print "\n- nbfois : nombre de repetitions"
        print "- message : message a afficher"
    else:
        ecrireXFois(int(argv[0]), argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])

