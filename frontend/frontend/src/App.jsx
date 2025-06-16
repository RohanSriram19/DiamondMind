import React from "react";
import PitchTypePredictor from "./components/PitchTypePredictor";
import PitchOutcomePredictor from "./components/PitchOutcomePredictor";
import PitchLocationPredictor from "./components/PitchLocationPredictor";
import SwingProbabilityPredictor from "./components/SwingProbabilityPredictor";
import StrikeProbabilityPredictor from "./components/StrikeProbabilityPredictor";

export default function App() {
  return (
    <div className="min-h-screen w-full flex flex-col items-center px-2 py-8 bg-gradient-to-br from-[#0a174e] to-[#133b5c]">
      <header className="mb-10 flex flex-col items-center">
        <h1 className="text-4xl font-extrabold text-yellow-300 tracking-tight mb-2 drop-shadow-lg">DiamondMind</h1>
        <p className="text-lg font-semibold text-blue-100 mb-2">Advanced MLB Analytics &amp; Prediction</p>
      </header>
      <div className="w-full max-w-4xl flex flex-col gap-8">
        <PitchTypePredictor />
        <PitchOutcomePredictor />
        <PitchLocationPredictor />
        <SwingProbabilityPredictor />
        <StrikeProbabilityPredictor />
      </div>
      <footer className="mt-8 text-sm text-blue-100 opacity-80">
        © 2025 DiamondMind Project
      </footer>
    </div>
  );
}
