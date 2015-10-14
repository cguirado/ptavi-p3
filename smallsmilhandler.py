#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.top = ""
        self.botton = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
#No necesitamos endElement (solo tenemos principio de etiqueta)
    def startElement(self,name,attrs):
        if name == "root-layout":
        #valores de los atributos"
            self.width = attrs.get(width,"")
            self.height = attrs.get(heigt,"")
            self.backgroundcolor = attrs.get(backgroundcolor,"")
        if name == "region":
            self.id = attrs.get(id,"")
            self.top = attrs.get(top,"")
            self.botton = attrs.get(botton,"")
            self.left = attrs.get(left,"")
            self.right = attrs.get(right,"")
        if name == "img":
            self.src = attrs.get(src,"")
            self.region = attrs.get(region,"")
            self.begin = attrs.get(begin,"")
            self.dur = attrs.get(dur,"")
        if name == "audio":
            self.src = attrs.get()
            self.begin = attrs.get()
            self.dur = attrs.get()
        if name == "textstream":
            self.src = attrs.get()
            self.regin = attrs.get()
    def get_tags (self):
        return (self.tag)
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    #parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(self.width)
