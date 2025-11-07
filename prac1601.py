# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    m = re.match(r"^UTC([+-]\d+):00", tz_str)
    tz_hour = int(m.group(1))
    tz_info = timezone(timedelta(hours=tz_hour))
    targettime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz_info)
    return targettime.timestamp()


# 测试:
t1 = to_timestamp("2015-6-1 08:10:30", "UTC+7:00")
assert t1 == 1433121030.0, t1

t2 = to_timestamp("2015-5-31 16:10:30", "UTC-09:00")
assert t2 == 1433121030.0, t2

print("ok")

# utc_dt = datetime.now(timezone.utc)
# bj_time = utc_dt.astimezone(timezone(timedelta(hours=8)))
# tokyo_time = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(f"beijing time is:{bj_time}")
# print(f"tokyo time is:{tokyo_time}")
# tokyo_time2 = bj_time.astimezone(timezone(timedelta(hours=9)))
# print(f"tokyo time is:{tokyo_time2}")

# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# print(now)


# print(type(now))
# print(f"现在的timestamp是：{now.timestamp()}")

# dt = datetime(2015, 4, 19, 12, 20, 30)
# print(dt)
# print(f"dt的timestamp是:{dt.timestamp()}")

# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# cday = datetime.strptime("2025-11-11 10:02:31", "%Y-%m-%d %H:%M:%S")
# print(f"strptime:{cday}")

# print(now.strftime("%a, %b %d %H:%M"))
