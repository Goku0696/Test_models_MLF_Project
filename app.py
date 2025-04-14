from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load saved model
model = joblib.load('xgb_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return 'XGBoost Stock (Close) Price Prediction API is running.'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Expecting input in this order: [open, high, low, volume]
        features = data.get('features')

        if features is None or len(features) != 4:
            return jsonify({'error': 'Please provide 4 features: [open, high, low, volume]'}), 400

        features_array = np.array(features).reshape(1, -1)

        prediction = model.predict(features_array)

        return jsonify({
            'predicted_close_price': round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#Example curl command to test
# curl -X POST http://127.0.0.1:5000/predict \
#      -H "Content-Type: application/json" \
#      -d '{"features": [51.83, 52.10, 50.70, 18000000]}'
