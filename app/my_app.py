from flask import Flask, render_template, request
import random
from models.models import ImpressionContent,User
from models.database import db_session
from datetime import datetime
from flask import session,redirect,url_for
from app import key
from hashlib import sha256
import glob
import os

app = Flask(__name__, static_folder=".", static_url_path='')
app.secret_key = key.SECRET_KEY

@app.route('/index')
# @app.route("/index")
def index():
    if "user_name" in session:
        name = session["user_name"]
        impression = ImpressionContent.query.all()
        return redirect("task/hypara_test")
    else:
        return redirect(url_for("top"))


@app.route('/redirect')
def redirect_test():
    return redirect("task/hypara_test")

@app.route('/task/hypara_test')
def task():
    if "user_name" in session:
        for k,v in session.items():
            print(k,v)

        hypara_set_id = "hoge"
        try:
            annotator_id = session["user_name"]
        except KeyError:
            annotator_id = "unknown_user"

        lst_image = ['RED.png','BLUE.png','BLUE_GREEN.png','YELLOW.png']
        lst_target = glob.glob('app/templates/Image/targets/*.png')

        reference1 = '/templates/color/' + random.choice(lst_image)
        reference2 = '/templates/color/' + random.choice(lst_image)
        while True:
            if reference1 == reference2:
                reference2 = '/templates/color/' + random.choice(lst_image)
            else:
                break
        
        target = random.choice(lst_target).split('app')[1]

        hyperparameters = {
            'reference_dulation': 300, #msc
            'target_dulation': 300, #ターゲット画像表示時間
            'slider_dulation': 15000,
        } # load from sql table.
        try:
            count = session["count"]
        except KeyError:
            count = 0
        progress = int(count/10)
        return render_template(
            'task.html',
            references=[reference1,reference2],
            target=target,
            annotator_id=annotator_id,
            hypara_set_id=hypara_set_id,
            hyperparameters=hyperparameters,
            progress=progress,
            )
    else:
        return redirect(url_for("top"))
#以下を追加
ll = []
@app.route("/add",methods=["post"])
def add():
    num_touches = request.form['num_touches']
    timestamp = request.form['timestamp']
    num_touches = int(num_touches)
    if num_touches > 0:
        count = session["count"] +1
        session["count"] = count
    else:
        count = session["count"]
        session["count"] = count
    name = request.form['annotator_id']
    reference1 = request.form['reference1']
    reference2 = request.form['reference2']
    target = request.form['target']
    impression = request.form["test5"]
    impression = float(impression)

    content = ImpressionContent(name, reference1,reference2,target, impression,datetime.now(), count, num_touches)
    db_session.add(content)
    db_session.commit()
    ll.append([1])
    n = count
   #print(n)
    if n <= 1000:
        return index()
    else :
        return logout()


@app.route('/submit', methods=['POST'])
def submit():
    reference1 = request.form['reference1']
    reference2 = request.form['reference2']
    target=request.form['target']
    annotator_id = request.form['annotator_id']
    hypara_set_id = request.form['hypara_set_id']
    timestamp = request.form['timestamp']

    print(reference1, reference2, target, annotator_id, hypara_set_id, timestamp)


@app.route("/top")
def top():
    status = request.args.get("status")
    print('os.getcwd()',os.getcwd())
    return render_template("top.html",status=status)


@app.route("/login",methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()

    if user:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            count = ImpressionContent.query.filter_by(name=user_name).count() - ImpressionContent.query.filter_by(name=user_name, num_touches=0).count()
            session["count"] = count
            return (redirect('/task/hypara_test'))#,redirect('/'))
        else:
            return redirect(url_for("top",status="wrong_password"))
    else:
        return redirect(url_for("top",status="user_notfound"))


@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)


@app.route("/registar",methods=["post"])
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer",status="exist_user"))
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        session["count"] = 0
        return redirect(url_for("task"))


@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))


app.run(host='0.0.0.0', port=8080,debug=True)
#app.run(port=8007,debug=True) # ローカルで実行する場合
