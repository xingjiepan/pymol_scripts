#!/usr/bin/env python3
'''Convert a file of list of residues into a pymol selection command.
Usage:
    ./list_to_pymol_sele.py list_file
'''

import sys


if __name__ == '__main__':

    list_file = sys.argv[1]

    with open(list_file, 'r') as f:
        s = f.read()

    delimiters = [',', '\n', '\t', ';']
    for d in delimiters:
        s.replace(d, ' ')

    residues = s.split()

    res_sele = ['res ' + r for r in residues]

    print('sele ' + ' '.join(res_sele))

