#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
            self.id = attrs.get()
            self.top = attrs.get()
            self.botton = attrs.get()
            self.left = attrs.get()
            self.right = attrs.get()
        if name == "img":
            self.src = attrs.get()
            self.region = attrs.get()
            self.begin = attrs.get()
            self.dur = attrs.get()
        if name == "audio":
            self.src = attrs.get()
            self.begin = attrs.get()
            self.dur = attrs.get()
        if name == "textstream":
            self.src = attrs.get()
            self.regin = attrs.get()
