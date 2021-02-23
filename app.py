# pip3
# pip3 install flask
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name="Dr.Maheshwari.A"
    return render_template('contact.html',name=name)

@app.route('/contact1', methods=['POST'])
def contact1():
    name="Mr.Pramesh"
    return render_template('contact.html',name=name)

@app.route('/contact2', methods=['POST'])
def contact2():
    name="Mr.Mithun"
    return render_template('contact.html',name=name)

@app.route('/contact3', methods=['POST'])
def contact3():
    name="Dr.Saravanan"
    return render_template('contact.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)