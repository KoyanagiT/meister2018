import hash
import url
import word
import re

def detect(dict_para):
    # リクエストのデータを元に、
    # 危険ならtrue、危険でなければfalseを返す
    data = dict_para["data"]
    
    result_1 = word.check_word(data)#,dict_para["name"])

    if re.match(r"^https?:\/\/", data) == True:

        result = url.check_url(data)#,dict_para["name"])
        return result

    else:
        if dict_para["type"] == "msg":

            return result_1

        #バイナリデータでないといけない
        else:

            result = hash.check_hash(data)#,dict_para["name"])

            return result

    # result = url.check_hash()みたいな感じで動く
