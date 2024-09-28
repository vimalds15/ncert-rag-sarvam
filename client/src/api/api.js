import axios from "axios";

export const api = axios.create({
  baseURL: "https://ncert-rag-sarvam-production.up.railway.app/",
  headers: {
    "Content-Type": "application/json",
  },
});
