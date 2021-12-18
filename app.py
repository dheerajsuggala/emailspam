from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def emailsspam():
    if request.method == 'POST':
        text = request.form['email_body']
        with open('emailspam.pkl', 'rb') as file:
            classifier = pickle.load(file)
        with open('vector.pkl', 'rb') as file:
            vector = pickle.load(file)
        return 'TRUE'
    
    return render_template('emailsspam.html')

@app.route('/b')
def bb():
    with open('var.pkl', 'rb') as file:
        b = pickle.load(file)
    return str(b)

@app.route('/app')
def cc():
    with open('varr.pkl', 'rb') as file:
        b = pickle.load(file)
    return str(b)

if __name__ == '__main__':
    app.run(debug=True)
