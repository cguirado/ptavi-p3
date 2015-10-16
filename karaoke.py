#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler


if __name__ == "__main__":

    comandos = sys.argv
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)

    print(len(comandos))
    if len(comandos) != 2:
        print ("Usage: python3 karaoke.py file.smil")
    else:
        parser.parse(open(comandos[1]))
        datos = cHandler.get_tags()
        total = ""
        for linea in datos:
            #lo primero que queremos el nombre mas el \t
            name = linea[0] + '\t'
            atributos = "" #Luego iremos mentiendo elementos
            #queremos es ir cogiendo los atributos tras coger el nombre e ir quitando blancos. lina[1] (diccionario) como anteriormente
            for atributo in linea[1].keys():
                if linea[1][atributo] != "":
                    elemento = linea[1][atributo]
                    atributos = atributo + elemento + "=" + "\t"
            total += name + atributos

        print (total)
