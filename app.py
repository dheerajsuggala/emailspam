from flask import Flask, render_template, request
import __main__
__main__.FlexibleScalar = FlexibleScalar
import joblib


app = Flask(__name__)
classifier = joblib.load('emailspam.pkl')
vector = joblib.load('vector.pkl')


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
