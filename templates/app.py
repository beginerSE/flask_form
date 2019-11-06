from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.route("/request_get")
def get():
    return render_template('send_get.html')

@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name)==0:
        return "名前が未入力です"
    else:
        return 'あなたが入力した名前は' + str(name) + "です"

if _name__ == __main__:
    app.run(dubug=True)


