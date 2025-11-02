import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Try to load model
try:
    model = joblib.load('xgboost_house_model.pkl')
    print("Model loaded successfully")
except Exception as e:
    print(f"Model load failed: {e}")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.json
        if 'features' not in data:
            return jsonify({'error': 'Missing features'}), 400

        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({'price': round(float(prediction), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return "House Price API is LIVE! POST to /predict"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
