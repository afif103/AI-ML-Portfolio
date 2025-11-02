import os
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "House Price API is LIVE! POST to /predict"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if 'features' not in data:
            return jsonify({'error': 'Missing features'}), 400
        
        features = data['features']
        # DUMMY PRICE: (bedrooms * 50k) + (sqft_living * 150) + (bathrooms * 20k)
        price = features[0] * 50000 + features[1] * 150 + features[4] * 20000
        return jsonify({'price': round(float(price), 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
