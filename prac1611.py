from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print(f"sax:start_element:{name},attrs:{str(attrs)}")

    def end_element(self, name):
        print(f"sax:end_element:{name}")

    def char_data(self, text):
        print(f"sax:char_data:{text}")


xml = r"""<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
"""
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
