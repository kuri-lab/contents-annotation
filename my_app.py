from flask import Flask, render_template

app = Flask(__name__, static_folder=".", static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/task')
def task():

    reference1 = "templates/blue.png"
    reference2 = "templates/red.png"
    target = "templates/cat.png"
    annotator_id = "Anno_test"

    return render_template('task.html',references=[reference1,reference2],target=target,annotator_id=annotator_id)
app.run(port=8000,debug=True)
