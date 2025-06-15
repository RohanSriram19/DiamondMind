import React, { useState } from "react";
import { predictStrike } from "../api";

// 15 features (as per your backend)
export default function StrikePredictor() {
  const [features, setFeatures] = useState(Array(15).fill(""));
  const [result, setResult] = useState(null);

  const handleChange = (i, value) => {
    const next = [...features];
    next[i] = value;
    setFeatures(next);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const numericFeatures = features.map(Number);
      const res = await predictStrike(numericFeatures);
      setResult(res.data.strike_probability);
    } catch (err) {
      setResult("Error: " + (err.response?.data?.error || err.message));
    }
  };

  return (
    <div className="p-4 max-w-lg mx-auto bg-white rounded-xl shadow mt-8">
      <h2 className="font-bold text-lg mb-2">Strike Probability Predictor</h2>
      <form onSubmit={handleSubmit} className="space-y-2">
        {features.map((val, i) => (
          <input
            key={i}
            className="border rounded p-2 w-full"
            type="number"
            value={val}
            placeholder={`Feature ${i + 1}`}
            onChange={e => handleChange(i, e.target.value)}
          />
        ))}
        <button className="bg-yellow-600 text-white px-4 py-2 rounded" type="submit">
          Predict
        </button>
      </form>
      {result !== null && (
        <div className="mt-4 font-mono">
          Probability: <span className="font-bold">{result}</span>
        </div>
      )}
    </div>
  );
}
