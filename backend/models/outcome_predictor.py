import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import joblib

# Load statcast data
df = pd.read_csv("../data/pitches.csv")

print("✅ Data loaded:", df.shape)

# Drop missing values
df = df.dropna(subset=[
    "description", "release_speed", "release_pos_x", "release_pos_z",
    "zone", "stand", "p_throws", "balls", "strikes", "outs_when_up", "bat_score", "fld_score"
])

# Combine and relabel rare outcomes
replace_map = {
    "foul_bunt": "other_strike",
    "foul_tip": "other_strike",
    "swinging_strike_blocked": "other_strike",
    "hit_by_pitch": "ball",
    "blocked_ball": "ball"
}
df["description"] = df["description"].replace(replace_map)

# Filter low-count outcomes
common_outcomes = df["description"].value_counts()
common_outcomes = common_outcomes[common_outcomes > 30].index
df = df[df["description"].isin(common_outcomes)]
print("🧹 After relabeling and filtering:", df['description'].nunique(), "labels")

# Features and target
features = [
    "release_speed", "release_pos_x", "release_pos_z", "zone", "stand", "p_throws",
    "balls", "strikes", "outs_when_up", "bat_score", "fld_score"
]
X = pd.get_dummies(df[features])
y = df["description"]

# Encode target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Evaluate
y_pred_encoded = model.predict(X_test)
y_pred = label_encoder.inverse_transform(y_pred_encoded)
y_test_labels = label_encoder.inverse_transform(y_test)
print("🎯 Classification Report (Outcome):")
print(classification_report(y_test_labels, y_pred))

# Save model and encoder
joblib.dump(model, "xgb_outcome_model.pkl")
joblib.dump(label_encoder, "xgb_outcome_encoder.pkl")
