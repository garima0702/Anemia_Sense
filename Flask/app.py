from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/health-tips')
def health_tips():
    return render_template('health_tips.html')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['Gender']
        hemo = float(request.form['Hemoglobin'])
        mch = float(request.form['MCH'])
        mchc = float(request.form['MCHC'])
        mcv = float(request.form['MCV'])

        input_data = np.array([[gender, hemo, mch, mchc, mcv]])
        prediction = model.predict(input_data)[0]
        result = "Anemic" if prediction == 1 else "Not Anemic"
        return render_template('predict.html', prediction_text=result)



if __name__ == '__main__':
    app.run(debug=True)
