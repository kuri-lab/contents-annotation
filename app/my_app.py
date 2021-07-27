from flask import Flask, render_template, request
import random
from models.models import ImpressionContent
#以下を追加
from models.database import db_session
from datetime import datetime

app = Flask(__name__, static_folder=".", static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/task/<hypara_set_id>')
def task(hypara_set_id):

    lst_image = ['green.png','blue.png','red.png','white.png','bluepurple.png','purple.png','yellow.png','yellowred.png']


    reference1 = '/templates/' + random.choice(lst_image)
    reference2 = '/templates/' + random.choice(lst_image)
    while True:
        if reference1 == reference2:
            reference2 = '/templates/' + random.choice(lst_image)
        else:
            break
    target = "/templates/cat.png"
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
    reference1 = request.form['reference1']
    reference2 = request.form['reference2']
    target = request.form['target']
    ref1 = request.form["test5"]
    ref1 = float(ref1)
    ref2 = - ref1
    # annotator_id = request.form['annotator_id']
    # hypara_set_id = request.form['hypara_set_id']
    content = ImpressionContent(reference1,reference2,target, ref1,ref2,datetime.now())
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

app.run(port=8000,debug=True)