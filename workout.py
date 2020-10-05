__author__ = "Natalie Gaston"
__copyright__ = "Copyright 2020"

__version__ = "1.0.0"
__email__ = "nmgaston@gmail.com"

import argparse
import sys

from deck import Deck


def main(argv):
    p = argparse.ArgumentParser(description='Generate a Deck of Cards workout.')
    p.add_argument('-d', '--dumbbells', action='store_true',
                   help='Select if dumbbells are available for workout.')
    p.add_argument('-k', '--kettlebell', action='store_true',
                   help='Select if a kettle bell is available for workout.')
    args = p.parse_args()
    Deck(args.dumbbells, args.kettlebell)


if __name__ == '__main__':
    main(sys.argv[1:])
