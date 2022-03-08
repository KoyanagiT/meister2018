#VirusTotalに送る
import requests
import key

params = {'apikey': key.API_KEY, 'resource': '7657fcb7d772448a6d8504e4b20168b8'}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }

response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)

listlist = response.json()
