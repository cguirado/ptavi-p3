#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import urllib


class KaraokeLocal():
    def __init__ (self, fich):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fich))
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
                    #print("vale")
                    if linea[1][atributo].split(':')[0] == "http":
                        #print(linea[1][atributo][-1])
                        urllib.request.urlretrieve(linea[1][atributo], linea[1][atributo].split('/')[-1])
                        linea[1][atributo] = linea[1][atributo].split('/')[-1]
if __name__ == "__main__":
    comandos = sys.argv
    if len(comandos) != 2:
        print ("Usage: python3 karaoke.py file.smil")
    else:
        fich = comandos[1]
        karaoke = KaraokeLocal(fich)
        print (karaoke)
        karaoke.do_local()
        print(karaoke)
