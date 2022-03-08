import requests
import json

def main():

        payload = {
                "type":"msg",
                "data":"poo",
                "name":"momo",
                "service":"twitter"
        }
        response = requests.post(
                        'http://127.0.0.1:5000/post',
                        json.dumps(payload),
                        headers={'Content-Type':'application/json'}
                        )
        print(response.text)
        
main()
