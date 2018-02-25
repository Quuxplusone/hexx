#!/usr/bin/env python

"""
    python findbit.py yes*.sav -- no*.sav

    Find all the bits which are turned ON in yes*.sav and OFF in no*.sav,
    or vice versa. These are the bits which might be responsible for saving
    the salient difference between yes*.sav and no*.sav.

    For things that might be represented as an integer index, try making
    yes*.sav the set of all savefiles where T=1 and no*.sav the set of all
    savefiles where T=2. If the index is saved in plaintext, you should see
    two adjacent bits show up in the output of this script.
"""

import sys

def as_hex(s):
    return ' '.join('%02X' % ch for ch in s)

def findbits(yeses, noes):
    yes_bits_invariably_1 = [0xFF] * 0xF670
    yes_bits_invariably_0 = [0xFF] * 0xF670
    no_bits_invariably_1 = [0xFF] * 0xF670
    no_bits_invariably_0 = [0xFF] * 0xF670
    for fname in yeses:
        with open(fname, "rb") as f:
            contents = f.read()
        assert len(contents) == 0xF670, 'Savefile has the wrong length'
        bits = [ord(byte) for byte in contents]
        yes_bits_invariably_1 = [a & b for a, b in zip(yes_bits_invariably_1, bits)]
        yes_bits_invariably_0 = [a & ~b for a, b in zip(yes_bits_invariably_0, bits)]
    for fname in noes:
        with open(fname, "rb") as f:
            contents = f.read()
        assert len(contents) == 0xF670, 'Savefile has the wrong length'
        bits = [ord(byte) for byte in contents]
        no_bits_invariably_1 = [a & b for a, b in zip(no_bits_invariably_1, bits)]
        no_bits_invariably_0 = [a & ~b for a, b in zip(no_bits_invariably_0, bits)]
    possible_culprit_bits = [(a & b) | (c & d) for a,b,c,d in zip(
        yes_bits_invariably_1, no_bits_invariably_0,
        yes_bits_invariably_0, no_bits_invariably_1
    )]
    for i in range(0, len(possible_culprit_bits), 16):
        row = possible_culprit_bits[i:i + 16]
        if sum(row) != 0:
            print '0x%04x %s-%s' % (i, as_hex(row[:8]), as_hex(row[8:]))

if __name__ == '__main__':
    yesfnames = []
    nofnames = []
    i = sys.argv.index('--')
    findbits(sys.argv[1:i], sys.argv[i+1:])
