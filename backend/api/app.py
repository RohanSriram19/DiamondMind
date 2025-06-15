import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load models and encoders
type_model = joblib.load('../models/xgb_pitch_type_model.pkl')
type_encoder = joblib.load('../models/xgb_pitch_type_encoder.pkl')

outcome_model = joblib.load('../models/xgb_outcome_model.pkl')
outcome_encoder = joblib.load('../models/xgb_outcome_encoder.pkl')

location_x_model = joblib.load('../models/pitch_loc_x.pkl')
location_z_model = joblib.load('../models/pitch_loc_z.pkl')
location_features = joblib.load('../models/location_features.pkl')  # list of feature names

swing_model = joblib.load('../models/swing_probability_model.pkl')
strike_model = joblib.load('../models/strike_probability_model.pkl')


@app.route('/predict/type', methods=['POST'])
def predict_pitch_type():
    data = request.get_json()
    features = np.array(data.get('features', [])).reshape(1, -1)
    expected_features = type_model.n_features_in_
    if features.shape[1] != expected_features:
        return jsonify({
            'error': f'Feature count mismatch. Expected {expected_features} features, but got {features.shape[1]}'
        }), 400
    pred = type_model.predict(features)
    label = type_encoder.inverse_transform(pred)[0]
    return jsonify({'pitch_type_prediction': label})


@app.route('/predict/outcome', methods=['POST'])
def predict_pitch_outcome():
    data = request.get_json()
    features = np.array(data.get('features', [])).reshape(1, -1)
    expected_features = outcome_model.n_features_in_
    if features.shape[1] != expected_features:
        return jsonify({
            'error': f'Feature count mismatch. Expected {expected_features} features, but got {features.shape[1]}'
        }), 400
    pred = outcome_model.predict(features)
    label = outcome_encoder.inverse_transform(pred)[0]
    return jsonify({'pitch_outcome_prediction': label})


@app.route('/predict/location', methods=['POST'])
def predict_location():
    print("---- /predict/location called ----")
    data = request.get_json()
    feature_dict = data.get('features', {})
    print("Feature dict received:", feature_dict)
    print("location_features:", location_features)
    features = [feature_dict.get(f, 0) for f in location_features]
    print("Features vector built:", features)
    features = np.array(features).reshape(1, -1)
    try:
        pred_x = float(location_x_model.predict(features)[0])  # Convert to Python float
        pred_z = float(location_z_model.predict(features)[0])  # Convert to Python float
        print("Predicted X:", pred_x, "Predicted Z:", pred_z)
        return jsonify({'plate_x': pred_x, 'plate_z': pred_z})
    except Exception as e:
        print("Prediction failed with exception:", repr(e))
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


@app.route('/predict/swing', methods=['POST'])
def predict_swing():
    data = request.get_json()
    features = np.array(data.get('features', [])).reshape(1, -1)
    expected_features = swing_model.n_features_in_
    if features.shape[1] != expected_features:
        return jsonify({
            'error': f'Feature count mismatch. Expected {expected_features} features, but got {features.shape[1]}'
        }), 400
    prob = swing_model.predict_proba(features)[0][1]
    return jsonify({'swing_probability': float(prob)})


@app.route('/predict/strike', methods=['POST'])
def predict_strike():
    data = request.get_json()
    features = np.array(data.get('features', [])).reshape(1, -1)
    expected_features = strike_model.n_features_in_
    if features.shape[1] != expected_features:
        return jsonify({
            'error': f'Feature count mismatch. Expected {expected_features} features, but got {features.shape[1]}'
        }), 400
    prob = strike_model.predict_proba(features)[0][1]
    return jsonify({'strike_probability': float(prob)})


@app.route('/')
def home():
    return "DiamondMind API is running!"


if __name__ == '__main__':
    app.run(debug=True)
