import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

# 🔄 Load data
print("🔄 Loading data...")
df = pd.read_csv('../data/pitches.csv')
print(f"✅ Data loaded: {df.shape}")

# 🧹 Filter rare pitch types
pitch_counts = df['pitch_type'].value_counts()
valid_pitches = pitch_counts[pitch_counts > 1].index
df = df[df['pitch_type'].isin(valid_pitches)]
print(f"🧹 After filtering rare pitch types: {df['pitch_type'].nunique()} types")

# 🎯 Prepare features and labels
X = df.drop(columns=['pitch_type', 'description', 'plate_x', 'plate_z'])
y = df['pitch_type']

# 🎯 Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 🧪 Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 🤖 Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# 📈 Evaluate
y_pred = model.predict(X_test)
print("🎯 Classification Report (XGBoost):")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

# 💾 Save model and encoder
joblib.dump(model, "xgb_pitch_type_model.pkl")
joblib.dump(encoder, "pitch_type_encoder.pkl")
print("💾 Model and encoder saved.")
