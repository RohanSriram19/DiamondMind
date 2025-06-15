import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_predict_type():
    url = f"{BASE_URL}/predict/type"
    data = {
        "features": [92.3, -1.7, 6.5, 5, 1, 0, 1, 0]  # example with 8 numeric features
    }
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_predict_type():
    url = f"{BASE_URL}/predict/type"
    data = {
        "features": [92.3, -1.7, 6.5, 5, 1, 0, 1, 0]  # 8 numeric features for pitch type
    }
    response = requests.post(url, json=data)
    print("Predict Type Response:", response.json())

def test_predict_outcome():
    url = f"{BASE_URL}/predict/outcome"
    data = {
        "features": [92.3, -1.7, 6.5, 5, 1, 0, 1, 0, 0, 1, 2, 0, 1]  # 13 numeric features for outcome
    }
    response = requests.post(url, json=data)
    print("Predict Outcome Response:", response.json())

def test_predict_location():
    url = f"{BASE_URL}/predict/location"
    data = {
        "features": {
            "release_speed": 92.3,
            "release_pos_x": -1.7,
            "release_pos_z": 6.5,
            "pfx_x": -1.9,
            "pfx_z": 4.5,
            "spin_rate": 2200,
            "release_extension": 5.8,
            "vx0": 5.1,
            "vy0": -130.5,
            "vz0": -9.3
        }
    }
    response = requests.post(url, json=data)
    print("Predict Location Response:", response.json())

def test_predict_swing():
    url = f"{BASE_URL}/predict/swing"
    data = {
        "features": [92.3, -1.7, 6.5, -1.9, 4.5, 1.2, 5.8, 5.1, -130.5, -9.3, 0.1, 0.2, 0.3, 2200, 0.4]  # 15 features
    }
    response = requests.post(url, json=data)
    print("Predict Swing Response:", response.json())

def test_predict_strike():
    url = f"{BASE_URL}/predict/strike"
    data = {
        "features": [92.3, -1.7, 6.5, -1.9, 4.5, 0.1, 2.3, 5.1, -130.5, -9.3, 0.1, 0.2, 0.3, 2200, 0.4]  # 15 features
    }
    response = requests.post(url, json=data)
    print("Predict Strike Response:", response.json())

if __name__ == "__main__":
    test_predict_type()
    test_predict_outcome()
    test_predict_location()
    test_predict_swing()
    test_predict_strike()
