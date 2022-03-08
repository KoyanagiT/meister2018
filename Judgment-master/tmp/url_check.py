#URLか確認
import re

url = input("Input URL : ")

if re.match(r"^https?:\/\/", url):
    print("あ、うん。")

else:
    print("value(url) is not URL")
