import React, { useState } from "react";
import axios from "axios";

const initialFeatures = {
  release_speed: "",
  release_pos_x: "",
  release_pos_z: "",
  pfx_x: "",
  pfx_z: "",
  spin_rate: "",
  release_extension: "",
  vx0: "",
  vy0: "",
  vz0: "",
};

export default function PitchLocationPredictor() {
  const [features, setFeatures] = useState(initialFeatures);
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = { features };
    const response = await axios.post("http://127.0.0.1:5000/predict/location", payload);
    setPrediction(response.data);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-6 rounded-2xl bg-[#222c47]/90 shadow-xl ring-2 ring-yellow-200 mb-4"
    >
      <h2 className="text-2xl font-bold mb-3 text-yellow-300 drop-shadow">Pitch Location Predictor</h2>
      <div className="grid grid-cols-2 gap-3">
        {Object.keys(initialFeatures).map((k) => (
          <label key={k}>
            <span className="block mb-1">{k.replace(/_/g, " ").replace(/\b\w/g, l => l.toUpperCase())}</span>
            <input
              type="text"
              inputMode="decimal"
              name={k}
              value={features[k]}
              onChange={handleChange}
              placeholder={"e.g. " + (k === "release_speed" ? "92.5" : "1.0")}
              className="border p-2 w-full"
            />
          </label>
        ))}
      </div>
      <button
        type="submit"
        className="mt-4 bg-yellow-400 text-[#0a174e] font-bold py-2 px-6 rounded hover:bg-yellow-300 transition-all"
      >
        Predict
      </button>
      {prediction && (
        <div className="mt-4 text-lg">
          Plate X: <span className="font-bold text-yellow-300">{prediction.plate_x?.toFixed(3)}</span>, Plate Z: <span className="font-bold text-yellow-300">{prediction.plate_z?.toFixed(3)}</span>
        </div>
      )}
    </form>
  );
}
