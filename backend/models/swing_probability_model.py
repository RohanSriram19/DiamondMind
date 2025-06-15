import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib

print("🔄 Loading data...")
df = pd.read_csv('../data/pitches.csv')

print(f"✅ Data loaded: {df.shape}")

swing_labels = [
    "swinging_strike", "foul", "foul_tip", "hit_into_play",
    "foul_bunt", "missed_bunt"
]
df = df[df["description"].notna()]
df["swing"] = df["description"].apply(lambda x: 1 if x in swing_labels else 0)

features = [
    "release_speed", "release_pos_x", "release_pos_z", "pfx_x", "pfx_z", "plate_x", "plate_z",
    "vx0", "vy0", "vz0", "ax", "ay", "az", "release_spin_rate", "release_extension"
]
df = df.dropna(subset=features + ["swing"])
X = df[features]
y = df["swing"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("🎯 Classification Report (Swing Probability):")
print(classification_report(y_test, y_pred))

joblib.dump(model, "swing_probability_model.pkl")
print("✅ Model saved as swing_probability_model.pkl")
