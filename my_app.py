from flask import Flask, render_template, request

app = Flask(__name__, static_folder=".", static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/task/<hypara_set_id>')
def task(hypara_set_id):

    reference1 = "/templates/blue.png"
    reference2 = "/templates/red.png"
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
