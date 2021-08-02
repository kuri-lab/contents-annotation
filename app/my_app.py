from flask import Flask, render_template, request
import random
from models.models import ImpressionContent,User
#以下を追加
from models.database import db_session
from datetime import datetime
from flask import session,redirect,url_for
from app import key
from hashlib import sha256

app = Flask(__name__, static_folder=".", static_url_path='')
app.secret_key = key.SECRET_KEY

@app.route('/')
# @app.route("/index")
def index():
    if "user_name" in session:
        name = session["user_name"]
        impression = ImpressionContent.query.all()
        return redirect(url_for("/task/<hypara_set_id>"))
    else:
        return redirect(url_for("top"))
# def index():
#     return app.send_static_file('index.html')

@app.route('/task/<hypara_set_id>')
def task(hypara_set_id):

    lst_image = ['green.png','blue.png','red.png','white.png','bluepurple.png','purple.png','yellow.png','yellowred.png']
    lst_target = ['dog.png','kyusu.png','cat.png','yakan.png','rabbit.png']


    reference1 = '/templates/' + random.choice(lst_image)
    reference2 = '/templates/' + random.choice(lst_image)
    while True:
        if reference1 == reference2:
            reference2 = '/templates/' + random.choice(lst_image)
        else:
            break
    target = '/templates/' + random.choice(lst_target)
    annotator_id = "Anno_test"

    hyperparameters = {
        'reference_dulation': 2000, #msec
        'target_dulation': 2000,
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
    name = session.get('user_name', None)
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
            return (redirect(url_for("add")),redirect(url_for("index")))
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


app.run(port=8000,debug=True)
