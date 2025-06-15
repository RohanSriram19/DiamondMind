import React, { useState } from "react";
import { predictLocation } from "../api";

// These should match your location_features.pkl order
const featureNames = [
  "release_speed",
  "release_pos_x",
  "release_pos_z",
  "pfx_x",
  "pfx_z",
  "spin_rate",
  "release_extension",
  "vx0",
  "vy0",
  "vz0"
];

export default function LocationPredictor() {
  const [features, setFeatures] = useState({});
  const [result, setResult] = useState(null);

  const handleChange = (name, value) => {
    setFeatures(prev => ({ ...prev, [name]: Number(value) }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await predictLocation(features);
      setResult(`plate_x: ${res.data.plate_x}, plate_z: ${res.data.plate_z}`);
    } catch (err) {
      setResult("Error: " + (err.response?.data?.error || err.message));
    }
  };

  return (
    <div className="p-4 max-w-lg mx-auto bg-white rounded-xl shadow mt-8">
      <h2 className="font-bold text-lg mb-2">Pitch Location Predictor</h2>
      <form onSubmit={handleSubmit} className="space-y-2">
        {featureNames.map((name) => (
          <input
            key={name}
            className="border rounded p-2 w-full"
            type="number"
            value={features[name] || ""}
            placeholder={name}
            onChange={e => handleChange(name, e.target.value)}
          />
        ))}
        <button className="bg-green-600 text-white px-4 py-2 rounded" type="submit">
          Predict
        </button>
      </form>
      {result && (
        <div className="mt-4 font-mono">
          {result}
        </div>
      )}
    </div>
  );
}
