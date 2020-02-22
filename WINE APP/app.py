import os
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tableau")
def tableau():
    return render_template('tableau.html')

@app.route("/winePreds")
def winePreds():
    return render_template('winePreds.html')

@app.route('/doShit/', methods=['POST'])
def doShit():
    content = request.json["data"]
    print(content)

    sulphates = content["sulphates"]
    fixedAcidity = content["fixedAcidity"]
    volatileAcidity = content["volatileAcidity"]
    citricAcid = content["citricAcid"]
    alcohol = content["alcohol"]
    residualSugar = content["residualSugar"]
    chlorides = content["chlorides"]
    freeSulfurDioxide = content["freeSulfurDioxide"]
    totalSulfurDioxide = content["totalSulfurDioxide"]
    density = content["density"]
    pH = content["pH"]

    one_pred = [sulphates, fixedAcidity, volatileAcidity, citricAcid, alcohol, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, density, pH]

    print(one_pred)
   
    # load the model from disk
    filename = "static/finalized_model_WHITE.sav"
    load_final_RED = pickle.load(open(filename, 'rb'))
    result = load_final_RED.predict_proba([one_pred])

    
    return jsonify({"prediction" : result.tolist()})



if __name__ == "__main__":
    app.run(debug=True)