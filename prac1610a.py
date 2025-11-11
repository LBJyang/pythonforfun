from urllib import request
import json


def fetch_data(url):
    resp = request.urlopen(url)
    return json.loads(resp.read().decode("utf-8"))


# 测试
URL = "https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no"
data = fetch_data(URL)
print(data)
assert data["location"]["name"] == "Beijing"
print("ok")
