#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":

    comandos = sys.argv

    print (comandos)
    print(len(comandos))
    if len(comandos) != 2:
        print ("Usage: python3 karaoke.py file.smil")
    else:
        fichero = open(comandos[1],'r')
        print(fichero)
