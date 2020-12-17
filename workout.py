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
                   help='Select if dumbbells are available for the workout.')
    p.add_argument('-k', '--kettlebell', action='store_true',
                   help='Select if a kettle bell is available for the workout.')
    p.add_argument('-t', '--trx', action='store_true',
                   help='Select if a TRX is available for the workout.')
    p.add_argument('-j', '--jumprope', action='store_true',
                   help='Select if a jump rope is available for the workout.')
    p.add_argument('-o', '--equipmentonly', action='store_true',
                   help='Select if you only want exercises that use equipment available for the workout.  '
                        'No body weight exercises')
    args = p.parse_args()
    Deck(args.dumbbells, args.kettlebell, args.trx, args.jumprope, args.equipmentonly)


if __name__ == '__main__':
    main(sys.argv[1:])
