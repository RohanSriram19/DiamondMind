import React, { useState } from "react";
import axios from "axios";

const initialFeatures = {
  release_speed: "",
  release_pos_x: "",
  release_pos_z: "",
  pfx_x: "",
  pfx_z: "",
  plate_x: "",
  plate_z: "",
  vx0: "",
  vy0: "",
  vz0: "",
  ax: "",
  ay: "",
  az: "",
  release_spin_rate: "",
  release_extension: "",
};

export default function StrikeProbabilityPredictor() {
  const [features, setFeatures] = useState(initialFeatures);
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const featureOrder = Object.keys(initialFeatures);
    const featureArray = featureOrder.map(f => features[f]);
    const response = await axios.post("http://127.0.0.1:5000/predict/strike", {
      features: featureArray,
    });
    setPrediction(response.data.strike_probability);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-6 rounded-2xl bg-[#222c47]/90 shadow-xl ring-2 ring-yellow-200 mb-4"
    >
      <h2 className="text-2xl font-bold mb-3 text-yellow-300 drop-shadow">Strike Probability Predictor</h2>
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
              placeholder="e.g. 1.0"
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
      {prediction !== null && (
        <div className="mt-4 text-lg">
          Probability: <span className="font-bold text-yellow-300">{(prediction * 100).toFixed(2)}%</span>
        </div>
      )}
    </form>
  );
}
