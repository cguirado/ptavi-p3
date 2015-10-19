#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.tags = []
        self.dicc = {"root-layout": ['width', 'height', 'background-color'],
                     "region": ['id', 'top', 'left', 'bottom', 'right'],
                     "img": ['src', 'region', 'begin', 'dur'],
                     "audio": ['src', 'begin', 'dur'],
                     "textstream": ['src', 'region']}

    def startElement(self, name, attrs):
        if name in self.dicc:
            dicc2 = {}
            for atributo in self.dicc[name]:
                dicc2[atributo] = attrs.get(atributo, "")
            self.tags.append([name, dicc2])

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    datos = cHandler.get_tags()
    print(datos)
