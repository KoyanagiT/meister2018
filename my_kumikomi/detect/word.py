import sys

sentence_list = ['ほげほげだお',"手伝って","てつだって","コンビニエンスストア","こんびにえんすすとあ","iTunes","カード","もらいま","てもいい","といい","ればいい","れば","ために出かけますか","貯蓄に","消息を教える","消息をおしえる","無事なんです","金","なんです","るんです","親友","友達"]

def check_word(data):#,name):
    # dataに特定の単語が含まれていないかをチェック
    # nameに送ってきた相手のアカウント名
    for i in sentence_list:
        if i in data:
            return True#"{0}さんのアカウントは乗っ取られている可能性があります。".format(name)
            sys.exit()
        else:
            continue
    return False

if __name__ == '__main__':
    check_word('ほげほげだお')#,'お名前')
