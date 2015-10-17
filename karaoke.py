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


    if len(comandos) != 2:
        print ("Usage: python3 karaoke.py file.smil")
    else:
        parser.parse(open(comandos[1]))
        datos = cHandler.get_tags()
        total = ""
        for linea in datos:
            #lo primero que queremos el nombre mas el \t
            name = linea[0] + '\T'
            atributos = "" #Luego iremos mentiendo elementos
            #queremos es ir cogiendo los atributos tras coger el nombre e ir quitando blancos.
            #lina[1] (diccionario) como anteriormente atributo (primera parte del atributo)
            for atributo in linea[1].keys():
                if linea[1][atributo] != "":
                    elemento = linea[1][atributo]#sacamos el valor del atributo
                    #print(elemento)
                    atributos = atributos + atributo
                    atributos += '=' + elemento + '\T' #Unimos mas cosas a nuestra lista
            total += name + atributos + '\n'#nombre mas atributo completo con su valor 2 listas diferentes
        #print (total)

        for linea in datos:
            for atributo in linea[1].keys():
                #print(atributo)
                if atributo == "src":#ESto me lo hace bien
                    if linea[1][atributo] == "http://":
                        print(linea[1].atributo)
