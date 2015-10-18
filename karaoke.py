#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import os


class KaraokeLocal():
    def __init__ (self):
        comandos = sys.argv
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(comandos[1]))
        if len(comandos) != 2:
            print ("Usage: python3 karaoke.py file.smil")
        self.datos = cHandler.get_tags()

    def __str__(self):
        total = ""
        for linea in self.datos:
            name = linea[0] + '\T'
            atributos = ""
            for atributo in linea[1].keys():
                if linea[1][atributo] != "":
                    elemento = linea[1][atributo]
                    atributos = atributos + atributo
                    atributos += '=' + elemento + '\T'
            total += name + atributos + '\n'
        return (total)

if __name__ == "__main__":
    karaoke = KaraokeLocal()
    print (karaoke.__str__())





"""
    comandos = sys.argv
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)

        for linea in datos:
            for atributo in linea[1].keys():
                #print(atributo)
                if atributo == "src":#ESto me lo hace bien
                    #print(linea[1][atributo].split('//'))
                    if linea[1][atributo].split(':')[0] == "http":
                        os.system( "wget -q" + linea[1][atributo])
"""
