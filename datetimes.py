from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# Daylight savings time
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)
print(dt.tzname())

# Standard Time
dt += timedelta(days=7)
print(dt)
print(dt.tzname())