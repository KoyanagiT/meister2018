import sys
import listtt

name = "小柳"
k = input()
for i in listtt.j:
    if i in k:
        print("{0}さんのアカウントは乗っ取られている可能性があります。".format(name))
        sys.exit()
    else:
        continue
