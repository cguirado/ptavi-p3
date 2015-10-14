#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
        self.tags = []
        self.dicc = {"root-layout":['width', 'height', 'background-color'],
                    "region":['id', 'top', 'left', 'bottom', 'right'],
                    "img":['src', 'region', 'begin', 'dur'],
                    "audio":['src', 'begin', 'dur'],
                    "textstream":['src','region']}

#No necesitamos endElement (solo tenemos principio de etiqueta)
    def startElement(self, name, attrs):
        if name in self.dicc:
            dicc2 = {}
            #Empiezo a meterme dentro del diccsmil para sacar atributos segun nombre
            for atributo in self.dicc[name]:
                #introduzco en mi nuevo diccionario los atributos que voy leyendo
                dicc2[atributo] = attrs.get(atributo,"")
            #introduzco en mi lista tag lo que voy a acumulando con nombre y dicc
            self.tags.append([name,dicc2])
            print("")

    def get_tags (self):
        return self.tags
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    datos = cHandler.get_tags()
    print(datos)
