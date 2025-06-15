import axios from "axios";
const BASE_URL = "http://127.0.0.1:5000";

export const predictType = (features) =>
  axios.post(`${BASE_URL}/predict/type`, { features });

export const predictOutcome = (features) =>
  axios.post(`${BASE_URL}/predict/outcome`, { features });

export const predictLocation = (featuresObj) =>
  axios.post(`${BASE_URL}/predict/location`, { features: featuresObj });

export const predictSwing = (features) =>
  axios.post(`${BASE_URL}/predict/swing`, { features });

export const predictStrike = (features) =>
  axios.post(`${BASE_URL}/predict/strike`, { features });
