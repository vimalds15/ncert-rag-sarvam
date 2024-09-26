import React, { createContext, useState, useContext } from "react";
import { dummyData } from "../mock/data";

const MessageContext = createContext();

export const useMessageContext = () => {
  return useContext(MessageContext);
};

export const MessageProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);

  const addMessage = (message) => {
    setMessages((prevMessages) => [...prevMessages, message]);
  };

  const clearMessages = () => {
    setMessages([]);
  };


  return (
    <MessageContext.Provider
      value={{ messages, addMessage, clearMessages }}
    >
      {children}
    </MessageContext.Provider>
  );
};
