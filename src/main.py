from flask import Flask, request, jsonify
import json
from detect import detect
import base64

app = Flask(__name__)

@app.route('/post', methods=["GET","POST"])
def main():
    if request.method !='POST':
        print("error")
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return (jsonify(res='error'), 400)
    else:
        print(request.json)
        result = {
            "hit": False,
            "msg": "foo"
        }

        
        hit = detect.detect(request.json)
        result["hit"] = hit
        
        print(result)
        return jsonify(result)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

