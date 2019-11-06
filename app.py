from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# トップ画面
@app.route('/')
def index():
    return render_template('index.html')

# get処理の入力フォームを表示
@app.route("/request_get")
def get():
    return render_template('send_get.html')

# getでの入力情報処理
@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name) == 0:
        return "名前が未入力です"
    else:
        return 'あなたが入力した名前は' + str(name) + "です"

# post処理の入力フォームを表示
@app.route("/request_post", methods=["GET"])
def post_sample():
    return render_template('send_post.html')

# postでの入力情報処理
@app.route("/request_post", methods=["POST"])
def post_action():
    if "gender" in request.form.keys():
        gender = request.form["gender"]
        if gender == "男":
            sex = '男性'
        elif gender == "女":
            sex = "女性"
    else:
        sex = '性別不明'

    if 'age' in request.form.keys():
        age_range = request.form['age']
    else:
        age_range = '年齢不詳'
    return f'あなたは{sex}で{age_range}です。'


# テスト環境起動
app.run(debug=True)
