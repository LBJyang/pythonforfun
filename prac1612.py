import requests
from bs4 import BeautifulSoup

# 1. 获取网页 HTML
url = "https://www.python.org/events/python-events/"
response = requests.get(url)
html = response.text

# 2. 用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, "html.parser")

# 3. 找到会议列表
# Python 官网会议页面，事件列表在 <ul class="list-recent-events menu"> 中
events_list = soup.find("ul", class_="list-recent-events menu")
if not events_list:
    print("没有找到会议列表！")
else:
    events = events_list.find_all("li")
    for event in events:
        # 时间
        time_tag = event.find("time")
        time_text = time_tag.get_text(strip=True) if time_tag else "未知时间"

        # 名称
        name_tag = event.find("a")
        name_text = name_tag.get_text(strip=True) if name_tag else "未知名称"

        # 地点
        location_tag = event.find("span", class_="event-location")
        location_text = (
            location_tag.get_text(strip=True) if location_tag else "未知地点"
        )

        print(f"{time_text} | {name_text} | {location_text}")
