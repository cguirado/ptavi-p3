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
        self.src_img = ""
        self.src_audio = ""
        self.region = ""
        self.begin_img = ""
        self.begin = ""
        self.dur = ""
        self.regin=""
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
            self.src_img = attrs.get(src_img,"")
            self.region = attrs.get(region,"")
            self.begin_img = attrs.get(begin_img,"")
            self.dur = attrs.get(dur,"")
        if name == "audio":
            self.src_audio = attrs.get(src_audio,"")
            self.begin = attrs.get(begin, "")
            self.dur = attrs.get()
        if name == "textstream":
            self.src = attrs.get()
            self.regin = attrs.get()
    def get_tags (self):
        tagroot = {"width": self.width, "height": self.height, "backgroundcolor": self.backgroundcolor}
        tagregion= {"id": self.id, "top": self.top, "botton": self.botton, "left": self.left, "right": self.right}
        tagimg = {"src_img": self.src_img, "region": self.region, "begin": self.begin, "dur":self.dur}
        tagaudio = {"src_audio": self.src_audio. "begin": self.begin, "dur": self.dur}
        tagtext = {"src": self.src, "regin": self.regin}
        self.tag = [tagroot, tagregion, tagimg, tagaudio, tagtext]
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    #parser.setContentHandler(cHandler)
    datos = cHandlet.get_tags()
    parser.parse(open('karaoke.smil'))
