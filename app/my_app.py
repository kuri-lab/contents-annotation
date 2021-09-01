from flask import Flask, render_template, request
import random
from models.models import ImpressionContent,User
from models.database import db_session
from datetime import datetime
from flask import session,redirect,url_for
from app import key
from hashlib import sha256
import os
from glob import glob

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
# @app.route("/index")
# def redirect2():
#     #print("test")
#     print("test" + url_for("task"))
#     return redirect("/task")

def redirect_test():
    return redirect("task/hypara_test")

# def index():
#     return app.send_static_file('index.html')
@app.route('/task/hypara_test')
def task():
    hypara_set_id = "hoge"
    try:
        annotator_id = session["user_name"]
    except KeyError:
        annotator_id = "unknown_user"
    
    lst_image = ['green.png','blue.png','red.png','white.png','bluepurple.png','purple.png','yellow.png','yellowred.png']
    
    lst_target  = ['03989.jpg','08789.jpg','08146.jpg','04071.jpg','07216.jpg','08668.jpg','08491.jpg','09208.jpg','02213.jpg','03590.jpg',
                   '01993.jpg','03109.jpg','06626.jpg','06518.jpg','08858.jpg','07250.jpg','02261.jpg','02141.jpg','03924.jpg','06510.jpg',
                   '06252.jpg','06250.jpg','07912.jpg','01764.jpg','08184.jpg','09132.jpg','00817.jpg','07918.jpg','03873.jpg','01670.jpg',
                   '06344.jpg','03026.jpg','04652.jpg','06774.jpg','05875.jpg','03229.jpg','08223.jpg','06095.jpg','08273.jpg','06663.jpg',
                   '05274.jpg','08116.jpg','04126.jpg','05846.jpg','01897.jpg','00150.jpg','00289.jpg','03544.jpg','09339.jpg','04057.jpg']
    
<<<<<<< HEAD
    for f in glob('/templates/target/*'):
        lst_target.append(os.path.split(f)[1])
=======
#     for f in glob('/templates/target/*'):
#         lst_target.append(os.path.split(f)[1])
>>>>>>> 7bb079bf76ba5fa2d75c24ef4b506ff4f8ec8e32
    
    reference1 = '/templates/color/' + random.choice(lst_image)
    reference2 = '/templates/color/' + random.choice(lst_image)
    while True:
        if reference1 == reference2:
            reference2 = '/templates/' + random.choice(lst_image)
        else:
            break
    
    target = '/templates/target/' + random.choice(lst_target)

    hyperparameters = {
        'reference_dulation': 2000, #
        'target_dulation': 100, #ターゲット画像表示時間
        'slider_dulation': 4000,
    } # load from sql table.

    return render_template(
        'task.html',
        references=[reference1,reference2],
        target=target,
        annotator_id=annotator_id,
        hypara_set_id=hypara_set_id,
        hyperparameters=hyperparameters,
        )

#以下を追加
@app.route("/add",methods=["post"])
def add():
    name = request.form['annotator_id']
    reference1 = request.form['reference1']
    reference2 = request.form['reference2']
    target = request.form['target']
    ref1 = request.form["test5"]
    ref1 = float(ref1)
    ref2 = - ref1
    # annotator_id = request.form['annotator_id']
    # hypara_set_id = request.form['hypara_set_id']
    content = ImpressionContent(name, reference1,reference2,target, ref1,ref2,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()


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
        return redirect(url_for("task"))


@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))


app.run(host='0.0.0.0', port=8000,debug=True)
