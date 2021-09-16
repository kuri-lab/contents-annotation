from flask import Flask, render_template, request
import random
from models.models import ImpressionContent,User
from models.database import db_session
from datetime import datetime
from flask import session,redirect,url_for
from app import key
from hashlib import sha256

from glob import glob
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
    for k,v in session.items():
        print(k,v)

    hypara_set_id = "hoge"
    try:
        annotator_id = session["user_name"]
    except KeyError:
        annotator_id = "unknown_user"

    lst_image = ['green.png','blue.png','red.png','yellow.png',]
#                  'purple.png','black.png',,'white.png','bluepurple.png','yellowred.png'

#     # なぜかうまくいかない ?????
#     lst_image = [os.path.basename(r) for r in glob('/templates/colors/*')]

    # tezuka 50 domainnet 50 をランダムに選んだ。合計100こ
    lst_target = ['sketch_264_000305.jpg','02662.jpg','sketch_311_000080.jpg','sketch_206_000010.jpg','05979.jpg','05939.jpg','sketch_267_000502.jpg',
                  'sketch_244_000045.jpg','00897.jpg','03700.jpg','sketch_303_000165.jpg','sketch_257_000125.jpg','02917.jpg','05740.jpg','03486.jpg',
                  'sketch_165_000210.jpg','01898.jpg','09160.jpg','sketch_266_000151.jpg','sketch_024_000092.jpg','06852.jpg','04731.jpg','06368.jpg',
                  'sketch_279_000426.jpg','01921.jpg','sketch_237_000045.jpg','08465.jpg','03025.jpg','sketch_238_000018.jpg','sketch_039_000202.jpg',
                  '00287.jpg','00716.jpg','00928.jpg','sketch_022_000194.jpg','05453.jpg','sketch_029_000061.jpg','01877.jpg','sketch_109_000249.jpg',
                  '07845.jpg','06778.jpg','00269.jpg','00407.jpg','sketch_219_000190.jpg','sketch_258_000019.jpg','sketch_254_000057.jpg','sketch_300_000255.jpg',
                  '05345.jpg','04411.jpg','sketch_219_000011.jpg','sketch_287_000038.jpg','sketch_259_000093.jpg','sketch_104_000141.jpg','07360.jpg','09030.jpg',
                  'sketch_178_000076.jpg','00793.jpg','06217.jpg','sketch_135_000040.jpg','sketch_103_000037.jpg','sketch_266_000214.jpg','sketch_330_000054.jpg',
                  'sketch_095_000026.jpg','08323.jpg','sketch_026_000078.jpg','05479.jpg','sketch_102_000144.jpg','04782.jpg','sketch_167_000102.jpg',
                  'sketch_261_000278.jpg','sketch_279_000024.jpg','sketch_032_000108.jpg','08266.jpg','03481.jpg','00622.jpg','sketch_186_000129.jpg',
                  'sketch_011_000193.jpg','06288.jpg','04665.jpg','sketch_101_000030.jpg','sketch_252_000334.jpg','01310.jpg','04697.jpg','sketch_121_000203.jpg',
                  '05205.jpg','02499.jpg','05870.jpg','sketch_072_000083.jpg','sketch_143_000091.jpg','sketch_121_000228.jpg','sketch_010_000102.jpg','sketch_032_000103.jpg',
                  '01511.jpg','sketch_267_000424.jpg','sketch_273_000666.jpg','09325.jpg','00533.jpg','07841.jpg','04373.jpg','02705.jpg','sketch_248_000318.jpg']

    reference1 = '/templates/colors/' + random.choice(lst_image)
    reference2 = '/templates/colors/' + random.choice(lst_image)
    while True:
        if reference1 == reference2:
            reference2 = '/templates/colors/' + random.choice(lst_image)
        else:
            break

    target = '/templates/Image/sample_target/' + random.choice(lst_target)

    hyperparameters = {
        'reference_dulation': 300, #msc
        'target_dulation': 300, #ターゲット画像表示時間
        'slider_dulation': 3000,
    } # load from sql table.
    count = session["count"]
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

#以下を追加
ll = []
@app.route("/add",methods=["post"])
def add():
    num_touches = request.form['num_touches']
    timestamp = request.form['timestamp']
    if num_touches > 0:
        count = session["count"] +1
        session["count"] = count

    name = request.form['annotator_id']
    reference1 = request.form['reference1']
    reference2 = request.form['reference2']
    target = request.form['target']
    impression = request.form["test5"]
    impression = float(impression)

    # progress = request.form["progress"]
    # progress = int(progress)
    # annotator_id = request.form['annotator_id']
    # hypara_set_id = request.form['hypara_set_id']
    content = ImpressionContent(name, reference1,reference2,target, impression,datetime.now())
    db_session.add(content)
    db_session.commit()
    ll.append([1])
    n = len(ll)
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
            session["count"] = 0
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


app.run(host='0.0.0.0', port=8000,debug=True)
