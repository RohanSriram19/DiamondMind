import PitchTypePredictor from "./components/PitchTypePredictor";
import OutcomePredictor from "./components/OutcomePredictor";
import LocationPredictor from "./components/LocationPredictor";
import SwingPredictor from "./components/SwingPredictor";
import StrikePredictor from "./components/StrikePredictor";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-purple-200">
      <div className="max-w-2xl mx-auto p-4">
        <h1 className="text-3xl font-bold mb-6 text-center">DiamondMind Demo</h1>
        <PitchTypePredictor />
        <OutcomePredictor />
        <LocationPredictor />
        <SwingPredictor />
        <StrikePredictor />
      </div>
    </div>
  );
}
