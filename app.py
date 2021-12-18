from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
# classifier = joblib.load('emailspam.pkl')
# vector = joblib.load('vector.pkl')

with open('emailspam.pkl', 'rb') as file:
    classifier = pickle.load(file)

with open('vector.pkl', 'rb') as file:
    vector = pickle.load(file)


@app.route('/', methods=['POST', 'GET'])
def emailsspam():
    if request.method == 'POST':
        text = request.form['email_body']
        input_text = vector.transform(text)
        result = classifier.predict(input_text)
        if str(result) == '1':
            return render_template('emailsspam.html', status='danger', result='Spam')
        else:
            return render_template('emailsspam.html', status='success', result='Not Spam')
    
    return render_template('emailsspam.html')


if __name__ == '__main__':
    app.run(debug=True)
