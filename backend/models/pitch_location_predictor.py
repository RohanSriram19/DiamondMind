import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

print("🔄 Loading data...")
df = pd.read_csv('../data/pitches.csv')

print(f"✅ Data loaded: {df.shape}")

# Drop rows with missing pitch location
df = df.dropna(subset=['plate_x', 'plate_z'])

# Define features for pitch location regression
X_columns = ['release_speed', 'release_pos_x', 'release_pos_z', 'pfx_x', 'pfx_z',
             'spin_rate', 'release_extension', 'vx0', 'vy0', 'vz0']
X_columns = [col for col in X_columns if col in df.columns]

# Save the feature list for consistency with API
joblib.dump(X_columns, '../models/location_features.pkl')

X = df[X_columns]
y_x = df['plate_x']
y_z = df['plate_z']

# Train/test split
X_train, X_test, y_train_x, y_test_x = train_test_split(X, y_x, test_size=0.2, random_state=42)
_, _, y_train_z, y_test_z = train_test_split(X, y_z, test_size=0.2, random_state=42)

# Train XGBoost regressors
print("🎯 Training model for plate_x...")
model_x = xgb.XGBRegressor(n_estimators=100, random_state=42)
model_x.fit(X_train, y_train_x)

print("🎯 Training model for plate_z...")
model_z = xgb.XGBRegressor(n_estimators=100, random_state=42)
model_z.fit(X_train, y_train_z)

# Evaluate
mse_x = mean_squared_error(y_test_x, model_x.predict(X_test))
mse_z = mean_squared_error(y_test_z, model_z.predict(X_test))
print(f"📏 MSE plate_x: {mse_x:.4f}")
print(f"📏 MSE plate_z: {mse_z:.4f}")

# Save models
joblib.dump(model_x, '../models/pitch_loc_x.pkl')
joblib.dump(model_z, '../models/pitch_loc_z.pkl')
print("💾 Models saved.")
