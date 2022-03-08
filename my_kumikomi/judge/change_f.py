import Siraikuroko_desuno
import sys

#list-response
lis = Siraikuroko_desuno.listlist

#response_code(ほとんど使われない)
aaaw = lis["response_code"]
if aaaw == -2:
    print("""要求されたアイテムが、まだ分析のためにキューに入れられています。

file:    {0}""".format(lis["resource"]))
    sys.exit()
if aaaw == 0:
    print("""検索したアイテムがVirusTotalのデータセットに存在しないようです。

file:    {0}""".format(lis["resource"]))
    sys.exit()

name = "小柳"
#main sentens(スペルなんか知らない)
b = lis['positives']
if b == 0:
    main_result = """
このfileを検出したエンジンはありません。"""
else:
    main_result = """
    {0}個のエンジンがこのfileを検出しました。
    {1}さんのアカウントは乗っ取られている可能性があります。""".format(b,name)
    

sen = """
file:                {0}
最終スキャン:　　　　{1}

    エンジン名 : 結果""".format(lis['resource'],lis["scan_date"])

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
