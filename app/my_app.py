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
    lst_target = ['muct_crop_ra/crop_i048ra-mn.png','muct_crop_ra/crop_i041ra-mn.png','muct_crop_ra/crop_i052ra-mn.png','muct_crop_ra/crop_i039ra-fn.png','muct_crop_ra/crop_i005ra-fn.png','muct_crop_ra/crop_i017ra-mg.png','muct_crop_ra/crop_i028ra-mg.png','muct_crop_ra/crop_i023ra-fn.png','muct_crop_ra/crop_i067ra-fn.png','muct_crop_ra/crop_i037ra-fn.png','muct_crop_ra/crop_i035ra-mn.png','muct_crop_ra/crop_i088ra-fn.png','muct_crop_ra/crop_i043ra-mn.png','muct_crop_ra/crop_i022ra-fn.png','muct_crop_ra/crop_i014ra-fn.png','muct_crop_ra/crop_i025ra-mn.png','muct_crop_ra/crop_i051ra-fn.png','muct_crop_ra/crop_i026ra-fn.png','muct_crop_ra/crop_i083ra-mn.png','muct_crop_ra/crop_i016ra-mn.png','muct_crop_ra/crop_i002ra-mn.png','muct_crop_ra/crop_i027ra-mn.png','muct_crop_ra/crop_i069ra-fg.png','muct_crop_ra/crop_i059ra-mg.png','muct_crop_ra/crop_i049ra-mn.png','muct_crop_ra/crop_i003ra-fn.png','muct_crop_ra/crop_i063ra-fn.png','muct_crop_ra/crop_i006ra-mn.png','muct_crop_ra/crop_i082ra-mn.png','muct_crop_ra/crop_i029ra-fg.png','muct_crop_ra/crop_i062ra-fn.png','muct_crop_ra/crop_i081ra-mn.png','muct_crop_ra/crop_i010ra-mn.png','muct_crop_ra/crop_i007ra-fn.png','muct_crop_ra/crop_i013ra-fn.png','muct_crop_ra/crop_i053ra-fg.png','muct_crop_ra/crop_i000ra-fn.png','muct_crop_ra/crop_i071ra-fn.png','muct_crop_ra/crop_i009ra-mn.png','muct_crop_ra/crop_i050ra-fg.png','muct_crop_ra/crop_i061ra-fn.png','muct_crop_ra/crop_i089ra-mn.png','muct_crop_ra/crop_i055ra-mn.png','muct_crop_ra/crop_i012ra-mn.png','muct_crop_ra/crop_i021ra-fn.png','muct_crop_ra/crop_i066ra-mn.png','muct_crop_ra/crop_i036ra-mg.png','muct_crop_ra/crop_i073ra-mg.png','muct_crop_ra/crop_i064ra-mn.png','muct_crop_ra/crop_i019ra-fn.png','muct_crop_ra/crop_i031ra-fn.png','muct_crop_ra/crop_i068ra-mn.png','muct_crop_ra/crop_i004ra-mn.png','muct_crop_ra/crop_i077ra-fn.png','muct_crop_ra/crop_i090ra-mn.png','muct_crop_ra/crop_i033ra-fn.png','muct_crop_ra/crop_i042ra-fn.png','muct_crop_ra/crop_i040ra-mn.png','muct_crop_ra/crop_i078ra-fg.png','muct_crop_ra/crop_i087ra-fn.png','muct_crop_ra/crop_i024ra-fn.png','muct_crop_ra/crop_i020ra-fg.png','muct_crop_ra/crop_i060ra-mn.png','muct_crop_ra/crop_i084ra-mn.png','muct_crop_ra/crop_i070ra-mn.png','muct_crop_ra/crop_i018ra-fn.png','muct_crop_ra/crop_i072ra-fn.png','muct_crop_ra/crop_i038ra-mn.png','muct_crop_ra/crop_i046ra-fn.png','muct_crop_ra/crop_i045ra-mn.png','muct_crop_ra/crop_i075ra-mn.png','muct_crop_ra/crop_i076ra-fn.png','muct_crop_ra/crop_i056ra-mn.png','muct_crop_ra/crop_i080ra-fn.png','muct_crop_ra/crop_i079ra-mn.png','muct_crop_ra/crop_i085ra-mg.png','muct_crop_ra/crop_i034ra-mg.png','muct_crop_ra/crop_i058ra-mn.png','muct_crop_ra/crop_i032ra-fn.png','muct_crop_ra/crop_i086ra-fn.png','muct_crop_ra/crop_i011ra-mn.png','muct_crop_ra/crop_i030ra-fg.png','muct_crop_ra/crop_i044ra-mn.png','muct_crop_ra/crop_i074ra-fn.png','muct_crop_ra/crop_i047ra-mn.png','muct_crop_ra/crop_i054ra-mg.png','muct_crop_ra/crop_i065ra-fn.png','muct_crop_ra/crop_i015ra-mn.png','muct_crop_ra/crop_i001ra-mn.png','muct_crop_ra/crop_i008ra-mn.png','muct_crop_ra/crop_i057ra-fn.png']
    
#     ['muct_crop_ra/crop_i067ra-fn.jpg','muct_crop_ra/crop_i056ra-mn.jpg','muct_crop_ra/crop_i059ra-mg.jpg','muct_crop_ra/crop_i003ra-fn.jpg',
#                   'muct_crop_ra/crop_i051ra-fn.jpg','muct_crop_ra/crop_i075ra-mn.jpg','muct_crop_ra/crop_i019ra-fn.jpg','muct_crop_ra/crop_i089ra-mn.jpg',
#                   'muct_crop_ra/crop_i034ra-mg.jpg','muct_crop_ra/crop_i070ra-mn.jpg','muct_crop_ra/crop_i021ra-fn.jpg','muct_crop_ra/crop_i069ra-fg.jpg',
#                   'muct_crop_ra/crop_i062ra-fn.jpg','muct_crop_ra/crop_i029ra-fg.jpg','muct_crop_ra/crop_i015ra-mn.jpg','muct_crop_ra/crop_i055ra-mn.jpg',
#                   'muct_crop_ra/crop_i045ra-mn.jpg','muct_crop_ra/crop_i049ra-mn.jpg','muct_crop_ra/crop_i084ra-mn.jpg','muct_crop_ra/crop_i065ra-fn.jpg',
#                   'muct_crop_ra/crop_i018ra-fn.jpg','muct_crop_ra/crop_i076ra-fn.jpg','muct_crop_ra/crop_i009ra-mn.jpg','muct_crop_ra/crop_i011ra-mn.jpg',
#                   'muct_crop_ra/crop_i004ra-mn.jpg','muct_crop_ra/crop_i041ra-mn.jpg','muct_crop_ra/crop_i050ra-fg.jpg','muct_crop_ra/crop_i039ra-fn.jpg',
#                   'muct_crop_ra/crop_i038ra-mn.jpg','muct_crop_ra/crop_i071ra-fn.jpg','muct_crop_ra/crop_i078ra-fg.jpg','muct_crop_ra/crop_i017ra-mg.jpg',
#                   'muct_crop_ra/crop_i044ra-mn.jpg','muct_crop_ra/crop_i036ra-mg.jpg','muct_crop_ra/crop_i068ra-mn.jpg','muct_crop_ra/crop_i048ra-mn.jpg',
#                   'muct_crop_ra/crop_i053ra-fg.jpg','muct_crop_ra/crop_i014ra-fn.jpg','muct_crop_ra/crop_i026ra-fn.jpg','muct_crop_ra/crop_i057ra-fn.jpg',
#                   'muct_crop_ra/crop_i073ra-mg.jpg','muct_crop_ra/crop_i042ra-fn.jpg','muct_crop_ra/crop_i023ra-fn.jpg','muct_crop_ra/crop_i005ra-fn.jpg',
#                   'muct_crop_ra/crop_i060ra-mn.jpg','muct_crop_ra/crop_i086ra-fn.jpg','muct_crop_ra/crop_i079ra-mn.jpg','muct_crop_ra/crop_i087ra-fn.jpg',
#                   'muct_crop_ra/crop_i064ra-mn.jpg','muct_crop_ra/crop_i008ra-mn.jpg','muct_crop_ra/crop_i035ra-mn.jpg','muct_crop_ra/crop_i025ra-mn.jpg',
#                   'muct_crop_ra/crop_i043ra-mn.jpg','muct_crop_ra/crop_i047ra-mn.jpg','muct_crop_ra/crop_i081ra-mn.jpg','muct_crop_ra/crop_i024ra-fn.jpg',
#                   'muct_crop_ra/crop_i031ra-fn.jpg','muct_crop_ra/crop_i083ra-mn.jpg','muct_crop_ra/crop_i066ra-mn.jpg','muct_crop_ra/crop_i058ra-mn.jpg',
#                   'muct_crop_ra/crop_i007ra-fn.jpg','muct_crop_ra/crop_i090ra-mn.jpg','muct_crop_ra/crop_i016ra-mn.jpg','muct_crop_ra/crop_i061ra-fn.jpg',
#                   'muct_crop_ra/crop_i080ra-fn.jpg','muct_crop_ra/crop_i020ra-fg.jpg','muct_crop_ra/crop_i063ra-fn.jpg','muct_crop_ra/crop_i085ra-mg.jpg',
#                   'muct_crop_ra/crop_i033ra-fn.jpg','muct_crop_ra/crop_i088ra-fn.jpg','muct_crop_ra/crop_i027ra-mn.jpg','muct_crop_ra/crop_i037ra-fn.jpg',
#                   'muct_crop_ra/crop_i000ra-fn.jpg','muct_crop_ra/crop_i054ra-mg.jpg','muct_crop_ra/crop_i077ra-fn.jpg','muct_crop_ra/crop_i013ra-fn.jpg',
#                   'muct_crop_ra/crop_i006ra-mn.jpg','muct_crop_ra/crop_i001ra-mn.jpg','muct_crop_ra/crop_i052ra-mn.jpg','muct_crop_ra/crop_i040ra-mn.jpg',
#                   'muct_crop_ra/crop_i002ra-mn.jpg','muct_crop_ra/crop_i072ra-fn.jpg','muct_crop_ra/crop_i032ra-fn.jpg','muct_crop_ra/crop_i082ra-mn.jpg',
#                   'muct_crop_ra/crop_i022ra-fn.jpg','muct_crop_ra/crop_i028ra-mg.jpg','muct_crop_ra/crop_i074ra-fn.jpg','muct_crop_ra/crop_i012ra-mn.jpg',
#                   'muct_crop_ra/crop_i010ra-mn.jpg','muct_crop_ra/crop_i030ra-fg.jpg','muct_crop_ra/crop_i046ra-fn.jpg']
# #     ['sketch_264_000305.jpg','02662.jpg','sketch_311_000080.jpg','sketch_206_000010.jpg','05979.jpg','05939.jpg','sketch_267_000502.jpg',
#                   'sketch_244_000045.jpg','00897.jpg','03700.jpg','sketch_303_000165.jpg','sketch_257_000125.jpg','02917.jpg','05740.jpg','03486.jpg',
#                   'sketch_165_000210.jpg','01898.jpg','09160.jpg','sketch_266_000151.jpg','sketch_024_000092.jpg','06852.jpg','04731.jpg','06368.jpg',
#                   'sketch_279_000426.jpg','01921.jpg','sketch_237_000045.jpg','08465.jpg','03025.jpg','sketch_238_000018.jpg','sketch_039_000202.jpg',
#                   '00287.jpg','00716.jpg','00928.jpg','sketch_022_000194.jpg','05453.jpg','sketch_029_000061.jpg','01877.jpg','sketch_109_000249.jpg',
#                   '07845.jpg','06778.jpg','00269.jpg','00407.jpg','sketch_219_000190.jpg','sketch_258_000019.jpg','sketch_254_000057.jpg','sketch_300_000255.jpg',
#                   '05345.jpg','04411.jpg','sketch_219_000011.jpg','sketch_287_000038.jpg','sketch_259_000093.jpg','sketch_104_000141.jpg','07360.jpg','09030.jpg',
#                   'sketch_178_000076.jpg','00793.jpg','06217.jpg','sketch_135_000040.jpg','sketch_103_000037.jpg','sketch_266_000214.jpg','sketch_330_000054.jpg',
#                   'sketch_095_000026.jpg','08323.jpg','sketch_026_000078.jpg','05479.jpg','sketch_102_000144.jpg','04782.jpg','sketch_167_000102.jpg',
#                   'sketch_261_000278.jpg','sketch_279_000024.jpg','sketch_032_000108.jpg','08266.jpg','03481.jpg','00622.jpg','sketch_186_000129.jpg',
#                   'sketch_011_000193.jpg','06288.jpg','04665.jpg','sketch_101_000030.jpg','sketch_252_000334.jpg','01310.jpg','04697.jpg','sketch_121_000203.jpg',
#                   '05205.jpg','02499.jpg','05870.jpg','sketch_072_000083.jpg','sketch_143_000091.jpg','sketch_121_000228.jpg','sketch_010_000102.jpg','sketch_032_000103.jpg',
#                   '01511.jpg','sketch_267_000424.jpg','sketch_273_000666.jpg','09325.jpg','00533.jpg','07841.jpg','04373.jpg','02705.jpg','sketch_248_000318.jpg']

    reference1 = '/templates/colors/' + random.choice(lst_image)
    reference2 = '/templates/colors/' + random.choice(lst_image)
    while True:
        if reference1 == reference2:
            reference2 = '/templates/colors/' + random.choice(lst_image)
        else:
            break

    target = '/templates/Image/' + random.choice(lst_target)

    hyperparameters = {
        'reference_dulation': 300, #msc
        'target_dulation': 300, #ターゲット画像表示時間
        'slider_dulation': 3000,
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

    # progress = request.form["progress"]
    # progress = int(progress)
    # annotator_id = request.form['annotator_id']
    # hypara_set_id = request.form['hypara_set_id']
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


app.run(host='0.0.0.0', port=8000,debug=True)
# app.run(port=8005,debug=True) # ローカルで実行する場合
