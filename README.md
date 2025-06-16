# DiamondMind

DiamondMind is a machine learning powered web application focused on analyzing Major League Baseball (MLB) pitches in real time. It leverages advanced predictive models to provide insights on pitch types, outcomes, locations, and batter behavior probabilities, helping baseball analysts, coaches, and fans understand the game better.

## Project Overview

DiamondMind consists of two main parts: a Python Flask backend API serving multiple pre-trained XGBoost machine learning models, and a React frontend built with Vite that provides an interactive user interface.

### Backend

- **Purpose:** The backend exposes RESTful endpoints that accept pitch-related features as input and return predictions such as pitch type, pitch outcome, strike probability, swing probability, and pitch location coordinates (x and z).
- **ML Models:** Multiple XGBoost models trained on historical MLB pitch data, saved as `.pkl` files, are loaded on startup. Models include:
  - Pitch Type Prediction Model
  - Pitch Outcome Prediction Model
  - Pitch Location (X and Z coordinate) Prediction Models
  - Swing Probability Model
  - Strike Probability Model
- **API:** Flask handles HTTP POST requests with JSON payloads of pitch features and responds with JSON predictions. This design enables easy integration with various frontend or external systems.

### Frontend

- **Purpose:** The frontend provides a sleek dashboard where users can input pitch data or view real-time predictions and analytics. It visualizes pitch outcomes and probabilities interactively, making complex data easy to digest.
- **Technologies:** Built using React and Vite for a fast development experience, styled with Tailwind CSS for modern UI aesthetics.
- **Deployment:** The frontend is bundled using Vite and served as static files. It consumes the backend API endpoints to fetch prediction data dynamically.

## Features

- **Pitch Type Prediction:** Predicts the kind of pitch thrown (fastball, curveball, slider, etc.) given pitch features.
- **Pitch Outcome Prediction:** Estimates the result of the pitch (strike, ball, hit, foul, etc.).
- **Pitch Location Prediction:** Predicts the horizontal (x) and vertical (z) coordinates where the pitch will cross the plate.
- **Swing Probability:** Calculates the likelihood that the batter will swing at the pitch.
- **Strike Probability:** Calculates the likelihood that the pitch will be called a strike.
- **Interactive Dashboard:** Users can input pitch parameters and get immediate feedback and visualizations.

## How to Use

1. **Run Backend API**

   - Install dependencies from `requirements.txt`
   - Place trained model `.pkl` files in the `backend/models/` directory
   - Start the Flask server using `python app.py`
   - The API will be available at `http://localhost:10000` (or configured port)

2. **Run Frontend**

   - Navigate to the frontend directory
   - Install npm dependencies
   - Run `npm run dev` to start the development server or `npm run build` for production build
   - Open the frontend in a browser, which interacts with the backend API for predictions

## Project Structure

DiamondMind/
├── backend/
│ ├── api/ # Flask API code
│ ├── models/ # Pre-trained ML model files (.pkl)
│ └── requirements.txt # Python dependencies
├── frontend/
│ └── frontend/ # React + Vite frontend
│ ├── package.json
│ ├── src/
│ └── ...
├── .gitignore
└── render.yaml # Deployment config for Render


## Deployment

- Backend and frontend are deployed as separate services on Render.com.
- Frontend is served as static files using the `serve` npm package.
- Backend runs the Flask API server with the models loaded in memory.
- Custom domains can be configured via Render's dashboard for professional branding.

## Future Improvements

- Integrate real-time MLB game data feed to auto-populate pitch inputs.
- Add user authentication for personalized dashboards.
- Expand models with deep learning architectures for improved accuracy.
- Implement caching and performance optimization for API.

## License

MIT © Rohan Sriram

---

Feel free to ask if you want me to generate this as a file for download!
