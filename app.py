import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the REAL model
try:
    model = joblib.load('xgboost_house_model.pkl')
    print("XGBoost model loaded successfully!")
except Exception as e:
    print(f"Model load failed: {e}")
    model = None

@app.route('/', methods=['GET'])
def home():
    return "<h1>AI House Price API is LIVE!</h1><p>POST to /predict with real XGBoost model</p>"

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({"error": "Invalid JSON: send {'features': [3,2000,8000,1500,2]}"}), 400

        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        
        # Convert numpy float32 → Python float
        price = float(prediction)
        return jsonify({"price": round(price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
