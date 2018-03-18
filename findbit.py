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

import argparse
import struct
import sys

def as_hex(s):
    return ' '.join('%02X' % ch for ch in s)

def get_contents(fname):
    with open(fname, "rb") as f:
        contents = f.read()
    assert len(contents) == 0xF670, 'Savefile has the wrong length'
    return contents

def find_bits(yeses, noes):
    yes_bits_invariably_1 = [0xFF] * 0xE004 + [0x00] * (0xF670 - 0xE004)
    yes_bits_invariably_0 = [0xFF] * 0xE004 + [0x00] * (0xF670 - 0xE004)
    no_bits_invariably_1  = [0xFF] * 0xE004 + [0x00] * (0xF670 - 0xE004)
    no_bits_invariably_0  = [0xFF] * 0xE004 + [0x00] * (0xF670 - 0xE004)
    for fname in yeses:
        bits = map(ord, get_contents(fname))
        yes_bits_invariably_1 = [a & b for a, b in zip(yes_bits_invariably_1, bits)]
        yes_bits_invariably_0 = [a & ~b for a, b in zip(yes_bits_invariably_0, bits)]
    for fname in noes:
        bits = map(ord, get_contents(fname))
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

def find_countdowns(fnames):
    def to_bytes(s):
        return map(ord, s)
    def to_shorts(s):
        result = []
        for i in xrange(len(s) - 1):
            result.append(struct.unpack('<H', s[i:i+2]))
        return result
    def is_strictly_ascending(seq):
        return all(earlier < later for earlier, later in zip(seq, seq[1:]))
    def is_strictly_descending(seq):
        return all(earlier > later for earlier, later in zip(seq, seq[1:]))

    contentses = map(get_contents, fnames)
    zipped_bytes = zip(*map(to_bytes, contentses))
    zipped_shorts = zip(*map(to_shorts, contentses))
    for i, seq in enumerate(zipped_bytes):
        if is_strictly_descending(seq):
            print 'Byte %04X:%04X is strictly descending: %r' % (i, i+1, seq)
        elif is_strictly_ascending(seq):
            print 'Byte %04X:%04X is strictly ascending: %r' % (i, i+1, seq)
    for i, seq in enumerate(zipped_shorts):
        if is_strictly_descending(seq):
            print 'Short %04X:%04X is strictly descending: %r' % (i, i+2, seq)
        elif is_strictly_ascending(seq):
            print 'Short %04X:%04X is strictly ascending: %r' % (i, i+2, seq)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--countdown', action='store_true', help='look for countdown bytes or shorts')
    parser.add_argument('rest', nargs=argparse.REMAINDER)
    options = parser.parse_args()

    if options.countdown:
        find_countdowns(options.rest)
    else:
        yesfnames = []
        nofnames = []
        i = rest.index('--')
        find_bits(options.rest[1:i], options.rest[i+1:])
