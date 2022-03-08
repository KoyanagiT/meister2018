import Judgment_desuno
import sys
from urllib.parse import urlparse

#list-response
lis = Judgment_desuno.listlist

#response_code(ほとんど使われない)
aaaw = lis["response_code"]
if aaaw == -2:
    print("""要求されたアイテムが、まだ分析のためにキューに入れられています。

URL:    {0}""".format(lis["resource"]))
    sys.exit()
if aaaw == 0:
    print("""検索したアイテムがVirusTotalのデータセットに存在しないようです。

URL:    {0}""".format(lis["resource"]))
    sys.exit()

#host
access_url = lis["url"]
parsed_url = urlparse(access_url)
host = parsed_url.netloc

#main sentens(スペルなんか知らない)
b = lis['positives']
if b == 0:
    main_result = """
このURLを検出したエンジンはありません。"""
else:
    main_result = """
    {0}個のエンジンがこのURLを検出しました。""".format(b)
    

sen = """
URL: 　　　　　　　　{0}
ホスト:　　　　　　　{1}
最終スキャン:　　　　{2}

    エンジン名 : 結果""".format(lis["url"],host,lis["scan_date"])

print(main_result)
print(sen)

#エンジンの表示
def force_of_sudo(b):
    a = lis['scans']
    a = list(a.values())
    c = a[b]
    if c['detected'] == True:
        s = "!!!"
    else:
        s = "-"
    return s

def force_of_ukon(q):
    g = lis['scans']
    g = list(g.keys())
    k = g[q]
    return k

scaners = lis['scans']
h = 0
numb = len(scaners)
while h < numb:
    popo = force_of_sudo(h)
    opop = force_of_ukon(h)
    print("""    {0} : {1}""".format(opop,popo))
    h += 1

print("""
* 検知したエンジンは\"!!!\"を表示します。""")
