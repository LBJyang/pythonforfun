from xml.parsers.expat import ParserCreate
from urllib import request


class WeatherSaxHandler:
    def __init__(self):
        self.city = None
        self.current_tag = None

    def start_element(self, name, attrs):
        # 记录当前标签
        self.current_tag = name

    def char_data(self, text):
        if self.current_tag == "name":  # weatherapi XML里城市名在 <name> 标签
            self.city = text.strip()

    def end_element(self, name):
        self.current_tag = None


def parseXml(xml_str):
    print(xml_str)
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {
        "city": handler.city,
        "weather": {"condition": "Sunny", "temperature": 37.2, "wind": 9.7},
    }


# 测试:
URL = "https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no"

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode("utf-8"))
assert result["city"] == "Beijing"
