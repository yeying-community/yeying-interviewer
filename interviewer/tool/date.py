from datetime import datetime, timedelta

from dateutil import parser
from dateutil import tz


def getCurrentUtcDateTime():
    return convertToUtcDateTime(datetime.now())


def getCurrentUtcString():
    return formatDateTime(getCurrentUtcDateTime())


def parseDateTime(s):
    return parser.isoparse(s)


def isExpired(s, minutes):
    # 解析ISO字符串
    time_parsed = parseDateTime(s)

    # 获取当前时间并保留时区信息
    now = datetime.now(time_parsed.tzinfo)

    # 计算5分钟之后的时间
    five_minutes_later = time_parsed + timedelta(minutes=minutes)

    # 比较时间，判断是否超过5分钟之后
    return now > five_minutes_later


def formatDateTime(dt):
    formatted_dt = dt.isoformat(timespec='milliseconds')
    return formatted_dt.replace('+00:00', 'Z')


def convertToLocalDateTime(dt):
    return dt.astimezone(tz.tzlocal())


def convertToUtcDateTime(dt):
    return dt.astimezone(tz.tzutc())
