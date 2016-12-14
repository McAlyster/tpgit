import sys
from lib import ecrireXFois

def main(argv):
    ecrireXFois(int(argv[0]), "Hello world!")

if __name__ == '__main__':
    main(sys.argv[1:])
