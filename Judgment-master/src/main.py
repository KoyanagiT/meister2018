from flask import Flask, request, jsonify
import json
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
            "hit": True,
            "msg": "poo",
            "name":"momo",
            "Service":"twitter"
        }

        return jsonify(result)


if __name__ =='__main__':
    app.run(debug=True)
