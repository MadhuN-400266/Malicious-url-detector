#app.py
from flask import Flask, render_template, request
import numpy as np
from feature import FeatureExtraction
import pickle  # if you saved your trained model

# Load your trained model
with open("newmodel.pkl", "rb") as f:
    gbc = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # web page for input

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # Extract features
    obj = FeatureExtraction(url)
    features = obj.getFeaturesList()
    
    # Pad/truncate to 30
    if len(features) < 30:
        features += [0] * (30 - len(features))
    else:
        features = features[:30]
        
    x = np.array(features).reshape(1,30)
    
    # Predict
    y_pred = gbc.predict(x)[0]
    if y_pred == 1:
        result = "It is a safe website ✅"
    else:
        result = "Caution! Suspicious website detected ⚠️"
    
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
