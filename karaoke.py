#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import urllib

class KaraokeLocal():
    def __init__ (self):

        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(comandos[1]))

        self.datos = cHandler.get_tags()

    def __str__(self):#Imprimir como pide
        total = ""
        for linea in self.datos:
            name = linea[0] + '\t'
            atributos = ""
            for atributo in linea[1].keys():
                if linea[1][atributo] != "":
                    elemento = linea[1][atributo]
                    atributos = atributos + atributo
                    atributos += '=' + elemento + '\t'
            total += name + atributos + '\n'
        return (total)

    def do_local(self):#Descargar
        for linea in self.datos:
            for atributo in linea[1].keys():
                if atributo == "src":#ESto me lo hace bien
                    if linea[1][atributo].split(':')[0] == "http":
                        urllib.request.urlretrieve(linea[1][atributo],sys.argv[1])
    """
    def do_json(self):
        principio = sys.argv[1].split('.')
        if principio[-1] == 'smil'

    """
if __name__ == "__main__":
    comandos = sys.argv
    if len(comandos) != 2:
        print ("Usage: python3 karaoke.py file.smil")
    else:
        karaoke = KaraokeLocal()
        print (karaoke)
        karaoke.do_local()
        print(karaoke)
