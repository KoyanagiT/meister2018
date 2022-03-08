import sys
import hashlib
import requests
import key

def check_hash(data):#,name):
    # ここでdataのハッシュ値を求めて、virus totalに投げる。
    # 危険な場合はTrue、それ以外はFalseを返す。

    SHA256 = hashlib.sha256(data).hexdigest()

    params = {'apikey': key.API_KEY, 'resource': SHA256}
    headers = {
      "Accept-Encoding": "gzip, deflate",
      "User-Agent" : "gzip,  My Python requests library example client or username"
      }

    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
      params=params, headers=headers)

    listlist = response.json()

    #文章作成

    #list-response
    lis = listlist

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
    
    #main sentens(スペルなんか知らない)
    b = lis['positives']
    if b == 0:
        main_result = False#"""
#このfileを検出したエンジンはありません。"""
    else:
    #ここら辺の#は消すだけでおけ
        main_result = True#"""
    #{0}個のエンジンがこのfileを検出しました。
    #{1}さんのアカウントは乗っ取られている可能性があります。""".format(b,name)
    

    sen = """
file:                {0}
最終スキャン:　　　　{1}

    エンジン名 : 結果""".format(lis['resource'],lis["scan_date"])

    #print(main_result)
    #ここ忘れてんな
    #print(sen)

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
        #print("""    {0} : {1}""".format(opop,popo))
        h += 1

    #print("""
#* 検知したエンジンは\"!!!\"を表示します。""")

    return main_result
    
if __name__ == '__main__':
    check_hash(b'hello world')#,"お名前")
