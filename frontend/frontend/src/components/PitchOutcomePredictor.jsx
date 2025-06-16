import React, { useState } from "react";
import axios from "axios";

const initialFeatures = {
  release_speed: "",
  release_pos_x: "",
  release_pos_z: "",
  zone: "",
  stand: "R",
  p_throws: "R",
  balls: "",
  strikes: "",
  outs_when_up: "",
  bat_score: "",
  fld_score: "",
};

export default function PitchOutcomePredictor() {
  const [features, setFeatures] = useState(initialFeatures);
  const [prediction, setPrediction] = useState("");

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const featureOrder = [
      "release_speed", "release_pos_x", "release_pos_z", "zone", "stand", "p_throws",
      "balls", "strikes", "outs_when_up", "bat_score", "fld_score"
    ];
    const featureArray = featureOrder.map(f => features[f]);
    const response = await axios.post("http://127.0.0.1:5000/predict/outcome", {
      features: featureArray,
    });
    setPrediction(response.data.pitch_outcome_prediction || response.data.error);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-6 rounded-2xl bg-[#222c47]/90 shadow-xl ring-2 ring-yellow-200 mb-4"
    >
      <h2 className="text-2xl font-bold mb-3 text-yellow-300 drop-shadow">Pitch Outcome Predictor</h2>
      <div className="grid grid-cols-2 gap-3">
        <label>
          <span className="block mb-1">Release Speed (mph)</span>
          <input type="text" inputMode="decimal" name="release_speed"
            value={features.release_speed} onChange={handleChange}
            placeholder="e.g. 92.5" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Release Pos X</span>
          <input type="text" inputMode="decimal" name="release_pos_x"
            value={features.release_pos_x} onChange={handleChange}
            placeholder="e.g. -1.5" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Release Pos Z</span>
          <input type="text" inputMode="decimal" name="release_pos_z"
            value={features.release_pos_z} onChange={handleChange}
            placeholder="e.g. 6.0" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Zone</span>
          <input type="text" inputMode="decimal" name="zone"
            value={features.zone} onChange={handleChange}
            placeholder="e.g. 5" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Batter Stands</span>
          <select name="stand" value={features.stand} onChange={handleChange}
            className="border p-2 w-full">
            <option value="R">Right</option>
            <option value="L">Left</option>
          </select>
        </label>
        <label>
          <span className="block mb-1">Pitcher Throws</span>
          <select name="p_throws" value={features.p_throws} onChange={handleChange}
            className="border p-2 w-full">
            <option value="R">Right</option>
            <option value="L">Left</option>
          </select>
        </label>
        <label>
          <span className="block mb-1">Balls</span>
          <input type="text" inputMode="decimal" min="0" max="3" name="balls"
            value={features.balls} onChange={handleChange}
            placeholder="e.g. 2" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Strikes</span>
          <input type="text" inputMode="decimal" min="0" max="2" name="strikes"
            value={features.strikes} onChange={handleChange}
            placeholder="e.g. 1" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Outs When Up</span>
          <input type="text" inputMode="decimal" name="outs_when_up"
            value={features.outs_when_up} onChange={handleChange}
            placeholder="e.g. 1" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Batter Score</span>
          <input type="text" inputMode="decimal" name="bat_score"
            value={features.bat_score} onChange={handleChange}
            placeholder="e.g. 2" className="border p-2 w-full" />
        </label>
        <label>
          <span className="block mb-1">Fielding Score</span>
          <input type="text" inputMode="decimal" name="fld_score"
            value={features.fld_score} onChange={handleChange}
            placeholder="e.g. 2" className="border p-2 w-full" />
        </label>
      </div>
      <button
        type="submit"
        className="mt-4 bg-yellow-400 text-[#0a174e] font-bold py-2 px-6 rounded hover:bg-yellow-300 transition-all"
      >
        Predict
      </button>
      {prediction && (
        <div className="mt-4 text-lg">
          Prediction: <span className="font-bold text-yellow-300">{prediction}</span>
        </div>
      )}
    </form>
  );
}
