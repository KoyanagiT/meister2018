#VirusTotalに送る
import requests
import key

url = 'https://www.virustotal.com/vtapi/v2/url/report'
reso = input("url: ")

params = {'apikey': key.API_KEY,
          'resource':reso}

response = requests.get(url, params=params)

listlist = response.json()
