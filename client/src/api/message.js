import { api } from "./api";

export const sendQuery = async (message) => {
  console.log(message)
  return await api.post("/query", {
    question: message,
  });
};

export const sendAgentQuery = async (message) => {
  return await api.post("/query/agent", {
    question: message,
  });
};
