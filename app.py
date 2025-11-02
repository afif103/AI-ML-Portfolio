import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model at startup
try:
    model = joblib.load('xgboost_house_model.pkl')
    print("XGBoost model loaded successfully!")
except Exception as e:
    print(f"Model load failed: {e}")
    model = None

@app.route('/', methods=['GET'])
def home():
    if model:
        return "<h1>AI House Price API LIVE</h1><p>XGBoost model loaded & ready!</p>"
    else:
        return "<h1>API Running</h1><p>Warning: Model failed to load</p>", 500

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({"error": "Missing 'features' in JSON"}), 400

        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        price = float(prediction)  # Convert numpy float32 → Python float
        return jsonify({"price": round(price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
