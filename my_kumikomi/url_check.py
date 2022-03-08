#URLか確認
import re

def url_checker(val):
    if re.match(r"^https?:\/\/", val):
        return True
    else:
        return False

lis={"type": "msg",
    "data": "hello",
    "name": "akakou",
    "service": "line"}
j=lis["data"]
print(url_checker(j))
