import React, { useState } from "react";
import InitialText from "./InitialText";
import { dummyData } from "../mock/data";
import { useMessageContext } from "../services/MessageContext";
import Input from "./Input";

const Chat = () => {
  const { messages } = useMessageContext();

  return (
    <div className="flex flex-col justify-between h-full">
      <div className="h-full p-2">
        {messages.length > 0 ? (
          <div>
            {messages.map((message) => (
              <div
                className={`flex flex-col ${
                  message.type === "user" && "items-end"
                }`}
              >
                <p className="text-sm font-semibold">
                  {message.type === "ai" ? "AI" : "You"}
                </p>
                <p className="text-sm bg-gray-200 w-fit px-6 py-2 rounded mt-1 font-semibold text-zinc-700 max-w-[80%]">
                  {message.content}
                </p>
              </div>
            ))}
          </div>
        ) : (
          <InitialText />
        )}
      </div>
      <div>
        <Input  />
      </div>
    </div>
  );
};

export default Chat;
