#
# Repete l'affichage d'un message
#

import sys
from lib import ecrireXFois


def main(argv):
    ecrireXFois(int(argv[0]), argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])

