#!/usr/bin/python

#-*- coding: UTF-8 -*-
__author__ = 'n30'

import binascii
import struct
import sys

class Pyndianizer:

    def __init__(self, numero = 0x0):
        self.numero = numero #yeah, Spanish because Spanish
        pass #do nothing, bitchslap

    def to_little_endian(self, hexstr):
        try:
            hexnum = int(hexstr, 16) if type(hexstr) is str else hexstr
            if isinstance(hexnum, int) or isinstance(hexnum, long):
                retstr = ""
                b8arr8 = {}
                if True:
                    b8arr8 = struct.pack('<I',hexnum)
                #else: # For compatibility with 64bit when I get my head around it
                #    b8arr8 = struct.pack('<d',hexnum)
                strindi = binascii.hexlify(b8arr8)
                couples = [strindi[i:i + 2] for i in range(0, len(strindi), 2)]
                for pair in couples:
                    retstr += ("\\x"+pair)
                return retstr
            else:
                return "[-] Not an int or long type number. Try: 0xBEBAFECA"
        except struct.error:
            return "[-] ERR: Number much long, very bit, many 64"
        except ValueError:
            return "[-] ERR: Not an hex number"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        argv_1 = sys.argv[1]
		pyndianizer = Pyndianizer()
        print pyndianizer.to_little_endian(argv_1)
    else:
        print
        print "==== PYNDIANIZER BY N30M1ND ===="
        print "Usage:"
        print "    ","pyndianizer.py","int||long"
