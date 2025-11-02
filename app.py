import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# HOME PAGE
@app.route('/', methods=['GET'])
def home():
    return "House Price API is LIVE! POST to /predict"

# PREDICT ENDPOINT — CRITICAL!
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        if not data or 'features' not in data:
            return jsonify({'error': 'Send {"features": [3,2000,8000,1500,2]}'}), 400

        features = data['features']
        if len(features) != 5:
            return jsonify({'error': 'Need 5 features'}), 400

        # DUMMY PRICE
        price = features[0] * 50000 + features[1] * 150 + features[4] * 20000
        return jsonify({'price': round(price, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# RENDER PORT
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
