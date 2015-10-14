#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__ (self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.botton = ""
        self.left = ""
        self.right = ""
        self.src_img = ""
        self.region_img = ""
        self.begin_img = ""
        self.dur_img = ""
        self.src_audio = ""
        self.begin = ""
        self.dur = ""
        self.src = ""
        self.region = ""

        self.tags = []

#No necesitamos endElement (solo tenemos principio de etiqueta)
    def startElement(self, name, attrs):
        if name == "root-layout":
        #valores de los atributos"
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('background-color',"")
            tagroot = {"width": self.width, "height": self.height, "background-color": self.backgroundcolor}
            self.tags.append([name, tagroot])

        if name == "region":
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.botton = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            tagregion = {"id": self.id, "top": self.top, "bottom": self.botton, "left": self.left, "right": self.right}
            self.tags.append([name,tagregion])
        if name == "img":
            self.src_img = attrs.get('src',"")
            self.region_img = attrs.get('region',"")
            self.begin_img = attrs.get('begin',"")
            self.dur_img = attrs.get('dur',"")
            tagimg = {"src": self.src_img, "region": self.region_img, "begin": self.begin_img, "dur":self.dur_img}
            self.tags.append([name,tagimg])
        if name == "audio":
            self.src_audio = attrs.get('src',"")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur',"")
            tagaudio = {"src": self.src_audio, "begin": self.begin, "dur": self.dur}
            self.tags.append([name,tagaudio])
        if name == "textstream":
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            tagtext = {"src": self.src, "region": self.region}
            self.tag.append([name,tagtext])
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
