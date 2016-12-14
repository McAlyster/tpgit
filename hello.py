#
# Repete l'affichage d'un message
#

import sys
from lib import ecrireXFois


def print_usage():
    print "Usage: python hello.py nbfois message"
    print "\n- nbfois : nombre de repetitions"
    print "- message : message a afficher"
    print "\n --help ou -h: affiche cet aide"


def main(argv):
    if len(argv) == 1 and (argv[0] == "--help" or argv[0] == "-h"):
        print_usage()
    elif len(argv) < 2 or not argv[0].isdigit():
        print "Erreur!"
	print_usage()
    else:
        ecrireXFois(int(argv[0]), argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])

