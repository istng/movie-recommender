from flask import Flask, render_template, request
import os

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '20190803005945_1.jpg')
    return render_template("index.html")


@app.route('/submitted', methods=["GET", "POST"])
def show_submission():
    req = request.form
    return render_template("index.html")

"""
@app.route('/testing/<thing>')
def do_thing(thing):
    return str(thing)
"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

