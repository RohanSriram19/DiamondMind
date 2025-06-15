import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib

print("🔄 Loading data...")
df = pd.read_csv('../data/pitches.csv')

print(f"✅ Data loaded: {df.shape}")

STRIKE_ZONE = {
    "x_min": -0.83,
    "x_max": 0.83,
    "z_min": 1.5,
    "z_max": 3.5
}
strike_data = df.dropna(subset=["plate_x", "plate_z"])
strike_data["is_strike"] = strike_data.apply(
    lambda row: 1 if STRIKE_ZONE["x_min"] <= row["plate_x"] <= STRIKE_ZONE["x_max"] and
                    STRIKE_ZONE["z_min"] <= row["plate_z"] <= STRIKE_ZONE["z_max"]
                else 0,
    axis=1
)

features = [
    "release_speed", "release_pos_x", "release_pos_z", "pfx_x", "pfx_z", "plate_x", "plate_z",
    "vx0", "vy0", "vz0", "ax", "ay", "az", "release_spin_rate", "release_extension"
]
strike_data = strike_data.dropna(subset=features)
X = strike_data[features]
y = strike_data["is_strike"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("🎯 Classification Report (Strike Probability):")
print(classification_report(y_test, y_pred))

joblib.dump(model, "strike_probability_model.pkl")
print("✅ Model saved as strike_probability_model.pkl")
