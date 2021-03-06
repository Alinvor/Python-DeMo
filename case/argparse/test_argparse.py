# -*- coding:utf-8 -*-

import argparse

#
#  python -m test_argparse.py --help
parser = argparse.ArgumentParser(description='Command-line example.')

# Add optional switches
parser.add_argument('-v',
                    action='store_true',
                    dest='is_verbose',
                    help='produce verbose output')
parser.add_argument('-o',
                    action='store',
                    dest='output',
                    metavar='FILE',
                    help='direct output to FILE instead of stdout')
parser.add_argument('-C',
                    action='store',
                    type=int,
                    dest='context',
                    metavar='NUM',
                    default=0,
                    help='display NUM lines of added context')

# Allow any number of additional arguments.
parser.add_argument(nargs='*',
                    action='store',
                    dest='inputs',
                    help='input filenames (default is stdin)')

args = parser.parse_args()
print args.__dict__
