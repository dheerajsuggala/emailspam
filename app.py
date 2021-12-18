from flask import Flask, render_template, request
import dill
import string
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def emailsspam():
    if request.method == 'POST':
        print('------------------>>>>>>1')
        text = request.form['email_body']
        with open('vector.joblib','rb') as io:
            vector=dill.load(io)
        with open('classifier.joblib','rb') as io:
            classifier=dill.load(io)
        print('------------------>>>>>>2', text)
        import string
        print(string.ascii_letters)
        input_text = vector.transform([text])
        print('------------------>>>>>>3')
        result = classifier.predict(input_text)
        print('------------------>>>>>>',str(result[0]))
        if str(result[0]) == '1':
            return render_template('emailsspam.html', status='danger', result='Spam')
        else:
            return render_template('emailsspam.html', status='success', result='Not Spam')   
    
    return render_template('emailsspam.html')



if __name__ == '__main__':
    app.run(debug=True)
