from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

classification_model=pickle.load(open('classification_model.pickle','rb'))
regression_model=pickle.load(open('regression_model.pickle','rb'))

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/regression", methods=['POST'])
@cross_origin()
def regression():
    return render_template('regressor.html')

@app.route("/classification", methods=['POST'])
@cross_origin()
def classification():
    return render_template('classifier.html')

@app.route("/temperature",methods=['POST'])
@cross_origin()
def temperature():
    month = int(request.form['month'])
    RH = float(request.form['RH'])
    Ws = float(request.form['Ws'])
    Rain = float(request.form['Rain'])
    FFMC = float(request.form['FFMC'])
    DMC = float(request.form['DMC'])
    DC = float(request.form['DC'])
    ISI = float(request.form['ISI'])
    Class=request.form['class']

    if Class=='Fire':
        fire=1
    else:
        fire=0

    data = {
        "RH": RH,
        "Ws": Ws,
        "Rain": Rain,
        "FFMC": FFMC,
        "DMC": DMC,
        "DC": DC,
        "ISI": ISI,
        "month": month,
        "Class":fire
    }

    pred=regression_model.predict([list(data.values())])
    return render_template('result.html',result=pred[0])

@app.route("/fire",methods=['POST'])
@cross_origin()
def fire():
    month = int(request.form['month'])
    temp = float(request.form['temp'])
    RH = float(request.form['RH'])
    Ws = float(request.form['Ws'])
    Rain = float(request.form['Rain'])
    FFMC = float(request.form['FFMC'])
    DMC = float(request.form['DMC'])
    DC = float(request.form['DC'])
    ISI = float(request.form['ISI'])

    data = {
        "temp": temp,
        "RH": RH,
        "Ws": Ws,
        "Rain": Rain,
        "FFMC": FFMC,
        "DMC": DMC,
        "DC": DC,
        "ISI": ISI,
        "month": month,
    }

    pred=classification_model.predict([list(data.values())])
    if pred[0]==1:
        res="Fire"
    else:
        res="Not Fire"
    return render_template('result.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)








